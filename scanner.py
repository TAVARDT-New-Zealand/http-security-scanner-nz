#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [('Strict-Transport-Security', 'Enforces HTTPS encryption and prevents downgrade and interception attacks.'), ('Content-Security-Policy', 'Restricts script loading to mitigate Cross-Site Scripting (XSS) and unauthorized code.'), ('X-Frame-Options', 'Prevents clickjacking attacks by managing iframe and frame embedding rules.'), ('X-Content-Type-Options', 'Blocks MIME-sniffing vulnerabilities in client browsers.'), ('Referrer-Policy', 'Protects sensitive URL parameters from cross-origin disclosure.'), ('Permissions-Policy', 'Enforces least-privilege control for browser hardware sensors and APIs.')]

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
            print(f"\nFull online diagnostic tool: https://tools.tavardt.com/nz/security-headers-check/")
            print(f"Corporate cyber resilience and consulting: https://ag.tavardt.com/nz/cybersecurity/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT New Zealand] Error inspecting target: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
