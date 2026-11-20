#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [('Strict-Transport-Security', 'Enforces strict HTTPS communications and mitigates downgrade risks (HSTS).'), ('Content-Security-Policy', 'Prevents Cross-Site Scripting (XSS) and unauthorized resource loading.'), ('X-Frame-Options', 'Mitigates clickjacking risks by governing frame inclusion.'), ('X-Content-Type-Options', 'Prevents MIME-sniffing vulnerabilities in client browsers.'), ('Referrer-Policy', 'Protects sensitive URL telemetry from leaking across web origins.'), ('Permissions-Policy', 'Restricts browser API privileges according to least-privilege standards.')]

def scan_target(target_url):
    print(f"\n[TAVARDT New Zealand] Starting HTTP security headers perimeter audit for: {target_url}\n")
    try:
        req = urllib.request.Request(
            target_url,
            headers={"User-Agent": "TAVARDT-Security-Scanner/3.0 (en-NZ)"}
        )
        with urllib.request.urlopen(req, timeout=12) as response:
            headers = dict(response.headers.items())
            
            score = 0
            total = len(SECURITY_HEADERS)
            
            for header_name, desc in SECURITY_HEADERS:
                found = any(h.lower() == header_name.lower() for h in headers.keys())
                if found:
                    print(f"  [PASS] {header_name}")
                    score += 1
                else:
                    print(f"  [FAIL] {header_name}: {desc}")
                    
            print(f"\n[TAVARDT New Zealand] Audit Score: {score}/{total}")
            print(f"\nVerificacao completa online: https://tools.tavardt.com/nz/security-headers-check/")
            print(f"Suporte corporativo e ciberdefesa: https://ag.tavardt.com/nz/cybersecurity/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT New Zealand] Erro ao inspecionar o alvo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
