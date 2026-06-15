
from pathlib import Path

import re

css = Path("src/app/globals.css")

s = css.read_text()

s += r"""

.brand {

  display: flex;

  align-items: center;

  gap: 10px;

}

.brand-mark {

  width: 38px;

  height: 38px;

  object-fit: contain;

  flex: 0 0 auto;

}

.brand-copy {

  display: flex;

  flex-direction: column;

  line-height: 1;

}

.brand-title {

  font-size: 18px;

  font-weight: 850;

  color: var(--ink);

  letter-spacing: -0.035em;

}

.brand-subtitle {

  margin-top: 4px;

  font-size: 11px;

  font-weight: 700;

  color: var(--muted);

}

@media (max-width: 980px) {

  .brand-mark {

    width: 34px;

    height: 34px;

  }

  .brand-title {

    font-size: 16px;

  }

  .brand-subtitle {

    font-size: 10px;

  }

}

"""

css.write_text(s)

page = Path("src/app/page.tsx")

p = page.read_text()

old_header_logo = '''        <a href="/" aria-label="Holocene home">

          <Image className="logo-img" src="/logo-transparent.png" alt="Holocene AI Pricing Co-Pilot" width={760} height={190} priority />

        </a>'''

new_header_logo = '''        <a className="brand" href="/" aria-label="Holocene home">

          <Image className="brand-mark" src="/logo-transparent.png" alt="Holocene" width={80} height={80} priority />

          <span className="brand-copy">

            <span className="brand-title">Holocene</span>

            <span className="brand-subtitle">AI Pricing Co-Pilot</span>

          </span>

        </a>'''

if old_header_logo in p:

    p = p.replace(old_header_logo, new_header_logo)

# Remove partner badges from hero

p = re.sub(

    r'\n\s*<div className="partner-badges"[\s\S]*?</div>\n\s*</div>',

    '\n            </div>',

    p,

    count=1,

)

# Remove old trust badges if still present

p = re.sub(

    r'\n\s*<div className="trust-badges"[\s\S]*?</div>\n\s*</div>',

    '\n            </div>',

    p,

    count=1,

)

page.write_text(p)

print("Header brand updated and hero badges removed.")

