
from pathlib import Path

p = Path("src/app/globals.css")

s = p.read_text()

if ".footer-inner {" in s:

    s = s.replace(

        ".footer-inner {",

        ".footer-inner {\n  align-items: center;"

    )

s = s.replace(

    "width: 270px;",

    "width: 180px;"

)

p.write_text(s)

print("Footer logo patch applied")

