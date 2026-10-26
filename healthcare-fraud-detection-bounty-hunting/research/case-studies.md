# Two healthcare fraud prosecutions: what public records show

Research cut-off: 25 October 2026. Both cases are pending criminal prosecutions. An indictment records allegations made by a grand jury. It is not a finding of guilt. The defendants are presumed innocent unless proven guilty. The dollar amounts below are allegations, not established losses, restitution, forfeiture, or money recovered.

## 1. Atherectomy case: United States v. Harold Tabaie and Hany Malek

### Who is charged and where the case stands

Harold A. Tabaie is a cardiothoracic surgeon. Hany Malek is a chiropractor. The indictment says they co-owned and operated Angelus Medical Clinic Multi Specialty Group and West Regional Cardio Thoracic and Vascular Surgeons, also known as West Regional Vein Center.

The CMS National Provider Identifier Registry lists Tabaie under individual NPI 1346286663. NPI means National Provider Identifier, a number used to identify a healthcare provider in billing and enrollment records. CMS's 2026 Medicare Revalidation List links that individual NPI to group NPI 1528740024, Southern California Cardiothoracic and Vascular Surgeons. These identifiers help connect public records. The [indictment](https://www.justice.gov/criminal/media/1467741/dl?inline=) does not list NPIs.

The case is in the Central District of California, case 2:26-cr-00668-JFW, before Judge John F. Walter. A grand jury indictment was filed on 20 October 2026 and announced on 22 October. The DOJ case page lists four healthcare fraud counts against Tabaie and Malek, plus two bank fraud counts against Malek. The case was pending with no disposition listed as of 25 October 2026.

The free primary charging record is the DOJ-hosted [17-page indictment](https://www.justice.gov/criminal/media/1467741/dl?inline=). I did not locate a separate public criminal complaint or affidavit.

### What prosecutors allege

The [indictment](https://www.justice.gov/criminal/media/1467741/dl?inline=) alleges a scheme from January 2016 through August 2023 to defraud Medicare through the two clinics. It says Malek met patients, reviewed tests, told patients they needed surgery, and referred them to Tabaie, although Malek was not a medical doctor. Prosecutors allege that Tabaie performed atherectomies on arteries without disease, repeated procedures after prior failures, and used procedures when less invasive options were appropriate.

The indictment also alleges that the defendants offered kickbacks such as transportation, groceries, household goods, utility payments, prescription costs, and $50 to $100 gift cards. It alleges they steered patients into Medicare plans that reimbursed the clinics more, billed some claims under other doctors' names, and split services into separate claims to increase payment. These are allegations, not established facts.

Prosecutors allege that the clinics billed Medicare about $134,955,000 and received at least about $54,817,000. Four illustrative fraud counts describe claims of about $14,000 each, submitted on 29 September 2021, 3 August 2022, 22 November 2022, and 14 September 2023. The indictment also seeks criminal forfeiture if the defendants are convicted. It does not establish a final loss or forfeiture amount.

### How the case was detected

The [DOJ's 22 October Central District announcement](https://www.justice.gov/usao-cdca/pr/la-health-care-fraud-takedown-results-15-defendants-charged-including-six-medical) says data analysis identified Tabaie as an extreme national outlier in Medicare atherectomy billing. The separate DOJ case-status page does not name a detection method. The indictment also does not explain how investigators first found the case or identify their data source.

### What an outside analyst can see

CMS publishes a free Medicare Physician & Other Practitioners file, organized by provider, procedure code, and place of service. It summarizes Original Medicare Part B claims, including service volume, submitted charges, and payments. NPI identifies the provider. HCPCS is the procedure or service code used in billing. Place of service identifies the setting. The file reports grouped totals, not individual claims.

A researcher can use it to look for unusually high provider volume and compare providers in the same specialty, year, and setting. That can produce a lead similar to the outlier signal DOJ described. It cannot establish whether a procedure was medically necessary, who actually performed it, what a patient's condition was, whether a claim was false, or what the defendant knew. The file covers Original Medicare fee-for-service, not commercial insurance or all Medicare Advantage claims. It does not include patient records, imaging, operative notes, referrals, complications, or intent. Small beneficiary counts are suppressed. The indictment also alleges that some claims used other doctors' names, which limits a screen that looks only at Tabaie's NPI.

### Direct code check in public CMS files

The indictment does not list procedure codes or billing NPIs. A retrospective query of CMS's official annual files found Tabaie's active individual NPI in 2021 through 2023 under procedure codes 37225 and 37229. The separate add-on code 37233 also appeared in all three years. This verifies that the codes appear in public claims-derived data during the alleged period. It does not prove these were the codes on the charged claims or that any service was improper.

CMS reports service units, not surgeries. A single procedure may create multiple code units, and add-on units are listed separately. In the table, O is CMS's non-facility place-of-service label. “Primary-code units” combine the published units for 37225 and 37229. Payment and charge amounts below are calculated from CMS's average per-service amounts. They do not come from the indictment.

| Year | Primary-code units, 37225 + 37229 | Separate 37233 add-on units | Estimated Medicare payment for primary codes | Submitted charges for primary codes | National volume rank / vascular-surgery rank |
|---|---:|---:|---:|---:|---:|
| 2021 | 495, from 245 + 250 | 412 | $3,791,675 | $7,175,000 | 12 of 695 / 2 of 271 |
| 2022 | 598, from 293 + 305 | 592 | $3,876,018 | $8,667,000 | 7 of 711 / 1 of 274 |
| 2023 | 429, from 214 + 215 | 380 | $2,667,521 | $6,310,000 | 14 of 695 / 1 of 283 |

The national rank compares combined units for codes 37225 and 37229 among providers with published rows in the same annual file and setting. The specialty rank uses CMS's Vascular Surgery label. The comparison screen covers four primary codes, 37225, 37227, 37229, and 37231. Tabaie had published rows for two of them. Add-on units are excluded from payment, charge, and rank totals. The data suppress small beneficiary groups and cannot show how codes combine for an individual patient. See [target-year-results.csv](../experiment/target-year-results.csv) and [target-code-results.csv](../experiment/target-code-results.csv) for the full screen and its limits.

The NPI Registry API returned one active individual record matching Harold A. Tabaie, MD, with thoracic surgery taxonomies. CMS labels his claims-file specialty as Vascular Surgery. The Medicare Revalidation List separately links his NPI to group NPI 1528740024. These records help match identities. They do not show that a claim was submitted or that anyone acted improperly. Direct CMS API links and the NPI lookup appear in [case-sources.csv](case-sources.csv).

### Were the data available before the charges?

CMS's 22 May 2025 MLN notice confirms that the CY2023 provider-payment and utilization files had been published by that date, before the October 2026 indictment. The catalog snapshot in this experiment was retrieved on 25 October 2026 and shows a CY2023 resource modified on 28 October 2025. That later catalog snapshot is not a copy of the original release. It confirms historical data were available before the indictment, but not that the exact file version or metadata were unchanged since initial publication.

### Any whistleblower or reward?

Neither the indictment nor DOJ's announcement credits a whistleblower or qui tam relator. DOJ names data analysis as the detection method. The records reviewed do not rule out other tips or leads, and they disclose no bounty or qui tam payment for this case.

## 2. Substance-treatment and sober-home case: United States v. Nathan Young et al.

### Who is charged and where the case stands

The principal indictment names Nathan Young, also known as “Pablo,” David Young, also known as “Sancho Lopez,” Honey Phipps, and Cody Phipps. It alleges that Nathan and his father David controlled dozens of facilities, including Rodeo Recovery LLC. It alleges that Honey and Cody Phipps worked as patient brokers and sometimes acted as nominee owners or operators. Rodeo Recovery is one company in the alleged network. The prosecution is not a case against Rodeo alone.

The case is in the Central District of California, case 2:26-cr-00670-PA, before Judge Percy Anderson. The free public copy of the indictment is stamped filed 21 October 2026. DOJ announced the charges on 22 October. The prosecution remained pending as of 25 October. An arrest, indictment, bail condition, or forfeiture allegation is not a conviction or a recovered loss.

The free [42-page indictment](https://www.courthousenews.com/wp-content/uploads/2026/10/usa-young-indictment.pdf) is a court charging document hosted by Courthouse News. The document identifies the court case and filing date. DOJ's takedown announcement summarizes the charges but does not link the indictment. I did not locate a separate public complaint affidavit.

### What prosecutors allege

The [indictment](https://www.courthousenews.com/wp-content/uploads/2026/10/usa-young-indictment.pdf) alleges a scheme from May 2020 through May 2026 in Los Angeles County and elsewhere. It involves private health plans, including Anthem, Aetna, Cigna, and UnitedHealthcare. Prosecutors allege that patient brokers recruited vulnerable people with offers of money, drugs, flights, and housing. They allege that patients were enrolled in better-paying insurance plans even when they were not eligible, then billed for treatment that was unnecessary, deficient, or never provided. The services named include detox, residential treatment, partial hospitalization, intensive outpatient, and outpatient care.

The indictment also alleges that some patients were coached to fake detox symptoms, that large Zoom sessions billed as therapy sometimes provided no therapy, and that some patients were drugged, isolated, or physically prevented from leaving. These are allegations and have not been adjudicated.

Prosecutors allege that the network submitted $1,619,276,243 in claims and received at least $210,274,793 from insurers. Neither amount is a court-established loss, damages award, restitution, or collected forfeiture. The indictment includes three forfeiture allegations, including a San Diego residence. Those requests apply only if the relevant defendants are convicted. The indictment does not say that $1.6 billion or $210 million was recovered.

DOJ separately announced that Nicholas Moore, an alleged area manager in a related case, pleaded guilty and admitted assisting with $199 million in claims. Moore's plea is evidence in his case. It is not a conviction of the four Young and Phipps defendants.

### How the case was detected

DOJ lists the FBI, IRS Criminal Investigation, and DEA as investigating agencies. The takedown announcement includes a general statement from IRS-CI about uncovering complex fraud by following the money. It does not say what triggered this specific case or whether an insurer, public complaint, journalist, or whistleblower brought it to investigators. The indictment describes evidence prosecutors say they gathered, but not how the investigation began.

### What an outside analyst can see

Before the federal indictment, public records included a 2020 nuisance lawsuit by the City of Beverly Hills involving Rodeo Recovery and Nathan Young. The defendants denied the nuisance allegations in their answer. Aetna filed a 2023 federal civil insurance-fraud case involving Young-affiliated companies. Its 2024 amended complaint added Aetna's allegations. Local and national reporting also discussed the industry and, by 2025, a federal investigation.

These records show that allegations and warning signs were public before the indictment. They do not show that federal investigators relied on them, that the allegations were true, or that the civil plaintiffs shared evidence with law enforcement.

An outside researcher can review business and licensing records, civil filings, and news reports. But private insurers do not publish provider-by-procedure claims files like CMS's Original Medicare file. The main questions in this case concern insurance eligibility, payments, actual treatment, attendance, medical necessity, patient identity, broker payments, and money flows. Those depend on private claims, patient records, messages, and financial records. Facility names, patient complaints, news reports, or an insurer's lawsuit are not enough to conclude that a claim was false.

### Any whistleblower or reward?

The indictment, DOJ announcement, and other public records reviewed do not identify a whistleblower who brought the federal case or an award recipient. The prior Aetna and Beverly Hills cases do not prove that a whistleblower started the federal investigation. The source of the case and any reward remain unknown from the public record reviewed.

## What these two cases mean for an outside researcher

The atherectomy case is the more reproducible starting point because DOJ confirms that data analysis found an outlier and CMS publishes relevant Medicare billing summaries. A public screen can flag unusual volume. It cannot establish medical necessity, correct provider identity, intent, or loss.

The substance-treatment case is harder to investigate from public claims data because the alleged payments came from commercial insurers. Public lawsuits and reports existed before the indictment, but their role in the federal investigation is unknown. The core claims and treatment evidence are private.

In either case, a public lead discovered after charges cannot be treated as a new tip. Billed charges and payer payments are different amounts. Neither case's public records reviewed here identify an outsider receiving a reward.
