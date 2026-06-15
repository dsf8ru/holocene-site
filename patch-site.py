from pathlib import Path

root = Path(".")
app = root / "src" / "app"

(app / "pricing").mkdir(parents=True, exist_ok=True)
(app / "privacy").mkdir(parents=True, exist_ok=True)
(app / "terms").mkdir(parents=True, exist_ok=True)
(app / "support").mkdir(parents=True, exist_ok=True)

(app / "layout.tsx").write_text(r'''import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Holocene — Amazon Pricing Analytics",
  description:
    "Amazon pricing analytics for Private Label sellers. Find revenue and profit opportunity based on Seller Central and Amazon Ads data.",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
''')

(app / "globals.css").write_text(r'''@import "tailwindcss";

:root {
  --bg: #f5f1e8;
  --card: #fffaf1;
  --ink: #15130f;
  --muted: #6f675a;
  --line: #dfd5c3;
  --dark: #11100d;
  --green: #2d6a4f;
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  background:
    radial-gradient(circle at top left, rgba(45, 106, 79, 0.08), transparent 32rem),
    var(--bg);
  color: var(--ink);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

a {
  color: inherit;
  text-decoration: none;
}

.container {
  width: min(1160px, calc(100% - 32px));
  margin: 0 auto;
}

.nav {
  position: sticky;
  top: 0;
  z-index: 20;
  backdrop-filter: blur(18px);
  background: rgba(245, 241, 232, 0.82);
  border-bottom: 1px solid rgba(223, 213, 195, 0.75);
}

.nav-inner {
  height: 76px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 800;
  letter-spacing: -0.04em;
}

.logo-mark {
  width: 34px;
  height: 34px;
  border-radius: 10px;
  background: var(--dark);
  color: #f7efe0;
  display: grid;
  place-items: center;
  font-size: 13px;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 22px;
  color: var(--muted);
  font-size: 14px;
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
  min-height: 42px;
  padding: 0 18px;
  border-radius: 999px;
  font-weight: 700;
  font-size: 14px;
  border: 1px solid var(--line);
}

.btn-dark {
  background: var(--dark);
  color: #fff7e9;
  border-color: var(--dark);
}

.btn-light {
  background: rgba(255, 250, 241, 0.72);
}

.hero {
  padding: 78px 0 48px;
}

.hero-grid {
  display: grid;
  grid-template-columns: 1fr 0.92fr;
  gap: 42px;
  align-items: center;
}

.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(45, 106, 79, 0.1);
  color: var(--green);
  border: 1px solid rgba(45, 106, 79, 0.18);
  border-radius: 999px;
  padding: 8px 12px;
  font-size: 13px;
  font-weight: 800;
}

h1 {
  font-size: clamp(44px, 7vw, 82px);
  line-height: 0.93;
  letter-spacing: -0.075em;
  margin: 22px 0 22px;
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
  margin-top: 30px;
  flex-wrap: wrap;
}

.metrics {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
  margin-top: 42px;
}

.metric {
  background: rgba(255, 250, 241, 0.7);
  border: 1px solid var(--line);
  border-radius: 22px;
  padding: 18px;
}

.metric strong {
  display: block;
  font-size: 24px;
  letter-spacing: -0.04em;
}

.metric span {
  color: var(--muted);
  font-size: 13px;
}

.product-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 32px;
  padding: 18px;
  box-shadow: 0 30px 80px rgba(40, 32, 18, 0.1);
}

.mock {
  background: #fbf7ee;
  border: 1px solid var(--line);
  border-radius: 24px;
  overflow: hidden;
}

.mock-top {
  height: 58px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 18px;
  border-bottom: 1px solid var(--line);
}

.pill {
  background: #eee5d5;
  color: var(--muted);
  border-radius: 999px;
  padding: 8px 12px;
  font-size: 12px;
  font-weight: 800;
}

.mock-body {
  padding: 18px;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.dash-card {
  min-height: 118px;
  border-radius: 18px;
  background: white;
  border: 1px solid #eadfcb;
  padding: 16px;
}

.dash-card small {
  color: var(--muted);
  font-weight: 700;
}

.dash-card b {
  display: block;
  margin-top: 14px;
  font-size: 26px;
  letter-spacing: -0.05em;
}

.section {
  padding: 64px 0;
}

.section-head {
  max-width: 740px;
  margin-bottom: 28px;
}

h2 {
  font-size: clamp(34px, 5vw, 56px);
  line-height: 1;
  letter-spacing: -0.065em;
  margin: 0 0 16px;
}

.section-head p {
  color: var(--muted);
  font-size: 18px;
  line-height: 1.55;
}

.cards-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.feature {
  background: rgba(255, 250, 241, 0.72);
  border: 1px solid var(--line);
  border-radius: 26px;
  padding: 24px;
}

.feature h3 {
  margin: 0 0 10px;
  letter-spacing: -0.035em;
}

.feature p {
  color: var(--muted);
  line-height: 1.55;
  margin: 0;
}

.workspace {
  display: grid;
  grid-template-columns: 0.82fr 1fr;
  gap: 18px;
  align-items: stretch;
}

.sidebar {
  background: #14130f;
  color: #fff5e4;
  border-radius: 28px;
  padding: 26px;
}

.sidebar p {
  color: #c9bfae;
  line-height: 1.55;
}

.list {
  display: grid;
  gap: 12px;
  margin-top: 24px;
}

.list div {
  background: rgba(255,255,255,0.08);
  border-radius: 16px;
  padding: 14px;
  font-weight: 700;
}

.chart {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 28px;
  padding: 24px;
  min-height: 360px;
}

.bars {
  height: 260px;
  display: flex;
  align-items: end;
  gap: 12px;
  margin-top: 26px;
}

.bar {
  flex: 1;
  border-radius: 12px 12px 0 0;
  background: linear-gradient(180deg, #2d6a4f, #9bbf9e);
}

.pricing-box {
  background: #14130f;
  color: #fff5e4;
  border-radius: 34px;
  padding: 34px;
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 24px;
  align-items: center;
}

.pricing-box p {
  color: #cfc5b4;
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
}

.footer-links {
  display: flex;
  gap: 18px;
}

.simple-page {
  padding: 72px 0;
  max-width: 860px;
}

.simple-page h1 {
  font-size: clamp(42px, 6vw, 64px);
}

.simple-page p,
.simple-page li {
  color: var(--muted);
  line-height: 1.7;
}

@media (max-width: 860px) {
  .nav-inner {
    height: auto;
    padding: 16px 0;
    align-items: flex-start;
  }

  .nav-links {
    display: none;
  }

  .actions .btn-light {
    display: none;
  }

  .hero {
    padding-top: 46px;
  }

  .hero-grid,
  .workspace,
  .pricing-box {
    grid-template-columns: 1fr;
  }

  .metrics,
  .cards-3 {
    grid-template-columns: 1fr;
  }

  .dashboard-grid {
    grid-template-columns: 1fr;
  }

  .lead {
    font-size: 18px;
  }

  .product-card {
    border-radius: 24px;
    padding: 12px;
  }

  .mock-body {
    padding: 12px;
  }

  .pricing-box {
    padding: 26px;
  }
}
''')

(app / "page.tsx").write_text(r'''const appUrl = "https://app.holocene.ee/login";

function Header() {
  return (
    <header className="nav">
      <div className="container nav-inner">
        <a className="logo" href="/">
          <span className="logo-mark">HS</span>
          <span>Holocene</span>
        </a>

        <nav className="nav-links">
          <a href="#dashboard">Dashboard</a>
          <a href="#workspace">Pricing Workspace</a>
          <a href="#how">How it works</a>
          <a href="/pricing">Pricing</a>
        </nav>

        <div className="actions">
          <a className="btn btn-light" href={appUrl}>Login</a>
          <a className="btn btn-dark" href={appUrl}>Start Free Analysis</a>
        </div>
      </div>
    </header>
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
              <h1>Find the revenue hidden in your pricing behavior.</h1>
              <p className="lead">
                Holocene analyzes your last 60 days of Seller Central and Amazon Ads data
                to show pricing activity, pricing evidence, revenue opportunity, and
                profit opportunity by product.
              </p>

              <div className="hero-actions">
                <a className="btn btn-dark" href={appUrl}>Start Free Analysis</a>
                <a className="btn btn-light" href="#dashboard">See how it works</a>
              </div>

              <div className="metrics">
                <div className="metric">
                  <strong>60 days</strong>
                  <span>sales data model</span>
                </div>
                <div className="metric">
                  <strong>7 days</strong>
                  <span>refresh cadence</span>
                </div>
                <div className="metric">
                  <strong>SKU-level</strong>
                  <span>pricing workspace</span>
                </div>
              </div>
            </div>

            <div className="product-card" id="dashboard">
              <div className="mock">
                <div className="mock-top">
                  <b>Pricing Dashboard</b>
                  <span className="pill">Amazon DE · Last 60 days</span>
                </div>
                <div className="mock-body">
                  <div className="dashboard-grid">
                    <div className="dash-card">
                      <small>Pricing Activity</small>
                      <b>Medium</b>
                    </div>
                    <div className="dash-card">
                      <small>Pricing Evidence</small>
                      <b>78 / 100</b>
                    </div>
                    <div className="dash-card">
                      <small>Revenue Opportunity</small>
                      <b>€18,420</b>
                    </div>
                    <div className="dash-card">
                      <small>Profit Opportunity</small>
                      <b>Add COGS</b>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section className="section">
          <div className="container">
            <div className="section-head">
              <h2>See where pricing is helping, hurting, or hiding growth.</h2>
              <p>
                The dashboard turns raw order, price, discount, and ads data into a simple
                seller-level view of pricing behavior and opportunity.
              </p>
            </div>

            <div className="cards-3">
              <div className="feature">
                <h3>Pricing Activity</h3>
                <p>Understand whether products are actively priced or sitting at one price while discounts do the work.</p>
              </div>
              <div className="feature">
                <h3>Revenue Opportunity</h3>
                <p>Prioritize products where better pricing could unlock additional revenue over the selected period.</p>
              </div>
              <div className="feature">
                <h3>Profit Opportunity</h3>
                <p>Add COGS and fees to move from revenue-only analysis to profit-aware price decisions.</p>
              </div>
            </div>
          </div>
        </section>

        <section className="section" id="workspace">
          <div className="container workspace">
            <div className="sidebar">
              <span className="eyebrow">Pricing Workspace</span>
              <h2>Go from dashboard signal to SKU-level action.</h2>
              <p>
                Open a product to review sales dynamics, price points, elasticity, and
                modeled price candidates before changing anything in Amazon.
              </p>
              <div className="list">
                <div>Sales Dynamics</div>
                <div>Demand Elasticity</div>
                <div>Price Insights</div>
                <div>Modeled Opportunity</div>
              </div>
            </div>

            <div className="chart">
              <b>Demand Elasticity</b>
              <p className="lead">Price vs units sold, filtered to meaningful price points.</p>
              <div className="bars" aria-hidden="true">
                <div className="bar" style={{ height: "45%" }} />
                <div className="bar" style={{ height: "72%" }} />
                <div className="bar" style={{ height: "64%" }} />
                <div className="bar" style={{ height: "88%" }} />
                <div className="bar" style={{ height: "58%" }} />
                <div className="bar" style={{ height: "76%" }} />
                <div className="bar" style={{ height: "52%" }} />
              </div>
            </div>
          </div>
        </section>

        <section className="section" id="how">
          <div className="container">
            <div className="section-head">
              <h2>Connect, analyze, prioritize, optimize.</h2>
              <p>
                Holocene is designed for sellers who want a practical pricing workflow,
                not another generic reporting dashboard.
              </p>
            </div>

            <div className="cards-3">
              <div className="feature">
                <h3>1. Connect Amazon</h3>
                <p>Connect Seller Central and Amazon Ads so Holocene can read order, price, and advertising data.</p>
              </div>
              <div className="feature">
                <h3>2. Review opportunity</h3>
                <p>Use the dashboard to see qualified products and where price behavior creates opportunity.</p>
              </div>
              <div className="feature">
                <h3>3. Work by SKU</h3>
                <p>Use Pricing Workspace to inspect evidence, price points, and recommended next actions.</p>
              </div>
            </div>
          </div>
        </section>

        <section className="section">
          <div className="container pricing-box">
            <div>
              <h2>Free during beta.</h2>
              <p>
                Start with a free pricing analysis while Holocene is in MVP beta.
                Built for Amazon Private Label sellers with enough sales history to model pricing behavior.
              </p>
            </div>
            <a className="btn btn-light" href={appUrl}>Start Free Analysis</a>
          </div>
        </section>
      </main>

      <Footer />
    </>
  );
}
''')

simple = {
"pricing/page.tsx": ("Pricing", "Holocene is currently free during MVP beta. Paid plans will be introduced after the beta period."),
"privacy/page.tsx": ("Privacy Policy", "Holocene uses connected Amazon data only to provide pricing analytics, dashboard reporting, and product-level pricing insights."),
"terms/page.tsx": ("Terms of Service", "By using Holocene, you agree to use the service for lawful business analytics purposes and to maintain access only to accounts you are authorized to connect."),
"support/page.tsx": ("Support", "For support, contact the Holocene team at support@holocene.ee."),
}

for file, (title, body) in simple.items():
    (app / file).write_text(f'''import Link from "next/link";

export default function Page() {{
  return (
    <main className="container simple-page">
      <Link className="btn btn-light" href="/">← Back</Link>
      <h1>{title}</h1>
      <p>{body}</p>
    </main>
  );
}}
''')

print("Holocene site patch applied.")
