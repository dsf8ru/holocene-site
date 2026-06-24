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

          <span>Holocene</span><small>AI Pricing Co-Pilot</small>

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
              <div className="eyebrow">AI Revenue Manager for Amazon Private Label and Brands</div>
              <h1>AI Revenue Manager<br />for Amazon Brands</h1>
              <p className="lead">
                Find where your Amazon business is leaving money behind — pricing, advertising, revenue, and profit opportunities in one dashboard.
              </p>

              <div className="hero-actions">
                <a className="btn btn-primary" href={registerUrl}>Start Free Analysis</a>
                <a className="btn btn-secondary" href={loginUrl}>Login</a>
              </div>
            </div>

            <Screen
              desktop="/revenue-manager-desktop.webp"
              mobile="/revenue-manager-mobile.webp"
              alt="Holocene AI Revenue Manager dashboard"
              priority
              hero
            />
          </div>
        </section>



        <section className="value-strip" aria-label="Revenue Manager capabilities">
          <div className="container value-grid">
            <div className="value-card">
              <span className="value-kicker">Revenue Opportunities</span>
              <strong>+$9,067/month</strong>
              <p>Find products with revenue upside from pricing and advertising.</p>
            </div>
            <div className="value-card">
              <span className="value-kicker">Profit Opportunities</span>
              <strong className="profit">+$3,218/month</strong>
              <p>See profit impact before you make changes.</p>
            </div>
            <div className="value-card">
              <span className="value-kicker">Advertising Expansion</span>
              <strong>+$1,257/month</strong>
              <p>Identify products where more ad spend can drive growth.</p>
            </div>
            <div className="value-card">
              <span className="value-kicker">Recommended Actions</span>
              <strong>3 products</strong>
              <p>Know what to review next for every product.</p>
            </div>
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
<section className="section" id="how">
          <div className="container workflow">
            <div className="section-head">
              <h2>How it works</h2>
              <p>
                Connect Amazon, let Holocene analyze the last 60 days, then review revenue opportunities or enable the AI co-pilot workflow.
              </p>
            </div>

            <div className="steps">
              <div className="step">
                <div className="step-num">1</div>
                <h3>Connect Amazon</h3>
                <p>Connect Seller Central and Amazon Ads.</p>
              </div>
              <div className="step">
                <div className="step-num">2</div>
                <h3>AI analyzes your business</h3>
                <p>Holocene reviews sales, pricing, advertising, and product economics from the last 60 days.</p>
              </div>
              <div className="step">
                <div className="step-num">3</div>
                <h3>Revenue opportunities identified</h3>
                <p>Find pricing, advertising, and profit improvements for every product.</p>
              </div>
              <div className="step">
                <div className="step-num">4</div>
                <h3>Review or automate</h3>
                <p>Start with recommendations, then enable AI Revenue Manager when ready.</p>
              </div>
            </div>
          </div>
        </section>

        <section className="section" id="faq">
          <div className="container faq">
            <div>
              <h2>FAQ</h2>
              <p className="lead">A practical AI Revenue Manager for sellers using Amazon Seller Central and Amazon Ads.</p>
            </div>

            <div className="faq-list">
              <div className="faq-item">
                <h3>What does AI Revenue Manager actually do?</h3>
                <p>Holocene identifies revenue, profit, pricing, and advertising opportunities for Amazon Private Label sellers, then turns them into product-level recommended actions.</p>
              </div>
              <div className="faq-item">
                <h3>What data does Holocene use?</h3>
                <p>Holocene uses Seller Central sales data and Amazon Ads performance data to analyze revenue opportunity, profit opportunity, pricing behavior, and advertising expansion.</p>
              </div>
              <div className="faq-item">
                <h3>Do I need product costs?</h3>
                <p>No. You can start with revenue opportunity first. Profit opportunities becomes available after COGS, FBA fees, and marketplace fees are added.</p>
              </div>
              <div className="faq-item">
                <h3>Does Holocene automatically change prices?</h3>
                <p>Holocene starts with analytics and recommendations. Automated optimization is designed as a controlled Revenue Manager workflow with seller-defined limits.</p>
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
              <h2>See how much revenue you're leaving behind.</h2>
              <p>Connect Amazon, review your revenue dashboard, and see where products may be leaving money behind.</p>
            </div>
            <a className="btn btn-secondary" href={registerUrl}>Start Free Analysis</a>
          </div>
        </section>
      </main>

      <Footer />
    </>
  );
}
