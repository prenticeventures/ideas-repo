# Free public data for outside healthcare-fraud screening

Audit date: October 25, 2026. This inventory reviews government data an independent analyst can access publicly or by request. “Tested” means a live request or download was made and a small response or header was inspected. Public data can support a lead, but cannot establish fraud. Records may be aggregated, incomplete, delayed, suppressed, or based on provider and state reporting.

The completed [Medicare prototype](../experiment/README.md) used only free public data. That was a condition of that experiment, not a continuing restriction on research. The current scope also allows requestable government sources and options costing less than $10,000. The operator has healthcare experience, but experience does not grant access to restricted data. See [government data access](government-data-access.md) for current fees, eligibility, and use limits.

## Data availability and limits

- A public physician procedure-billing screen is feasible. CMS's Physician & Other Practitioners files are free, annual, published through CY2024, and organized by NPI and HCPCS. They cover Original Medicare fee-for-service Part B, not Medicare Advantage, Medicaid, commercial insurance, or cash services. Data arrives well after the service year. The CY2024 file was created in May 2026. CMS suppresses small beneficiary cells. The API supports direct queries, so an analyst can screen the public file without buying claims.
- The newly public Medicaid file covers more payers but needs careful validation. HHS published monthly provider-by-procedure aggregates for 2018 to 2024, including fee-for-service, managed-care encounters, and CHIP. The file requires at least 12 claim lines and 12 beneficiaries per published cell. HHS says the 2024 data are preliminary. A 2 KB sample from the start of the CSV showed an extreme `TOTAL_PAID` value of `7469333333258.64` for code 20 with 8,403 claim lines and 915 patients. The servicing NPI `5200000300` had no matching result in the CMS NPI Registry API. This sample may not represent the full file, but it fails basic payment and identifier checks. Do not rank leads by payment until units, malformed rows, state differences, and source values have been checked independently. The exact byte range and headers are logged in [the preserved access evidence](access-evidence/medicaid-sample-metadata.json). The 2,048-byte sample is retained for reproducibility.
- Hospice and home-health screening has usable public payment data and ownership data. CMS's annual PAC PUF has provider-level payment and utilization summaries (CY2024 HHA, FY2024 hospice, each by 6-digit CCN). CMS also provides current PECOS owner extracts for HHAs, hospices and SNFs, including individuals, organizations, owner roles, addresses, ownership percentages, and selected owner-type flags (including PE/REIT). These ownership records are provider self-reports and are not a comprehensive map of all physician/practice ownership.
- Several useful exclusion, license and financial-relationship checks cost nothing. OIG's active LEIE CSV, NPPES public API/downloads, CMS Open Payments, and California Medical Board public license records can add context. LEIE matches must be identity-verified because the downloadable file omits SSN/EIN. A payment from industry is not itself evidence of a kickback. California bulk data is delivered by Box after a request, and the DCA verification API requires approval.
- Some federal enforcement records are available at no cost through CourtListener and RECAP. The service searches and provides records that PACER users have contributed, so its federal-court archive is incomplete. It does not comprehensively cover California state-court cases. An absent document does not show that a case or filing does not exist.

## Most useful source combinations

| Screening question | Smallest workable public-data combination | Key limitation |
|---|---|---|
| Does a physician have unusual Medicare procedure volume? | Physician & Other Practitioners by Provider and Service for CY2024 and earlier years. NPPES for identity and taxonomy. California MBC for license and discipline where applicable. | Original Medicare FFS Part B only. Annual provider-level totals, suppressed small cells, and no patient-level clinical rationale. |
| Does a DME orderer show a suspicious pattern? | DME by Referring Provider and Service plus Supplier and Service for CY2024. NPPES and LEIE. | The DME file covers fee-for-service only and suppresses small cells. Check the orderer and supplier separately. |
| Does a Part D prescriber have an unusual drug mix or cost? | Part D Prescribers by Provider and Drug for CY2024. NPPES and Open Payments. | Total drug cost is not the amount Medicare paid. The file covers only the Part D population and has redactions and population differences from Part B. |
| Does a hospice or home-health operator show high payment and repeated ownership? | PAC PUF by provider and service for 2024. All Owners extracts. CCN and provider enrollment. Care Compare quality and penalties. LEIE. | Medicare-only annual PUF with suppressed small cells and self-reported ownership. No nationwide public claims file covers every payer. |
| Does Medicaid volume look unusual across payers? | HHS Medicaid Provider Spending by HCPCS, provider enrollment segments, NPPES, and LEIE. | One aggregate release covering 2018 to 2024, with likely state variation, preliminary 2024 data, suppression below 12 claim lines or beneficiaries, and a payment-value issue observed in the sample. |

The atherectomy experiment uses historical Medicare physician/service data for primary codes 37225, 37227, 37229 and 37231, with add-on codes 37233 and 37235 kept separate. Supra-inguinal codes 0234T to 0238T are outside that bounded screen. Medicaid data require separate payer, payment and data-quality validation.

## Source-by-source audit

### 1. Medicare Physician & Other Practitioners, by Provider and Service

- Source and access: [CMS dataset](https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service), [API docs](https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service/api-docs). CMS API route: `GET https://data.cms.gov/data-api/v1/dataset/{version_uuid}/data`. `size` and `filter[FIELD]=value` work. Current CY2024 version UUID `92396110-2aed-4d63-a6a2-5d6207d46a29`. The tested historical version identifiers are recorded in [the experiment manifest](../experiment/manifest.json).
- Scope and fields: One row per rendering NPI × HCPCS × place/geography components of CMS's annual file. Includes NPI, provider name/type/specialty, state/address, HCPCS code/descriptor, place of service, beneficiary count, services, submitted charges, allowed amount, Medicare payment and standardized payment. Provider demographic/beneficiary summary fields vary by table. The by-provider-only file is a separate aggregate (2024 has 1,296,739 rows and 81 columns).
- Years, cadence, lag: Annual, 2013 to 2024 for the by-provider-and-service series. Latest CY2024 version created May 2026, around 17 months after calendar-year close. The previous vintage is retained as separate annual data versions.
- Join IDs: `Rndrng_NPI`/rendering NPI is a direct join to NPPES. `HCPCS_Cd` supports code selection. Taxonomy/specialty is useful for peer grouping, not proof of eligibility for a service. The by-service file describes rendering billing provider, not referring provider.
- Coverage and suppression: 100% final-action Original Medicare FFS Part B claims in the reporting population, not Medicare Advantage, Medicaid or commercial. CMS suppresses counts associated with 10 or fewer beneficiaries and redacts sensitive small-cell values. Annual aggregation cannot distinguish medically appropriate from inappropriate procedures.
- Cost and terms: CMS labels the dataset a free Public Use File. Use of the public file does not require an account or payment. The CMS API response was live-tested with a `filter[HCPCS_Cd]` query returning rows. [CMS dataset/API metadata](https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider/api-docs). [CMS data dictionary](https://data.cms.gov/resources/medicare-physician-other-practitioners-by-provider-and-service-data-dictionary).

### 2. Medicare Part D Prescribers, by Provider and Drug

- Source and access: [CMS dataset](https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/medicare-part-d-prescribers-by-provider-and-drug), free CMS data API/download. CY2024 version UUID `9552739e-3d05-4c1b-8eff-ecabf391e2e5` in CMS's public data catalog. API uses the version UUID.
- Scope and fields: Prescriber NPI × drug brand/generic name. Prescription fills (including refills), standardized 30-day fill counts, days supply and total drug cost. Prescriber demographics/specialty/address are included or are available in related provider-level summary. Updated NPPES/specialty sourcing can vary for providers with no Part B claims.
- Years, cadence, lag: Annual. Public years 2013 to 2024. Latest CY2024 page was created May 2026 (~17 months after year end). CMS says the series is typically updated once per year.
- Join IDs: `Prscrbr_NPI` directly joins to NPPES and Medicare physician table. CMS warns the Part D and Part B populations differ: some people have one benefit without the other. Drug names are descriptive text, not a billing code.
- Coverage, suppression and interpretation: Medicare Part D prescription drug events submitted by plans for people with Part D coverage and a valid NPI. CMS redacts some information to protect privacy. Total drug cost includes payer, beneficiary and third-party amounts and is not just the Medicare payment. This cannot identify beneficiary-level overprescribing or establish medical necessity. [CMS Part D methodology](https://data.cms.gov/sites/default/files/2026-05/MUP_DPR_RY26_20260421_Methodology_508.pdf).
- Cost and terms: Free Public Use File, no account. Download/API routes are public CMS routes. No paid product needed.

### 3. Medicare Durable Medical Equipment, Devices & Supplies (DMEPOS)

- Source and access: [CMS DME series](https://data.cms.gov/provider-summary-by-type-of-service/medicare-durable-medical-equipment-devices-supplies). Useful products are by Referring Provider and Service (orderer NPI × HCPCS × supplier-rental indicator), by Supplier and Service (supplier NPI × HCPCS × rental indicator), and aggregate by referring provider or supplier. CMS API docs show the `/dataset/{uuid}/data` route. Current 2024 version IDs: provider (version UUID `f24ef7ea-c773-4ad6-80db-7345cb7e521d` per API docs), referring-provider-and-service (`86b4807a-d63a-44be-bfdf-ffd398d5e623` in CMS catalog), and current supplier/service product is listed on the CMS series page.
- Scope and fields: NPI, provider demographics, HCPCS, rental indicator, beneficiary counts, services, charges, allowed amounts and Medicare payments. Referrer identifies the ordering/referring clinician. Supplier identifies the furnishing/payee provider. Analyze those roles separately.
- Years, cadence, lag: Annual. Current files include CY2024. CMS published referring-provider file in July 2026 (roughly 19 months after year end). Other DME service tables may have earlier releases, so check each product's version page.
- Coverage, suppression and caveats: Original Medicare FFS Part B DMEPOS claims only. Does not cover Medicare Advantage or non-Medicare payers. CMS excludes aggregate records derived from 10 or fewer beneficiaries. CMS states this may not represent the provider's broader practice. NPPES demographics are sampled after the reporting year, so addresses can lag/reflect a later registry state. [CMS DME methodology](https://data.cms.gov/sites/default/files/2025-06/a837dcf7-3d06-4c1f-8d4a-82ee737b7932/MUP_DME_RY25_Methodology_20250617_508.pdf).
- Cost and terms: Free CMS Public Use File. No sign-in or purchase required.

### 4. HHS Medicaid Provider Spending by HCPCS (new public dataset)

- Source and access: [HHS Open Data page](https://opendata.hhs.gov/datasets/medicaid-provider-spending/). Page embeds three public static artifacts, no query API listed: CSV (11.55 GB), zipped CSV (3.76 GB), Parquet (3.07 GB). The direct CSV URL is `https://stopendataprod.blob.core.windows.net/datasets/medicaid-provider-spending/2026-02-09/dataset/medicaid-provider-spending.csv`. No account required. I issued an HTTP byte-range request and verified its header and sample rows.
- Scope and fields: Jan 2018 to Dec 2024, national all states/territories. Grain is billing-provider NPI × servicing-provider NPI × HCPCS × claim month. Fields: `BILLING_PROVIDER_NPI_NUM`, `SERVICING_PROVIDER_NPI_NUM`, `HCPCS_CODE`, `CLAIM_FROM_MONTH`, `TOTAL_PATIENTS`, `TOTAL_CLAIM_LINES`, `TOTAL_PAID`. Uses outpatient/professional claim lines with populated HCPCS. CMS/HHS describes fee-for-service, managed-care encounters and CHIP. The dataset page says claims are finalized and adjustments/orphans handled as documented.
- Years and lag: Initial release Feb. 9, 2026, about 13 months after end of latest 2024 month. No later release/version was listed as of audit date. HHS calls 2024 preliminary and subject to change while states finalize T-MSIS submissions.
- Join IDs: NPI columns can join to NPPES and the Medicare provider data. The billing and servicing NPI columns can be blank. Procedure code and month align conceptually to code/time analysis but differ in payer, aggregation and reporting logic. A separate HHS provider-enrollment-segments extract overlaps Jan. 2018 to Dec. 2024. Inspect its documented keys before joining.
- Coverage, suppression and data risks: HHS suppresses rows with fewer than 12 claim lines or fewer than 12 beneficiaries. T-MSIS state submission/data quality and code practices vary. Live sample sanity check exposed `TOTAL_PAID` around $6.5 trillion for an example NPI/code/month with 8,403 lines/874 beneficiaries. This can be bad units/source values or another artifact and blocks payment-based ranking until validated. The `TOTAL_PAID` field must be reconciled to state-specific source semantics and line-level sums. Missing provider NPI also means public file cannot always attribute claims to a named clinician.
- Cost and terms: Free static public file. Downloadable without login. Large files make local compute/storage a real cost even though data access is free. HHS page carries artifact SHA-256 checksums.
- Companion public Medicaid files: [HHS catalog](https://opendata.hhs.gov/dataset/medicaid-provider-spending) lists Medicaid Provider Spending by NDC (billing NPI × prescribing NPI × NDC × month), Medicaid Provider Enrollment Segments, and Revoked Medicare Providers and Suppliers. They were not individually range-sampled in this pass. Investigate their fields/artifact size and matching keys before use.

### 5. Medicare Post-Acute Care (PAC) PUF, home health, hospice and related facilities

- Source and access: [CMS PAC & Hospice series](https://data.cms.gov/provider-summary-by-type-of-service/medicare-post-acute-care-hospice), free public data/API. Current CMS data catalog UUIDs: HHA by Geography/Provider CY2024 `43ef03ce-2b60-40a8-958e-146195b5fec7`. HHA by Geography, Provider and Service CY2024 `6c63099b-0794-40a0-925c-51a66b9b9901`. Hospice by Geography/Provider FY2024 `4e73f1b5-82cb-4682-8ad2-28493f0b6840`. Query route: `https://data.cms.gov/data-api/v1/dataset/{uuid}/data`.
- Scope and fields: CMS's 2026 methods say HHA data are CY2014 to 24 and hospice, SNF, IRF and LTCH generally FY2014 to 24. Records include provider/CCN, provider name/state/city/ZIP, beneficiaries, episodes/stays, service days, charges, allowed amount, Medicare and standardized payments, and care/utilization/demographic categories. HHA has a supplemental provider × service/case-mix grouping view. Hospice's provider-level aggregate contains total charges/allowed/payment and beneficiary/care characteristics.
- Join IDs: Provider ID is the 6-digit CMS Certification Number (`PRVDR_ID`/CCN), not NPI. Join to CMS provider enrollment, Care Compare, PECOS All Owners and cost reports by CCN. Avoid fuzzy name-only joins when a CCN exists. HHA all-owner dataset's `ENROLLMENT ID` and `ASSOCIATE ID` are PECOS identifiers and do not equal NPI.
- Lag and suppression: RY26 methodology was posted August 2026 for CY/FY2024. Annual summary. Likely lag about 20 months for CY2024 and variable by reporting year. Claims-derived small beneficiary counts are suppressed. Hospice public-file documentation states providers with 10 or fewer Medicare beneficiaries are excluded and small derived cells are set missing. Check the HHA/hospice methodology before using any specific suppression flag.
- Coverage: Medicare FFS public use, not all-payer claims. Hospice data reflects Medicare's hospice claims/utilization. CMS has also publicly reported some characteristics based on hospice PUF/PAC PUF. [RY26 PAC methodology](https://data.cms.gov/sites/default/files/2026-08/338c40d4-05f7-4339-9ef8-0a7834fcf538/MUP_PAC_RY26_Methodology.pdf). [HHA data dictionary](https://data.cms.gov/sites/default/files/2025-08/1ddc73a0-90e4-42cc-9bfc-5811139c7dbc/Medicare%20PAC%20Utilization%20-%20HHA%20by%20GeographyProvider%20and%20CMG%20Data%20Dictionary%202020%20-%202023.pdf).
- Live test: Both the HHA 2024 and hospice FY2024 APIs returned JSON rows with plausible national totals and the published schema.
- Cost and terms: Free CMS Public Use File. API call does not require a paid service.

### 6. NPPES / NPI registry

- Source and access: [CMS NPI downloadable files](https://download.cms.gov/nppes/NPI_Files.html), [NPI Registry API](https://npiregistry.cms.hhs.gov/api-page). V2 monthly full replacement, weekly increments and monthly deactivation files are public. October 12, 2026 V2 monthly full file was listed at 1,106 MB. Version 1 ceased being supported March 3, 2026. Use V2. Public registry API is `https://npiregistry.cms.hhs.gov/api/?version=2.1&number={NPI}`.
- Scope/fields: NPI, individual/entity type, legal and other names, mailing/practice locations, taxonomy, enumeration/deactivation, authorized official for Type 2 entities and linked separate practice location/other name/endpoint reference files. Monthly full replacement is the most complete state. Weekly file is incremental, not standalone.
- Join ID and limits: NPI is the principal join ID across CMS files. NPI issuance does not ensure a professional is licensed or credentialed. Taxonomy is registrant-selected and not independently verified as proof of specialty. Registry has no claims or ownership graph. The facility/organization NPI is often not the rendering clinician's NPI.
- Live test: The registry API returned current names, addresses, and taxonomy for NPI 1003000126. The full V2 bulk archive is documented at more than 1 GB and was not downloaded in full during this audit.
- Cost and terms: Free public access/no API key. Follow CMS/NIH bulk download guidance. Do not treat registry fields as verified credentials. [CMS NPI Files](https://download.cms.gov/nppes/NPI_Files.html), [NPI Registry API](https://npiregistry.cms.hhs.gov/api-page), [CMS Data Dissemination](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination).

### 7. PECOS ownership and change-of-ownership extracts

- Source and access: CMS Provider Characteristics > [Hospitals and Other Facilities](https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities) publishes All Owners/enrollment/CHOW tables. Direct current HHA All Owners CY/Q4 2026 API version UUID `87e65a9e-3695-4b48-bd5c-4d5f4dfc7f08` (Oct. 19, 2026). SNF All Owners October 2026 UUID `afe44b85-cc6d-40d7-b5df-00ae8910d1d2`. CMS also lists Hospice All Owners, Hospital All Owners, HHA/Hospice/SNF enrollments and certain CHOW owner records. Tables are free and queryable from CMS Data API.
- Fields/joins: For HHA/similar extracts: `ENROLLMENT ID`, `ASSOCIATE ID`, provider legal name. Owner associate ID, owner type/role, association date, first/middle/last name or organization name/DBA, address, percentage ownership, and owner category flags including PE, REIT, investment firm, holding company, management-services company. Join provider to relevant enrollment files/CCN or CMS public enrollment record. Owner IDs are PAC IDs, not NPI. Where current data publishes both 6-digit CCN and enrollment IDs, confirm with the dataset's guidance/dictionary before stitching.
- Coverage/time: HHA, hospice and SNF owner rows concern Medicare-enrolled facilities. Snapshots are quarterly or monthly and historical versions may be available in the API. Ownership is provider self-reported through PECOS. CMS has suspended the previous Jan 2026 expanded SNF ownership-report deadline, so missing owner fields and under-reporting matter. These extracts do not disclose all owners of individual physicians or all commercial practice entities.
- Live test: The current SNF API returned JSON. The current HHA API returned JSON and one owner-linked record. Data includes IDs, owner role and name, and ownership percentage. CMS owns this data. No fee or login is required.
- Interpretation: Strong use is connecting repeat owners across eligible facility corporations and checking public quality/penalties. It does not demonstrate improper billing. [SNF All Owners overview](https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/skilled-nursing-facility-all-owners). [HHA All Owners API/data](https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/home-health-agency-all-owners/api-docs). [PECOS CMS enrollment page](https://www.cms.gov/medicare/enrollment-renewal/providers-suppliers/chain-ownership-system-pecos).

### 8. HHS-OIG List of Excluded Individuals/Entities (LEIE)

- Source and access: [OIG LEIE page](https://oig.hhs.gov/exclusions/exclusions_list.asp?hero=leie-hero). Full active-exclusions CSV: `https://oig.hhs.gov/exclusions/downloadables/UPDATED.csv`. Monthly exclusion/reinstatement supplements are also posted. OIG recommends replacing the full local file each month or correctly applying both supplements. No public API is planned.
- Fields and join: Last/first/middle or business name, general/specialty, UPIN, NPI (where available), DOB, address/city/state/ZIP, exclusion type/date, reinstatement/waiver fields. NPI is useful for join but not universal. Full-file and monthly refreshes only present exclusions currently in effect. No historical status timeline beyond archived monthly supplements (OIG archives only the previous 12 months).
- Live test: The full CSV downloaded successfully (10.8 MB), and its header and sample rows were inspected. The latest full file linked on the page is free to download without logging in.
- Hard limitation: LEIE CSV deliberately omits SSNs and EINs. OIG says final identity verification must use SSN/EIN through its online query. A name match by itself is not enough. A list hit is an exclusion fact, not proof of fraud in a particular payment.
- Cost and terms: Free. Monthly updates are generally available by the 10th/middle of the month. [LEIE instructions](https://oig.hhs.gov/exclusions/leie-quick-tips-instructions/), [record layout and downloads](https://oig.hhs.gov/exclusions/exclusions_list.asp?hero=leie-hero).

### 9. California physician licenses and discipline

- Source and access: [Medical Board of California Public Information](https://www.mbc.ca.gov/Resources/Statistics/Public-Information.aspx), [online physician/license lookup](https://www.mbc.ca.gov/Resources/Medical-Resources/doctor-information.aspx), and DCA [Search API access page](https://search.dca.ca.gov/api). One-at-a-time public lookup is online. Board bulk physician/surgeon and outpatient-surgery-setting databases are free Microsoft Access downloads, but delivered by Box after a request form. DCA Search API applications need approval before keys work.
- Fields and joins: Board bulk file includes public physician license details and discipline. No NPI is collected by the Medical Board, so join using state license number/name, not NPI. MBC public discipline documents include accusations, decisions, suspension orders, public reprimands and citations. MBC says discipline documents stay online 10 years after received. Resolved citations generally 5 years, then obtainable on request.
- Update and coverage: Physician/surgeon file refreshed Tuesday mornings. Outpatient surgery settings monthly. MBC records cover California licensees and public board actions, not all criminal/civil investigations. License number or exact identity match needed. Same names create false matches.
- Access test/status: I opened the public DCA lookup and searched the Medical Board of California, license type Physician’s and Surgeon’s, first name Harold, last name Tabaie. The page returned “0 RESULTS.” This was only one board/name query. It is not evidence that the person has no California license or has no discipline. The experiment’s NPI-to-person identity is confirmed from NPPES only. California licensure was not independently confirmed. License 20A4475 has not been checked against the appropriate board and may belong to the Osteopathic Medical Board, so use the correct board and known license number before drawing any conclusion. Bulk files and DCA API remain restricted by an administrative request/approval step (not payment): the Board sends a Box invite after processing a request. DCA application status is pending until approved. No request/account/API approval was attempted.
- Cost and terms: MBC calls bulk data free. API has an access approval process. [MBC public-info page](https://www.mbc.ca.gov/Resources/Statistics/Public-Information.aspx), [MBC finding information about a doctor](https://www.mbc.ca.gov/Resources/Medical-Resources/doctor-information.aspx), [DCA API instructions](https://search.dca.ca.gov/api), [DCA API guide](https://iservices.dca.ca.gov/docs/iservice_user_guide.pdf).

### 10. CMS Open Payments (Sunshine Act)

- Source and access: [Open Payments data overview](https://www.cms.gov/priorities/key-initiatives/open-payments/data) and [CMS Dataset Explorer](https://openpaymentsdata.cms.gov/datasets). Full program-year data are downloadable as ZIP/CSV. Viewer allows filtering/export and API access per dataset. PY2025 currently available. CMS reports 17.07 million records / $14.67B for that program year.
- Fields and join: General, research and ownership/investment transfers from applicable manufacturers and GPOs to covered physicians, teaching hospitals, and covered non-physician practitioners. Current reporting schema includes covered recipient NPI for physician/NPP, individual/group-related fields, state license numbers, reporting company, date, nature-of-payment category, value, product/device and context fields. Use the physician's NPI (not group NPI) where present. Name/license state+number are secondary checks. This resolves a conflict in older 2024 CMS FAQs that said NPI was absent. Current CMS reporting guide includes `COVERED_RECIPIENT_NPI`.
- Years and lag: Detailed searchable data 2019 to 2025. Archived downloads cover 2013 to 18. Full prior-year publication by June 30 and refresh in January, so PY2025 was published June 2026 (~6 months after year end), with a scheduled correction cycle in January 2027. Current Search Tool shows latest seven years.
- Coverage, thresholds and interpretation: Only statutory reporting entities and covered recipient categories. Reporting thresholds are indexed (for PY2025 $13.46 per individual transfer or aggregate $134.54 annual threshold). Data may include food, travel, consulting, research, royalties, ownership and other transfers. It is not all physician income and does not prove a kickback, referral or clinical bias. Pre-publication provider review/disputes are voluntary. Records may be corrected in later publication.
- Cost and terms: Full data is free to download without payment. CSV bundles can be large. [CMS methodology/data dictionary](https://www.cms.gov/files/document/open-payments-methodology-and-data-dictionary-document-june-2025.pdf), [CMS PY2025 data page](https://www.cms.gov/priorities/key-initiatives/open-payments).

### 11. Federal cases and enforcement records: CourtListener / RECAP

- Source and access: [CourtListener RECAP Archive](https://www.courtlistener.com/recap/) and [Free Law Project RECAP project](https://free.law/recap/). Search/view is free. CourtListener has APIs for dockets/documents, but automated API usage may require an account/token. The RECAP fetch API can pull material from PACER and is distinct from free already-archived files. Do not assume fetch is free because PACER fees can apply.
- Coverage and limits: Federal district/bankruptcy/appellate PACER material submitted by users, plus public opinions. The archive is not a complete mirror of PACER, contains what users have captured, and sealed/nonpublic material cannot be used. State cases (including California state-court files) require the applicable state court system and may be restricted or fee-based. A hit is a filing/docket clue, not a finding of liability. Read the disposition and current status.
- Cost/terms/status: Basic public search and archived downloads free. Some PACER access is charged by federal judiciary. No PACER purchase was made in this audit. API conditions/keys should be checked at [CourtListener API docs](https://www.courtlistener.com/help/api/). We did not run an API query for a specific enforcement case. This source is documented, not sample-tested.

## Data that exists but is not a free public claims source

- CMS Limited Data Set (LDS) / Medicare claims files: CMS makes beneficiary-level Standard Analytical Files (including carrier, DME, home health, hospice, outpatient and inpatient) available only to approved research organizations under an organization-level Data Use Agreement through the EPPE request process. Current CMS instructions also require an approved Data Management Plan Self-Attestation Questionnaire (DMP SAQ). The LDS DUA requires CMS review and fees. Approved files are delivered through the Chronic Conditions Warehouse Secure File Transfer System (SFTS). The current instructions do not establish that all analysis must occur in the Virtual Research Data Center (VRDC), so this audit does not characterize VRDC as a mandatory workspace. CMS's current fee page lists, for example, DME, hospice, home-health and SNF SAF rates in the hundreds to thousands of dollars depending on year/file size. This is a restricted, paid research source, not part of the free public inventory. We did not apply or obtain files. [CMS LDS request process and fees](https://www.cms.gov/data-research/cms-data/data-available-researchers/requesting-limited-data-sets-lds-files), [LDS file list](https://www.cms.gov/data-research/cms-data/data-available-researchers/limited-data-set-lds-files), [LDS SAF files](https://www.cms.gov/data-research/files-for-order/limited-data-set-lds-files/standard-analytical-files-medicare-claims-lds).
- Medicare Blue Button API: It exposes a beneficiary's own Medicare A/B/D claims only after that beneficiary authorizes an approved application. CMS production credentials require application approval and the data is per-user. The developer sandbox has synthetic records. This does not let an outsider query arbitrary providers or beneficiaries. We did not register or request production access. [CMS Blue Button API](https://bluebutton.cms.gov/api-documentation/), [production access](https://bluebutton.cms.gov/production-access/).

## Practical conclusion

The completed Medicare/Medicaid and facility-screening prototype used free public CMS/HHS files. That experiment's no-purchase condition does not restrict future research. The current research scope includes government sources available by request and options costing less than $10,000. See [government data access](government-data-access.md) for access terms and limits. A narrow, code-specific Medicare FFS screen with provider identity, discipline, and exclusion checks remains the strongest near-term public-data path. Public records lack patient-level diagnoses, clinical notes, referral communications, and payer adjudication context. They can locate outliers, but cannot prove a false claim or establish reward eligibility. The new Medicaid source expands payer coverage, but should not be used for financial outlier scoring until its extraordinary payment values are reconciled. Public-record investigation and a legally compliant whistleblower submission are later steps. An anomaly score alone cannot produce them.


## 12. Medicare Part A hospital utilization

- Source: [Official source](https://data.cms.gov/data.json)
- Scope and data structure: Annual hospital aggregate by CMS Certification Number (CCN) and diagnosis-related group (DRG)
- Latest period: FY2024
- History: CMS lists historical years in its catalog. This check tested 2024 only
- Cadence and lag: Published annually. The current catalog publication date varies by release.
- Join identifiers: CCN, DRG, and year
- Useful fields: Discharges, average covered charges, and total and Medicare payments
- Coverage and limits: Original Medicare inpatient hospital aggregates. The file has no patient charts or evidence of medical necessity. Suppression applies.
- Access status: tested
- Access route: [Access route](https://data.cms.gov/data-api/v1/dataset/ca9b5ef0-1386-4759-b2b6-5f9b35116786/data?size=1)
- Cost and terms: Free public CMS API
- Verification: A sample was retrieved after an initial access failure. The raw response is saved.


## 13. Medicare Part B hospital outpatient utilization

- Source: [Official source](https://data.cms.gov/data.json)
- Scope and data structure: Annual hospital aggregate by CCN and ambulatory payment classification (APC)
- Latest period: CY2024
- History: CMS lists historical years in its catalog. This check tested 2024 only
- Cadence and lag: Published annually. See catalog metadata for release dates.
- Join identifiers: CCN, APC, and year
- Useful fields: Beneficiaries, Comprehensive APC services, average charges, and Medicare payments
- Coverage and limits: Institutional hospital outpatient payments, not the physician component. There is no patient-level linkage. Suppression applies.
- Access status: tested
- Access route: [Access route](https://data.cms.gov/data-api/v1/dataset/771e94a2-cd8f-4702-a9d7-8f777f363938/data?size=1)
- Cost and terms: Free public CMS API
- Verification: A sample JSON response was retrieved and saved.


## 14. Medicare Advantage encounter sources

- Source: [Official source](https://download.cms.gov/encounter_data/medicare%20advantage%20encounter%20data%20analytical%20methods%20June%202026%20Final.pdf)
- Scope and data structure: Public utilization summaries and restricted detailed research encounters
- Latest period: Varies by product
- History: 2026 methods reviewed. No raw research file obtained
- Cadence and lag: Varies
- Join identifiers: CCN, NPI, and encounter fields where released. The record-level detail varies by file.
- Useful fields: Public summaries include utilization measures and institutional service events. Detailed files require separate access.
- Coverage and limits: MA encounter completeness and deduplication are limitations. Do not assume the FFS PUF covers all MA services. The methods specifically limit home-health service measures.
- Access status: documented/restricted for detailed files
- Access route: [Access route](https://download.cms.gov/encounter_data/medicare%20advantage%20encounter%20data%20analytical%20methods%20June%202026%20Final.pdf)
- Cost and terms: The methods are free. Detailed research-identifiable files require approved access, which was not requested.
- Verification: Official methods were opened. No raw MA file was downloaded.


## 15. Private insurance pricing disclosures

- Source: [Official source](https://www.cms.gov/newsroom/fact-sheets/transparency-coverage-final-rules-cms-9882-f)
- Scope and data structure: Rates by plan, network, and provider, plus selected out-of-network payment disclosures
- Latest period: Current plan releases vary
- History: Rules have been enforced since 2022. Source documents were checked in 2026.
- Cadence and lag: Current releases and future 2026-rule changes have separate applicability dates
- Join identifiers: Payer or plan, provider identifiers, and billing code where populated
- Useful fields: Negotiated rates, out-of-network allowed amounts, and billed charges
- Coverage and limits: These are not a universal ledger of paid claims and do not provide complete patient-level utilization. Future taxonomy and utilization files are not assumed to be live.
- Access status: documented
- Access route: [Access route](https://www.cms.gov/initiatives/healthplan-price-transparency/overview/public-data)
- Cost and terms: Public files are free but can be very large. No paid tool was authorized.
- Verification: CMS's official explanation and 2026 fact sheet were opened. Insurer bulk files were not downloaded.


## 16. California all-payer database

- Source: [Official source](https://hcai.ca.gov/data/request-data/hpd-data-access-and-release/)
- Scope and data structure: Approved access can include claims or encounters, eligibility, and provider data. Separate public aggregate reports are available.
- Latest period: 2018 to 2024 files are requestable under current documentation
- History: Files covering 2018 to 2024 are requestable. Public-report periods differ.
- Cadence and lag: Current documentation describes an annual lag of about 15 months.
- Join identifiers: Provider and plan/patient linkage fields subject to release approvals
- Useful fields: Medical and pharmacy claims, with charged and paid amounts in approved files
- Coverage and limits: Public reports differ from detailed nonpublic data. Approvals, use limits, and fees apply. Clinical charts are not included.
- Access status: Detailed data is restricted. Public reports are documented.
- Access route: [Access route](https://hcai.ca.gov/data/request-data/hpd-data-access-and-release/)
- Cost and terms: Application and release fees apply as documented. No request or payment was made.
- Verification: The official access page was opened. No nonpublic files were obtained.


## 17. California Medicaid directory and aggregate rates

- Source: [Official source](https://www.dhcs.ca.gov/medi-cal-fee-for-service-comparative-payment-rate-analysis/)
- Scope and data structure: An enrolled-provider directory for fee-for-service (FFS), plus separate aggregates for selected service codes
- Latest period: Current directory. The CPRA page links to a 2025 report.
- History: Release-specific. No bulk extract obtained
- Cadence and lag: Directory at least quarterly per DHCS. CPRA periodic
- Join identifiers: NPI in the directory where populated, and billing codes in CPRA
- Useful fields: Provider enrollment and contact context, selected-service rates, and aggregate claims and beneficiaries
- Coverage and limits: The directory does not show paid claims. CPRA has not been established as a provider billing extract. The linked report could not be retrieved, so its details remain unverified.
- Access status: Documentation reviewed. The linked extract was not tested.
- Access route: [Access route](https://www.dhcs.ca.gov/providers-partners/provider-directory-requirements-for-medi-cal-fee-for-service-providers/)
- Cost and terms: Public documentation. No account or payment was used.
- Verification: DHCS pages were opened. The linked CPRA data file could not be retrieved.
