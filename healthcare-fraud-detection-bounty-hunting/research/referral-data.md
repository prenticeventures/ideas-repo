# Medicare provider pairs and shared-patient data

Checked October 25, 2026. This supplements the original 19-source inventory.

CMS still publishes the historical provider-pair data discussed in this research. These files add relationships between providers that cannot be reconstructed from the annual procedure totals in the billing experiment.

## Sources and tested access

| Source | Years and access | What was verified |
|---|---|---|
| [CMS Physician Shared Patient Patterns](https://www.cms.gov/regulations-and-guidance/legislation/foia/referral-data-faqs) | Free files for 2009 through 2015, with 30, 60, 90 and 180-day windows | Retrieved the first 2,048 bytes of the 2015 30-day ZIP. The response identified a 355,555,833-byte ZIP and began with the ZIP signature. No full national download was attempted. |
| [NBER archive](https://www.nber.org/research/data/physician-shared-patient-patterns-data) | Historical CMS files in CSV, Stata, SAS and source ZIP formats | The research tool could not open the landing page. The normal browser succeeded. A separate partial CSV request returned actual headers and rows from the 2015 30-day file. Its reported size was 2,112,622,936 bytes. |
| [CareSet DocGraph](https://careset.com/data-store/) | Lists annual data from 2014 through 2025, under commercial and noncommercial licenses | Documentation and listed prices checked. No request, download, purchase or license acceptance was made. |

Tested direct files:

- [CMS 2015 30-day ZIP](https://downloads.cms.gov/foia/physician-shared-patient-patterns-2015-days30.zip). The test used the HTTP link published on the CMS page.
- [NBER 2015 30-day CSV](https://data.nber.org/physician-shared-patient-patterns/2015/pspp2015_30.csv).

The partial samples were inspected during the access test but were not retained as new experiment datasets. The existing 5,730-row billing experiment remains unchanged.

## Fields and meaning

The [CMS methodology](https://downloads.cms.gov/foia/physician_shared_patient_patterns_technical_requirements.pdf) specifies initial NPI, secondary NPI, pair count, distinct beneficiary count and same-day count. NBER adds year, interval and date-range fields. The retrieved CSV header was:

```text
npi1,npi2,paircount,benecount,samedaycount,year,days,begdate,enddate
```

Providers and organizations remain identifiable by NPI. Patient identifiers are absent. Relationships involving fewer than eleven distinct beneficiaries are excluded.

These are inferred patient-sharing relationships. A beneficiary seeing provider A and then provider B within the chosen interval creates a connection. This does not establish an actual referral, a payment arrangement or misconduct. CMS excludes the actual referring-NPI field from the calculation. Same-day direction is assigned using NPI order and does not establish referral direction.

The historical series includes institutional and non-institutional claim types. The methodology even lists Medicare Advantage no-pay claims, so it should not be described as complete Medicare Advantage encounter coverage or assumed identical to the current DocGraph product. The 2015 files cover only part of that year. Read the individual file's dates before comparison.

## Newer data and the budget

CareSet's current price table lists the following commercial annual-network licenses:

| Dataset year | Listed price |
|---|---:|
| Each individual year from 2014 through 2023 | $500 |
| 2024 | $11,000 |
| 2025 | $44,000 |

Free access for 2014 through 2022 is restricted to qualifying noncommercial use. A business seeking contingent rewards should not assume it qualifies. The listed commercial price for 2021, 2022 or 2023 is within the user's less-than-$10,000 research ceiling. Specific permitted uses, delivery, coverage, suppression and methodology still require review of the actual license and documentation. No purchase is authorized by this note.

The historical CMS files can support network analysis for old cases. They do not overlap the 2021 through 2023 billing experiment. No newer direct government download was located in this check. That is an access finding, not proof that newer aggregates cannot be requested.

## Business relevance

The billing dashboard answers who billed high procedure volumes and payments. Provider-pair data can instead show which providers share patients and how concentrated those relationships are. Joining provider pairs to NPPES, ownership and billing summaries could add context for a network investigation. Patient sharing alone does not show why patients moved, which specific procedures they received or whether a referral arrangement was improper.
