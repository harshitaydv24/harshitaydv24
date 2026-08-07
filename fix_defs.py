"""
Fix: move vigL/vigR/vigB linearGradient elements into <defs> in banner.svg and banner-light.svg
"""
import re, os

def fix_banner(filepath):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    # Extract the three inline gradient definitions
    grad_pattern = re.compile(
        r'\s*<linearGradient id="(vigL|vigR|vigB)"[^>]*>.*?</linearGradient>',
        re.DOTALL
    )

    grads_found = grad_pattern.findall(content)
    grads_text  = grad_pattern.findall(content)

    # Collect full gradient blocks
    extracted = []
    for m in grad_pattern.finditer(content):
        extracted.append(m.group(0))

    if not extracted:
        print(f"  No inline gradients found in {os.path.basename(filepath)}")
        return

    # Remove them from body
    for block in extracted:
        content = content.replace(block, '', 1)

    # Build the defs insertion string
    defs_insert = "\n    <!-- ── vignette gradients (moved to defs) ── -->"
    for block in extracted:
        # Normalize indentation
        defs_insert += "\n   " + block.strip()

    # Insert before closing </defs>
    content = content.replace('</defs>', defs_insert + '\n  </defs>', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Fixed {os.path.basename(filepath)}: moved {len(extracted)} gradients into <defs>")

fix_banner("banner.svg")
fix_banner("banner-light.svg")

# Re-validate XML
import xml.etree.ElementTree as ET
for fn in ["banner.svg", "banner-light.svg"]:
    try:
        ET.parse(fn)
        print(f"  XML OK: {fn}")
    except Exception as e:
        print(f"  XML FAIL: {fn} -> {e}")

print("Done!")
