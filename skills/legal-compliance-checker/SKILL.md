---
name: legal-compliance-checker
description: >-
  Audit an app's legal and compliance implementation before launch or after
  changes to signup, tracking, email, billing, or user uploads. Check six common
  risks with US-first jurisdiction scoping and targeted international coverage.
---

# Legal Compliance Checker

Produce an evidence-backed engineering audit of six risks: children's privacy,
third-party fonts, session replay, marketing email, subscription renewals, and
copyright safe harbor for user uploads. These are a focused launch checklist,
not a complete legal certification. Explain concrete gaps and remediation;
reserve disputed legal interpretations and business decisions for counsel.

## Scope jurisdictions first

Most apps reviewed with this skill serve the United States only. Default to a
**provisional US-only scope**, including applicable state laws; do not default
to California-only or silently apply every international regime.

Inspect product documentation, storefront availability, checkout countries,
marketing, existing customers, operator establishments, and data flows. Record
known markets and evidence separately from assumptions. Ask for missing market
or business facts when they affect a finding; continue independent inspection.
An English interface, US incorporation, USD prices, or a US-only statement does
not prove geographic restriction. Public accessibility alone does not establish
GDPR applicability either.

For global apps, identify actual countries or regions rather than treating
“global” as one legal regime. Read [international scope](references/international.md)
when non-US establishment, targeting, users, or monitoring suggests additional
obligations. A US-only product may still send data to overseas processors.

## Inspect and assess

Read [the six checks](references/six-checks.md). Trace relevant frontend,
backend, SDK initialization, deployed configuration, vendor settings, templates,
and user flows. Search with available repository tools; use runtime/browser or
device inspection when needed and authorized. Do not send real marketing mail,
charge customers, or upload sensitive production data to test a flow.

Before asserting a legal requirement, verify current primary sources for the
audit date and applicable jurisdiction. Check effective dates, amendments,
thresholds, exemptions, and relevant court decisions. Distinguish statutes,
regulator guidance, contractual vendor/platform rules, and engineering choices.
The linked sources are starting points, not frozen legal advice. If research or
runtime access is unavailable, identify the resulting uncertainty.

For each of the six checks, record:

- Applicability: applies, does not apply with reason, or unresolved with missing facts.
- Evidence: file and line, observed flow, network request, configuration, or external record.
- Result: verified control, confirmed gap, potential risk, or not verified.
- Action: smallest useful fix, verification method, and any owner or counsel dependency.

Do not label absent evidence a confirmed violation or treat a present policy
page as proof that behavior matches it. Avoid copied penalty figures or
per-user/session multipliers; amounts and liability depend on current law and
facts. Prioritize by exposure, data sensitivity, and reachable behavior, without
inventing dollar estimates or a compliance score.

## Remediation and verification

An audit request authorizes inspection and recommendations. Implement fixes
when the user requests them, using existing project conventions. Do not invent
a postal address, legal entity, age policy, consent wording, retention period,
or registered agent. Prepare concrete proposed changes and identify business
facts needed to finish them. External filings, payments, publication, and
production vendor changes require authorization for those actions.

Test behavior that addresses the finding: pre-consent network activity, blocked
collection paths, unsubscribe suppression, billing consent and cancellation,
or takedown processing. A changed string alone does not verify compliance.
Masking must prevent collection before transmission; hiding data in a replay
viewer is insufficient. Check affected build/type/lint commands as appropriate.

## Deliver the audit

Lead with consequential findings and the market scope. Use a six-row table with
check, applicability, result, evidence, and next action. Follow with prioritized
fixes, completed changes and verification, and unresolved facts requiring an
owner or counsel. Keep verified facts distinct from assumptions. Flag other
material risks encountered (for example state privacy rights, accessibility,
health/financial data, or misleading claims) as outside this checklist rather
than declaring the whole app compliant.
