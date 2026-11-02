# Document 23 - Pilot Test Results and BookEasy Acceptance

**Project:** AegisShield AppProtect  
**Stage:** Week 7 simulated pilot review  
**Status:** Accepted with conditions for a controlled pilot build

> These results are simulated. They do not show real security performance or a real customer approval.

## Test results

| Scenario | Result | Evidence |
|---|---|---|
| Legitimate login | Pass | Safe test request allowed and event recorded. |
| Legitimate booking | Pass after APP-ISS-01 correction | Booking request allowed after rule scope was narrowed. |
| Simulated malicious request | Pass | Controlled test request was blocked. |
| Block explanation | Pass | Event showed matched rule, action, time, and safe identifier. |
| Exception flow | Pass | Exception had owner, reason, expiry, and audit record. |
| Viewer permissions | Pass | Viewer could not edit rules or exceptions. |
| Data protection | Pass | No credentials or unapproved sensitive values were shown in test evidence. |
| Recovery | Pass for configuration restore | Last safe configuration was restored and safe booking was checked again. |
| Performance | Pending final target confirmation | Engineering and Operations must confirm the target before production use. |

## BookEasy review

The simulated BookEasy representative reviewed the agreed login, booking, block, event, and exception scenarios. BookEasy accepted the results for the controlled pilot scope with the following conditions:

- The pilot remains in a non-production environment.
- Production blocking is not approved by this record.
- Exceptions require an owner, expiry, and review.
- The performance target must be confirmed before any future production decision.
- Customer Success receives the support and escalation path.

## Acceptance decision

**Decision:** Accepted with conditions for controlled pilot build planning.  
**Accepted by:** BookEasy representative, simulated.  
**Date:** May 15, 2026 (simulated).  
**Next decision:** Sponsor go/no-go for controlled pilot build.

## Key terms

**Pilot:** A limited test with a defined customer, environment, and scope.

**Acceptance:** The customer confirms that the agreed scenarios met the expected result.

**Condition:** A requirement that must remain true for the acceptance to apply.

**Production:** The live environment used by real customers.
