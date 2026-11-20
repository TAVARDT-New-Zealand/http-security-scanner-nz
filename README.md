# HTTP Security Headers Scanner | TAVARDT New Zealand

[![Auditoria de Segurança](https://img.shields.io/badge/TAVARDT-Diagn%C3%B3stico%20T%C3%A9cnico-5b3cf5.svg)](https://tools.tavardt.com/nz/security-headers-check/)
[![Conformidade](https://img.shields.io/badge/Jurisdi%C3%A7%C3%A3o-New Zealand-00C853.svg)](https://ag.tavardt.com/nz/cybersecurity/)

Automated technical audit of HTTP security headers aligned with CERT NZ Critical Controls, the NZISM, and the New Zealand Privacy Act 2020.

Desenvolvido e mantido pela divisão de cibersegurança e proteção de infraestruturas da **[TAVARDT New Zealand](https://ag.tavardt.com/nz/)**.

---

## 1. Scope of Perimeter Verification

This command-line utility evaluates web perimeter security and browser protection directives for New Zealand organisations:

* **Strict-Transport-Security (HSTS):** Força comunicações encriptadas via HTTPS e impede ataques de downgrade e interceptação SSL.
* **Content-Security-Policy (CSP):** Mitiga ataques de injeção de scripts (XSS) e restringe as origens autorizadas para carregamento de recursos.
* **X-Frame-Options:** Previne ataques de clickjacking regulando as permissões de incorporação em frames e iframes.
* **X-Content-Type-Options:** Impede a execução indevida de ficheiros derivados de vulnerabilidades de MIME-sniffing.
* **Referrer-Policy:** Protege dados sensíveis contidos em URLs de referência contra fuga para domínios terceiros.
* **Permissions-Policy:** Aplica o princípio do menor privilégio sobre APIs de hardware do navegador (câmara, microfone e geolocalização).

---

## 2. Quick Start Guide

Execute a ferramenta diretamente via Python sem necessidade de instalar dependências externas:

```bash
python scanner.py exemplo.com
```

---

## 3. Online Diagnostic Tools (New Zealand)

Audite a infraestrutura pública das suas aplicações utilizando a suíte de diagnósticos da TAVARDT:

* [HTTP Security Headers Checker](https://tools.tavardt.com/nz/security-headers-check/)
* [Consent Mode v2 & Privacy Act Validator](https://tools.tavardt.com/nz/consent-mode-v2-checker/)
* [DMARC & Anti-Spoofing Verifier](https://tools.tavardt.com/nz/dmarc-checker/)
* [Exposed Credentials & Secret Scanner](https://tools.tavardt.com/nz/exposed-files-scanner/)
* [Full New Zealand Diagnostic Portal](https://tools.tavardt.com/nz/)

---

## 4. Technical Advisory & Remediation

For CERT NZ Critical Controls alignment, infrastructure hardening, and cyber defence in New Zealand, contact **[TAVARDT New Zealand](https://ag.tavardt.com/nz/contact/)**.
