# Phase 2 Manifest

This bundle is initialized for a website-first Career Operator MVP.

## Live Pod

The bundle has been imported into Lemma:

```text
Pod name: career-operator
Pod id: 019f13b1-e825-765d-b506-fc39a4d05cf9
Doctor status: healthy; Phase 4 agent import has no errors
```

## Incorporated Product Changes

The current structure explicitly includes:

```text
Portal/account memory as the main pain point
Credential-safe account guidance
Reusable autofill profiles and fields
Resume Review Studio with accept/reject/manual edit flow
Dashboard tracking website, role, status, resume used, account state, deadlines, and pending actions
Email sync as a first-class system
No mandatory auto-login
No irreversible action without user approval
```

## Phase 3 Datastores

Phase 3 added 17 table schemas:

```text
users
companies
portal_sites
portal_accounts
autofill_profiles
autofill_fields
applications
job_descriptions
resumes
resume_versions
resume_suggestions
resume_change_sets
career_memory
notifications
interview_history
email_updates
application_events
```

`companies` and `portal_sites` are shared reference data. All other tables use RLS so each user only sees their own career data.

## Phase 4 Agents

Phase 4 added and imported 8 specialized agents:

```text
job-intelligence-agent
portal-operator-agent
autofill-operator-agent
resume-intelligence-agent
application-operator-agent
career-memory-agent
email-operator-agent
dashboard-agent
```

The agents use least-privilege grants over the tables and folders they need. Security-sensitive instructions explicitly require user approval before account creation, credential storage/use, email connection, resume version generation, external messaging, or application submission.

## Phase 5 Workflows

Phase 5 added and imported 5 approval-driven workflows:

```text
job_intake_workflow         — FORM → Job Intelligence Agent → Portal Operator Agent → END
portal_account_workflow     — FORM → Portal Operator Agent → FORM (credential approval) → Portal Operator Agent → END
resume_review_workflow      — FORM → Resume Intelligence Agent → FORM (review decision) → Resume Intelligence Agent → END
application_autofill_workflow — FORM → Autofill Operator Agent → Application Operator Agent → FORM (final confirmation) → Application Operator Agent → END
email_update_workflow       — FORM → Email Operator Agent → FORM (classification review) → Email Operator Agent → END
```

All workflows are manual start and enforce approval gates before credential storage, resume versioning, and final submission confirmation.

## Phase 6 Dashboard

Phase 6 built and deployed the production dashboard website using Lemma SDK.

The dashboard includes:
- Summary cards with application counts and deadlines
- Job URL pasting with workflow trigger
- Applications table showing website, company, role, status, resume used, ATS score, account status, credential save state, deadline, and pending action
- Application detail view with timeline events
- Portal Accounts management view
- Resume Review Studio launcher with application selector
- Email Updates classification view
- Analytics with per-status breakdown
- Career Memory viewer

The replaced placeholder html.html is now a functional Lemma-powered single-page app at:

```text
http://career-operator-dashboard.127-0-0-1.sslip.io:8711
```

## Phase 7 Email Integration

Phase 7 added email reporting and monitoring:

- Created `deadline_reminder_schedule` — TIME cron schedule that triggers email-operator-agent daily at 8am (inactive by default, enable with `lemma schedules update deadline_reminder_schedule --is-active true --pod career-operator`)
- Added "Report Email" form to the dashboard (sender, subject, snippet) that submits to the `email_update_workflow`
- Added "Sync Now" button for manual email sync
- Email Operator Agent can create notifications and update application status when emails are classified
- Email updates are displayed in the dashboard Email Updates page with classification badges (interview, assessment, offer, rejection, etc.)

## Phase 9 Testing and Seed Data

Phase 9 added seed data and the final verification runbook:

- Created `seed/companies.jsonl` — 6 sample companies (Google, Stripe, Notion, Anthropic, Datadog, Figma)
- Created `seed/portal_sites.jsonl` — 6 sample portal sites (Workday, Greenhouse, Lever, Ashby, ICIMS, LinkedIn Jobs)
- Updated `seed/seed.sh` — run `bash seed/seed.sh` to populate demo data after import
- Verified companies and portal sites imported correctly
- All pod wiring healthy

## Final Pod Summary

| Resource | Count | Status |
|---|---|---|
| Tables | 17 | Imported, verified |
| Agents | 8 | Imported, granted, no errors |
| Workflows | 5 | Imported, manual-start |
| Schedules | 1 | Created (deadline_reminder, inactive) |
| File folders | 6 | Created |
| App | 1 | Deployed, READY |
| Seed data | 12 records | Companies + Portal Sites |

Dashboard URL: http://career-operator-dashboard.127-0-0-1.sslip.io:8711
