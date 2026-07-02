# Agent Design Contract

Career Operator uses specialized agents instead of one giant agent. Each agent receives only the resources it needs.

## Job Intelligence Agent

Extracts job information from pasted URLs and job descriptions: company, role, location, salary, skills, responsibilities, qualifications, employment type, deadlines, ATS platform, portal URL, and confidence.

## Portal Operator Agent

Central agent for the main pain point. Detects career portals, checks portal memory, identifies whether the user already has an account, prepares account creation guidance, and enforces approval gates before credential storage or credential use.

## Autofill Operator Agent

Maps Career Memory and autofill profile data to portal fields. Produces autofill packets, identifies missing reusable answers, and asks the user before saving sensitive answers.

## Resume Intelligence Agent

Analyzes resume fit against the job. Produces ATS score, keyword matches, skill gaps, and editable suggestions for Resume Review Studio. Never modifies original resumes.

## Application Operator Agent

Coordinates application readiness: selected resume version, autofill packet, portal account state, pending fields, documents, and final submission confirmation.

## Career Memory Agent

Stores and retrieves durable user knowledge: profile, education, skills, projects, experience, certifications, reusable answers, preferences, portal history, and application history.

## Email Operator Agent

Classifies synced emails into verification, recruiter reply, assessment, interview, offer, rejection, deadline, or generic update. Matches messages to applications and creates timeline events.

## Dashboard Agent

Summarizes applications, pending actions, portal/account health, resume performance, deadlines, email updates, and analytics.
