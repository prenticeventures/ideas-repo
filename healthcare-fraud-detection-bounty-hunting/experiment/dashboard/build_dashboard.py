#!/usr/bin/env python3
"""Build an offline dashboard from the pinned experiment snapshots. No downloads."""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIELDS = [
    'Rndrng_NPI', 'Rndrng_Prvdr_First_Name', 'Rndrng_Prvdr_MI', 'Rndrng_Prvdr_Last_Org_Name',
    'Rndrng_Prvdr_Crdntls', 'Rndrng_Prvdr_Ent_Cd', 'Rndrng_Prvdr_St1', 'Rndrng_Prvdr_St2',
    'Rndrng_Prvdr_City', 'Rndrng_Prvdr_State_Abrvtn', 'Rndrng_Prvdr_State_FIPS',
    'Rndrng_Prvdr_Zip5', 'Rndrng_Prvdr_Cntry', 'Rndrng_Prvdr_Type',
    'Rndrng_Prvdr_Mdcr_Prtcptg_Ind', 'Rndrng_Prvdr_RUCA', 'Rndrng_Prvdr_RUCA_Desc',
    'HCPCS_Cd', 'HCPCS_Desc', 'HCPCS_Drug_Ind', 'Place_Of_Srvc', 'Tot_Benes',
    'Tot_Srvcs', 'Tot_Bene_Day_Srvcs', 'Avg_Sbmtd_Chrg', 'Avg_Mdcr_Alowd_Amt',
    'Avg_Mdcr_Pymt_Amt', 'Avg_Mdcr_Stdzd_Amt',
]

def main():
    manifest = json.loads((ROOT / 'manifest.json').read_text())
    packed, sources = [], []
    for entry in sorted(manifest['sources'], key=lambda e: (e['year'], e['code'])):
        path = ROOT / 'raw' / f"{entry['year']}_{entry['code']}.json"
        contents = path.read_bytes()
        assert hashlib.sha256(contents).hexdigest() == entry['sha256'], f'Changed snapshot: {path}'
        records = json.loads(contents)
        assert len(records) == entry['row_count']
        source_index = len(sources)
        sources.append(entry)
        for record in records:
            assert set(record) == set(FIELDS), f'Unexpected fields: {path}'
            packed.append([entry['year'], source_index] + [record[f] for f in FIELDS])
    assert len(packed) == 5730
    with (ROOT / 'provider-year-results.csv').open() as stream:
        provider_year = list(csv.DictReader(stream))
    payload = {'fields': FIELDS, 'rows': packed, 'sources': sources,
               'providerYears': provider_year, 'summary': json.loads((ROOT / 'summary.json').read_text())}
    encoded = json.dumps(payload, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
    template = (ROOT / 'dashboard' / 'dashboard-template.html').read_text()
    assert template.count('__DATA_PAYLOAD__') == 1
    output = ROOT / 'provider-data-dashboard.html'
    logic = (ROOT / 'dashboard' / 'explorer-logic.js').read_text()
    ui = (ROOT / 'dashboard' / 'explorer-ui.js').read_text()
    assert template.count('__EXPLORER_LOGIC__') == 1
    assert template.count('__EXPLORER_UI__') == 1
    output.write_text(template.replace('__DATA_PAYLOAD__', encoded).replace('__EXPLORER_LOGIC__', logic).replace('__EXPLORER_UI__', ui))
    print(json.dumps({'output': str(output), 'raw_rows': len(packed), 'raw_fields': len(FIELDS),
                      'provider_year_rows': len(provider_year), 'snapshots_verified': len(sources),
                      'bytes': output.stat().st_size}))

if __name__ == '__main__':
    main()
