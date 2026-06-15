from pathlib import Path

app = Path("src/app")

(app / "globals.css").write_text(r'''@import "tailwindcss";

:root {
  --bg: #f6f8fb;
  --ink: #080f24;
  --muted: #66748b;
  --line: #dbe3ef;
  --card: #ffffff;
  --blue: #2f63f6;
  --green: #16a34a;
  --orange: #f97316;
  --navy: #020817;
}

* { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
  margin: 0;
  background:
    radial-gradient(circle at 20% 0%, rgba(47, 99, 246, 0.08), transparent 34rem),
    linear-gradient(180deg, #f8fbff 0%, #f3f6fb 100%);
  color: var(--ink);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

a { color: inherit; text-decoration: none; }

.container {
  width: min(1220px, calc(100% - 32px));
  margin: 0 auto;
}

.nav {
  position: sticky;
  top: 0;
  z-index: 20;
  background: rgba(248, 251, 255, 0.84);
  backdrop-filter: blur(18px);
  border-bottom: 1px solid rgba(219, 227, 239, 0.9);
}

.nav-inner {
  min-height: 78px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

.logo-img {
  height: 42px;
  width: auto;
  object-fit: contain;
  display: block;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 24px;
  color: var(--muted);
  font-size: 14px;
  font-weight: 650;
}

.actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 0 18px;
  border-radius: 999px;
  font-size: 14px;
  font-weight: 800;
  border: 1px solid var(--line);
  white-space: nowrap;
}

.btn-primary {
  color: white;
  background: var(--navy);
  border-color: var(--navy);
}

.btn-secondary {
  background: white;
  color: var(--ink);
}

.hero {
  padding: 72px 0 44px;
}

.hero-grid {
  display: grid;
  grid-template-columns: 0.86fr 1.14fr;
  gap: 42px;
  align-items: center;
}

.eyebrow {
  display: inline-flex;
  align-items: center;
  color: #14532d;
  background: #dcfce7;
  border: 1px solid #bbf7d0;
  border-radius: 999px;
  padding: 8px 12px;
  font-size: 13px;
  font-weight: 850;
}

h1 {
  font-size: clamp(46px, 7vw, 84px);
  line-height: 0.92;
  letter-spacing: -0.075em;
  margin: 22px 0;
}

h2 {
  font-size: clamp(34px, 5vw, 58px);
  line-height: 1;
  letter-spacing: -0.06em;
  margin: 0 0 16px;
}

h3 {
  margin: 0 0 10px;
  letter-spacing: -0.035em;
}

.lead {
  color: var(--muted);
  font-size: 20px;
  line-height: 1.55;
  max-width: 680px;
}

.hero-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 30px;
}

.trust-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 28px;
}

.trust-pill {
  background: white;
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 10px 13px;
  color: var(--muted);
  font-size: 13px;
  font-weight: 750;
}

.screen-frame {
  background: white;
  border: 1px solid var(--line);
  border-radius: 28px;
  padding: 10px;
  box-shadow: 0 30px 90px rgba(8, 15, 36, 0.12);
  overflow: hidden;
}

.screen-frame img {
  width: 100%;
  display: block;
  border-radius: 20px;
}

.mobile-shot { display: none !important; }

.section {
  padding: 70px 0;
}

.section-head {
  max-width: 800px;
  margin-bottom: 28px;
}

.section-head p {
  color: var(--muted);
  font-size: 18px;
  line-height: 1.6;
}

.split {
  display: grid;
  grid-template-columns: 0.72fr 1.28fr;
  gap: 30px;
  align-items: center;
}

.split-reverse {
  grid-template-columns: 1.24fr 0.76fr;
}

.feature-list {
  display: grid;
  gap: 14px;
}

.feature {
  background: white;
  border: 1px solid var(--line);
  border-radius: 22px;
  padding: 22px;
}

.feature p {
  color: var(--muted);
  line-height: 1.55;
  margin: 0;
}

.feature-icon {
  width: 42px;
  height: 42px;
  border-radius: 14px;
  display: grid;
  place-items: center;
  margin-bottom: 14px;
  font-weight: 900;
}

.green { background: #dcfce7; color: var(--green); }
.orange { background: #ffedd5; color: var(--orange); }
.blue { background: #dbeafe; color: var(--blue); }
.purple { background: #ede9fe; color: #7c3aed; }

.cards-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.integration-box {
  background: var(--navy);
  color: white;
  border-radius: 32px;
  padding: 34px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 22px;
  align-items: stretch;
}

.integration-box p {
  color: #bac6d8;
  line-height: 1.6;
}

.integration-card {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.14);
  border-radius: 22px;
  padding: 22px;
}

.faq {
  display: grid;
  grid-template-columns: 0.7fr 1.3fr;
  gap: 30px;
}

.faq-list {
  display: grid;
  gap: 14px;
}

.faq-item {
  background: white;
  border: 1px solid var(--line);
  border-radius: 22px;
  padding: 22px;
}

.faq-item p {
  margin: 0;
  color: var(--muted);
  line-height: 1.6;
}

.cta {
  background:
    radial-gradient(circle at 20% 0%, rgba(47, 99, 246, 0.35), transparent 24rem),
    var(--navy);
  color: white;
  border-radius: 34px;
  padding: 42px;
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 24px;
  align-items: center;
}

.cta p {
  color: #c5d0e2;
}

.footer {
  border-top: 1px solid var(--line);
  padding: 34px 0;
  color: var(--muted);
}

.footer-inner {
  display: flex;
  justify-content: space-between;
  gap: 18px;
  flex-wrap: wrap;
  align-items: center;
}

.footer-links {
  display: flex;
  gap: 18px;
}

.simple-page {
  max-width: 860px;
  padding: 70px 0;
}

.simple-page h1 {
  font-size: clamp(40px, 6vw, 62px);
}

.simple-page p,
.simple-page li {
  color: var(--muted);
  line-height: 1.7;
}

@media (max-width: 920px) {
  .nav-inner {
    min-height: auto;
    padding: 14px 0;
  }

  .logo-img {
    height: 36px;
    max-width: 210px;
  }

  .nav-links {
    display: none;
  }

  .actions .btn-secondary {
    display: none;
  }

  .hero {
    padding-top: 44px;
  }

  .hero-grid,
  .split,
  .split-reverse,
  .integration-box,
  .faq,
  .cta {
    grid-template-columns: 1fr;
  }

  .cards-3 {
    grid-template-columns: 1fr;
  }

  .lead {
    font-size: 18px;
  }

  .desktop-shot { display: none !important; }
  .mobile-shot { display: block !important; }

  .screen-frame {
    border-radius: 22px;
    padding: 8px;
  }

  .screen-frame img {
    border-radius: 16px;
  }

  .cta {
    padding: 28px;
  }
}
''')

(app / "page.tsx").write_text(r'''import Image from "next/image";

const appUrl = "https://app.holocene.ee/login";

function Header() {
  return (
    <header className="nav">
      <div className="container nav-inner">
        <a href="/" aria-label="Holocene home">
          <Image
            className="logo-img"
            src="/new_logo.png"
            alt="Holocene AI Pricing Co-Pilot"
            width={520}
            height={130}
            priority
          />
        </a>

        <nav className="nav-links">
          <a href="#dashboard">Dashboard</a>
          <a href="#workspace">Pricing Workspace</a>
          <a href="#integrations">Integrations</a>
          <a href="/pricing">Pricing</a>
        </nav>

        <div className="actions">
          <a className="btn btn-secondary" href={appUrl}>Login</a>
          <a className="btn btn-primary" href={appUrl}>Start Free Analysis</a>
        </div>
      </div>
    </header>
  );
}

function Screen({
  desktop,
  mobile,
  alt,
  priority = false,
}: {
  desktop: string;
  mobile: string;
  alt: string;
  priority?: boolean;
}) {
  return (
    <div className="screen-frame">
      <Image
        className="desktop-shot"
        src={desktop}
        alt={alt}
        width={1440}
        height={900}
        priority={priority}
      />
      <Image
        className="mobile-shot"
        src={mobile}
        alt={alt}
        width={520}
        height={900}
        priority={priority}
      />
    </div>
  );
}

function Footer() {
  return (
    <footer className="footer">
      <div className="container footer-inner">
        <div>© {new Date().getFullYear()} Holocene. Amazon pricing analytics for Private Label sellers.</div>
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
              <h1>Amazon pricing analytics for better price decisions.</h1>
              <p className="lead">
                Holocene AI Pricing Co-Pilot analyzes Seller Central and Amazon Ads data
                to show pricing activity, pricing evidence, revenue opportunity, and
                profit opportunity by product.
              </p>

              <div className="hero-actions">
                <a className="btn btn-primary" href={appUrl}>Start Free Analysis</a>
                <a className="btn btn-secondary" href="#workspace">View Pricing Workspace</a>
              </div>

              <div className="trust-row">
                <div className="trust-pill">Seller Central data</div>
                <div className="trust-pill">Amazon Ads data</div>
                <div className="trust-pill">60-day pricing model</div>
                <div className="trust-pill">Weekly refresh cadence</div>
              </div>
            </div>

            <Screen
              desktop="/image1.jpg"
              mobile="/image_m1.jpg"
              alt="Holocene Pricing Dashboard showing revenue opportunity, profit opportunity, pricing activity, and qualified products."
              priority
            />
          </div>
        </section>

        <section className="section" id="dashboard">
          <div className="container split">
            <div>
              <div className="section-head">
                <h2>Pricing Dashboard</h2>
                <p>
                  See where pricing behavior may be leaving money on the table before
                  opening individual products.
                </p>
              </div>

              <div className="feature-list">
                <div className="feature">
                  <div className="feature-icon green">↗</div>
                  <h3>Revenue Opportunity</h3>
                  <p>Identify products where pricing may be limiting growth based on recent sales behavior.</p>
                </div>
                <div className="feature">
                  <div className="feature-icon orange">$</div>
                  <h3>Profit Opportunity</h3>
                  <p>Use product costs to estimate profit impact, not just top-line revenue movement.</p>
                </div>
                <div className="feature">
                  <div className="feature-icon blue">▥</div>
                  <h3>Pricing Activity</h3>
                  <p>Understand how actively your prices are being managed across qualified products.</p>
                </div>
              </div>
            </div>

            <Screen
              desktop="/image1.jpg"
              mobile="/image_m1.jpg"
              alt="Holocene dashboard interface."
            />
          </div>
        </section>

        <section className="section" id="workspace">
          <div className="container split split-reverse">
            <Screen
              desktop="/image2.jpg"
              mobile="/image_m2.jpg"
              alt="Holocene Pricing Workspace showing recommended revenue price, recommended profit price, pricing readiness, ads performance, and price history."
            />

            <div>
              <div className="section-head">
                <h2>Pricing Workspace</h2>
                <p>
                  Move from seller-level opportunity to SKU-level analysis. Review
                  recommended price candidates, expected impact, pricing readiness,
                  ads performance, and price history.
                </p>
              </div>

              <div className="feature-list">
                <div className="feature">
                  <div className="feature-icon green">◎</div>
                  <h3>Recommended Revenue Price</h3>
                  <p>Compare current price against a candidate price selected for revenue impact.</p>
                </div>
                <div className="feature">
                  <div className="feature-icon orange">$</div>
                  <h3>Recommended Profit Price</h3>
                  <p>Use COGS and fees to evaluate price decisions with profit context.</p>
                </div>
                <div className="feature">
                  <div className="feature-icon purple">⌁</div>
                  <h3>Price History</h3>
                  <p>Inspect meaningful price points and understand how products performed at different prices.</p>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section className="section" id="integrations">
          <div className="container integration-box">
            <div>
              <h2>Works with Amazon Seller Central and Amazon Ads.</h2>
              <p>
                Holocene connects to the Amazon data sources sellers already use:
                order and product data from Seller Central, plus advertising metrics
                from Amazon Ads.
              </p>
            </div>

            <div className="cards-3">
              <div className="integration-card">
                <h3>Seller Central</h3>
                <p>Orders, product sales, marketplace, SKU, and pricing history.</p>
              </div>
              <div className="integration-card">
                <h3>Amazon Ads</h3>
                <p>Advertising spend, clicks, impressions, ROAS, and TACOS context.</p>
              </div>
              <div className="integration-card">
                <h3>Pricing Analytics</h3>
                <p>Dashboard and Pricing Workspace built around product-level decisions.</p>
              </div>
            </div>
          </div>
        </section>

        <section className="section">
          <div className="container">
            <div className="section-head">
              <h2>Designed for pricing workflows, not generic reporting.</h2>
              <p>
                Holocene is built for Amazon Private Label sellers who want to understand
                whether price behavior, discounting, or incomplete cost data is hiding opportunity.
              </p>
            </div>

            <div className="cards-3">
              <div className="feature">
                <h3>Private Label focus</h3>
                <p>Built for sellers who control their own product pricing and need SKU-level decision support.</p>
              </div>
              <div className="feature">
                <h3>Evidence-aware</h3>
                <p>Pricing recommendations are shown with pricing evidence and readiness context.</p>
              </div>
              <div className="feature">
                <h3>Revenue and profit</h3>
                <p>Start with revenue opportunity, then add product costs to evaluate profit opportunity.</p>
              </div>
            </div>
          </div>
        </section>

        <section className="section">
          <div className="container faq">
            <div>
              <h2>FAQ</h2>
              <p className="lead">
                A practical pricing analytics layer for sellers using Amazon Seller Central and Amazon Ads.
              </p>
            </div>

            <div className="faq-list">
              <div className="faq-item">
                <h3>What data does Holocene use?</h3>
                <p>Holocene uses connected Seller Central and Amazon Ads data to analyze sales, pricing behavior, advertising context, and product-level opportunity.</p>
              </div>
              <div className="faq-item">
                <h3>How often is the model updated?</h3>
                <p>The MVP analyzes the last 60 days of data and is designed around a weekly refresh cadence.</p>
              </div>
              <div className="faq-item">
                <h3>Do I need product costs?</h3>
                <p>You can start with revenue opportunity without COGS. Profit opportunity becomes available after product costs and fees are added.</p>
              </div>
              <div className="faq-item">
                <h3>Does Holocene change prices automatically?</h3>
                <p>The current MVP focuses on analytics, recommendations, and pricing workspace review. Pricing automation is planned as a controlled workflow after beta.</p>
              </div>
            </div>
          </div>
        </section>

        <section className="section">
          <div className="container cta">
            <div>
              <h2>Start with a free pricing analysis.</h2>
              <p>
                Connect Amazon data, review your pricing dashboard, and open the Pricing Workspace
                to inspect product-level opportunities.
              </p>
            </div>
            <a className="btn btn-secondary" href={appUrl}>Start Free Analysis</a>
          </div>
        </section>
      </main>

      <Footer />
    </>
  );
}
''')

print("Patch v2 applied.")
