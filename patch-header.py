
from pathlib import Path

p = Path("src/app/globals.css")

s = p.read_text()

replacements = {

    "min-height: 64px;": "min-height: 56px;",

    "width: 205px;": "width: 270px;",

    "font-size: 14px;": "font-size: 15px;",

    "padding: 24px 0;": "padding: 18px 0;",

}

for old, new in replacements.items():

    s = s.replace(old, new)

p.write_text(s)

print("Header/Footer patch applied")

