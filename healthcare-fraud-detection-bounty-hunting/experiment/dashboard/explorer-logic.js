/* Pure calculations for the interactive explorer. Does not alter original results. */
const BillingData = (() => {
  const primaryCodes = ['37225', '37227', '37229', '37231'];
  const addonCodes = ['37233', '37235'];
  function selectedCodes(selection) {
    if (selection === 'primary') return primaryCodes;
    if (selection === 'addon') return addonCodes;
    if (!selection || selection === 'all') return [...primaryCodes, ...addonCodes];
    return [selection];
  }
  function aggregate(records, filters = {}) {
    const allowed = new Set(selectedCodes(filters.code ?? 'primary'));
    const grouped = new Map();
    for (const row of records) {
      if (!allowed.has(row.code)) continue;
      if (filters.year && row.year !== +filters.year) continue;
      if (filters.setting && row.setting !== filters.setting) continue;
      if (filters.state && row.state !== filters.state) continue;
      if (filters.specialty && row.specialty !== filters.specialty) continue;
      if (filters.entity && row.entity !== filters.entity) continue;
      const key = `${row.year}|${row.npi}`;
      if (!grouped.has(key)) {
        grouped.set(key, {year: row.year, npi: row.npi, name: row.name,
          state: row.state, specialty: row.specialty, entity: row.entity,
          setting: filters.setting || 'Both combined', services: 0, payment: 0,
          charges: 0, source_rows: 0, codeSet: new Set()});
      }
      const total = grouped.get(key);
      total.services += row.services;
      total.payment += row.payment;
      total.charges += row.charges;
      total.source_rows++;
      total.codeSet.add(row.code);
    }
    const result = [...grouped.values()].map(row => {
      const {codeSet, ...rest} = row;
      return {...rest, codes: [...codeSet].sort().join(', ')};
    });
    const metric = filters.metric || 'payment';
    for (const year of new Set(result.map(row => row.year))) {
      const cohort = result.filter(row => row.year === year)
        .sort((a, b) => b[metric] - a[metric] || a.npi.localeCompare(b.npi));
      let rank = 0, previous;
      cohort.forEach((row, index) => {
        if (index === 0 || row[metric] !== previous) rank = index + 1;
        row.cohort_rank = rank;
        row.cohort_size = cohort.length;
        previous = row[metric];
      });
    }
    return result;
  }
  function sorted(records, key, direction = 'desc', secondary = 'payment') {
    const sign = direction === 'asc' ? 1 : -1;
    return [...records].sort((a, b) => {
      const av = a[key], bv = b[key];
      const first = typeof av === 'number' && typeof bv === 'number'
        ? av - bv : String(av ?? '').localeCompare(String(bv ?? ''), 'en', {numeric: true});
      if (first) return first * sign;
      if (key !== 'year' && a.year !== b.year) return b.year - a.year;
      if (key !== secondary && a[secondary] !== b[secondary]) return b[secondary] - a[secondary];
      return a.npi.localeCompare(b.npi) || String(a.code || '').localeCompare(String(b.code || ''));
    });
  }
  return {selectedCodes, aggregate, sorted};
})();
