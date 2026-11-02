# Document 21 - Decision and Change Log

**Project:** AegisShield AppProtect  
**Stage:** Fictional execution  
**Status:** Simulated decision record

## Decision DEC-APP-01 - Safe response to APP-ISS-01

| Field | Record |
|---|---|
| Requested by | Security Lead and Project Manager |
| Date | May 8, 2026 (simulated) |
| Problem | A legitimate booking was blocked by a broad test rule. |
| Decision | Move the rule to monitor mode, narrow the rule, use a time-limited exception, and retest. |
| Decision owner | Security Lead |
| Approver | Product Lead and Sponsor informed |
| Result | Approved for controlled test correction. |

## Schedule decision

No schedule change was approved. The correction used the testing buffer already included in weeks 6 and 7. The week-8 sponsor gate remained unchanged.

## Why this option was selected

It protected the legitimate booking flow, kept the test safe, avoided a permanent bypass, and allowed the team to collect evidence before recommending a pilot build.

## Follow-up actions

| Action | Owner | Due | Status |
|---|---|---|---|
| Record the rule change and test result | Security / QA | Week 7 | Done |
| Confirm the exception expiry and removal | Product / Security | Week 7 | Done |
| Update pilot readiness evidence | PM | Week 7 | Done |
| Tell BookEasy what changed and what was tested | Customer Success | Week 7 | Done |

## Key terms

**Decision log:** A record of an important choice and why it was made.

**Change:** A change to a rule, scope, schedule, cost, or approved plan.

**Buffer:** Time or capacity held for expected uncertainty.

**Permanent bypass:** A broad exception with no clear end or review.
