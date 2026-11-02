# Document 16 - Test and Validation Plan

**Project:** AegisShield AppProtect  
**Stage:** Pilot planning  
**Status:** Draft for Product, Security, QA, Operations, and BookEasy review

## Test purpose

Show that AppProtect can protect the agreed BookEasy test application without blocking legitimate login and booking requests, exposing unsafe data, or making the service impossible to support.

## Test environment and data

- Non-production environment only.
- Synthetic requests and approved masked BookEasy examples.
- No production credentials, payment data, or unmasked customer content.
- Test users for admin and viewer roles.
- Known safe booking requests and known simulated malicious requests.
- A recorded configuration snapshot before each major test.

## Test scenarios

| ID | Scenario | Expected result | Owner |
|---|---|---|---|
| T-01 | Legitimate login | Request is allowed and the event is recorded without sensitive values. | QA / BookEasy |
| T-02 | Legitimate booking | Booking request is allowed and the expected event is visible. | QA / BookEasy |
| T-03 | Simulated malicious request | Request is flagged or blocked according to the test rule. | Security / QA |
| T-04 | Block explanation | Admin can see the matched rule and safe request details. | Product / QA |
| T-05 | False-positive correction | Admin creates a short-lived exception and the safe booking passes after the change. | Product / Security / QA |
| T-06 | Viewer permissions | Viewer can read approved events but cannot edit rules or exceptions. | Security / QA |
| T-07 | Audit record | Rule and exception changes show user, time, reason, and result. | Security / QA |
| T-08 | Service health | Operations can see healthy, warning, and failed states. | Operations / QA |
| T-09 | Event delivery | A simulated delivery failure creates an actionable alert. | Engineering / Operations |
| T-10 | Recovery | The team restores the last safe configuration and confirms service behavior. | Engineering / Operations |
| T-11 | Performance | The test result is compared with the agreed pilot performance target. | Engineering / QA |
| T-12 | Data protection | Logs and views do not expose credentials or unapproved sensitive data. | Security |

## Acceptance rules

- T-01 and T-02 must pass before any block-mode test.
- T-05 must pass before the pilot is recommended.
- T-06, T-07, and T-12 must pass before access is approved.
- T-08, T-09, and T-10 must pass before Operations accepts readiness.
- T-11 must meet the performance target agreed by Engineering, Operations, and BookEasy.
- Any critical issue must have a fix, accepted limitation, or sponsor decision before the gate.

## Evidence to keep

- Test case and expected result.
- Test date, environment, and tester.
- Request or event identifier using simulated values.
- Screenshot or safe log excerpt.
- Pass, fail, blocked, or not run status.
- Defect link and retest result when needed.

## Key terms

**Test scenario:** A situation the team uses to check the product.

**False-positive test:** A test that checks whether a safe request is incorrectly blocked.

**Retest:** Running a failed scenario again after a correction.

**Test evidence:** The record that shows what was tested and what happened.

**Acceptance rule:** A condition that must pass before the work can advance.
