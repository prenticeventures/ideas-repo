let explorerCohort = [], explorerVisible = [], explorerPage = 0;
let annualSort = {key: 'year', direction: 'desc'};
const metricLabels = {payment: 'Estimated Medicare payments', charges: 'Estimated submitted charges', services: 'Service units'};
fillSelect('explore-state', rows.map(r => r.state));
fillSelect('explore-specialty', rows.map(r => r.specialty));
function explorerFilters() {
  return {year: $('explore-year').value, code: $('explore-code').value,
    metric: $('explore-metric').value, setting: $('explore-setting').value,
    state: $('explore-state').value, specialty: $('explore-specialty').value,
    entity: $('explore-entity').value};
}
function explorerCodeLabel() {
  return $('explore-code').selectedOptions[0].textContent;
}
function updateSortHeadings(scope, key, direction) {
  document.querySelectorAll(`[data-${scope}-column]`).forEach(th => {
    const selected = th.getAttribute(`data-${scope}-column`) === key;
    th.setAttribute('aria-sort', selected ? (direction === 'asc' ? 'ascending' : 'descending') : 'none');
    th.querySelector('.sort-arrow').textContent = selected ? (direction === 'asc' ? '↑' : '↓') : '↕';
  });
}
function updateExplorer(resetPage = true) {
  const filters = explorerFilters();
  explorerCohort = BillingData.aggregate(rows, filters);
  const query = $('explore-search').value.trim().toLowerCase();
  explorerVisible = explorerCohort.filter(row => !query || (row.name + ' ' + row.npi).toLowerCase().includes(query));
  if (resetPage) explorerPage = 0;
  const metric = filters.metric;
  const selectedYears = filters.year ? [+filters.year] : [2021, 2022, 2023];
  const limit = +$('explore-top').value;
  const yearly = selectedYears.map(year => ({year,
    cohort: explorerCohort.filter(row => row.year === year),
    visible: explorerVisible.filter(row => row.year === year).sort((a, b) => b[metric] - a[metric] || a.npi.localeCompare(b.npi))}));
  const maximum = Math.max(0, ...yearly.flatMap(group => group.visible.slice(0, limit).map(row => row[metric])));
  const settingLabel = filters.setting === 'O' ? 'Non-facility' : filters.setting === 'F' ? 'Facility' : 'Both settings combined';
  $('explore-definition').textContent = `${metricLabels[metric]} · ${explorerCodeLabel()} · ${settingLabel}. Payments and charges are estimated from each published row's average times service units. Service units are not unique operations or patients. Dollar amounts are nominal and are not adjusted for geography or case mix.`;
  $('year-charts').classList.toggle('one-year', selectedYears.length === 1);
  $('year-charts').innerHTML = yearly.map(group => {
    const top = group.visible.slice(0, limit);
    return `<section class="year-panel" aria-label="${group.year} top billers"><h3>${group.year}</h3><p class="year-context">${nf.format(group.cohort.length)} NPIs in selected cohort${query ? ' · ' + nf.format(group.visible.length) + ' match search' : ''}</p><div class="annual-bars">${top.map(row => `<div class="annual-item"><div class="bill-provider"><button data-provider="${esc(row.npi)}">${esc(row.name)}</button><span class="bill-value">${metric === 'services' ? nf.format(row[metric]) : compactMoney(row[metric])}</span></div><div class="bill-identity">NPI ${esc(row.npi)} · ${esc(row.state)} · Rank ${row.cohort_rank}${row.npi === TARGET ? ' · Historical case' : ''}</div><div class="bill-track" aria-hidden="true"><div class="bill-fill ${row.npi === TARGET ? 'case' : ''}" style="width:${maximum ? 100 * row[metric] / maximum : 0}%"></div></div></div>`).join('') || '<p class="no-results">No published rows match this selection.</p>'}</div></section>`;
  }).join('');
  $('chart-scale-note').textContent = `${metricLabels[metric]} use one shared bar scale across the displayed years${maximum ? ', up to ' + (metric === 'services' ? nf.format(maximum) + ' units' : money.format(maximum)) : ''}. Each year has its own top list. Gold identifies the known historical case, not a new fraud finding. Select a name to inspect the selected-code totals and original records.`;
  renderExplorerTable();
}
function renderExplorerTable() {
  const size = +$('explore-page-size').value;
  const sorted = BillingData.sorted(explorerVisible, annualSort.key, annualSort.direction, $('explore-metric').value);
  const pages = Math.max(1, Math.ceil(sorted.length / size));
  explorerPage = Math.max(0, Math.min(explorerPage, pages - 1));
  const start = explorerPage * size;
  const shown = sorted.slice(start, start + size);
  $('explore-body').innerHTML = shown.map(row => `<tr><td>${row.year}</td><td><button class="provider" data-provider="${esc(row.npi)}">${esc(row.name)}</button>${row.npi === TARGET ? '<div class="subtle">Historical case</div>' : ''}</td><td class="code">${esc(row.npi)}</td><td>${esc(row.specialty)}<div class="subtle">${esc(row.state)}${row.entity === 'O' ? ' · Organization' : ''}</div></td><td>${row.setting === 'O' ? 'Non-facility' : row.setting === 'F' ? 'Facility' : 'Both combined'}</td><td class="code">${esc(row.codes)}</td><td class="num">${nf.format(row.services)}</td><td class="num">${money.format(row.payment)}</td><td class="num">${money.format(row.charges)}</td><td class="num">${row.cohort_rank} / ${row.cohort_size}</td></tr>`).join('') || '<tr><td colspan="10" class="no-results">No providers match these filters.</td></tr>';
  $('explore-page-info').textContent = sorted.length ? `${nf.format(start + 1)} to ${nf.format(start + shown.length)} of ${nf.format(sorted.length)} provider-year totals` : '0 provider-year totals';
  $('explore-prev').disabled = explorerPage === 0;
  $('explore-next').disabled = explorerPage >= pages - 1;
  updateSortHeadings('annual', annualSort.key, annualSort.direction);
}
function selectedProviderContext(npi) {
  if ($('view-explore').hidden) return '';
  const current = explorerCohort.filter(row => row.npi === npi).sort((a, b) => a.year - b.year);
  if (!current.length) return '';
  return `<h3>Current chart selection: ${esc(explorerCodeLabel())}</h3><p class="mini-note">Selected-cohort ranks use ${esc(metricLabels[$('explore-metric').value].toLowerCase())} and the current filters. The fixed original experiment appears separately below.</p><div class="table-scroll"><table><thead><tr><th>Year</th><th>Codes observed</th><th class="num">Service units</th><th class="num">Est. Medicare payments</th><th class="num">Est. submitted charges</th><th class="num">Selected-cohort rank</th></tr></thead><tbody>${current.map(row => `<tr><td>${row.year}</td><td>${esc(row.codes)}</td><td class="num">${nf.format(row.services)}</td><td class="num">${exactMoney.format(row.payment)}</td><td class="num">${exactMoney.format(row.charges)}</td><td class="num">${row.cohort_rank} / ${row.cohort_size}</td></tr>`).join('')}</tbody></table></div>`;
}
function defaultSortDirection(key) {
  return ['name', 'npi', 'specialty', 'state', 'code', 'codes', 'setting', 'cohort_rank'].includes(key) ? 'asc' : 'desc';
}
document.querySelectorAll('[data-raw-sort]').forEach(button => button.addEventListener('click', () => {
  const key = button.dataset.rawSort;
  const repeated = $('sort').value === key;
  $('sort-direction').value = repeated ? ($('sort-direction').value === 'desc' ? 'asc' : 'desc') : defaultSortDirection(key);
  $('sort').value = key;
  updateRecords();
}));
document.querySelectorAll('[data-annual-sort]').forEach(button => button.addEventListener('click', () => {
  const key = button.dataset.annualSort;
  annualSort = {key, direction: annualSort.key === key ? (annualSort.direction === 'desc' ? 'asc' : 'desc') : defaultSortDirection(key)};
  explorerPage = 0;
  renderExplorerTable();
}));
for (const id of ['explore-code', 'explore-metric', 'explore-year', 'explore-setting', 'explore-specialty', 'explore-state', 'explore-entity', 'explore-top']) {
  $(id).addEventListener('change', () => updateExplorer());
}
$('explore-search').addEventListener('input', () => updateExplorer());
$('explore-page-size').addEventListener('change', () => {explorerPage = 0; renderExplorerTable();});
$('explore-prev').addEventListener('click', () => {explorerPage--; renderExplorerTable();});
$('explore-next').addEventListener('click', () => {explorerPage++; renderExplorerTable();});
$('reset-explore').addEventListener('click', () => {
  $('explore-code').value = 'primary'; $('explore-metric').value = 'payment';
  $('explore-year').value = ''; $('explore-setting').value = 'O';
  $('explore-specialty').value = ''; $('explore-state').value = '';
  $('explore-entity').value = 'I'; $('explore-top').value = '10';
  $('explore-search').value = ''; annualSort = {key: 'year', direction: 'desc'};
  updateExplorer();
});
$('export-explore').addEventListener('click', () => {
  const metric = $('explore-metric').value;
  const exported = BillingData.sorted(explorerVisible, annualSort.key, annualSort.direction, metric).map(row => ({
    year: row.year, npi: row.npi, provider_name: row.name, cms_specialty: row.specialty,
    state: row.state, provider_entity: row.entity, setting: row.setting,
    selected_codes: BillingData.selectedCodes($('explore-code').value).join(','),
    codes_observed: row.codes, service_units: row.services,
    estimated_medicare_payments: row.payment.toFixed(2), estimated_submitted_charges: row.charges.toFixed(2),
    source_rows: row.source_rows, rank_measure: metric, selected_cohort_rank: row.cohort_rank, selected_cohort_size: row.cohort_size
  }));
  const fields = ['year', 'npi', 'provider_name', 'cms_specialty', 'state', 'provider_entity', 'setting', 'selected_codes', 'codes_observed', 'service_units', 'estimated_medicare_payments', 'estimated_submitted_charges', 'source_rows', 'rank_measure', 'selected_cohort_rank', 'selected_cohort_size'];
  download(csvText(fields, exported), 'text/csv;charset=utf-8', 'medicare-annual-provider-totals.csv');
});
