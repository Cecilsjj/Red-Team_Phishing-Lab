# Red Team Phishing Simulation — Final Report

## 1. Executive Summary

A controlled phishing email simulation was conducted
against a fictional organization, Northstar Technologies.

The exercise demonstrated how a simulated phishing
message can be constructed, delivered through SMTP,
and linked to a locally hosted verification page.

All testing occurred in an isolated local environment.

## 2. Scope and Authorization

- Organization: Northstar Technologies (fictional)
- Environment: Docker, Mailpit, Python HTTP Server
- Recipient: employee@northstar.example
- Sender: security@northstar-support.example
- External delivery: None
- Credential collection: None

## 3. What Happened?

1. A simulated account-verification phishing email
   was constructed using a lookalike sender domain.

2. A local account-verification landing page was
   created and hosted on 127.0.0.1:8080.

3. A Python script submitted the email through SMTP
   to Mailpit on port 1025.

## 4. What Was the Outcome?

1. Mailpit successfully received the email.

2. The local landing page was accessible through
   the Python HTTP server.

3. The original email was exported as an EML file
   for defensive analysis.

No credentials were collected, and no unauthorized
account access was demonstrated.

## 5. Evidence Collected

- evidence/phishing-email.eml
- evidence/attack-timeline.md
- emails/authentication-results.txt
- emails/phishing-email.txt
- emails/phishing-email.html
- landing-page/index.html
- scripts/send_email.py

Note: Authentication results in
authentication-results.txt are synthetic training data.

## 6. MITRE ATT&CK Mapping

### T1566 — Phishing

The simulation demonstrates phishing-style
social engineering through an email message.

### T1566.002 — Spearphishing Link

The email contained a link directing the test
recipient to a locally hosted verification page.

These mappings describe simulated techniques,
not real-world compromise.

## 7. Defensive Lessons

- Display names do not establish sender legitimacy.
- Lookalike domains can be used for impersonation.
- Email authentication does not guarantee safety.
- Suspicious links should be examined safely.
- Preserving original email headers supports investigation.

## 8. Investigation Required?

Yes.

The corresponding Blue Team lab will analyze the
simulated message, sender identity, routing metadata,
URL indicators, and recommended defenses.

## 9. Final Outcome

The controlled phishing simulation successfully
demonstrated email construction, SMTP delivery,
local landing-page hosting, and evidence preservation.

No external systems were targeted.
No credentials were collected.
