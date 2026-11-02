# Document 06 - Product Scope and Requirements

**Project:** AegisShield AppProtect  
**Stage:** Product definition  
**Status:** Draft baseline for review

## Product goal

Help a customer protect one web application, understand why requests were blocked, and correct a rule when a legitimate booking is affected.

## First-release scope

| Area | Included in the first version | Not included |
|---|---|---|
| Application | Register one BookEasy web application | Multiple customer applications |
| Rules | Create, enable, disable, and test a small rule set | Automatic rule creation |
| Events | Review request details, matched rule, action, and time | Full security analytics platform |
| Blocking | Run controlled block tests in a non-production environment | Unsupervised production blocking |
| Exceptions | Add an approved exception and record who changed it | Permanent bypass without review |
| Access | Admin and viewer roles | Complex enterprise role design |
| Integration | Assess an event feed to the existing SIEM | Rebuild the SIEM |

## Requirements and acceptance

| ID | Requirement | How we will check it |
|---|---|---|
| APR-01 | An admin can register one BookEasy web application. | The application appears with name, environment, owner, and status. |
| APR-02 | An admin can create and change a basic protection rule. | A rule can be saved, enabled, disabled, and shown with an audit record. |
| APR-03 | The service records request and rule-match events. | Test events show time, action, matched rule, and a safe request identifier. |
| APR-04 | An admin can review why a request was blocked. | The event view explains the rule and shows the request details approved for display. |
| APR-05 | A controlled test can block a request in the test environment. | A known test request is blocked and the result is recorded. |
| APR-06 | An approved admin can create an exception for a legitimate booking request. | The request passes after the exception, the change is logged, and the exception can be removed. |
| APR-07 | Viewer users cannot change rules or exceptions. | Permission tests show that a viewer can read allowed events but cannot edit controls. |
| APR-08 | The product can show its service health and failed delivery attempts. | Operations can see a health state and receive an alert for a simulated failure. |
| APR-09 | Sensitive request data is protected in the product and test records. | Security confirms masking, access control, retention, and no credentials in logs. |
| APR-10 | A pilot can return to the prior safe configuration. | The team rehearses rule rollback and records the result before pilot approval. |

## Customer acceptance scenarios

1. A legitimate BookEasy login request is allowed.
2. A legitimate booking request is allowed.
3. A simulated malicious request is blocked in the test environment.
4. An admin can see which rule caused the block.
5. An admin can add an approved exception for a legitimate booking.
6. A viewer can review events but cannot change rules.
7. Operations can see service health and a simulated delivery failure.

## Open items before baseline approval

- Confirm the exact security engine and license terms.
- Confirm which request fields can be stored and displayed.
- Confirm the performance target for the pilot environment.
- Confirm the exception approval and expiration process.
- Confirm whether the SIEM event feed is in the first pilot or a later increment.

## Key terms

**Requirement:** A condition the product must meet.

**Acceptance:** The evidence that shows a requirement was met.

**Rule:** A condition that tells the service what to do with a request.

**Exception:** An approved case where a request should not follow the normal block rule.

**Viewer:** A role that can review information but cannot change protection settings.
