
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

    radial-gradient(circle at 16% 0%, rgba(47, 99, 246, 0.08), transparent 34rem),

    linear-gradient(180deg, #f8fbff 0%, #f3f6fb 100%);

  color: var(--ink);

  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;

}

a { color: inherit; text-decoration: none; }

.container {

  width: min(1320px, calc(100% - 48px));

  margin: 0 auto;

}

.nav {

  position: sticky;

  top: 0;

  z-index: 20;

  background: rgba(248, 251, 255, 0.88);

  backdrop-filter: blur(18px);

  border-bottom: 1px solid rgba(219, 227, 239, 0.9);

}

.nav-inner {

  min-height: 76px;

  display: flex;

  align-items: center;

  justify-content: space-between;

  gap: 24px;

}

.brand {

  display: flex;

  align-items: center;

  gap: 11px;

}

.brand-icon {

  width: 34px;

  height: 34px;

  border: 1.8px solid var(--ink);

  border-radius: 8px;

  display: grid;

  place-items: center;

  font-size: 17px;

  font-weight: 800;

  letter-spacing: -0.08em;

  line-height: 1;

}

.brand-text strong {

  display: block;

  font-size: 17px;

  line-height: 1;

  letter-spacing: -0.04em;

}

.brand-text span {

  display: block;

  color: var(--muted);

  font-size: 11px;

  font-weight: 700;

  margin-top: 3px;

}

.nav-links {

  display: flex;

  align-items: center;

  gap: 28px;

  color: var(--muted);

  font-size: 14px;

  font-weight: 700;

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

  font-weight: 850;

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

  padding: 74px 0 70px;

}

.hero-grid {

  display: grid;

  grid-template-columns: 0.62fr 1.38fr;

  gap: 38px;

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

  font-size: clamp(40px, 5.4vw, 68px);

  line-height: 0.96;

  letter-spacing: -0.065em;

  margin: 22px 0;

}

h2 {

  font-size: clamp(34px, 4.7vw, 54px);

  line-height: 1;

  letter-spacing: -0.058em;

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

  max-width: 650px;

}

.hero-actions {

  display: flex;

  gap: 12px;

  flex-wrap: wrap;

  margin-top: 30px;

}

.micro-links {

  margin-top: 24px;

  display: flex;

  flex-wrap: wrap;

  gap: 16px;

  color: var(--muted);

  font-size: 13px;

  font-weight: 700;

}

.micro-links a {

  border-bottom: 1px solid rgba(102,116,139,.45);

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

.hero-screen {

  transform: scale(1.04);

  transform-origin: center;

}

.mobile-shot { display: none !important; }

.section {

  padding: 76px 0;

}

.section-head {

  max-width: 780px;

  margin-bottom: 28px;

}

.section-head p {

  color: var(--muted);

  font-size: 18px;

  line-height: 1.6;

}

.workspace-grid {

  display: grid;

  grid-template-columns: 1.35fr 0.65fr;

  gap: 34px;

  align-items: center;

}

.workspace-copy {

  max-width: 460px;

}

.compact-list {

  display: grid;

  gap: 12px;

  margin-top: 24px;

}

.compact-item {

  display: grid;

  grid-template-columns: 42px 1fr;

  gap: 14px;

  align-items: start;

}

.compact-icon {

  width: 42px;

  height: 42px;

  border-radius: 14px;

  display: grid;

  place-items: center;

  font-weight: 900;

}

.compact-item p {

  margin: 0;

  color: var(--muted);

  line-height: 1.5;

}

.green { background: #dcfce7; color: var(--green); }

.orange { background: #ffedd5; color: var(--orange); }

.blue { background: #dbeafe; color: var(--blue); }

.purple { background: #ede9fe; color: #7c3aed; }

.workflow {

  background: var(--navy);

  color: white;

  border-radius: 34px;

  padding: 38px;

}

.workflow p {

  color: #bac6d8;

  line-height: 1.6;

}

.steps {

  display: grid;

  grid-template-columns: repeat(3, 1fr);

  gap: 18px;

  margin-top: 28px;

}

.step {

  background: rgba(255,255,255,0.08);

  border: 1px solid rgba(255,255,255,0.14);

  border-radius: 24px;

  padding: 24px;

}

.step-num {

  width: 36px;

  height: 36px;

  border-radius: 999px;

  background: white;

  color: var(--navy);

  display: grid;

  place-items: center;

  font-weight: 900;

  margin-bottom: 18px;

}

.cards-3 {

  display: grid;

  grid-template-columns: repeat(3, 1fr);

  gap: 18px;

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

@media (max-width: 980px) {

  .container {

    width: min(100% - 32px, 720px);

  }

  .nav-inner {

    min-height: auto;

    padding: 14px 0;

  }

  .brand-text span {

    display: none;

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

  .workspace-grid,

  .faq,

  .cta {

    grid-template-columns: 1fr;

  }

  .steps,

  .cards-3 {

    grid-template-columns: 1fr;

  }

  .lead {

    font-size: 18px;

  }

  .hero-screen {

    transform: none;

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

  .workflow,

  .cta {

    padding: 28px;

  }

}

''')

(app / "page.tsx").write_text(r'''import Image from "next/image";

const loginUrl = "https://app.holocene.ee/login";

const registerUrl = "https://app.holocene.ee/register";

function Brand() {

  return (

    <a className="brand" href="/" aria-label="Holocene home">

      <span className="brand-icon">HS</span>

      <span className="brand-text">

        <strong>Holocene</strong>

        <span>AI Pricing Co-Pilot</span>

      </span>

    </a>

  );

}

function Header() {

  return (

    <header className="nav">

      <div className="container nav-inner">

        <Brand />

        <nav className="nav-links">

          <a href="#how">How it works</a>

          <a href="#algorithm">ML algorithm</a>

          <a href="/pricing">Pricing</a>

        </nav>

        <div className="actions">

          <a className="btn btn-secondary" href={loginUrl}>Login</a>

          <a className="btn btn-primary" href={registerUrl}>Start Free Analysis</a>

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

  hero = false,

}: {

  desktop: string;

  mobile: string;

  alt: string;

  priority?: boolean;

  hero?: boolean;

}) {

  return (

    <div className={`screen-frame ${hero ? "hero-screen" : ""}`}>

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

        <Brand />

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

                <a className="btn btn-primary" href={registerUrl}>Start Free Analysis</a>

                <a className="btn btn-secondary" href={loginUrl}>Login</a>

              </div>

              <div className="micro-links">

                <a href="#how">Seller Central + Amazon Ads workflow</a>

                <a href="#algorithm">ML pricing algorithm</a>

              </div>

            </div>

            <Screen

              desktop="/image1.jpg"

              mobile="/image_m1.jpg"

              alt="Holocene Pricing Dashboard showing revenue opportunity, profit opportunity, pricing activity, and qualified products."

              priority

              hero

            />

          </div>

        </section>

        <section className="section" id="workspace">

          <div className="container workspace-grid">

            <Screen

              desktop="/image2.jpg"

              mobile="/image_m2.jpg"

              alt="Holocene Pricing Workspace showing recommended revenue price, recommended profit price, pricing readiness, ads performance, and price history."

            />

            <div className="workspace-copy">

              <div className="section-head">

                <h2>Pricing Workspace</h2>

                <p>

                  Move from seller-level opportunity to SKU-level analysis. Review

                  recommended price candidates, expected impact, pricing readiness,

                  ads performance, and price history.

                </p>

              </div>

              <div className="compact-list">

                <div className="compact-item">

                  <div className="compact-icon green">◎</div>

                  <div>

                    <h3>Recommended prices</h3>

                    <p>Compare current price against revenue and profit candidates.</p>

                  </div>

                </div>

                <div className="compact-item">

                  <div className="compact-icon orange">$</div>

                  <div>

                    <h3>Expected impact</h3>

                    <p>Estimate revenue or profit movement before changing anything in Amazon.</p>

                  </div>

                </div>

                <div className="compact-item">

                  <div className="compact-icon purple">⌁</div>

                  <div>

                    <h3>Price history</h3>

                    <p>Inspect meaningful price points and product performance over time.</p>

                  </div>

                </div>

              </div>

            </div>

          </div>

        </section>

        <section className="section" id="how">

          <div className="container workflow">

            <div className="section-head">

              <h2>How Holocene works</h2>

              <p>

                Connect Amazon data, let the pricing analytics model evaluate recent sales behavior,

                then use Pricing Workspace to review product-level recommendations.

              </p>

            </div>

            <div className="steps">

              <div className="step">

                <div className="step-num">1</div>

                <h3>Connect Amazon data</h3>

                <p>Connect Seller Central and Amazon Ads so Holocene can read product, order, pricing, and advertising data.</p>

              </div>

              <div className="step">

                <div className="step-num">2</div>

                <h3>Analyze pricing behavior</h3>

                <p>The model reviews the last 60 days, pricing activity, pricing evidence, revenue opportunity, and cost completeness.</p>

              </div>

              <div className="step">

                <div className="step-num">3</div>

                <h3>Use the pricing co-pilot</h3>

                <p>Open Pricing Workspace to inspect recommended prices, expected impact, ads context, and price history.</p>

              </div>

            </div>

          </div>

        </section>

        <section className="section" id="algorithm">

          <div className="container">

            <div className="section-head">

              <h2>ML pricing algorithm with evidence checks.</h2>

              <p>

                Holocene does not treat every SKU the same. The system evaluates whether a product

                has enough pricing history, order volume, price range, and meaningful price points

                before showing modeled recommendations.

              </p>

            </div>

            <div className="cards-3">

              <div className="feature">

                <h3>Pricing evidence</h3>

                <p>Recommendations are supported by an evidence score based on history, sales volume, price points, and price range.</p>

              </div>

              <div className="feature">

                <h3>Revenue and profit candidates</h3>

                <p>The workspace separates revenue opportunity from profit opportunity after costs and fees are available.</p>

              </div>

              <div className="feature">

                <h3>Controlled optimization</h3>

                <p>The MVP focuses on analytics and review. Pricing automation is planned as a controlled workflow after beta.</p>

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

                <p>The current MVP focuses on analytics, recommendations, and Pricing Workspace review. Pricing automation is planned as a controlled workflow after beta.</p>

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

            <a className="btn btn-secondary" href={registerUrl}>Start Free Analysis</a>

          </div>

        </section>

      </main>

      <Footer />

    </>

  );

}

''')

print("Patch v3 applied.")

