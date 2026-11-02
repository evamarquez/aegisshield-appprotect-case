# Document 03 - Discovery Findings and Sponsor Decision

**Project:** AegisShield AppProtect  
**Stage:** Discovery decision gate  
**Status:** Simulated findings and recommendation for sponsor review

> All findings in this document are simulated for portfolio use. They are not real customer research or competitive research.

## Discovery evidence used

The team reviewed a simulated BookEasy interview summary, a short competitor comparison, an initial technical assessment, an operating-cost estimate, and a prototype review.

## Simulated customer findings

| Area | Simulated finding | What it means |
|---|---|---|
| Current protection | BookEasy uses a basic hosted protection service and reviews alerts in more than one place. | A simpler view could be useful, but the value is not proven for every customer. |
| Main pain point | The team needs to understand why a request was blocked and restore a legitimate booking quickly. | Event details, rule explanation, and a safe exception path are important for the first version. |
| Ownership | Engineering configures protection today, while support receives the first customer questions. | The product needs clear roles, permissions, and an escalation path. |
| Pilot interest | The simulated BookEasy representative is open to reviewing a limited pilot if booking traffic is protected and rollback is ready. | The pilot is possible, but it is not a purchase commitment. |
| Buying reason | The strongest proposed reason is guided setup and support from the existing AegisShield team. | The value proposition should stay focused instead of promising a full security platform. |

## Simulated options comparison

| Option | Summary | Assessment |
|---|---|---|
| Continue with current protection | Do not add an AegisShield product now. | Lowest delivery cost, but does not address the visibility and support gap found in discovery. |
| Buy or resell an existing service | Offer another vendor's service to customers. | Faster path, but less control over the customer experience, data flow, and product direction. |
| Build around an existing security engine | Use an established engine and create the AegisShield setup, event, exception, and support experience. | Recommended for a limited first version, subject to licensing, technical, and performance checks. |
| Build a proprietary engine | Create the detection and blocking engine inside AegisShield. | Not recommended for the first version because the cost, risk, and support burden are too high. |

## Recommendation

Authorize a limited product-definition and technical validation stage for AppProtect. The first version should use an established security engine and focus on one BookEasy web application.

The first version should cover:

- Registering one application.
- Configuring a small set of protection rules.
- Viewing requests and rule matches.
- Blocking a request in a controlled test setting.
- Creating and reviewing an exception for a legitimate booking.
- Recording security events for the existing SIEM integration if the technical assessment supports it.

The first version should not include a proprietary engine, broad customer rollout, or a promise of protection against every threat.

## Conditions before development approval

- Engineering confirms that the selected engine can meet the pilot needs.
- Product confirms the first-release scope and customer validation scenarios.
- Security reviews data handling, access control, rule safety, and audit needs.
- Operations confirms monitoring, support, recovery, and escalation requirements.
- Finance or the sponsor reviews the simulated budget and ongoing operating-cost assumptions.
- BookEasy confirms the pilot boundary and agrees how legitimate bookings will be protected during testing.

## Sponsor decision

**Simulated decision:** Approve the limited product-definition and technical-validation stage.

**Decision owner:** CTO / Project Sponsor.

**Approved boundary:** One BookEasy web application, an established security engine, a limited set of rules, a controlled test environment, and a pilot-readiness recommendation.

**Not approved:** Production protection, broad customer rollout, a proprietary engine, or a full AppProtect launch.

## Next step

Use this decision to prepare the Project Brief and Project Charter. The Charter will define the approved stage, authority, resources, milestones, and success criteria before detailed delivery planning begins.

## Key terms

**Finding:** Information learned during discovery. In this case, a simulated customer need or constraint.

**Option:** A possible path the sponsor could choose, such as buy, integrate, or build.

**Recommendation:** The option the team supports after reviewing the evidence.

**Decision gate:** The point where the sponsor decides whether the work can move to the next stage.

**Approved boundary:** The clear limit of what the decision allows the team to do.
