# Phishing Simulation — Attack Timeline

## Scenario

Organization: Northstar Technologies
Environment: Local Docker, Mailpit, Python HTTP Server

## Event Timeline

### Event 1 — Email Preparation

- Simulated phishing email created.
- Fictional sender domain configured.
- Plain-text and HTML email templates prepared.

### Event 2 — Landing Page Preparation

- Local Northstar account-verification page created.
- Python HTTP server started on 127.0.0.1:8080.
- Landing page accessibility verified.

### Event 3 — Email Delivery

- Python script submitted the test email to Mailpit.
- Recipient: employee@northstar.example
- Mailpit Received timestamp: 2026-11-03 15:07:43 UTC
- Delivery: Confirmed

### Event 4 — Evidence Collection

- Original email exported as phishing-email.eml.
- Email headers examined.
- Sender and SMTP routing information identified.

## Observed Outcome

- Simulated phishing email successfully delivered.
- Local verification page accessible.
- No credentials collected.
- No unauthorized account access demonstrated.

## Evidence Limitations

- SPF, DKIM, and DMARC results are synthetic.
- Delivery occurred only within the local testing environment.
- No external phishing campaign was conducted.
