# Document 20 - Issue Log

**Project:** AegisShield AppProtect  
**Issue:** APP-ISS-01  
**Stage:** Week 6 to week 7 simulated execution  
**Status:** Closed for pilot scope

## Issue summary

| Field | Record |
|---|---|
| Detected | Week 6 during a safe BookEasy booking test |
| Description | The rule “Unexpected request pattern” blocked a legitimate booking request. |
| Impact | The booking flow could not be treated as safe for pilot approval. |
| Priority | High |
| Owner | Security Lead with Engineering and QA support |
| Related requirement | APR-05 and APR-06 |
| Current status | Closed in week 7 |
| Customer impact | No production impact; the issue was found in the controlled test environment. |

## Investigation

The team reproduced the request with a known safe test user. The request matched a broad rule pattern. The rule was working as configured, but the rule scope was too broad for the agreed BookEasy booking path.

## Options considered

| Option | Result |
|---|---|
| Leave the rule active and continue the pilot | Rejected because the safe booking would remain blocked. |
| Disable the rule and stop all protection testing | Rejected because the team would lose the controlled block scenario. |
| Move the rule to monitor mode, narrow its scope, and retest | Selected because it protects the safe flow while keeping a controlled test path. |
| Create a permanent broad exception | Rejected because it could create an unsafe bypass. |

## Correction and retest

1. Moved the rule to monitor mode.
2. Narrowed the rule to the intended test request pattern.
3. Added an approved, time-limited exception for the safe booking path.
4. Retested login, booking, block, event detail, exception, and audit behavior.
5. Removed the test exception after the scenario passed.

## Closure evidence

- Legitimate login passed.
- Legitimate booking passed.
- Simulated malicious request was blocked in the controlled test.
- Event detail showed the matched rule and safe request identifier.
- Viewer could not change the rule.
- Exception had an owner, reason, expiry, and audit record.

## Key terms

**Issue:** A current problem that needs action.

**Root cause:** The reason the problem happened.

**False positive:** A safe request incorrectly treated as a threat.

**Retest:** Repeating the failed scenario after the correction.

**Closure evidence:** Proof that the issue was resolved for the agreed scope.
