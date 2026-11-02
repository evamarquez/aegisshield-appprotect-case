# Document 09 - Product Experience and Prototype

**Project:** AegisShield AppProtect  
**Stage:** Product design  
**Status:** Prototype for review

> This is a visual prototype for a fictional product. It does not inspect traffic, block requests, or provide real security protection.

## Design goal

Make it easy for an administrator to understand what AppProtect is doing, see why a request was blocked, and correct a safe false positive without guessing.

## Administrator journey

1. Open AppProtect and check service health.
2. Register or select the BookEasy application.
3. Review the current protection mode and rules.
4. Open a request event and understand the matched rule.
5. Decide whether the block looks correct or may be a false positive.
6. Create an approved exception for a legitimate booking request.
7. Test the change in a safe mode.
8. Review the audit record and share the result with Support or Security.

## Main screens

| Screen | User goal | Main content |
|---|---|---|
| Overview | Know if the service is healthy | Application status, requests, blocks, possible false positives, and alerts |
| Applications | Select the application to manage | BookEasy app, environment, owner, protection mode, and last change |
| Rules | Understand and manage rules | Rule name, reason, mode, status, last change, and owner |
| Event detail | Understand a block | Request time, action, matched rule, safe request details, and next step |
| Exception review | Correct a false positive | Proposed exception, reason, expiry, approver, and test result |
| Audit and access | See who changed what | User, action, time, result, and permission level |

## Important product choices

- Start in monitor mode before enabling a block in the pilot.
- Show the matched rule before asking a user to change it.
- Require a reason and expiration for an exception.
- Keep a record of rule and exception changes.
- Separate viewer access from admin access.
- Keep request details masked when they could contain sensitive information.

## False-positive scenario

The prototype includes a fictional blocked booking request. The administrator can see that a rule matched a request pattern, review the safe details, and create a short-lived exception for the BookEasy booking path. The exception must be tested and reviewed before it is treated as ready.

## Prototype review questions

- Can a new administrator tell which application they are managing?
- Is it clear whether the service is monitoring or blocking?
- Can the user understand why a request was blocked?
- Is the safe path for a false positive easy to find?
- Does the design show who approved an exception and when it expires?
- Are sensitive request details hidden by default?

## Key terms

**Monitor mode:** The service observes and records requests but does not block them.

**Block mode:** The service stops a request that matches an active rule.

**False positive:** A safe request that the system treats as a threat.

**Exception:** A limited, approved change that allows a known safe request.

**Audit record:** A history of who made a change, what changed, and when.
