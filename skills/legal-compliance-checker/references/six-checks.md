# Six checks

Inspired by [Suraj Sharma's six-risk post](https://x.com/suraj_sharma14/status/2107478486227071360)
on October 6, 2026. Use its categories, not its blanket liability claims or
penalty arithmetic. Verify current primary sources during each audit.

## 1. Children's privacy: COPPA

Determine audience, collection of personal information (including relevant SDK
identifiers), and actual knowledge of under-13 users. General-audience apps do
not automatically violate COPPA because signup lacks an age question. Asking
age can create actual knowledge; a child-directed service cannot simply evade
obligations by declaring users must be older.

Where applicable, inspect neutral age screening where appropriate, collection
before screening or parental consent, verifiable parental consent, parental
notices and rights, SDK disclosures, minimization, security, and retention.
Verify the current amended rule and separate consent requirements. An age gate
alone is not a complete COPPA solution. Avoid collecting full birthdates when a
less intrusive implementation supports the chosen policy.

Sources: [FTC COPPA FAQ](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions)
and [2025 final rule](https://www.govinfo.gov/content/pkg/FR-2025-04-22/html/2025-05904.htm).

## 2. Third-party fonts and resource disclosure

Find remote font stylesheets, font files, CSS imports, framework font loaders,
and other automatic third-party resource requests. Inspect actual requests:
build-time font downloads may produce self-hosted assets and no visitor request.
Account for IP addresses and other transmitted information, existing notices,
vendor relationships, and applicable privacy laws.

US-only apps have no blanket GDPR font-hosting mandate. For EU/UK or other
markets, read [international scope](international.md). Consider licensed local
hosting as a data-minimizing fix; verify no residual remote import, rendering,
weights, and license compliance. Report this as mitigation unless an applicable
legal requirement has been established.

## 3. Session replay and interception risk

Identify replay SDKs, tag managers, server/proxy collection, vendor access,
sampling, and default startup timing. Inspect signup, checkout, chat, and forms
for passwords, health/financial details, message bodies, and other sensitive
data. Determine what is collected, who receives it, and when consent occurs.

California CIPA and other interception/privacy rules require fact-specific
analysis; SDK presence alone does not prove unlawful wiretapping. Consent,
party/vendor roles, communication type, and current case law matter. Do not
state automatic liability per session. Disable unnecessary replay or ensure
appropriate prior consent and exclusion of sensitive inputs before collection.
Verify no replay traffic before required consent, refusal/revocation behavior,
and raw payload masking. Masking alone does not resolve consent or interception
questions; escalate unresolved legal interpretation to counsel.

Source: [California Penal Code section 631](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=631.&lawCode=PEN).
Research current relevant decisions for the actual implementation.

## 4. Marketing email: CAN-SPAM

Inventory campaigns, launch announcements, onboarding sequences, templates,
provider defaults, and mailing-list suppression. Classify messages by primary
purpose; promotional content may change classification of a mixed message.
Do not add marketing to essential account messages as a workaround.

For commercial email, inspect accurate sender and subject information,
required advertising identification, valid physical postal address, clear
opt-out, and operational suppression. Verify opt-outs are honored within the
current statutory period (FTC guidance: 10 business days), the mechanism stays
available for the required period, and vendors honor the same suppression.
Do not require login, payment, or unnecessary personal information to opt out.
CAN-SPAM does not impose a universal US prior-opt-in requirement; international
markets may impose additional consent rules. Test using fixtures or authorized
test recipients; a footer link without suppression behavior is a gap.

Source: [FTC CAN-SPAM business guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business).

## 5. Subscriptions and automatic renewal

Determine consumer markets, contract dates, billing channels, trials, renewal
periods, price changes, and cancellation paths. Check federal ROSCA and
applicable state laws, including California when relevant. Verify the legal
status of any FTC negative-option rule before citing it: the 2024 expanded rule
was vacated and must not be treated as active merely because older guidance
describes it.

Inspect clear material terms before billing information is collected, express
informed consent before charging, and a simple cancellation mechanism. For
California, verify current requirements for proximate renewal terms, affirmative
consent and records, acknowledgments, reminders/notices, and cancellation under
the version applicable to the contract. Check mobile/store and hosted-payment
flows too. A billing provider does not prove the merchant has met its duties.
Test actual cancellation and future-charge prevention. Do not promise automatic
refunds or characterize every subscription violation as an unconditional gift.

Sources: [ROSCA](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section8403&num=0&edition=prelim),
[California renewal statute](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=17602.&lawCode=BPC),
[California AG guidance](https://oag.ca.gov/node/608083), and
[FTC negative-option rule status](https://www.ftc.gov/legal-library/browse/rules/negative-option-rule).

## 6. User uploads and DMCA safe harbor

Inventory public/private uploads, comments, avatars, shared files, and imported
content; determine the relevant section 512 safe harbor rather than assuming
every app needs an agent. For hosting user content and seeking section 512(c)
protection, verify the operator's actual Copyright Office designation, matching
entities/alternate names, public contact details, and renewal status. A page
claiming registration is insufficient.

Check notice-and-takedown and counter-notice handling, repeat-infringer policy
and implementation, and other applicable safe-harbor conditions. Registration
alone does not establish eligibility; lacking it does not automatically prove
infringement or damages. Check current fees and renewal intervals at filing time
instead of hardcoding the post's figures. Prepare registration instructions and
identify the responsible owner; do not submit a filing or invent agent details.

Sources: [Copyright Office section 512 resources](https://www.copyright.gov/512/index.html)
and [designated-agent FAQs](https://www.copyright.gov/dmca-directory/faq.html).
