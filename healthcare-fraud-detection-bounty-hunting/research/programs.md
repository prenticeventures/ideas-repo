# U.S. healthcare fraud reward routes for a public-data researcher

Research date: October 25, 2026. This is a screen of possible payment routes, not legal advice or a prediction that a report or lawsuit will qualify. No agency was contacted and no report was filed.

## Which routes may pay an outsider?

| Route | When it may pay | Fit for a solo researcher using public data |
|---|---|---|
| Federal False Claims Act (FCA) | A person files a sealed lawsuit on the United States' behalf and the government or relator recovers money. The usual share is 15 to 25% if DOJ takes the case, or 25 to 30% if DOJ declines and the relator wins. A separate rule may cap the share at 10% if the government takes a case based mainly on specified public disclosures. | This route offers the largest potential recovery, but it requires a lawsuit, not a paid tip. The case needs specific evidence of false claims. A lawyer must file and pursue it for the United States. |
| DOJ Criminal Tip Rewards Pilot (WHIP) | DOJ may pay $10,000 to $30,000 for a distinct tip that leads to an unsealed criminal charge. No minimum loss or forfeiture is required. DOJ expects payment around the time charges are filed. | This is the most direct fit for a solo analyst if the analysis reveals a useful fact that was not generally known. Only individuals qualify. DOJ decides whether to pay and requires cooperation. |
| DOJ Corporate Whistleblower Awards Pilot (CWA) | DOJ may pay from money taken from criminal conduct after a final forfeiture. The award can be up to 30% of the first $100 million, up to 5% of the next $400 million, and nothing above $500 million. The case must produce more than $1 million in net proceeds. | A public-record analysis may qualify if it reveals an insight not generally known. The conduct must fit a listed corporate crime area, including certain federal health offenses or fraud against patients and other private parties in healthcare. Payment follows forfeiture and may take years. |
| CMS Medicare reward | CMS may pay up to 10% of recovered Medicare overpayments or $1,000, whichever is less. It pays only after all overpayments, fines, and penalties are collected, and only if another law does not provide a reward. | This is a small tip reward. The report must identify a specific person or organization and time period. It will not qualify if the subject is already under government review or investigation. |
| State False Claims Acts | State rules vary. A successful case may pay a percentage of the state's recovery. | Check the state law separately. HHS-OIG's approval list measures eligibility for a federal Medicaid funding incentive. It is not a complete list of state laws. See the [state screening file](state-programs.csv). |
| Private insurance reports | Insurer investigation units, insurance departments, and police generally accept tips without promising payment. | Two state laws allow some private insurance fraud lawsuits: California's Insurance Frauds Prevention Act and Illinois's Insurance Claims Fraud Prevention Act. Their eligibility rules make them uncertain routes for an outside researcher. |

## Federal False Claims Act

| Screen | Summary |
|---|---|
| Who can file | A person, including an organization, may bring a case for the United States. The relator need not work for the target. |
| Lawyer | Yes. A nonlawyer cannot represent the United States in the federal case. |
| Main requirements | File a detailed lawsuit under seal, give the government the evidence, and identify specific false claims. Public-disclosure and first-to-file rules may block the case. |
| Potential payment | 15 to 25% if the government proceeds, or 25 to 30% if it declines and the relator wins. A separate rule may cap the share at 10% in certain cases based mainly on public disclosures. |

### Further details

The FCA lets a private person file a lawsuit on the United States' behalf. This type of case is called a qui tam case. The relator is the person who brings it. The law does not require the relator to work for the company being sued, and its definition of “person” can include an organization. The complaint and supporting evidence are filed under seal, which means the defendant is not notified at first. The government gets at least 60 days to review the case and often asks for more time. DOJ may take over, decline, or join the case later.

There is no payment just for sending a tip. The government or relator must recover money. The normal share is 15 to 25% if DOJ proceeds, and 25 to 30% if DOJ declines and the relator wins. A separate statutory rule allows a share of no more than 10% when the court finds an intervened case is based mainly on specified public disclosures other than information the relator provided. That 10% rule is separate from the public-disclosure bar and its original-source exception. See [31 U.S.C. § 3730](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title31-section3730), especially subsections (b), (d), (e)(4), and (f).

The public-disclosure bar can block a case when substantially the same allegations or transactions already appeared in a federal hearing, a congressional or GAO report, another federal report or investigation, or news media. Unless DOJ opposes dismissal, the court must dismiss a barred case unless DOJ brings it or the relator qualifies as an original source.

The law has two original-source paths. A person may qualify by voluntarily giving the information to the government before it becomes public. Someone who learned the information independently may also qualify by adding an important fact to public allegations and voluntarily giving that information to DOJ before filing. A public-data researcher should identify the new fact their method uncovered, not just say they are skilled at analyzing records. The complaint must also describe the fraud in detail and identify false claims. Outlying billing statistics alone may not show that any claim was false.

If the case succeeds, a relator may recover necessary expenses and reasonable attorney fees and costs from the defendant. The government does not advance case expenses. A relator who litigates after DOJ declines can face the defendant's fees if the case was clearly frivolous, vexatious, or brought mainly to harass. A lawyer is required to pursue the case for the United States. In the Ninth Circuit, Stoner held that a nonlawyer cannot represent the United States in a qui tam case pro se. See [Stoner v. Santa Clara County Office of Education](https://cdn.ca9.uscourts.gov/datastore/opinions/2007/09/07/0415984.pdf).

The House Office of the Law Revision Counsel preliminary version of §3730 used here says it contains laws in effect on September 10, 2026. That is the latest official date checked, not a guarantee that no later amendment has occurred.

### What the public-data cases show

- Integra and Providence: Integra was not affiliated with Providence and relied mainly on its statistical analysis of CMS claims data. It did not have insider medical records. The Ninth Circuit issued an unpublished, nonprecedential decision in 2021. It found Integra had not plausibly shown the claims were false because Providence might simply have been better at compliant documentation and coding. It reversed the denial of dismissal and sent the case back. The panel did not decide whether online news media counted as a public disclosure. [Ninth Circuit memorandum](https://cdn.ca9.uscourts.gov/datastore/memoranda/2021/03/31/19-56367.pdf).
- Integra and Baylor Scott & White: The Fifth Circuit affirmed dismissal of an upcoding case based on public Medicare data and statistical comparisons. The data were also consistent with lawful explanations, and the complaint lacked concrete facts showing why the claims were false. Statistical outliers alone did not establish falsity. [Fifth Circuit opinion](https://www.ca5.uscourts.gov/opinions/unpub/19/19-50818.0.pdf).
- Silbersher and Allergan: A patent lawyer used public patent records and other government records to argue that patents obtained through fraud delayed generic competition and raised public drug costs. The Ninth Circuit said patent prosecution could count as a federal hearing for the public-disclosure bar, then sent the case back. It did not decide whether Silbersher was an original source. On remand, the district court found he was not an original source, and the Ninth Circuit affirmed in an unpublished 2025 decision. [2022 published opinion](https://cdn.ca9.uscourts.gov/datastore/opinions/2022/08/25/21-15420.pdf), [2025 disposition](https://cdn.ca9.uscourts.gov/datastore/memoranda/2025/01/29/23-15613.pdf).
- Silbersher and Valeant: The Ninth Circuit reversed dismissal because the public records did not themselves disclose the key fact he assembled: the defendants took conflicting positions in patent proceedings. This is a narrow example of a public-record analysis adding a missing fact. It does not create a general exception to the public-disclosure bar. [2023 published opinion](https://cdn.ca9.uscourts.gov/datastore/opinions/2023/08/03/20-16176.pdf).

The business takeaway is that public data can identify a lead, but a viable FCA case needs evidence that explains why specific claims were false and addresses plausible lawful explanations. The FCA's original-source test is different from the “original information” tests used in DOJ's CWA and WHIP. Qualifying under one program does not qualify someone under another.

## DOJ Criminal Tip Rewards Pilot (WHIP)

| Screen | Summary |
|---|---|
| Who can report | An individual. Companies cannot receive awards. The tipster must not have meaningfully participated in the crime and must cooperate. |
| Lawyer | No for a named report. Yes for an anonymous report. DOJ must verify the tipster's identity before payment. |
| Main requirements | Send truthful, complete, original information in writing. Public-data analysis may qualify if it reveals a useful fact not generally known, materially adds to what DOJ knows, and leads to criminal charges. |
| Potential payment | Discretionary $10,000 to $30,000 per distinct tip, usually at or around an unsealed criminal charge. No minimum loss or forfeiture. |

### Further details

DOJ calls the program the Criminal Tip Rewards Pilot Program. Its press release uses the name Fraud Whistleblower Incentive Program, or WHIP. The three-year pilot began October 20, 2026. It covers federal healthcare crimes and related crimes involving health benefit programs, fraud against patients and others in healthcare, and fraud against listed federal benefit programs. DOJ highlights hospice, home health, day care, and special-services or autism care fraud. DOJ says state or local program fraud may qualify when federal programs ultimately bear part of the loss, even if the fraud did not initially target a federal program.

Only an individual can receive an award. The tip must be truthful, complete, written, and original. The person must cooperate and must not have meaningfully participated in the crime, subject to a narrow DOJ exception for minimal participation. “Original information” can include independent analysis of public information if it reveals something not generally known or available. The information must be nonpublic, not already known to DOJ, and add materially to what DOJ knows if the agency has related information.

DOJ says a tip must be specific, credible, and timely. It must cause DOJ to open or reopen an investigation, or to examine distinct conduct in an existing investigation, and then lead to criminal charges. The usual payment trigger is an unsealed indictment, information, or criminal complaint. There is no minimum loss or forfeiture. DOJ expects awards of $10,000 to $30,000 for each distinct tip, but both the award and whether tips are distinct are discretionary. More than one person may qualify. DOJ expects payment at or around charges, not when the tip is submitted.

A named tip does not require a lawyer. An anonymous tip requires a lawyer, and DOJ must verify and learn the tipster's identity before paying. DOJ says it will protect identifying information except where law or policy requires disclosure, including possible disclosure to a defendant in a proceeding. It may share tips with other enforcement agencies. The program terms say they create no enforceable right to an award. DOJ says WHIP eligibility does not prevent a later award under another program, including CWA. The unresolved business questions are how DOJ will define a distinct tip, how often awards will be paid, and how long payment will take in practice. See [DOJ WHIP terms](https://www.justice.gov/fraud/national-fraud-enforcement-division-criminal-tip-rewards-pilot-program), [FAQs](https://www.justice.gov/fraud/criminal-tip-rewards-pilot-program-faqs), and the [October 20 announcement](https://www.justice.gov/opa/pr/justice-department-announces-innovative-whistleblower-rewards-program-combat-fraud).

### Additional findings for an outside healthcare analyst

The [WHIP deep dive](../WHIP-RESEARCH.md) reviews the complete terms and live first intake step. Two material wording questions remain: the originality rule contemplates new information in an existing investigation, while the voluntary rule requires the absence of a government investigation. Professional-source exceptions also overlap with a separate exclusion for audit, accounting, compliance and internal-investigation information. These are unresolved questions, not blanket exclusions for every healthcare employee.

The first form step limits the narrative to 2,000 characters and displays up to five attachments of 50 MB each. Later signature and contact steps were not inspected. DOJ may deny a reward solely for reporting outside its established portal. Cooperation can require testimony and further investigative work.

A reported launch example has no independently verified completed payment or DOJ award determination in this review. See the [rules reference](whip-rules-reference.md), [form inspection](whip-submission-route.md) and [track record](whip-track-record.md).

## DOJ Corporate Whistleblower Awards Pilot (CWA)

| Screen | Summary |
|---|---|
| Who can report | An individual with original information about qualifying company-related crimes. |
| Lawyer | No for a named report. Yes for an anonymous report. DOJ must verify the person's identity before payment. |
| Main requirements | Public-record analysis may qualify if it reveals information not generally known and materially adds to what DOJ knows. The case must fit a listed corporate crime area and produce more than $1 million in net forfeiture proceeds. |
| Potential payment | DOJ may award up to 30% of the first $100 million, up to 5% of the next $400 million, and nothing above $500 million. It pays only after forfeiture. |

### Further details

The three-year pilot began August 1, 2024 and is scheduled for review in August 2027. It covers company-related federal healthcare offenses and related crimes involving health benefit programs. It also covers certain fraud against patients, investors, and other private parties in healthcare. Private insurance fraud may fit if the conduct meets the program's corporate and criminal requirements. This is a DOJ criminal forfeiture program, not a civil reward for private insurance claims.

An individual submits original information in writing through the [DOJ portal](https://www.justice.gov/criminal/criminal-division-corporate-whistleblower-portal/). A public-record analysis may qualify if it reveals information not generally known or available. The information must be nonpublic, unknown to DOJ, and materially add to what DOJ has if the agency already has related information.

The case must produce more than $1 million in net proceeds deposited in the Assets Forfeiture Fund. Forfeiture means the government takes money or property tied to the crime. DOJ pays only after that happens. DOJ may award up to 30% of the first $100 million, up to 5% of the next $400 million, and nothing above $500 million. The maximum is shared across award recipients. DOJ presumes an award at the maximum rate on the first $10 million when an award is appropriate and no reduction factors apply. Awards remain discretionary. DOJ considers the information's value, cooperation, internal reporting, the person's role or culpability, delay, and overlapping awards. The current guidance permits a person to qualify even if another program could pay for the same conduct, but DOJ says it will not pay twice for the same recovery and may reduce or deny an award for overlap.

A named submission does not require a lawyer. Anonymous submissions require one, and DOJ must learn and verify the person's identity before payment. DOJ may disclose identifying information when required by law or policy or to a defendant in a proceeding. CWA payment is less predictable and usually later than WHIP because the case must end in forfeiture. A person must claim an award within 90 days after DOJ publishes a successful forfeiture notice. The guidance says it creates no enforceable award right. See [current DOJ guidance](https://www.justice.gov/criminal/media/1454776/dl), [pilot overview](https://www.justice.gov/criminal/criminal-division-corporate-whistleblower-awards-pilot-program), and [FAQs](https://www.justice.gov/criminal/whistleblower/frequently-asked-questions).

## CMS Medicare reward, 42 C.F.R. § 420.405

| Screen | Summary |
|---|---|
| Who can report | Any person, subject to exclusions for some government or law-enforcement employees, people who learned the facts through official duties, participants, and people who obtained information illegally. |
| Lawyer | The reward rule does not require one. The report must include contact information to claim payment. |
| Main requirements | Identify a specific person or organization and time period. The subject cannot already be under government review or investigation when the tip arrives. Another law must not provide a reward. |
| Potential payment | Discretionary, up to 10% of Medicare overpayments recovered or $1,000, whichever is less. Payment follows collection of all overpayments, fines, and penalties. |

### Further details

CMS may pay a discretionary reward if information leads to recovery of at least $100 in Medicare funds from sanctionable fraud or abuse. The reward is available only if another law does not provide one. The report must identify a specific person or organization and time period. No reward is available if CMS, its contractors, OIG, DOJ, FBI, or another federal, state, or local law enforcement agency was already reviewing or investigating the subject when the tip arrived.

Any person may qualify, with exclusions for certain HHS, DOJ, and law-enforcement employees and their close family, officials who learned the information through their government duties, people who obtained it illegally, and people who participated in the misconduct. CMS may pay up to 10% of recovered Medicare overpayments or $1,000 total, whichever is less. Multiple eligible tipsters share the reward. CMS pays only after it collects all overpayments, fines, and penalties. The amount depends on the tip's value, CMS pays no interest, and a reward is not guaranteed. CMS says it will keep the tipster's identity confidential except where law requires disclosure. Report to OIG or the Medicare contractor responsible for the case and provide contact information to claim a reward. Source: [42 C.F.R. § 420.405, 2025 CFR](https://www.govinfo.gov/content/pkg/CFR-2025-title42-vol3/pdf/CFR-2025-title42-vol3-sec420-400.pdf). This is the latest official annual compilation checked. Confirm whether a later rule changed it.

## State laws and California examples

The [state-programs.csv](state-programs.csv) file lists all 50 states and the District of Columbia. It combines HHS-OIG's Medicaid False Claims Act review status with a screening of state laws and identified information rewards. OIG approval means a state meets federal criteria for a 10-percentage-point increase in its share of Medicaid recoveries. The review checks Medicaid liability, a working qui tam process, at least 60 days for state review, and FCA-level penalties. It does not tell whether a particular person can sue and it does not list every state law.

As of October 25, 2026, OIG listed 24 approved states, five states it did not approve, and no decision for 21 states. D.C. was not listed. The file marks statutes supported by current primary sources separately from those taken from the 2023 National Association of Medicaid Fraud Control Units inventory. “Not verified” means we did not confirm the current code. It does not mean the state has no law. Sources: [HHS-OIG State FCA Reviews](https://oig.hhs.gov/fraud/state-false-claims-act-reviews/) and [2023 NAMFCU inventory](https://www.naag.org/wp-content/uploads/2023/04/NAMFCU-Statistics-2023.pdf).

### California False Claims Act

| Screen | Summary |
|---|---|
| Who can file | A private person may sue for California, including over Medi-Cal claims. Public-disclosure rules and special rules for some insiders may limit eligibility. |
| Lawyer | This requires a civil lawsuit. Counsel is practically needed. The research did not verify a California-specific rule that every relator must have counsel. |
| Main requirements | File under seal and give the Attorney General or prosecutor the evidence. Publicly disclosed allegations may bar the case unless an original-source exception applies. |
| Potential payment | 15 to 33% if California proceeds, or 25 to 50% if it declines and the relator wins. |

### Further details

California's False Claims Act covers false claims involving state or local public money, including Medi-Cal claims. A private person can sue for the state. The case begins under seal with evidence sent to the Attorney General or prosecutor. If the state proceeds, the relator's share is 15 to 33%. If the state declines and the relator wins, the share is 25 to 50%. Publicly disclosed allegations may block the case unless the relator meets an original-source exception. Some insiders outside Medi-Cal cases may need to report through their employer first. California's Attorney General identifies the law as a route for private Medi-Cal fraud cases. Sources: [Cal. Gov. Code §12652](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=12652.), [California DOJ Medi-Cal private-fraud laws](https://oag.ca.gov/dmfea/laws/private_fraud), and [HHS-OIG approval letter](https://oig.hhs.gov/documents/state-false-claims-act-reviews/643/ca2019.pdf).

### California private insurance law

| Screen | Summary |
|---|---|
| Who can file | A qualifying “interested person” may sue over specified insurance fraud, including health insurance fraud. Personal injury is not required, but public-data access alone does not establish eligibility. |
| Lawyer | This requires a civil lawsuit. Counsel is practically needed. The research did not verify a California-specific rule that every relator must have counsel. |
| Main requirements | Serve the county district attorney and Insurance Commissioner. A separate public-disclosure rule applies. |
| Potential payment | 30 to 40% if a public authority joins, or 40 to 50% if it declines and the relator wins. |

### Further details

The Insurance Frauds Prevention Act allows a qualifying “interested person” to sue over specified insurance fraud, including health insurance fraud. If a public authority joins the case, the relator receives 30 to 40%. If the authority declines and the relator wins, the share is 40 to 50%. The relator must serve the county district attorney and Insurance Commissioner. They have 60 days to decide whether to join, and can ask for more time.

The public-disclosure rules are separate from the federal FCA. California appellate courts say the relator need not have suffered personal injury, but still must qualify as an interested person. The public-disclosure bar also aims to prevent lawsuits that simply repackage public allegations. A public-data analyst should not assume eligibility just because this law covers private health insurance. The official [California Insurance Code §1871.7](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=INS&sectionNum=1871.7.) was checked in the normal browser on October 25, 2026. The [Alzayat decision](https://law.justia.com/cases/california/court-of-appeal/2017/e066471.html), [Weitzman decision](https://law.justia.com/cases/california/court-of-appeal/2003/b151252.html), and [Discovery Radiology decision](https://law.justia.com/cases/california/court-of-appeal/2023/b315264.html) explain parts of the eligibility and public-disclosure rules. Award allocation still depends on the case and statute.

## Other federal rewards need a separate violation

IRS and SEC rewards do not pay for healthcare billing fraud by itself. They may apply if the same facts also show a tax or securities violation.

### IRS Whistleblower Award Program

| Screen | Summary |
|---|---|
| Who can file | An individual with specific, credible, and timely information about tax underpayment or another law enforced by the IRS. A healthcare billing lead alone is not enough. |
| Lawyer | No for a named claim. The applicant must identify themself and personally sign Form 211. |
| Main requirements | Submit Form 211 before the IRS acts based on the information. Public-source information may lead to a reduced award. |
| Potential payment | Generally 15 to 30% of proceeds actually collected. Mandatory awards require more than $2 million in disputed proceeds and, for an individual taxpayer target, gross income above $200,000 in a year at issue. Otherwise, IRS may consider a discretionary award. |

### Further details

A person with specific, credible, and timely information about tax underpayment or another law enforced by the IRS can submit Form 211. IRS generally pays 15 to 30% of proceeds it actually collects. The mandatory award track applies only when disputed proceeds exceed $2 million. If the target is an individual taxpayer, that person must also have had gross income above $200,000 in a year at issue. Below those thresholds, IRS may consider a discretionary award.

IRS says it may reduce awards based on public-source information. We found no public-analysis safe harbor. The applicant must identify themself and sign Form 211 under penalty of perjury. IRS protects identity only as law allows. Payment can wait years for final tax determinations, appeals, and collection. IRS guidance says to file Form 211 before the IRS acts based on the information. Sources: [IRS claim instructions](https://www.irs.gov/help/submit-a-whistleblower-claim-for-award), [Publication 5251, revised August 2026](https://www.irs.gov/pub/irs-pdf/p5251.pdf), and [IRS Internal Revenue Manual](https://www.irs.gov/irm/part25/irm_25-002-002).

### SEC Whistleblower Program

| Screen | Summary |
|---|---|
| Who can file | An individual who voluntarily provides original information about a possible securities-law violation. Healthcare billing fraud alone does not qualify. |
| Lawyer | No for a named tip. Yes for an anonymous tip seeking an award. |
| Main requirements | Public-record analysis must reveal an insight not generally known or apparent from the records. Submit Form WB-APP within 90 days after the SEC posts a Notice of Covered Action. |
| Potential payment | 10 to 30% of money collected in a successful SEC action with more than $1 million in sanctions. |

### Further details

The SEC program covers possible securities-law violations, not healthcare billing fraud by itself. An eligible individual who voluntarily submits original information may receive 10 to 30% of money collected in a successful SEC action with more than $1 million in sanctions. Public-record analysis can qualify if it reveals a useful insight that was not generally known and was not apparent from the records. Simply pointing the SEC to public records does not qualify.

Tips go through the SEC TCR portal or Form TCR. To seek an award, submit Form WB-APP within 90 days after the SEC posts a Notice of Covered Action. A named tip does not require a lawyer. Anonymous award submissions require one. The SEC may have to disclose identity in some circumstances. Sources: [SEC whistleblower program](https://www.sec.gov/enforcement-litigation/whistleblower-program), [FAQs](https://www.sec.gov/enforcement-litigation/whistleblower-program/whistleblower-frequently-asked-questions), [submission instructions](https://www.sec.gov/enforcement-litigation/whistleblower-program/information-about-submitting-whistleblower-tip), and [FY2025 annual report](https://www.sec.gov/files/fy25-annual-whistleblower-report.pdf).

## State information rewards

| State route | Who can claim | Lawyer | Main gate | Potential payment |
|---|---|---|---|---|
| Florida Medicaid report reward | A person with original information about another person's criminal Medicaid fraud. | No lawsuit is required to report. A counsel requirement was not identified in the statute reviewed. | The report must go to a listed state agency and lead to a fine, penalty, or forfeiture. The state pays only if funds are available. | The state may pay up to the lesser of 25% of the recovery or $500,000. Florida bars an FCA award for the same fraud after the person takes this reward. |
| Texas Medicaid report award | An individual. | No lawsuit is required to report. A counsel requirement was not identified in the statute reviewed. | Disclosure must cause a recovery, and the agency or Attorney General must not already know. A Texas Medicaid FCA relator is ineligible. | The agency may award up to 5% of the qualifying remedy, at its discretion. |
| Kansas public-funds informant reward | Any person who first gives the information to the Attorney General. Government employees are generally excluded unless the information is unrelated to their work. | No lawsuit is required to report. A counsel requirement was not identified in the statute reviewed. | The AG must certify the information was previously unknown and materially contributed. Payment follows a state judgment or conviction. | The AG may award up to $5,000, at their discretion. |
| Arkansas Medicaid information reward | A person whose information helped detect false Medicaid claims. Assigned government employees and contractors are excluded. | A person may need to petition a court if the AG does not. Whether counsel is legally required was not verified. | Civil penalty recovery. Restitution cannot fund the award. Current 2025 code text was checked on a secondary code host. | A court may award up to 10% of collected civil penalties. The 2025 text reviewed states no dollar cap. |
| Louisiana Medicaid information reward | Qualifying informant. Prior agency knowledge, involvement in the conduct and certain public duties can disqualify the person. | No private lawsuit is required. A mandatory counsel requirement was not identified. | Information must lead to recovery. Funding must be appropriated. | Secretary may approve up to $2,000. Current rule verified, but funding and actual payments were not established. |
| California Medi-Cal information reward | Any person with specific information tied to a Medi-Cal provider conviction. Public employees and contractors cannot be paid for information learned through their duties. | No lawsuit is required to report. A counsel requirement was not identified in the statute reviewed. | Information must identify the activity, actor, and time period and lead to at least $100 in recovery. Payment follows collection of all recoverable funds. | The Department of Justice may award up to the lesser of 10% of recovered restitution or $1,000, at its discretion. |

### Further details
Some states have separate payments for useful information. These are not general cash bounties for sending a lead. Each has its own subject, novelty, recovery, and eligibility requirements. The [state index](state-programs.csv) lists them separately from HHS-OIG's state FCA approval status.

- Florida: A person who provides original information about another person's criminal Medicaid fraud and reports it to a listed state agency may receive a reward if the report leads to a fine, penalty, or forfeiture. The award is subject to available funds and capped at the lesser of 25% of the recovery or $500,000 per case. A person who receives this reward cannot also receive Florida FCA money for the same Medicaid fraud. [Fla. Stat. §409.9203](https://www.flsenate.gov/Laws/Statutes/2025/409.9203).
- Texas: The Health and Human Services Commission may award an individual up to 5% of a remedy recovered after a report of Medicaid fraud, abuse, or overcharges. The agency or Attorney General must not already know about the activity. A person who brings a Texas Medicaid FCA case cannot receive this separate award. The award provision took effect April 1, 2025. [Tex. Gov't Code §544.0205](https://statutes.capitol.texas.gov/Docs/GV/pdf/GV.544.pdf) and [Hum. Res. Code ch. 32](https://statutes.capitol.texas.gov/Docs/HR/pdf/HR.32.pdf).
- Kansas: The Attorney General may pay up to $5,000 for information first provided to the AG about Medicaid fraud, false claims, or another law protecting public funds. The information must be previously unknown to the AG and materially contribute to an investigation. Payment is discretionary and comes only after a state judgment or conviction. Most government employees are excluded unless the information is unrelated to their job. [K.S.A. 75-727](https://www.kslegislature.gov/b2025_26/laws/075_000_0000_chapter/075_007_0000_article/075_007_0027_section/075_007_0027_k/).
- Arkansas: A court may award up to 10% of collected civil penalties for information that led to detection of Medicaid false claims. The 2025 code text reviewed has no dollar cap. Restitution cannot fund the award. The AG may ask the court to pay an informant after a civil penalty recovery or agree to pay up to 10% of civil penalties in a settlement. If the AG does not petition, the person may petition. Government employees and contractors assigned to refer or investigate Medicaid fraud are excluded. This is not a general right to bring a state lawsuit based on public data. The official code text was not located, so the [2025 code mirror](https://law.justia.com/codes/arkansas/title-20/subtitle-5/chapter-77/subchapter-9/section-20-77-911/) was used. The 2023 SB515 proposal to cap rewards at $10,000 was withdrawn and not enacted. The official [bill status](https://arkleg.state.ar.us/Bills/Detail?ddBienniumSession=2023%2F2023R&id=sb515) confirms this.
- Louisiana: The current official code contains §4605, which permits the secretary to approve a reward up to $2,000 for information resulting in recovery. Payment depends on appropriated funds and is discretionary. Section 4607 excludes previously known information, participants, certain Medicaid-excluded people and public-duty reporters. The rule was promulgated in May 2026. Funding and actual payment history were not established. Sources: [La. R.S. 46:440.2](https://www.legis.la.gov/legis/Law.aspx?d=100879), [current official Title 50](https://www.doa.louisiana.gov/media/ogee2gb4/50.docx) and the [preserved rule excerpt](access-evidence/louisiana-lac-title50-section4605-excerpt-2026-10-25.txt). Older 10% formulas are not the current rule.
- California: The Department of Justice may award up to the lesser of 10% of recovered restitution or $1,000 for information that leads to recovery of at least $100 in Medi-Cal funds. The information must identify the activity, actor, and time period. It must relate to conduct that led to a Medi-Cal provider conviction. Employees and contractors cannot be paid for information learned through their duties. Payment waits until all recoverable funds are collected. DOJ's decision on eligibility, amount, and timing cannot be appealed. The official [Welfare and Institutions Code §14107.12](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=WIC&sectionNum=14107.12.) was checked in the normal browser on October 25, 2026.

Two other statutes we checked do not pay an outside reporter. Missouri Rev. Stat. §191.905(12) may reduce a defendant's civil penalties if the defendant promptly reports and cooperates. It is not a reporter reward. [Missouri Revisor](https://revisor.mo.gov/main/OneSection.aspx?section=191.905). Ohio Rev. Code §5162.21 concerns recovery of Medicaid costs from an estate, not an informant payment. [Ohio Revised Code](https://codes.ohio.gov/ohio-revised-code/section-5162.21). This is a limited check of these candidate statutes, not proof that no other state reward exists.

A solo researcher should not assume any of these state rewards will be paid. Terms differ on whether information must be original, new to the agency, or cause a recovery. Payment may be discretionary, and work-related public employees may be excluded. Check each statute's overlap rules before counting an award on top of an FCA share. Florida bars an FCA payment for the same Medicaid fraud after its information reward. Texas excludes Medicaid FCA relators from its separate report award.

## Private insurance: reporting and reward distinctions

| Screen | Summary |
|---|---|
| Who can report | Insurer investigation units, state insurance departments, and law enforcement accept reports under their own intake rules. |
| Lawyer | No lawyer is needed to send a tip. Civil lawsuits under state statutes are different and need legal review. |
| Main requirements | A tip may prompt an investigation but does not create a right to payment. The eight insurer pages reviewed did not advertise cash rewards. Louisiana law allows a possible reward fund, but current operation was not confirmed. |
| Potential payment | The insurer pages reviewed advertised no cash reward. Louisiana law permits a possible reward fund, but current operation was not confirmed. WHIP and CWA may apply to qualifying criminal conduct, but neither pays a general share of private insurance recoveries. |

### Further details
The [payer comparison and eight insurer reporting-page checks](payer-coverage.md) compare funding source, advertised cash terms, noncash customer rewards, and ordinary reporting. They cover only the pages reviewed, not every insurer program.

The insurer pages reviewed did not advertise a cash bounty. They are reporting channels with no established payment entitlement. State insurance hotlines also do not promise a share of a recovery. DOJ's CWA may pay later if the facts meet its corporate-crime requirements and lead to more than $1 million in net forfeiture. WHIP may pay after criminal charges if its scope and causation rules are met. Neither program pays a general percentage of private insurance recoveries.

### Illinois private insurance law

| Screen | Summary |
|---|---|
| Who can file | An “interested person” may sue over listed private-insurance fraud or kickbacks. A patient with no personal injury or role in billing was found ineligible. |
| Lawyer | This requires a civil lawsuit. Counsel is practically needed. The research did not verify an Illinois-specific rule that every relator must have counsel. |
| Main requirements | The statute has its own Attorney General or prosecutor notice, public-disclosure, and eligibility rules. A public-data analyst without direct involvement is a weak fit. |
| Potential payment | The relator receives at least 30% if the Attorney General or State's Attorney takes the case, or at least 40% if the government declines and the relator wins. In some public-disclosure cases, the court may reduce the share to 10% or less. |

### Further details

California's IFPA is described above. The Illinois Insurance Claims Fraud Prevention Act covers specific private-insurance fraud and kickbacks. If the Attorney General or State's Attorney takes the case, the relator receives at least 30%. If the government declines and the relator wins, the relator receives at least 40%. In some public-disclosure cases not based on information the relator supplied, the court may reduce the share to 10% or less. The law requires an “interested person,” not simply any person. In Feingold, an Illinois appellate court found a patient who had no personal injury and no role in billing was not an interested person. Leibowitz treated an employee who learned about alleged insurer fraud at work differently. A researcher with no direct involvement is a weak fit unless they meet the statute's eligibility test. See [Illinois ICFPA](https://www.ilga.gov/Legislation/ILCS/Articles?ActID=2039&ActName=Insurance+Claims+Fraud+Prevention+Act.&ChapAct=740%EF%BF%BDILCS%EF%BF%BD92%2F&ChapterID=57&ChapterName=CIVIL+LIABILITIES), [Feingold appeal](https://www.illinoiscourts.gov/Resources/4f5c7068-7bac-49af-8924-33dd758fe1e3/1181560_R23.pdf), and [Leibowitz opinion](https://www.illinoiscourts.gov/files/124754.pdf/opinion).

### Louisiana insurance-fraud reward fund

| Screen | Summary |
|---|---|
| Who can report | A person with information sufficient to help secure a conviction for insurance fraud. Law enforcement, insurance commissioner employees, insurer employees, and insurance professionals are excluded. |
| Lawyer | A lawyer is not needed to report. The statute does not describe a lawsuit by the informant. |
| Main requirements | The statute says state police may create a fund using voluntary contributions from insurers and insurance professionals. This review did not confirm that the fund operates or accepts reports. |
| Potential payment | The statute gives no amount or payment schedule. Treat this as authority for a possible program, not an active reward. |

### Further details

Louisiana law allows the state police to set up an insurance-fraud reward fund with voluntary insurer and insurance-industry funding. The fund may pay for information that leads to a conviction. This review did not confirm that the fund currently operates, has money, or accepts reports. Treat it as a possible legal authority, not an active bounty. Law enforcement, insurance commissioner employees, insurer employees, and insurance professionals are excluded. [La. R.S. 40:1426](https://www.legis.la.gov/Legis/Law.aspx?d=97486). California's Department of Insurance says it handles suspected insurance-fraud referrals, but that statement does not promise a reward. [California Department of Insurance](https://www.insurance.ca.gov/01-consumers/105-type/95-guides/15-gen/insur-fraud-is-felony.cfm).

## Practical limits across programs

- Lawsuits: FCA complaints begin under seal, but the relator's identity may become public later. The government can extend its review. If DOJ declines, the relator may have to fund and run the case against the defendant. A successful relator may recover fees and costs, but no law guarantees a lawyer will take the case or advance expenses. No program guarantees payment. No standard market fee was verified. The fee arrangement is negotiated. No attorney was contacted for this research.
- DOJ tips: A named WHIP or CWA report does not require a lawyer. An anonymous report does. Anonymous reporting still requires DOJ to learn the person's identity before payment. DOJ may share information or disclose identity when required by law or in a proceeding.
- Medicare: CMS needs contact information to pay a reward. Identity protection is subject to law. The cap and late payment trigger make this a small, delayed reward.
- Multiple programs: WHIP says a person may qualify for another program, including CWA. CWA may reduce or deny overlapping awards and will not pay twice for the same recovery. CMS pays only when another law does not already provide a reward. FCA first-to-file and public-disclosure rules may independently block a later case. One evidence package may fit more than one program, but the rules do not guarantee multiple payments for the same recovery.

## Sources and limits

Sources are linked where each claim appears. They include federal statutes and regulations, DOJ program rules and FAQs, HHS-OIG review letters, state laws, and court opinions. Case descriptions are limited to what the opinions decided. For example, the Ninth Circuit's Silbersher decision on Allergan addressed the public-disclosure bar and did not decide whether he was an original source.

The state screen does not infer that a state lacks a law because OIG has no approval decision. Federal FCA text was checked through the House Office of the Law Revision Counsel preliminary edition noted above. The 2025 CFR compilation is the latest official annual compilation used for CMS. The official California CFCA, IFPA, and Medi-Cal reward provisions were checked in the normal browser on October 25, 2026. Automated access failed, but browser access succeeded. State law and agency program terms may change. Confirm current requirements before relying on a route.
