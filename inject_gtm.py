#!/usr/bin/env python3
"""Inject Google Tag Manager scripts into the built index.html"""

import sys
from pathlib import Path

GTM_HEAD = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-MVDTHBQ');</script>
<!-- End Google Tag Manager -->
"""

GTM_BODY = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MVDTHBQ"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""

def inject_gtm(html_path: Path):
    """Inject GTM scripts into the HTML file"""
    if not html_path.exists():
        print(f"Error: {html_path} does not exist")
        sys.exit(1)
    
    html_content = html_path.read_text()
    
    # Inject GTM head script after <head> or at the beginning if no head tag
    if '<head>' in html_content:
        html_content = html_content.replace('<head>', f'<head>\n{GTM_HEAD}', 1)
    elif '<html' in html_content.lower():
        # Find end of html opening tag and inject there
        import re
        html_content = re.sub(r'(<html[^>]*>)', rf'\1\n{GTM_HEAD}', html_content, count=1, flags=re.IGNORECASE)
    
    # Inject GTM body script after <body> or similar opening tag
    if '<body>' in html_content:
        html_content = html_content.replace('<body>', f'<body>\n{GTM_BODY}', 1)
    elif '<body' in html_content.lower():
        import re
        html_content = re.sub(r'(<body[^>]*>)', rf'\1\n{GTM_BODY}', html_content, count=1, flags=re.IGNORECASE)
    
    html_path.write_text(html_content)
    print(f"✓ GTM scripts injected into {html_path}")

if __name__ == '__main__':
    html_file = Path('build/web/index.html')
    inject_gtm(html_file)
