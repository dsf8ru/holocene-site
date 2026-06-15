from pathlib import Path

css = Path("src/app/globals.css")
s = css.read_text()

if ".trust-badges" not in s:
    s += r"""

.trust-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 22px;
}

.trust-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 38px;
  padding: 0 13px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.78);
  color: var(--ink);
  font-size: 13px;
  font-weight: 800;
  box-shadow: 0 10px 30px rgba(8, 15, 36, 0.05);
}

.trust-badge span {
  color: var(--green);
}

.trust-badge:hover {
  border-color: rgba(47, 99, 246, 0.35);
}
"""
css.write_text(s)

page = Path("src/app/page.tsx")
p = page.read_text()

old = '''              <div className="hero-actions">
                <a className="btn btn-primary" href={registerUrl}>Start Free Analysis</a>
                <a className="btn btn-secondary" href={loginUrl}>Login</a>
              </div>'''

new = '''              <div className="hero-actions">
                <a className="btn btn-primary" href={registerUrl}>Start Free Analysis</a>
                <a className="btn btn-secondary" href={loginUrl}>Login</a>
              </div>

              <div className="trust-badges" aria-label="Holocene marketplace and partner listings">
                <a
                  className="trust-badge"
                  href="https://advertising.amazon.com/en-gb/partners/directory/details/amzn1.ads1.ma1.9zh2pgko4bqxt16cod1g95l55/Holocene-Services-OU"
                  target="_blank"
                  rel="noreferrer"
                >
                  <span>✓</span> Amazon Ads Verified Partner
                </a>
                <a
                  className="trust-badge"
                  href="https://sellercentral.amazon.ae/selling-partner-appstore/dp/amzn1.sp.solution.a0501115-4484-46ea-abf4-4c64bba219ea"
                  target="_blank"
                  rel="noreferrer"
                >
                  <span>✓</span> Amazon Appstore
                </a>
                <a
                  className="trust-badge"
                  href="https://apps.shopify.com/holoceneapi"
                  target="_blank"
                  rel="noreferrer"
                >
                  <span>✓</span> Shopify App Store
                </a>
              </div>'''

if old not in p:
    raise SystemExit("Hero actions block not found. Patch not applied.")

p = p.replace(old, new)
page.write_text(p)

print("Trust badges added.")
