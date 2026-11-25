# HTTP Security Headers Scanner

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Scope of Perimeter Verification](https://img.shields.io/badge/TAVARDT-Technical%20Audit-5b3cf5.svg)](https://tools.tavardt.com/nz/security-headers-check/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

Automated technical audit of HTTP security headers aligned with NZISM controls, CERT NZ recommendations, and the Privacy Act 2020.

Developed and maintained by the cybersecurity and digital sovereignty division of **TAVARDT**.

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

Verify your digital infrastructure against technical baselines using the TAVARDT suite:

* HTTP Security Headers Checker
* [Consent Mode v2 & Privacy Act Validator](https://tools.tavardt.com/nz/consent-mode-v2-checker/)
* [DMARC & Anti-Spoofing Verifier](https://tools.tavardt.com/nz/dmarc-checker/)
* [Exposed Credentials & Secret Scanner](https://tools.tavardt.com/nz/exposed-files-scanner/)
* [Full New Zealand Tools Portal](https://tools.tavardt.com/nz/)

***

## 4. Technical Advisory & Remediation

For NZISM alignment, CERT NZ mitigation implementation, and technical privacy consulting in New Zealand, contact **TAVARDT**.

***

## Useful Links

* **Corporate Portal:** https://ag.tavardt.com/nz/
* **Diagnostic Suite:** https://tools.tavardt.com/nz/
* **Technical Contact:** https://ag.tavardt.com/nz/contact/

***

### License
Released under the MIT License. See [LICENSE](LICENSE) for full details.

***

© 2026 TAVARDT. All rights reserved.
