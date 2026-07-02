#!/usr/bin/env bash
# Career Operator Seed Script
# Run after pod import: bash seed/seed.sh
set -euo pipefail

POD="career-operator"

echo "=== Seeding Companies ==="
lemma records import companies ./seed/companies.jsonl --pod "$POD"

echo "=== Seeding Portal Sites ==="
lemma records import portal_sites ./seed/portal_sites.jsonl --pod "$POD"

echo ""
echo "=== Seed Complete ==="
echo "Open your dashboard at:"
echo "  http://career-operator-dashboard.127-0-0-1.sslip.io:8711"
echo ""
echo "Next step: Paste a job URL from the dashboard to start your first application."
