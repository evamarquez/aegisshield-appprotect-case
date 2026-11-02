# Document 18 - Data Protection and Operational Readiness

**Project:** AegisShield AppProtect  
**Stage:** Pilot planning  
**Status:** Draft for Security and Operations review

## Data protection controls

| Control | Expected practice | Evidence |
|---|---|---|
| Access | Admin and viewer permissions are separate and reviewed. | Permission test and access list |
| Masking | Request values that could contain secrets or personal data are masked or excluded. | Security review and safe event sample |
| Logging | Logs show action and result without credentials or unapproved content. | Log review |
| Retention | The team defines how long pilot events and audit records are kept. | Retention decision |
| Changes | Rules and exceptions require an owner, reason, and audit record. | Change record |
| Environment | Tests use synthetic or approved masked data. | Test-data checklist |

## Monitoring and support

Operations should be able to see:

- Service health.
- Event delivery failures.
- Rule or exception changes.
- Unusual error volume.
- Failed recovery or configuration restore.

Support should know how to report an incorrect block. The escalation path is Support -> Customer Success -> Security or Engineering, with the PM informed when the issue could affect pilot acceptance or schedule.

## Recovery approach

1. Stop the affected rule or return the service to monitor mode.
2. Restore the last approved safe configuration.
3. Confirm legitimate login and booking scenarios.
4. Preserve the event and audit evidence needed for investigation.
5. Communicate the result and decide whether the rule needs a correction, removal, or new test.

## Handover readiness

Operations must receive:

- Service and application ownership.
- Monitoring view and alert route.
- Rule and exception change process.
- Recovery steps and last safe configuration.
- Known limits and open items.
- Support and escalation contacts.

## Readiness conditions

The service is not ready for pilot approval until the data controls, monitoring, recovery rehearsal, and support path have been reviewed by Security and Operations.

## Key terms

**Data masking:** Hiding sensitive values while keeping enough detail for a test or investigation.

**Retention:** How long a record is kept.

**Runbook:** Step-by-step instructions for operating or recovering a service.

**Handover:** Moving service knowledge and support responsibility to Operations.
