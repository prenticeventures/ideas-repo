# Public Medicare atherectomy screen: methods and results

Research date: October 25, 2026. This is a retrospective feasibility demonstration, not a fraud classifier, medical opinion, or submission to an agency.

## Explore the retrieved data

[Open the interactive provider-data dashboard](provider-data-dashboard.html). It includes all 5,730 retrieved rows and all 28 original CMS fields, with search, filters, provider comparisons, source details and CSV export. The 56 organization rows remain visible in the full retrieval and are excluded from the original individual-provider comparison.

The dashboard states the research question and procedure-first cohort selection at the top. Its Top billers by year view sums selected code rows per NPI and year, with code, setting, specialty, state and provider-type filters. Choose estimated Medicare payments, estimated submitted charges or service units. The charts use one shared scale across displayed years. Both the annual totals table and the original source-row table have column sorting in both directions. Year sorting uses the selected measure, highest first, within each year. Explorer ranks are recalculated for the selected cohort and are separate from the fixed original experiment.

Build the dashboard again from the unchanged saved snapshots with `python3 dashboard/build_dashboard.py`. The builder verifies all 18 source hashes and makes no network requests.

## Result

Eighteen free CMS API requests returned 5,730 provider × procedure × setting rows for six codes over 2021 to 2023. No account or payment was required. All pagination, filter, duplicate-key, beneficiary-suppression, and numeric checks passed. The first end-to-end download/analysis run took 4.52 seconds in this execution environment. That is machine runtime, not research, clinical review, or case-building labor. A cached offline rerun took about one second and reproduced the target outputs. These timings should not be generalized to another network or computer.

For individual NPI 1346286663, the NPPES response identifies Harold A. Tabaie at the same 400 N Ford Blvd location that appears in the billing data. DOJ has charged him. The case remains pending. His CMS specialty in these utilization files is Vascular Surgery, while the current NPPES taxonomy is Thoracic Surgery (Cardiothoracic Vascular Surgery). Comparisons use the billing file's year-specific specialty consistently rather than silently substituting the registry label.

| Data year | Primary-code service units | National rank / published non-facility providers | Vascular-surgery rank / published non-facility peers | Estimated Medicare payments for selected primary codes |
|---|---:|---:|---:|---:|
| 2021 | 495 | 12 / 695 | 2 / 271 | $3,791,675 |
| 2022 | 598 | 7 / 711 | 1 / 274 | $3,876,018 |
| 2023 | 429 | 14 / 695 | 1 / 283 | $2,667,521 |

For add-on code 37233, kept separate from primary-code totals, his services-per-beneficiary ratio ranked first among published non-facility rows in each year: 3.46, 4.70, and 3.92. That code counts additional-vessel services. Those ratios are not counts of operations or proof that repeated treatment was improper.

The named historical case would appear in a simple national top-20 volume screen in all three years. The experiment shows that the billing pattern can be seen retrospectively in public data and that the technical extraction was inexpensive. It does not show that an outsider could prove fraud, report it first, or receive a reward.

## Fixed definitions and source selection

- We used the 2021, 2022 and 2023 files because they overlap DOJ's alleged conduct period, January 2016 to August 2023. The full 2023 file includes months after the alleged period. The indictment identifies a claim submitted in September 2023, but annual files cannot isolate the relevant months.
- Primary lower-extremity atherectomy codes: 37225, 37227, 37229, 37231. Additional-vessel codes 37233, 37235 are retrieved but excluded from primary totals. Supra-inguinal codes 0234T to 0238T are outside this bounded lower-extremity screen. This is not a complete recreation of the government's scope or all atherectomy billing.
- Code meanings are supported by observed historical CMS code rows, the CMS coding manual and the contemporaneous 2023 Kentucky Medicaid physician fee schedule. Codes were available within the selected years. Code-specific totals remain separate. No claim is made about compatibility with changed codes in later years.
- Source API versions are pinned by UUID in `run_analysis.py` and `catalog-snapshot.json`. Historical releases can be revised. `manifest.json` records exact URLs, retrieval timestamps, hashes, and row counts for the saved snapshots.
- Comparison population: U.S. individual providers (`Rndrng_Prvdr_Ent_Cd=I`), shown separately for facility (`F`) and non-facility (`O`) settings. Tabaie's observed rows are `O`. This is CMS's aggregate non-facility category, not a detailed location code for a particular clinic.
- National primary-volume rank sums service units across the four primary codes for each rendering NPI, year, and setting. The same-specialty rank compares only providers in the CMS specialty listed for that year. Rank equals one plus the number of providers with a strictly larger total. Ties share a rank.
- Code-specific volume and services-per-beneficiary ranks compare the same code, year, and setting. Specialty-adjusted volume ranks are also reported. There is no clinical risk adjustment: public procedure rows lack the patient-level severity and diagnostic detail necessary for that.
- Estimated payment equals `Tot_Srvcs × Avg_Mdcr_Pymt_Amt`, summed only over the selected code rows. It is a reconstruction from rounded averages, not a claim-by-claim audit, fraud-loss estimate, or the indictment's total.
- Never add beneficiary counts across codes: the same patient can appear in multiple rows. Primary service units are also not unique surgeries, patients, limbs, or encounters.

## What was exploratory

This case was already known, so selection has hindsight bias. The codes and 2021 to 2023 year range were fixed before the full national extraction and ranking. A target-NPI lookup and one-code access probe had already shown two relevant codes before the scripted experiment. This was not preregistered or blinded. No rank threshold was tuned to obtain a particular answer. The top-20 review uses the latest selected year (2023), non-facility setting, the four primary codes, and descending units, breaking display-order ties by NPI. It does not train a model or estimate sensitivity, specificity, precision, prevalence, or a payout probability.

## Top-20 review and lawful alternative explanations

`top20-review.csv` and `top20-review-notes.md` examine the twenty highest-volume 2023 non-facility results. The review export uses anonymous result labels except that it identifies which label is the already-public historical case. Raw public-source files and full descriptive rank tables retain original provider names/NPIs for reproducibility. Their inclusion is not an allegation against those providers.

The review is desk triage of aggregate data, not twenty clinical or investigative case reviews. It considers specialty concentration, unusually small peer groups, repeated-service ratios, multi-vessel coding, setting differences, referral concentration, and absent severity information. All twenty remain unadjudicated by this analysis. We obtained no records, interviews, patient authorizations, or expert opinions.

## Timing and leakage

The current catalog marks the retrieved 2021/2022 versions modified in March 2025 and points to replacement files under November 2025 paths. The 2023 entry is modified October 28, 2025. These fields do not establish initial release dates. A [CMS bulletin dated May 22, 2025](https://www.cms.gov/training-education/medicare-learning-network/newsletter/2025-05-22-mlnc) independently confirms publication of CY2023 physician data by that date, before the October 2026 prosecution. The current snapshot is not necessarily byte-for-byte the initial 2025 release.

We have not established that these exact versions were public before August 2023 or before the government began investigating. A retrospective rank is therefore not proof of early discovery or reward originality. The 2026 NPPES identity check and indictment were used for validation after case selection. They cannot be treated as newly available prospective evidence.

## Reproduce on the local Mac

Run the commands in the local Mac terminal. Python 3.10 or later is the only software dependency.

```sh
cd /Users/teeraprice/Code/ideas-repo
python3 healthcare-fraud-detection-bounty-hunting/experiment/run_analysis.py --offline
```

To fetch the pinned datasets again instead of using the supplied snapshots:

```sh
cd /Users/teeraprice/Code/ideas-repo
python3 healthcare-fraud-detection-bounty-hunting/experiment/run_analysis.py --refresh
```

Refreshing overwrites local snapshots and outputs. CMS revisions may change results. Preserve the original folder before refreshing if comparing versions. A portable copy can be run with `python3 /absolute/path/to/experiment/run_analysis.py --offline`. Paths resolve relative to the script, not the shell directory.

Verification included a successful cold retrieval and an offline reproduction. All 18 response filters and unique row keys were checked, as were saved hashes, the suppressed-cell cutoff, and nonnegative payments. Target totals were independently recalculated from the cached rows. No patients or clinical outcomes were assessed.

## Sources

- [CMS catalog](https://data.cms.gov/data.json) and [provider/service data](https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service).
- [CMS methodology, March 2025](https://data.cms.gov/sites/default/files/2025-04/MUP_PHY_RY25_202350312_Methodology_508.pdf).
- [NPPES target identity API](https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1346286663), response saved in `target-npi-verification.json`.
- [2023 Kentucky Medicaid physician fee schedule](https://www.chfs.ky.gov/agencies/dms/DMSFeeRateSchedules/2023PhysicianFeeSchedule.pdf), contemporaneous code descriptions, not Medicare pricing authority.
- [CMS 2025 coding manual](https://www.cms.gov/files/document/2025nccimedicaidpolicymanualcomplete.pdf), which lists atherectomy code families. It was not used to infer medical necessity for 2021 to 2023.
- [DOJ indictment](https://www.justice.gov/criminal/media/1467741/dl?inline=), which gives the allegations and charged conduct period but does not identify HCPCS codes for the charged claims.
