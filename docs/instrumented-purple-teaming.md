# Instrumented Purple Teaming

Back to [README](../README.md).

Purple teaming becomes much more useful when the goal is not simply to execute a technique but to **measure the complete defensive dependency chain**.

## 1. The dependency graph

~~~text
ATT&CK technique
      ↓
data component / expected evidence
      ↓
detection strategy
      ↓
analytic / rule
      ↓
log source
      ↓
sensor / configuration
      ↓
alert
      ↓
analyst decision
~~~

If an emulation produces no alert, the failure can exist at any layer.

## 2. Reverse reasoning

~~~text
No alert
  ↓
Did the analytic execute?
  ↓
Did the required log reach the platform?
  ↓
Did the sensor collect the required event?
  ↓
Did the authorized test produce the expected evidence?
~~~

This turns a purple-team exercise into detection engineering rather than theater with screenshots.

## 3. ATT&CK + D3FEND

ATT&CK describes adversary behavior. D3FEND provides defensive-knowledge relationships. Together with detection metadata they support a bidirectional model linking adversary technique, defensive countermeasure, telemetry requirement and analytic implementation.

## 4. 2026 knowledge-driven research

The C&ESAR 2026 work titled **From Attack Scenario to Measurable Detection Improvement: A Knowledge-Driven ATT&CK/D3FEND Framework for Instrumented Purple Teaming** is worth tracking because it explicitly models the dependency chain from attack scenario to measurable detection improvement.

As of September 28, 2026, C&ESAR 2026 is scheduled for November 2026. This repository therefore treats the work as **provisional research**, not completed peer-reviewed evidence.

That date distinction is precisely why the repository has an evidence model.

## 5. Metrics that matter

- implementation coverage;
- telemetry availability;
- analytic coverage;
- detection quality;
- alert fidelity;
- analyst response outcome;
- mean time from behavior to usable signal;
- failure cause by dependency layer.

Avoid reducing program health to percentage of ATT&CK techniques colored green.

## 6. Validation resources

| Need | Resource |
|---|---|
| Atomic behavior validation | Atomic Red Team |
| Multi-step emulation | MITRE Caldera |
| Cloud behavior validation | Stratus Red Team |
| Detection lab / telemetry generation | Splunk Attack Range |
| Coverage / visibility modeling | DeTT&CT |
| Detection quality | Summiting the Pyramid |

Use controlled systems that are explicitly authorized for testing.

## 7. Evidence package per test

~~~yaml
technique:
expected_telemetry:
sensor:
log_source:
analytic:
expected_alert:
observed_evidence:
result:
failure_layer:
analyst_notes:
timestamp:
environment:
~~~

This makes exercises reproducible and turns failures into engineering work items.

## 8. Scope

The objective is defensive validation: confirm that expected telemetry, controls and analytics work as designed.