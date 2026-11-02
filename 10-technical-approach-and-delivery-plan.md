# Document 10 - Technical Approach and Delivery Plan

**Project:** AegisShield AppProtect  
**Stage:** Technical validation and delivery planning  
**Status:** Proposed approach for review

## Approach

Use an established security engine as the protection layer and build a small AegisShield control service around it. The control service manages applications, rules, events, exceptions, roles, audit records, and operational status.

The engine choice is not final. Engineering and Security must confirm licensing, supported deployment, rule behavior, performance, data handling, and recovery before a pilot build is approved.

## Simple service flow

BookEasy request -> AppProtect control point -> security engine -> allow, monitor, or block -> event record -> AppProtect console -> optional SIEM event feed.

The pilot must start in monitor mode. Block tests use known simulated requests and must not affect real BookEasy users.

## Main technical areas

| Area | Proposed direction | Owner |
|---|---|---|
| Security engine | Compare established engines and choose one only after technical and license review. | Engineering / Security |
| Control service | Store application, rule, exception, role, and audit information. | Engineering |
| Event view | Show safe request details, action, matched rule, and time. | Engineering / Design |
| Exception flow | Require reason, owner, expiry, test result, and approval. | Product / Security |
| Permissions | Separate admin and viewer access. | Security / Engineering |
| Operations | Monitor service health, event delivery, and failed changes. | Operations |
| SIEM integration | Assess an event feed as an optional first increment. | Engineering / SIEM team |

## Delivery sequence

1. Confirm the first-release requirements and customer scenarios.
2. Compare engine options and record licensing and technical limits.
3. Design the administrator experience and review it with Product and BookEasy.
4. Build or configure a non-production proof of the control flow.
5. Test allow, monitor, block, event review, permissions, exception, and recovery behavior.
6. Review cost, support, data protection, and pilot readiness.
7. Present evidence to the sponsor for the pilot-build decision.

## Guardrails

- Monitor mode comes before block mode.
- No production traffic is connected during discovery or validation.
- Rules and exceptions have owners, reasons, and audit records.
- Sensitive request values are masked or excluded.
- A safe configuration can be restored before any pilot test.
- Engineering owns detailed design; the PM coordinates decisions and evidence.

## Methodology

The team uses a hybrid model. The plan sets scope, decision gates, risks, budget assumptions, and milestones. Short delivery loops are used for the prototype, engine assessment, technical proof, and test corrections.

## Key terms

**Security engine:** The component that evaluates a request against protection rules.

**Control service:** The AegisShield layer that manages applications, rules, events, users, and exceptions.

**Monitor mode:** Observe and record without blocking.

**Block mode:** Stop a request that matches an active rule.

**Guardrail:** A rule that keeps the work safe and within its approved limits.
