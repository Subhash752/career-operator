# Career Operator

Tagline: **Paste a job. Career Operator handles the rest.**

Career Operator is a website-first Lemma pod for eliminating repetitive career application work. The core pain point is not job search. The core pain point is repeatedly creating accounts, filling the same profile fields, remembering which portal was used, tracking credentials safely, choosing the right resume, and monitoring follow-up emails.

## MVP Focus

The hackathon MVP prioritizes:

1. Portal and account memory for every career website.
2. Secure credential references with explicit user approval.
3. Reusable autofill profiles and common application answers.
4. Resume Review Studio before applying.
5. Application dashboard showing website, role, status, resume used, account state, deadline, and pending action.
6. Email sync for verification emails, assessments, interviews, recruiter replies, offers, and rejections.

## Primary Flow

```text
User pastes job URL
  -> Career Operator detects company, role, website, ATS, and portal
  -> Portal memory checks if the website/company account already exists
  -> If no account exists, the user approves account creation guidance/autofill
  -> User approves whether credentials can be stored as an encrypted secret reference
  -> Resume Intelligence analyzes the job against the resume
  -> Resume Review Studio shows suggestions on the left and editable resume preview on the right
  -> User accepts, rejects, or manually edits changes
  -> A new resume version is created; the original resume is never modified
  -> Autofill packet prepares profile, education, experience, links, and reusable answers
  -> User confirms before final submission
  -> Dashboard tracks status and email sync updates the application timeline
```

## Product Pillars

### Portal Memory

Career Operator remembers career websites, ATS platforms, company portals, login URLs, signup URLs, account status, and the resume/application history for each portal.

### Credential-Safe Account Guidance

The system may help prepare account creation fields and remember the login identity, but must never expose passwords or save raw passwords in normal tables. Datastores store only `credential_secret_ref` metadata. Account creation, credential storage, credential use, and application submission all require explicit user approval.

### Autofill Operator

Autofill data is saved once and reused across portals: name, email, phone, address, work authorization, education, experience, projects, skills, GitHub, LinkedIn, portfolio, certifications, resume versions, cover letters, and common questions.

### Resume Review Studio

Before applying, the user gets a two-panel review experience:

```text
Left: AI suggestions, ATS gaps, keyword matches, weak bullets, project ordering, reasons, accept/reject/edit controls
Right: resume preview/editor with highlighted proposed changes and manual edit support
```

The original resume is never changed. Every approved or edited output becomes a reusable resume version tied to an application.

### Website Dashboard

The dashboard must answer:

```text
Which website was used?
Which company and role is this?
What is the status?
Which resume was used?
Do I have an account there?
Are credentials saved?
What do I need to do next?
What changed from email sync?
```

Core dashboard columns:

```text
Website / Portal
Company
Role
Status
Resume Used
ATS Score
Account Status
Credential Saved
Deadline
Last Update
Pending Action
```

## Lemma Resources

### Tables

The initial schema folders are created in `tables/`. Phase 3 will fill these with production-ready table definitions.

Important tables:

```text
portal_sites
portal_accounts
autofill_profiles
autofill_fields
applications
companies
job_descriptions
resumes
resume_versions
resume_suggestions
resume_change_sets
email_updates
notifications
application_events
career_memory
interview_history
users
```

### Document Store

File folders are created in `files/` for original resumes, generated resume versions, job descriptions, cover letters, interview notes, and supporting documents.

### Agents

Specialized agents are scaffolded in `agents/`:

```text
job-intelligence-agent
portal-operator-agent
resume-intelligence-agent
application-operator-agent
career-memory-agent
email-operator-agent
dashboard-agent
```

### Functions

Initial function folders are scaffolded in `functions/`:

```text
parse_job_url
calculate_ats_score
create_resume_version
update_application_status
generate_dashboard_metrics
prepare_autofill_packet
store_credential_reference
```

### Workflows

Initial workflow folders are scaffolded in `workflows/`:

```text
job_intake_workflow
resume_review_workflow
portal_account_workflow
application_autofill_workflow
email_update_workflow
```

### App

The website app currently imports as a single-file placeholder:

```text
apps/career-operator-dashboard/html.html
```

Phase 6 can replace it with a full Vite app under `apps/career-operator-dashboard/source/`.

## Security Rules

Hard approval gates:

```text
Account creation
Credential storage
Credential use
Email connection
Resume version generation
Application submission
External message sending
```

Credential rules:

```text
Never store raw passwords in tables
Never display saved passwords
Store only encrypted secret references
Allow credential deletion/update
Log credential-related actions in application_events
Require approval before using a credential
```

## Phase Plan

Phase 1: Architecture complete.

Phase 2: Local Lemma pod bundle initialized.

Phase 3: Datastore/table definitions complete.

Phase 4: Agents and instructions complete.

Phase 5: Workflows and approval forms complete.

Phase 6: Frontend dashboard and Resume Review Studio complete.

Phase 7: Email integration complete.

Phase 8: Portal automation/autofill assistance complete.

Phase 9: Testing and demo seed data complete.

All 9 phases are complete.

## Verification

After importing and seeding, run:

```bash
lemma pods doctor career-operator
lemma query run "select count(*) from companies" --pod career-operator
lemma query run "select count(*) from portal_sites" --pod career-operator
```

Expected: doctor returns no errors, query returns 6+ companies and 6 portal sites.

## Demo Walkthrough

1. Open the dashboard: http://career-operator-dashboard.127-0-0-1.sslip.io:8711
2. Paste a job URL into the "Capture Job" input
3. Watch the application appear in the dashboard table
4. Click on the role to open detail view with timeline and autofill readiness
5. Navigate to Portal Accounts to see saved website memory
6. Navigate to Autofill Profile to see reusable career data
7. Navigate to Resume Studio to analyze resume against a job
8. Navigate to Email Updates to report career emails
9. Navigate to Analytics to see application metrics

## Architecture Overview

Career Operator is a Lemma pod that uses:

- **17 tables** for durable structured state (applications, portal accounts, autofill profiles, resumes, email updates, etc.)
- **8 specialized agents** for job extraction, portal/account handling, autofill, resume intelligence, application coordination, career memory, email classification, and dashboard analytics
- **5 workflows** for approval-gated processes (job intake, portal account management, resume review, autofill readiness, email updates)
- **1 schedule** for deadline reminders (inactive by default)
- **1 browser app** for the Career Operator dashboard
