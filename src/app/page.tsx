import Image from "next/image";

const loginUrl = "https://app.holocene.ee/login";
const registerUrl = "https://app.holocene.ee/register";

function Header() {
  return (
    <header className="nav">
      <div className="container nav-inner">
        <a className="brand" href="/" aria-label="Holocene home">
          <Image className="brand-mark" src="/logo-transparent.png" alt="Holocene" width={96} height={96} priority />
          <span>
            <span className="brand-title">Holocene</span>
            <span className="brand-subtitle">AI Pricing Co-Pilot</span>
          </span>
        </a>

        <nav className="nav-links">
          <a href="/algorithm">ML Algorithm</a>
          <a href="#faq">FAQ</a>
        </nav>

        <div className="actions">
          <a className="btn btn-secondary" href={loginUrl}>Login</a>
          <a className="btn btn-primary" href={registerUrl}>Start Free Analysis</a>
        </div>
      </div>
    </header>
  );
}

function Screen({ desktop, mobile, alt, priority = false, hero = false }: {
  desktop: string;
  mobile: string;
  alt: string;
  priority?: boolean;
  hero?: boolean;
}) {
  return (
    <div className={`screen-frame ${hero ? "hero-screen" : ""}`}>
      <Image className="desktop-shot" src={desktop} alt={alt} width={1440} height={900} priority={priority} />
      <Image className="mobile-shot" src={mobile} alt={alt} width={520} height={900} priority={priority} />
    </div>
  );
}

function Footer() {
  return (
    <footer className="footer">
      <div className="container footer-inner">
        <a className="footer-brand" href="/" aria-label="Holocene home">

          <Image className="footer-mark" src="/logo-transparent.png" alt="Holocene" width={64} height={64} />

          <span>Holocene</span>

        </a>
        <div className="footer-links">
          <a href="/privacy">Privacy</a>
          <a href="/terms">Terms</a>
          <a href="/support">Support</a>
        </div>
      </div>
    </footer>
  );
}

export default function Home() {
  return (
    <>
      <Header />

      <main>
        <section className="hero">
          <div className="container hero-grid">
            <div>
              <div className="eyebrow">Built for Amazon Private Label sellers</div>
              <h1>Holocene AI Pricing Co-Pilot</h1>
              <p className="lead">
                Understand how pricing behavior impacts revenue and profit. Analyze Seller Central and Amazon Ads data to identify pricing opportunities, evaluate pricing evidence, and make better pricing decisions.
              </p>

              <div className="hero-actions">
                <a className="btn btn-primary" href={registerUrl}>Start Free Analysis</a>
                <a className="btn btn-secondary" href={loginUrl}>Login</a>
              </div>
            </div>

            <Screen
              desktop="/image1.jpg"
              mobile="/image_m1.jpg"
              alt="Holocene Pricing Dashboard"
              priority
              hero
            />
          </div>
        </section>

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
          <div className="container workspace-grid">
            <Screen
              desktop="/image2.jpg"
              mobile="/image_m2.jpg"
              alt="Holocene Pricing Workspace"
            />

            <div className="workspace-copy">
              <div className="section-head">
                <h2>Pricing Workspace</h2>
                <p>
                  Move from product opportunity to price-level analysis. Review pricing evidence,
                  historical price points, recommended revenue prices, recommended profit prices,
                  and expected impact before making changes in Amazon.
                </p>
              </div>
            </div>
          </div>
        </section>

        <section className="section" id="how">
          <div className="container workflow">
            <div className="section-head">
              <h2>How it works</h2>
              <p>
                Connect Amazon data, let Holocene evaluate pricing behavior, then review recommendations
                or enable the AI co-pilot workflow.
              </p>
            </div>

            <div className="steps">
              <div className="step">
                <div className="step-num">1</div>
                <h3>Connect Amazon data</h3>
                <p>Connect Seller Central and Amazon Ads.</p>
              </div>
              <div className="step">
                <div className="step-num">2</div>
                <h3>Analyze pricing behavior</h3>
                <p>Holocene reviews sales, price changes, discounts, advertising context, and cost completeness.</p>
              </div>
              <div className="step">
                <div className="step-num">3</div>
                <h3>Review recommendations</h3>
                <p>Inspect pricing evidence, revenue opportunity, profit opportunity, and recommended prices.</p>
              </div>
              <div className="step">
                <div className="step-num">4</div>
                <h3>Enable AI co-pilot</h3>
                <p>Use recommendation mode first, then move toward controlled price optimization when ready.</p>
              </div>
            </div>
          </div>
        </section>

        <section className="section" id="faq">
          <div className="container faq">
            <div>
              <h2>FAQ</h2>
              <p className="lead">A practical pricing analytics layer for sellers using Amazon Seller Central and Amazon Ads.</p>
            </div>

            <div className="faq-list">
              <div className="faq-item">
                <h3>Who is Holocene built for?</h3>
                <p>Holocene is built for Amazon Private Label sellers who control their own prices and want product-level pricing decisions backed by data.</p>
              </div>
              <div className="faq-item">
                <h3>What data does Holocene use?</h3>
                <p>Holocene uses Seller Central sales data and Amazon Ads performance data to analyze pricing behavior, revenue opportunity, profit opportunity, and advertising context.</p>
              </div>
              <div className="faq-item">
                <h3>Do I need product costs?</h3>
                <p>No. You can start with revenue opportunity first. Profit opportunity becomes available after COGS, FBA fees, and marketplace fees are added.</p>
              </div>
              <div className="faq-item">
                <h3>Does Holocene automatically change prices?</h3>
                <p>Holocene starts with analytics and recommendations. Automated price optimization is designed as a controlled co-pilot workflow with seller-defined limits.</p>
              </div>
              <div className="faq-item">
                <h3>Why does Holocene use the last 60 days?</h3>
                <p>A 60-day window gives the model enough recent price and sales behavior to evaluate pricing activity without relying on outdated market conditions.</p>
              </div>
            </div>
          </div>
        </section>

        <section className="section">
          <div className="container cta">
            <div>
              <h2>Start with a free pricing analysis.</h2>
              <p>Connect Amazon data, review your pricing dashboard, and open Pricing Workspace to inspect product-level opportunities.</p>
            </div>
            <a className="btn btn-secondary" href={registerUrl}>Start Free Analysis</a>
          </div>
        </section>
      </main>

      <Footer />
    </>
  );
}
