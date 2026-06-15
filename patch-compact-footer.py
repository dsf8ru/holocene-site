
from pathlib import Path

page = Path("src/app/page.tsx")

s = page.read_text()

old = '''        <Image className="logo-img" src="/logo-transparent.png" alt="Holocene AI Pricing Co-Pilot" width={760} height={190} />'''

new = '''        <a className="footer-brand" href="/" aria-label="Holocene home">

          <Image className="footer-mark" src="/logo-transparent.png" alt="Holocene" width={64} height={64} />

          <span>Holocene</span>

        </a>'''

s = s.replace(old, new)

page.write_text(s)

css = Path("src/app/globals.css")

c = css.read_text()

c += """

.footer {

  padding: 14px 0 !important;

}

.footer-inner {

  min-height: 44px;

}

.footer-brand {

  display: flex;

  align-items: center;

  gap: 10px;

}

.footer-mark {

  width: 32px;

  height: 32px;

  object-fit: contain;

}

.footer-brand span {

  font-size: 15px;

  font-weight: 850;

  color: var(--ink);

}

"""

css.write_text(c)

print("Compact footer applied.")

