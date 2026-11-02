# Document 04 - Project Brief

**Project:** AegisShield AppProtect  
**Stage:** Product definition and technical validation  
**Status:** Draft for Charter approval  
**Customer:** BookEasy pilot, fictional

## Purpose

Turn the discovery recommendation into a small, testable product stage. The team will define the first AppProtect experience, confirm technical feasibility, and prepare a safe pilot recommendation.

## Problem

BookEasy needs to protect an online scheduling application without making legitimate login and booking requests fail. Its current protection and alert review are spread across more than one place. The team needs a clearer way to understand blocked requests and correct a rule when it affects a real customer action.

## Objective

Define and validate a limited AppProtect first version for one BookEasy web application. The stage must show how an administrator registers the application, configures basic rules, reviews events, tests a block, and creates a safe exception for a legitimate booking.

## Proposed scope

### Included

- One BookEasy web application in a controlled test environment.
- Application registration and basic protection settings.
- A small set of rules for common request patterns.
- Request and rule-match event review.
- Controlled block testing.
- Exception management for an approved legitimate request.
- Roles, permissions, audit records, monitoring, and recovery planning.
- Technical assessment of an established security engine.

### Excluded

- Production protection for BookEasy.
- Rollout to other customers.
- A proprietary detection or blocking engine.
- A complete SIEM redesign.
- A promise to detect every type of attack.
- Automated rule changes without an approval step.

## Main deliverables

1. Approved product brief and charter.
2. Product scope, requirements, and acceptance checklist.
3. Administrator journey and clickable visual prototype.
4. Technical option, licensing, and operating-cost assessment.
5. WBS, RACI, backlog, estimates, schedule, risks, and test plan.
6. Pilot-readiness recommendation and sponsor decision.

## Assumptions and constraints

- The company and customer are fictional.
- Customer interviews and competitor findings are simulated.
- A security engine may be licensed or integrated, but its terms must be reviewed.
- The prototype uses simulated data and is not a working firewall.
- Legitimate login and booking must remain available in the pilot test.
- The first stage uses a part-time cross-functional team.

## Success criteria for this stage

- The first-release boundary is approved.
- The main customer journey is clear and understandable.
- Engineering confirms at least one feasible technical path.
- Security and Operations identify the controls needed for a pilot.
- BookEasy confirms the pilot scenarios and the safe way to test blocks and exceptions.
- The sponsor has enough evidence to decide whether to authorize pilot build work.

## Methodology

This stage uses a hybrid approach. The plan controls scope, decisions, risks, budget assumptions, and gates. The team uses short discovery and design loops to test the product idea, learn from findings, and adjust the first version before approval.

## Key terms

**First version:** The smallest product scope that can test the main customer problem.

**Pilot readiness:** Evidence that the team can test the product with the agreed customer and controls.

**Operating cost:** The ongoing cost to host, monitor, license, and support the product.

**Scope boundary:** What the team is allowed to include and what it must leave out.
