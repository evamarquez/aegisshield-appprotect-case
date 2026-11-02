# Document 13 - Product Backlog and Estimates

**Project:** AegisShield AppProtect  
**Stage:** Delivery planning  
**Status:** Initial planning backlog

**Estimate unit:** person-days. These are simulated planning assumptions, not actual time records.

| ID | WBS | Work item | Owner | Priority | Estimate | Dependency | Acceptance evidence |
|---|---|---|---|---|---:|---|---|
| AP-01 | 1.3 | Confirm first-release scope and scenarios | Product / PM | High | 2 | Charter | Approved scope and scenario list |
| AP-02 | 2.1 | Map administrator journey | Design / Product | High | 3 | AP-01 | Journey reviewed by Product and BookEasy |
| AP-03 | 2.2 | Build visual prototype | Design | High | 5 | AP-02 | Setup, event, block, and exception screens reviewed |
| AP-04 | 3.1 | Compare security engine options | Engineering / Security | High | 5 | AP-01 | Option matrix and license questions |
| AP-05 | 3.2 | Define control service and data flow | Engineering | High | 4 | AP-04 | Data-flow note and feasibility review |
| AP-06 | 3.3 | Estimate infrastructure and operating costs | Engineering / Ops | Medium | 3 | AP-04 | Cost assumptions and open questions |
| AP-07 | 4.1 | Write requirements and test scenarios | Product / QA | High | 4 | AP-01 | Requirements linked to scenarios |
| AP-08 | 4.2 | Define security, data, and recovery controls | Security / Ops | High | 4 | AP-05 | Control checklist and recovery approach |
| AP-09 | 4.3 | Prepare pilot-readiness recommendation | PM / QA | High | 3 | AP-03, AP-06, AP-07, AP-08 | Evidence summary and open conditions |
| AP-10 | 5.1 | Prepare sponsor evidence package | PM | High | 2 | AP-09 | Decision pack ready |
| AP-11 | 5.2 | Hold sponsor decision gate | Sponsor / PM | High | 1 | AP-10 | Recorded go, no-go, or defer decision |
| AP-12 | 6.3 | Record closure and lessons | PM | Medium | 2 | AP-11 | Closure record and lessons |

## Prioritization

- High: required to make the sponsor decision or protect the pilot.
- Medium: needed for a complete planning view but can move slightly without blocking the decision.
- Low: useful follow-up work outside the first decision gate.

## Estimate notes

The estimate reflects part-time work and review time. A five-day item may occupy more than one calendar week if the owner is available only part time or is waiting for input.

## Backlog controls

The PM tracks status, owner, dependency, estimate, acceptance evidence, and changes. A change to scope or estimate is reviewed for impact before it is accepted into the baseline.

## Key terms

**Backlog:** An ordered list of project work.

**Estimate:** A planning view of effort, not a promise of exact time.

**Dependency:** Work that must happen before another item can finish.

**Acceptance evidence:** Proof that the work meets the agreed result.
