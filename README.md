# HTTP Security Headers Scanner

[![Scope of Perimeter Verification](https://img.shields.io/badge/TAVARDT-Technical%20Audit-5b3cf5.svg)](https://tools.tavardt.com/nz/security-headers-check/)
Automated technical audit of HTTP security headers aligned with NZISM controls, CERT NZ recommendations, and the Privacy Act 2020.

Developed and maintained by the cybersecurity and digital sovereignty division of **TAVARDT New Zealand**.

***

## 1. Scope of Perimeter Verification

This command-line utility audits critical browser protection directives and transport layer configurations for New Zealand entities:

* **Strict-Transport-Security (HSTS):** Enforces HTTPS encryption and prevents downgrade and interception attacks.
* **Content-Security-Policy (CSP):** Restricts script loading to mitigate Cross-Site Scripting (XSS) and unauthorized code.
* **X-Frame-Options:** Prevents clickjacking attacks by managing iframe and frame embedding rules.
* **X-Content-Type-Options:** Blocks MIME-sniffing vulnerabilities in client browsers.
* **Referrer-Policy:** Protects sensitive URL parameters from cross-origin disclosure.
* **Permissions-Policy:** Enforces least-privilege control for browser hardware sensors and APIs.

***

## 2. Quick Start Guide

Run this tool directly via Python without installing third-party packages:

```bash
python scanner.py example.co.nz
```

***

## 3. Online Diagnostic Tools (New Zealand)

Verify your digital infrastructure against technical baselines using the TAVARDT New Zealand suite:

* HTTP Security Headers Checker
* [Consent Mode v2 & Privacy Act Validator](https://tools.tavardt.com/nz/consent-mode-v2-checker/)
* [DMARC & Anti-Spoofing Verifier](https://tools.tavardt.com/nz/dmarc-checker/)
* [Exposed Credentials & Secret Scanner](https://tools.tavardt.com/nz/exposed-files-scanner/)
* [Full New Zealand Tools Portal](https://tools.tavardt.com/nz/)

***

## 4. Technical Advisory & Remediation

For NZISM alignment, CERT NZ mitigation implementation, and technical privacy consulting in New Zealand, contact **TAVARDT New Zealand**.

***

© 2026 TAVARDT. All rights reserved.
