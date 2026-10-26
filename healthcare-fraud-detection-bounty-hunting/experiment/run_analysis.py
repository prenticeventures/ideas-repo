#!/usr/bin/env python3
"""Cached descriptive CMS billing screen; Python 3.10+ standard library only."""
import argparse
import collections
import concurrent.futures
import csv
import datetime
import hashlib
import json
import pathlib
import statistics
import time
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
YEARS = {2021: '31dc2c47-f297-4948-bfb4-075e1bec3a02',
         2022: 'e650987d-01b7-4f09-b75e-b0b075afbf98',
         2023: '0e9f2f2b-7bf9-451a-912c-e02e654dd725'}
PRIMARY = ['37225', '37227', '37229', '37231']
ADDON = ['37233', '37235']
TARGET = '1346286663'
PAGE = 5000


def write_csv(name, rows):
    if rows:
        with (ROOT / name).open('w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)


def fetch(job, refresh=False, offline=False):
    year, code = job
    path = ROOT / 'raw' / f'{year}_{code}.json'
    meta_path = path.with_suffix('.meta.json')
    if path.exists() and not refresh:
        rows, meta = json.loads(path.read_text()), json.loads(meta_path.read_text())
        assert hashlib.sha256(path.read_bytes()).hexdigest() == meta['sha256']
        return year, code, rows, meta
    if offline:
        raise RuntimeError(f'Missing cached data: {path}')
    start, rows, urls, offset = time.perf_counter(), [], [], 0
    while True:
        query = urllib.parse.urlencode({'filter[HCPCS_Cd]': code, 'size': PAGE, 'offset': offset})
        url = f'https://data.cms.gov/data-api/v1/dataset/{YEARS[year]}/data?{query}'
        urls.append(url)
        for attempt in range(3):
            try:
                request = urllib.request.Request(url, headers={'User-Agent': 'PublicDataFeasibilityResearch/1.0'})
                with urllib.request.urlopen(request, timeout=90) as response:
                    assert response.status == 200
                    batch = json.load(response)
                break
            except Exception:
                if attempt == 2:
                    raise
                time.sleep(1 + attempt)
        assert isinstance(batch, list)
        assert all(r['HCPCS_Cd'] == code for r in batch), 'API ignored filter'
        rows.extend(batch)
        if len(batch) < PAGE:
            break
        offset += PAGE
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rows, sort_keys=True, separators=(',', ':')))
    meta = {'year': year, 'code': code, 'dataset_uuid': YEARS[year], 'urls': urls,
            'retrieved_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'row_count': len(rows), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'download_seconds': round(time.perf_counter() - start, 3)}
    meta_path.write_text(json.dumps(meta, indent=2))
    return year, code, rows, meta


def analyze(results):
    annual, manifest, checks = collections.defaultdict(list), [], []
    for year, code, rows, meta in results:
        keys = [(r['Rndrng_NPI'], r['HCPCS_Cd'], r['Place_Of_Srvc']) for r in rows]
        assert len(keys) == len(set(keys)), 'Duplicate keys / pagination error'
        for r in rows:
            assert float(r['Tot_Benes']) > 10
            assert float(r['Tot_Srvcs']) >= float(r['Tot_Benes'])
            assert float(r['Avg_Mdcr_Pymt_Amt']) >= 0
        annual[year].extend(rows)
        manifest.append(meta)
        checks.append({'year': year, 'code': code, 'rows': len(rows), 'unique_keys': len(set(keys)),
                       'min_beneficiaries': min((float(r['Tot_Benes']) for r in rows), default=None),
                       'all_filter_values_match': True})
    target_rows, provider_results, all_rows = [], [], []
    for year, rows in sorted(annual.items()):
        rows = [r for r in rows if r['Rndrng_Prvdr_Cntry'] == 'US' and r['Rndrng_Prvdr_Ent_Cd'] == 'I']
        groups = collections.defaultdict(list)
        totals = collections.defaultdict(lambda: {'services': 0., 'payment': 0., 'charges': 0.,
                                                  'addon_services': 0., 'codes': set()})
        for r in rows:
            code, pos, npi, typ = r['HCPCS_Cd'], r['Place_Of_Srvc'], r['Rndrng_NPI'], r['Rndrng_Prvdr_Type']
            s = float(r['Tot_Srvcs'])
            groups[(code, pos)].append(r)
            t = totals[(npi, pos, typ)]
            t.update(name=r['Rndrng_Prvdr_First_Name'] + ' ' + r['Rndrng_Prvdr_Last_Org_Name'],
                     state=r['Rndrng_Prvdr_State_Abrvtn'])
            if code in PRIMARY:
                t['services'] += s
                t['payment'] += s * float(r['Avg_Mdcr_Pymt_Amt'])
                t['charges'] += s * float(r['Avg_Sbmtd_Chrg'])
                t['codes'].add(code)
            else:
                t['addon_services'] += s
        for r in rows:
            code, pos, typ = r['HCPCS_Cd'], r['Place_Of_Srvc'], r['Rndrng_Prvdr_Type']
            s, b = float(r['Tot_Srvcs']), float(r['Tot_Benes'])
            ratio, peers = s / b, groups[(code, pos)]
            sp = [x for x in peers if x['Rndrng_Prvdr_Type'] == typ]
            out = {'year': year, 'npi': r['Rndrng_NPI'],
                   'name': r['Rndrng_Prvdr_First_Name'] + ' ' + r['Rndrng_Prvdr_Last_Org_Name'],
                   'specialty': typ, 'state': r['Rndrng_Prvdr_State_Abrvtn'], 'code': code, 'place': pos,
                   'services': s, 'beneficiaries_this_code_place': b,
                   'services_per_beneficiary_this_code_place': round(ratio, 6),
                   'estimated_medicare_payment': round(s * float(r['Avg_Mdcr_Pymt_Amt']), 2),
                   'national_code_place_n': len(peers),
                   'national_volume_rank': 1 + sum(float(x['Tot_Srvcs']) > s for x in peers),
                   'national_ratio_rank': 1 + sum(float(x['Tot_Srvcs']) / float(x['Tot_Benes']) > ratio for x in peers),
                   'specialty_code_place_n': len(sp),
                   'specialty_volume_rank': 1 + sum(float(x['Tot_Srvcs']) > s for x in sp),
                   'national_services_median': statistics.median(float(x['Tot_Srvcs']) for x in peers)}
            all_rows.append(out)
            if r['Rndrng_NPI'] == TARGET:
                target_rows.append(out)
        for (npi, pos, typ), t in totals.items():
            if not t['services']:
                continue
            peers = [v for (p, l, k), v in totals.items() if l == pos and v['services'] > 0]
            sp = [v for (p, l, k), v in totals.items() if l == pos and k == typ and v['services'] > 0]
            provider_results.append({'year': year, 'npi': npi, 'name': t['name'], 'state': t['state'],
                'specialty': typ, 'place': pos, 'primary_code_units': t['services'],
                'addon_code_units_separate': t['addon_services'], 'primary_codes_observed': ','.join(sorted(t['codes'])),
                'estimated_primary_medicare_payment': round(t['payment'], 2),
                'estimated_primary_submitted_charges': round(t['charges'], 2),
                'national_same_place_n': len(peers),
                'national_primary_unit_rank': 1 + sum(v['services'] > t['services'] for v in peers),
                'specialty_same_place_n': len(sp),
                'specialty_primary_unit_rank': 1 + sum(v['services'] > t['services'] for v in sp)})
    write_csv('target-code-results.csv', target_rows)
    write_csv('target-year-results.csv', [r for r in provider_results if r['npi'] == TARGET])
    write_csv('provider-year-results.csv', provider_results)
    write_csv('all-code-results.csv', all_rows)
    top = sorted([r for r in provider_results if r['year'] == max(YEARS) and r['place'] == 'O'],
                 key=lambda r: (-r['primary_code_units'], r['npi']))[:20]
    review = []
    for i, r in enumerate(top, 1):
        rr = [x for x in all_rows if x['year'] == max(YEARS) and x['npi'] == r['npi']
              and x['place'] == 'O' and x['code'] in PRIMARY]
        review.append({'review_id': f'P{i:02d}', 'known_case': r['npi'] == TARGET, 'year': max(YEARS),
            'specialty': r['specialty'], 'national_volume_rank': r['national_primary_unit_rank'],
            'primary_code_units': r['primary_code_units'], 'estimated_payment': r['estimated_primary_medicare_payment'],
            'largest_code_specific_services_per_beneficiary': max(x['services_per_beneficiary_this_code_place'] for x in rr),
            'specialty_volume_rank': r['specialty_primary_unit_rank'], 'specialty_peer_count': r['specialty_same_place_n'],
            'corroboration_status': 'Not adjudicated; no clinical or patient-level evidence; volume establishes no fraud'})
    write_csv('top20-review.csv', review)
    summary = {'target_npi': TARGET, 'years': list(YEARS), 'primary_codes': PRIMARY,
        'addon_codes_separate': ADDON, 'raw_rows': sum(x['row_count'] for x in manifest),
        'requests': sum(len(x['urls']) for x in manifest), 'all_checks_passed': True,
        'target_year_results': [r for r in provider_results if r['npi'] == TARGET],
        'top20_target_present': any(r['known_case'] for r in review),
        'warning': 'Retrospective exploratory screen; units are not surgeries; beneficiaries overlap across codes; published >10-beneficiary cells only; no accuracy estimate or fraud finding.'}
    (ROOT / 'manifest.json').write_text(json.dumps({'as_of_date': '2026-10-25', 'sources': manifest, 'quality_checks': checks}, indent=2))
    (ROOT / 'summary.json').write_text(json.dumps(summary, indent=2))
    return summary


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--refresh', action='store_true')
    p.add_argument('--offline', action='store_true')
    args = p.parse_args()
    start = time.perf_counter()
    jobs = [(year, code) for year in YEARS for code in PRIMARY + ADDON]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(lambda job: fetch(job, args.refresh, args.offline), jobs))
    summary = analyze(results)
    summary['run_seconds'] = round(time.perf_counter() - start, 3)
    (ROOT / 'run-metrics.json').write_text(json.dumps({'run_seconds': summary['run_seconds'], 'offline': args.offline}, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
