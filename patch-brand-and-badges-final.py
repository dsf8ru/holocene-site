from pathlib import Path
import re

css = Path("src/app/globals.css")
s = css.read_text()

s += r"""

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-mark {
  width: 46px;
  height: 46px;
  object-fit: contain;
  flex: 0 0 auto;
}

.brand-title {
  display: block;
  font-size: 20px;
  font-weight: 900;
  letter-spacing: -0.04em;
  color: var(--ink);
  line-height: 1;
}

.brand-subtitle {
  display: block;
  margin-top: 4px;
  font-size: 12px;
  font-weight: 750;
  color: var(--muted);
  line-height: 1;
}

.badges-section {
  padding: 10px 0 42px;
}

.badges-row {
  display: flex;
  align-items: center;
  gap: 22px;
  flex-wrap: wrap;
}

.badge-img {
  display: block;
  height: 54px;
  width: auto;
  object-fit: contain;
}

.badge-link:hover {
  opacity: 0.9;
}

@media (max-width: 980px) {
  .brand-mark {
    width: 38px;
    height: 38px;
  }

  .brand-title {
    font-size: 17px;
  }

  .brand-subtitle {
    font-size: 10px;
  }

  .badge-img {
    height: 42px;
  }
}
"""

css.write_text(s)

page = Path("src/app/page.tsx")
p = page.read_text()

# Header logo -> HTML brand
p = re.sub(
    r'''<a href="/" aria-label="Holocene home">\s*<Image className="logo-img" src="/logo-transparent.png" alt="Holocene AI Pricing Co-Pilot" width=\{760\} height=\{190\} priority />\s*</a>''',
    '''<a className="brand" href="/" aria-label="Holocene home">
          <Image className="brand-mark" src="/logo-transparent.png" alt="Holocene" width={96} height={96} priority />
          <span>
            <span className="brand-title">Holocene</span>
            <span className="brand-subtitle">AI Pricing Co-Pilot</span>
          </span>
        </a>''',
    p
)

# Remove old trust/partner badges if any
p = re.sub(r'\n\s*<div className="trust-badges"[\s\S]*?</div>', '', p)
p = re.sub(r'\n\s*<div className="partner-badges"[\s\S]*?</div>', '', p)

hero_end = '''        </section>

        <section className="section">
          <div className="container workspace-grid">'''

badges = '''        </section>

        <section className="badges-section" aria-label="Holocene marketplace and partner listings">
          <div className="container badges-row">
            <a className="badge-link" href="https://advertising.amazon.com/en-gb/partners/directory/details/amzn1.ads1.ma1.9zh2pgko4bqxt16cod1g95l55/Holocene-Services-OU" target="_blank" rel="noreferrer">
              <img className="badge-img" src="/badges/amazon-ads.png" alt="Amazon Ads Verified Partner" />
            </a>
            <a className="badge-link" href="https://sellercentral.amazon.ae/selling-partner-appstore/dp/amzn1.sp.solution.a0501115-4484-46ea-abf4-4c64bba219ea" target="_blank" rel="noreferrer">
              <img className="badge-img" src="/badges/amazon-appstore.png" alt="Available at Amazon Appstore" />
            </a>
            <a className="badge-link" href="https://apps.shopify.com/holoceneapi" target="_blank" rel="noreferrer">
              <img className="badge-img" src="/badges/shopify-appstore.png" alt="Find it on the Shopify App Store" />
            </a>
          </div>
        </section>

        <section className="section">
          <div className="container workspace-grid">'''

if hero_end not in p:
    raise SystemExit("Could not find hero end marker.")

p = p.replace(hero_end, badges)

page.write_text(p)

print("Brand and badges final patch applied.")
