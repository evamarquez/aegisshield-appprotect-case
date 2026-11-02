# Document 01 - Sponsor Handoff and Scenario

**Project:** AegisShield AppProtect  
**Timing:** Before project planning  
**Status:** Initial sponsor request

## Business context

AegisShield is a fictional cybersecurity company. Its existing product is a SIEM, a service that collects security events and helps analysts investigate suspicious activity.

Leadership wants to expand the product portfolio with AppProtect, a web application firewall. AppProtect would inspect incoming web requests and could block requests that match configured security rules.

## Customer problem to validate

BookEasy is an existing SIEM customer with an online scheduling application. Its booking and login functions must stay available to legitimate users while being protected from malicious requests.

For this fictional case, leadership identifies BookEasy as a possible pilot customer. Its needs, willingness to participate, and current protections still require confirmation.

## Proposed product direction

AppProtect would be a separate service for configuring application protection, reviewing security events, and managing blocking rules.

The first direction is to use an established security engine and build the customer controls and service around it. Engineering must assess technical feasibility, licensing, and operational needs before a solution is selected.

## Sponsor request

The CTO asks the Project Manager to coordinate an initial discovery and feasibility stage with Product, Engineering, Security, Design, and Operations.

The team must:

- Clarify customer needs.
- Compare competing solutions and build, buy, or integrate options.
- Propose a limited first release.
- Estimate resources, costs, and delivery time.

The sponsor will review this evidence before authorizing development and a BookEasy pilot.

## Initial boundaries

AppProtect is a new product initiative. Changes to the existing SIEM are outside the initial discovery scope, except for assessing a possible event integration.

The proposed first release focuses on one BookEasy web application. Broader customer rollout, a proprietary security engine, and additional protection products require separate decisions.

Protection must be evaluated together with service availability. The team must consider how to prevent incorrect blocks from interrupting legitimate bookings.

## Expected discovery outputs

A documented customer problem, proposed product scope, prototype, technical options, initial risks, estimated budget and schedule, and a recommendation for the sponsor's investment decision.

## Key terms

**SIEM:** A service that collects security events to support monitoring and investigation.

**Web application firewall:** A security filter that inspects web requests and applies rules to allow or block them.

**Web request:** A message sent to an application, such as a request to log in or create a booking.

**False positive:** A legitimate request incorrectly identified as a threat.

**Discovery:** Early work to understand the problem and evaluate possible solutions.

**Pilot:** A limited trial with an agreed customer and scope.

## Approval boundary

The sponsor authorizes investigation and proposal work only. Approval to build the product will come later, after enough information is available.
