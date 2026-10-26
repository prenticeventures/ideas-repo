# DOJ WHIP submission route check

Checked October 25, 2026. This is a read-only route inspection. I opened the America.gov report page, followed its generic start prompt, and opened the first intake step. I did not enter tip facts, contact details, or other personal information. I did not attach a file, continue past the first step, or submit a report.

## Route and identity

| Item | What I verified |
|---|---|
| Public entry point | The DOJ says WHIP submissions are received through [America.gov/fraud](https://america.gov/fraud). The landing page has a “Start your report” link. |
| Actual first step | The start link opens an America.gov chat conversation. Clicking its generic “Start” card opened an intake panel in that conversation. The visible page stayed on America.gov. |
| Agency and underlying service | America.gov’s [privacy policy](https://america.gov/privacy-policy) says GSA operates America.gov and that a fraud report opens a form from Treasury’s Fraud.gov service. It says report text, optional contact details, and attachments go directly from the browser to Treasury, bypassing America.gov’s servers and model. DOJ’s [WHIP terms](https://www.justice.gov/fraud/whistleblower) and [FAQ](https://www.justice.gov/fraud/criminal-tip-rewards-pilot-program-faqs) name America.gov/fraud as the portal. |
| Domains and alias | The user-facing route is America.gov. DOJ refers to Fraud.gov as the service, but no separate Fraud.gov page or final form-host domain was exposed before a report description was entered. I did not inspect browser network traffic. Treat the precise Treasury endpoint and whether Fraud.gov is a separate domain or service label as unknown. |

## Fields and constraints visible at the first intake step

| Field or control | What the live first step showed |
|---|---|
| Report narrative | “What raised your concern” is a text area. Its prompt asks what the reporter saw, heard, or read, and suggests including names, dates, amounts, records, how they know, and uncertainty. The field accepts up to 2,000 characters. The visible control did not have a required marker, but Continue was disabled while it was blank. |
| Attachments | The page says up to 5 files, 50 MB each. The file input lists CSV, DOC, DOCX, EML, JSON, JPEG, JPG, MSG, PDF, PNG, TXT, WEBP, XLS, and XLSX. No total submission-size limit, file-retention period, or encryption method for individual attachments was stated in the first step. |
| Contact details | No contact field was visible in the first step. The America.gov landing page says contact details are optional. That message does not describe WHIP anonymity eligibility. |
| Continue | Continue was disabled until a narrative was entered. I did not enter a placeholder to advance because report text may be sent directly to Treasury. |
| Report copy and reference | The public landing page says a submitter receives a reference number and can download a copy. The page’s “DEMO” reference is an illustration, not an actual submission receipt. Actual post-submit behavior was not tested. |

The landing-page workflow illustration lists review fields as “What happened,” “Who was involved,” “Amount,” “Supporting documents,” and “Contact information.” Those are labels in a demonstration. They were not visible as fields on the live first intake step, so I do not treat them as verified live fields.

## Privacy, notices, and certifications

The first step offered a button for a Paperwork Reduction Act notice, not a consent checkbox. The notice identified OMB control number 1505-0284, an expiration date of November 30, 2026, and a 30-minute estimated burden. It says giving information is voluntary and that submitted information may be shared with appropriate federal agencies, Inspectors General, law-enforcement organizations, or other authorized entities for review, referral, investigation, audit, enforcement, recovery, litigation, or other authorized government purposes.

The first step displayed no certification checkbox or signature field. The [DOJ WHIP terms](https://www.justice.gov/fraud/whistleblower) nevertheless say a qualifying tip must be voluntary, truthful, complete, original, and in writing, and describe the submission route as a completed and signed Intake Form. The form screen where any signature or certification is collected was not reached, so the signing mechanism and exact certification wording remain unknown.

The landing page says a name is optional, but WHIP rules qualify that statement. DOJ says a person submitting anonymously must be represented by an attorney, whose submission must certify that the attorney verified the reporter’s identity and reviewed accuracy and completeness with them. A person submitting on their own must provide enough information for DOJ to contact and verify identity. Before any award is paid, the person must disclose identity and DOJ must verify it. The Department may share information with another enforcement agency for a law-enforcement or public-protection purpose. Its confidentiality promise is limited: it will not publicly disclose information reasonably expected to reveal identity except as required by law or policy, or when disclosure to a defendant is required in a proceeding.

## Evidence and use rules that affect an analyst

DOJ terms require original information derived from independent knowledge or independent analysis, non-public and not already known to DOJ, and materially additive to what DOJ already has. Independent analysis may examine public data, but the analysis must reveal information not generally known or available. A public-data report that only repeats a public allegation, published court claim, government report, or news story is not original under the terms unless the reporter was the source. A researcher should document the analytical steps, what the public sources show, what new inference the analysis supports, and what independent corroboration is available.

The reporter must act voluntarily, provide all material facts including their own role, and cooperate with DOJ. The terms exclude information obtained through specified internal compliance, audit, investigation, client-representation, or privileged channels, subject to stated exceptions. They also warn that the reward program does not protect someone from prosecution for unlawfully obtaining information. The form’s first screen does not explain these eligibility requirements, so a narrative that is technically accepted by the portal is not necessarily reward-eligible.

## Follow-up and what remains unverified

America.gov says agencies may contact a reporter who supplies contact information. DOJ’s FAQ says portal submissions are reviewed under the Fraud Division and the reporter may or may not be contacted for more information. If DOJ determines someone may qualify for an award, it says DOJ personnel will contact the person or representative before payment. A report receipt, a reference number, investigator contact, a criminal charge, or an award is not guaranteed by the first-step screen.

I verified only the first narrative-and-attachment step. The later live fields, routing questions, whether the user selects an agency, later contact fields, exact signature or certification screen, final privacy acknowledgment, form validation, and receipt download remain unverified because advancing requires submitting some report content to a form whose privacy policy says it sends data directly to Treasury. No personal details or files were sent.

## Primary sources

- [America.gov fraud reporting page](https://america.gov/fraud)
- [America.gov privacy policy](https://america.gov/privacy-policy)
- [DOJ WHIP terms and conditions](https://www.justice.gov/fraud/whistleblower)
- [DOJ WHIP frequently asked questions](https://www.justice.gov/fraud/criminal-tip-rewards-pilot-program-faqs)
- [DOJ WHIP announcement](https://www.justice.gov/opa/pr/justice-department-announces-innovative-whistleblower-rewards-program-combat-fraud)
