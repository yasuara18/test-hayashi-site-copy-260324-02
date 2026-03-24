import re

with open(r'C:\Users\yasuy\AppData\Local\Temp\temp_hematology\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract header and hero CSS from original HTML
match = re.search(r'/\* ===== HEADER / NAV ===== \*/.*?/\* ===== SECTIONS ===== \*/', html, re.DOTALL)
if match:
    original_css = match.group(0).replace('/* ===== SECTIONS ===== */', '')
else:
    print("Could not find original CSS block")
    exit()

# Replace in style.css
with open('style.css', 'r', encoding='utf-8') as f:
    style_css = f.read()

# We need to replace our current header & hero section
# From /* Header */ to /* Sections */
style_css = re.sub(r'/\* Header \*/.*?/\* Sections \*/', original_css + '/* Sections */', style_css, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(style_css)
print("Updated style.css successfully")
