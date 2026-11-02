# Document 17 - Risk Register

**Project:** AegisShield AppProtect  
**Stage:** Pilot planning  
**Status:** Week 5 simulated baseline; review weekly

## Scoring guide

- **Low probability:** Not expected under the current plan.
- **Medium probability:** A credible chance exists without more information or action.
- **High probability:** Likely unless the team takes action.
- **Low impact:** Small rework with no customer or gate effect.
- **Medium impact:** Material rework, cost, or schedule effect.
- **High impact:** Customer disruption, data exposure, unsafe protection, or a blocked decision.

## Initial risks

| ID | Risk and consequence | Probability / impact | Prevention | Trigger | Contingency | Owner | Status |
|---|---|---|---|---|---|---|---|
| R01 | A selected engine cannot meet the pilot rules or license terms. | Medium / High | Compare options early and review license questions. | Required rule or license condition fails review. | Select another engine or recommend no-go. | Engineering / Security | Open |
| R02 | A legitimate login or booking is blocked. | Medium / High | Start in monitor mode and test safe flows first. | T-01 or T-02 fails. | Disable the rule, restore safe config, investigate, and retest. | Security / QA | Open |
| R03 | The product adds too much request delay. | Medium / High | Define a performance target and test before pilot approval. | Performance result misses the agreed target. | Reduce scope, adjust engine settings, or defer the pilot. | Engineering / Operations | Open |
| R04 | Sensitive request information appears in logs or event views. | Medium / High | Mask fields, limit access, and review retention. | Security finds an unapproved value. | Stop the test, remove exposure, and review affected records. | Security | Open |
| R05 | Exceptions remain active too long or are not reviewed. | Medium / Medium | Require owner, reason, expiry, and audit record. | Exception has no owner or expiry. | Disable it and review the affected flow. | Product / Security | Open |
| R06 | BookEasy cannot provide the people or scenarios needed for the pilot. | Medium / Medium | Confirm availability and scenarios early. | Customer review is missed or scenarios are unclear. | Move the review within available float or recommend defer. | Customer Success | Open |
| R07 | Operations cannot support the service after handover. | Medium / High | Define monitoring, recovery, and escalation before the gate. | Runbook or recovery test is incomplete. | Keep the work in validation and do not recommend pilot launch. | Operations | Open |
| R08 | Ongoing license and support costs are higher than expected. | Medium / Medium | Use assumptions, request vendor input, and show sensitivity. | Cost estimate exceeds the sponsor boundary. | Reduce scope, negotiate, partner, or stop the initiative. | PM / Sponsor | Open |

## Review rule

The PM reviews risks weekly with the owners. If a risk happens, it becomes an issue with a date, impact, owner, actions, and evidence. The baseline should not describe a later issue as if it were already known.

## Key terms

**Risk:** An uncertain event that could affect the project.

**Issue:** A current problem that has happened or needs action now.

**Risk owner:** The role that monitors and responds to the risk.

**Trigger:** A sign that the risk may be happening.

**Mitigation:** An action that reduces the chance or impact of a risk.

**Contingency:** The action used if the risk happens.
