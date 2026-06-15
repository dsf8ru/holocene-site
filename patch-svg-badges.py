from pathlib import Path

public = Path("public")
badges = public / "badges"
badges.mkdir(parents=True, exist_ok=True)

def write(name: str, svg: str):
    (badges / name).write_text(svg)

write("amazon-ads.svg", r'''<svg xmlns="http://www.w3.org/2000/svg" width="260" height="96" viewBox="0 0 260 96">
  <rect x="2" y="2" width="256" height="92" rx="22" fill="white" stroke="#dbe3ef"/>
  <text x="24" y="34" font-family="Inter, Arial, sans-serif" font-size="25" font-weight="800" fill="#111827">amazon ads</text>
  <path d="M43 42c21 12 54 12 79-1" stroke="#111827" stroke-width="4" fill="none" stroke-linecap="round"/>
  <path d="M115 37l13 1-7 10" stroke="#111827" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="24" y="65" font-family="Inter, Arial, sans-serif" font-size="20" font-weight="850" fill="#0f9f9a">Verified</text>
  <text x="24" y="84" font-family="Inter, Arial, sans-serif" font-size="20" font-weight="850" fill="#1f2937">partner</text>
</svg>''')

write("amazon-appstore.svg", r'''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="76" viewBox="0 0 300 76">
  <rect x="2" y="2" width="296" height="72" rx="12" fill="white" stroke="#111827" stroke-width="2"/>
  <text x="126" y="24" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="15" font-weight="700" fill="#4b5563">available at</text>
  <text x="150" y="53" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="33" font-weight="850" fill="#3f3f46">amazon appstore</text>
  <path d="M80 58c25 13 67 13 98-1" stroke="#3f3f46" stroke-width="4" fill="none" stroke-linecap="round"/>
  <path d="M170 53l13 1-7 10" stroke="#3f3f46" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</svg>''')

write("shopify-appstore.svg", r'''<svg xmlns="http://www.w3.org/2000/svg" width="320" height="76" viewBox="0 0 320 76">
  <rect x="2" y="2" width="316" height="72" rx="10" fill="white" stroke="#d1d5db"/>
  <path d="M37 22l29-6 8 7-4 39-41-6 4-31 4-3z" fill="#95bf47"/>
  <path d="M46 23c1-10 13-12 15 0" stroke="white" stroke-width="3" fill="none"/>
  <text x="53" y="54" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="32" font-weight="900" fill="white">S</text>
  <text x="92" y="29" font-family="Inter, Arial, sans-serif" font-size="13" font-weight="850" letter-spacing="2" fill="#111827">FIND IT ON THE</text>
  <text x="92" y="56" font-family="Inter, Arial, sans-serif" font-size="30" font-weight="500" fill="#111827">Shopify App Store</text>
</svg>''')

css = Path("src/app/globals.css")
s = css.read_text()

s += r'''

.partner-badges {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-top: 24px;
  flex-wrap: wrap;
}

.partner-badge {
  display: inline-flex;
  align-items: center;
  transition: transform 0.15s ease, opacity 0.15s ease;
}

.partner-badge:hover {
  transform: translateY(-1px);
  opacity: 0.92;
}

.partner-badge img {
  display: block;
  height: 44px;
  width: auto;
}

.partner-badge:first-child img {
  height: 56px;
}

@media (max-width: 980px) {
  .partner-badges {
    gap: 10px;
  }

  .partner-badge img,
  .partner-badge:first-child img {
    height: 42px;
  }
}
'''
css.write_text(s)

page = Path("src/app/page.tsx")
p = page.read_text()

start = p.find('              <div className="trust-badges"')
if start != -1:
    end = p.find('              </div>', start)
    end = p.find('\n', end) + 1
    p = p[:start] + '''              <div className="partner-badges" aria-label="Holocene marketplace and partner listings">
                <a className="partner-badge" href="https://advertising.amazon.com/en-gb/partners/directory/details/amzn1.ads1.ma1.9zh2pgko4bqxt16cod1g95l55/Holocene-Services-OU" target="_blank" rel="noreferrer">
                  <img src="/badges/amazon-ads.svg" alt="Amazon Ads Verified Partner" />
                </a>
                <a className="partner-badge" href="https://sellercentral.amazon.ae/selling-partner-appstore/dp/amzn1.sp.solution.a0501115-4484-46ea-abf4-4c64bba219ea" target="_blank" rel="noreferrer">
                  <img src="/badges/amazon-appstore.svg" alt="Available at Amazon Appstore" />
                </a>
                <a className="partner-badge" href="https://apps.shopify.com/holoceneapi" target="_blank" rel="noreferrer">
                  <img src="/badges/shopify-appstore.svg" alt="Find it on the Shopify App Store" />
                </a>
              </div>
''' + p[end:]
else:
    marker = '''              <div className="hero-actions">
                <a className="btn btn-primary" href={registerUrl}>Start Free Analysis</a>
                <a className="btn btn-secondary" href={loginUrl}>Login</a>
              </div>'''
    replacement = marker + '''

              <div className="partner-badges" aria-label="Holocene marketplace and partner listings">
                <a className="partner-badge" href="https://advertising.amazon.com/en-gb/partners/directory/details/amzn1.ads1.ma1.9zh2pgko4bqxt16cod1g95l55/Holocene-Services-OU" target="_blank" rel="noreferrer">
                  <img src="/badges/amazon-ads.svg" alt="Amazon Ads Verified Partner" />
                </a>
                <a className="partner-badge" href="https://sellercentral.amazon.ae/selling-partner-appstore/dp/amzn1.sp.solution.a0501115-4484-46ea-abf4-4c64bba219ea" target="_blank" rel="noreferrer">
                  <img src="/badges/amazon-appstore.svg" alt="Available at Amazon Appstore" />
                </a>
                <a className="partner-badge" href="https://apps.shopify.com/holoceneapi" target="_blank" rel="noreferrer">
                  <img src="/badges/shopify-appstore.svg" alt="Find it on the Shopify App Store" />
                </a>
              </div>'''
    if marker not in p:
        raise SystemExit("Hero actions marker not found.")
    p = p.replace(marker, replacement)

page.write_text(p)

print("SVG partner badges created and inserted.")
