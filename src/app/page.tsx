import Image from "next/image";

const loginUrl = "https://app.holocene.ee/login";
const registerUrl = "https://app.holocene.ee/register";

function Header() {
  return (
    <header className="rev-nav">
      <div className="rev-container rev-nav-inner">
        <a className="rev-brand" href="/">
          <Image className="rev-brand-mark" src="/logo-transparent.png" alt="Holocene" width={64} height={64} priority />
          <span>Holocene</span>
        </a>

        <nav className="rev-menu">
          <a href="#product">Product</a>
          <a href="#team">AI Team</a>
          <a href="#how">How it works</a>

        </nav>

        <a className="rev-btn rev-btn-primary" href={registerUrl}>Become a Design Partner</a>
      </div>
    </header>
  );
}

function DashboardMock() {
  return (
    <div className="rev-dashboard">
      <aside className="rev-dash-sidebar">
        <div className="rev-dash-logo">
          <Image src="/logo-transparent.png" alt="Holocene" width={32} height={32} />
          <span>Holocene</span>
        </div>
        {["Overview", "Opportunities", "Pricing", "Advertising", "Listings", "Reviews", "Competitors", "Reports", "Settings"].map((item, index) => (
          <div className={index === 0 ? "rev-side-item active" : "rev-side-item"} key={item}>{item}</div>
        ))}
      </aside>

      <main className="rev-dash-main">
        <div className="rev-dash-top">
          <h3>Overview</h3>
          <span>🇺🇸 Amazon.com</span>
        </div>

        <div className="rev-metrics">
          <div className="rev-metric">
            <p>Revenue Opportunity</p>
            <strong>+$12,371</strong>
            <span>vs last 30 days</span>
          </div>
          <div className="rev-metric">
            <p>Profit Opportunity</p>
            <strong>+$3,659</strong>
            <span>vs last 30 days</span>
          </div>
        </div>

        <div className="rev-dash-grid">
          <div className="rev-table-card">
            <h4>Top Opportunities</h4>
            {[
              ["Raise price: Organic cotton t-shirt", "+$1,240 /month", "High impact"],
              ["Reduce TACOS: Auto Campaign", "+$980 /month", "High impact"],
              ["Improve listing: Main image", "+$720 /month", "Medium"],
              ["Fix negative review trend", "+$550 /month", "Medium"],
              ["Competitor price change detected", "+$340 /month", "Low"],
            ].map((row, i) => (
              <div className="rev-table-row" key={row[0]}>
                <span>{i + 1}</span>
                <p>{row[0]}</p>
                <strong>{row[1]}</strong>
                <em>{row[2]}</em>
              </div>
            ))}
          </div>

          <div className="rev-chart-card">
            <h4>Performance Trend</h4>
            <div className="rev-chart-lines">
              <svg viewBox="0 0 220 120" preserveAspectRatio="none">
                <polyline points="0,90 25,70 50,82 75,50 100,64 125,38 150,54 175,28 220,18" fill="none" stroke="#7c3aed" strokeWidth="4" />
                <polyline points="0,100 25,88 50,94 75,78 100,84 125,66 150,72 175,55 220,42" fill="none" stroke="#10b981" strokeWidth="4" />
              </svg>
            </div>
            <div className="rev-insight">
              <b>AI Insight</b>
              <p>Your pricing is 7% below the optimal range for 23 SKUs.</p>
              <a href={registerUrl}>View opportunity →</a>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

const team = [
  ["🏷️", "AI Pricing Manager", ["Finds pricing opportunities", "Recommends controlled price actions", "Tracks pricing performance"], false],
  ["📣", "AI Advertising Analyst", ["Monitors TACOS & ROAS", "Finds inefficient campaigns", "Suggests advertising optimizations"], false],
  ["📋", "AI Listing Specialist", ["Analyzes listing quality", "Detects content gaps", "Suggests improvements"], true],
  ["⭐", "AI Review Analyst", ["Detects review trends", "Identifies product issues", "Alerts on risks"], true],
  ["🏪", "AI Competitor Analyst", ["Tracks competitor moves", "Monitors pricing & stock", "Spots market changes"], true],
];

function Footer() {
  return (
    <footer className="rev-footer">
      <div className="rev-container rev-footer-inner">
        <div className="rev-brand small">
          <Image className="rev-brand-mark" src="/logo-transparent.png" alt="Holocene" width={40} height={40} />
          <span>Holocene</span>
        </div>
        <div className="rev-footer-links">
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
        <section className="rev-hero" id="product">
          <div className="rev-container rev-hero-grid">
            <div>
              <div className="rev-eyebrow">Built for Amazon Brands & Private Label Sellers</div>
              <h1>Your AI Revenue Manager for <span>Amazon Brands</span></h1>
              <p>
                While you run your business, Holocene continuously finds new opportunities
                to increase revenue and profit through pricing and advertising decisions.
              </p>

              <div className="rev-actions">
                <a className="rev-btn rev-btn-primary" href={registerUrl}>Become a Design Partner</a>
                <a className="rev-btn rev-btn-secondary" href={loginUrl}>Log in</a>
              </div>

              <div className="rev-quick">
                <div>✓ Connect your Amazon account in minutes</div>
                <div>↗ Find revenue opportunities continuously</div>
                <div>⚡ Take action and track results</div>
              </div>
            </div>

            <div className="rev-product-shot">
              <picture>
                <source media="(max-width: 720px)" srcSet="/revenue-manager-mobile.webp" />
                <img
                  src="/revenue-manager-desktop.webp"
                  alt="Holocene AI Revenue Manager dashboard overview"
                />
              </picture>
            </div>
          </div>
        </section>

        <section className="rev-section" id="team">
          <div className="rev-container">
            <h2 className="rev-center">Your AI Revenue Manager uses specialist agents</h2>

            <div className="rev-team-grid">
              {team.map(([icon, title, items, soon]) => (
                <div className="rev-team-card" key={String(title)}>
                  <div className="rev-team-icon">{icon}</div>
                  <div className="rev-team-title-row">
                    <h3>{title}</h3>
                    <span>{soon ? "In development" : "Working"}</span>
                  </div>
                  <ul>
                    {(items as string[]).map((item) => <li key={item}>✓ {item}</li>)}
                  </ul>
                </div>
              ))}
            </div>

            <div className="rev-strip">
              <span>▣ All in one place.</span>
              <span>◎ Always working.</span>
              <span>◈ Focused on your profit.</span>
            </div>
          </div>
        </section>

        <section className="rev-section" id="how">
          <div className="rev-container rev-how-grid">
            <div>
              <h2>Your AI Revenue Manager never stops working</h2>
              <div className="rev-steps">
                {[
                  ["🔗", "1. Connect", "Securely connect your Amazon account"],
                  ["🛢️", "2. Analyze", "Analyzes pricing, ads and product data"],
                  ["🔍", "3. Prioritize", "Finds the most important revenue opportunities"],
                  ["✓", "4. Recommend", "Shows clear actions with expected impact"],
                  ["📈", "5. Improve", "You take action, Holocene tracks results"],
                ].map((step) => (
                  <div className="rev-step" key={step[1]}>
                    <div>{step[0]}</div>
                    <h3>{step[1]}</h3>
                    <p>{step[2]}</p>
                  </div>
                ))}
              </div>
            </div>

            <div className="rev-partner-card">
              <div className="rev-eyebrow">Founding Design Partners</div>
              <h2>Become one of only 5 Founding Design Partners</h2>
              <p>Build the first AI Revenue Manager for Amazon together with us. We are looking for Amazon brands and agencies that want the product shaped around their real workflow.</p>
              <ul>
                <li>✓ Free access for 12 months</li>
                <li>✓ Direct access to founders</li>
                <li>✓ Weekly product updates</li>
                <li>✓ Priority support & early features</li>
              </ul>
              <a className="rev-btn rev-btn-primary" href={registerUrl}>Apply to become a Design Partner</a>
            </div>
          </div>
        </section>

        <section className="rev-container rev-final">
          <div className="rev-final-icon">▲</div>
          <div>
            <h2>Ready to build your AI Revenue Manager?</h2>
            <p>Join a small group of forward-thinking Amazon brands and agencies and help shape Holocene around real marketplace workflows.</p>
          </div>
          <a className="rev-btn rev-btn-primary" href={registerUrl}>Become a Design Partner →</a>
        </section>
      </main>

      <Footer />
    </>
  );
}
