from pathlib import Path

Path("src/app/page.tsx").write_text(r'''import Image from "next/image";

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
          <a href="/algorithm">About us</a>
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
  ["🏷️", "AI Pricing Manager", ["Finds pricing opportunities", "Runs price tests", "Tracks price performance"], false],
  ["📣", "AI Advertising Analyst", ["Monitors TACOS & ROAS", "Finds inefficient campaigns", "Suggests optimizations"], false],
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
              <div className="rev-eyebrow">AI Revenue Manager for Amazon Brands</div>
              <h1>Your AI Revenue Manager for <span>Amazon Brands</span></h1>
              <p>
                An AI team of specialists that continuously monitors your business,
                finds revenue opportunities, and recommends actions to grow your profit.
              </p>

              <div className="rev-actions">
                <a className="rev-btn rev-btn-primary" href={registerUrl}>Become a Design Partner</a>
                <a className="rev-btn rev-btn-secondary" href={loginUrl}>See Live Demo</a>
              </div>

              <div className="rev-quick">
                <div>✓ Connect your Amazon account in minutes</div>
                <div>↗ Get opportunities 24/7</div>
                <div>⚡ Take action and see results</div>
              </div>
            </div>

            <DashboardMock />
          </div>
        </section>

        <section className="rev-section" id="team">
          <div className="rev-container">
            <h2 className="rev-center">Your AI team of specialists</h2>

            <div className="rev-team-grid">
              {team.map(([icon, title, items, soon]) => (
                <div className="rev-team-card" key={String(title)}>
                  <div className="rev-team-icon">{icon}</div>
                  <div className="rev-team-title-row">
                    <h3>{title}</h3>
                    {soon ? <span>Coming soon</span> : null}
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
              <h2>How Holocene works</h2>
              <div className="rev-steps">
                {[
                  ["🔗", "1. Connect", "Securely connect your Amazon account"],
                  ["🛢️", "2. Analyze", "Analyzes millions of data points 24/7"],
                  ["🔍", "3. Find", "Finds revenue opportunities"],
                  ["✓", "4. Recommend", "Recommends clear actions"],
                  ["📈", "5. Improve", "You take action and see measurable results"],
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
              <h2>Help shape the future of AI for Amazon</h2>
              <p>We are looking for 5 Amazon brands and agencies to join as Founding Design Partners.</p>
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

        <section className="rev-section">
          <div className="rev-container">
            <h2 className="rev-center">What Amazon professionals say</h2>
            <div className="rev-testimonials">
              {[
                ["Holocene found pricing opportunities we completely missed. It is like having another analyst on the team.", "Mike D.", "Amazon Brand Owner"],
                ["It saves us hours every week. The recommendations are spot on and easy to act on.", "Sarah K.", "Amazon Agency Owner"],
                ["Finally a tool that looks at the whole business, not just ads or pricing.", "James L.", "E-commerce Director"],
              ].map((t) => (
                <div className="rev-quote" key={t[1]}>
                  <b>“</b>
                  <p>{t[0]}</p>
                  <strong>{t[1]}</strong>
                  <span>{t[2]}</span>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className="rev-container rev-final">
          <div className="rev-final-icon">▲</div>
          <div>
            <h2>Ready to build your AI Revenue Team?</h2>
            <p>Join a small group of forward-thinking Amazon brands and agencies and help shape Holocene.</p>
          </div>
          <a className="rev-btn rev-btn-primary" href={registerUrl}>Become a Design Partner →</a>
        </section>
      </main>

      <Footer />
    </>
  );
}
''')

Path("src/app/globals.css").write_text(r'''@import "tailwindcss";

:root {
  --bg: #fbfbff;
  --ink: #0b1023;
  --muted: #5f6b83;
  --line: #e3e7f0;
  --purple: #6d28d9;
  --purple2: #8b5cf6;
  --green: #11a36a;
  --blue: #2563eb;
  --navy: #050b1d;
}

* { box-sizing: border-box; }

html {
  scroll-behavior: smooth;
  scroll-padding-top: 90px;
}

body {
  margin: 0;
  background:
    radial-gradient(circle at 15% 0%, rgba(124, 58, 237, 0.08), transparent 34rem),
    radial-gradient(circle at 85% 10%, rgba(37, 99, 235, 0.06), transparent 32rem),
    var(--bg);
  color: var(--ink);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

a { color: inherit; text-decoration: none; }

.rev-container {
  width: min(1180px, calc(100% - 48px));
  margin: 0 auto;
}

.rev-nav {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(255,255,255,.82);
  backdrop-filter: blur(18px);
  border-bottom: 1px solid rgba(227,231,240,.85);
}

.rev-nav-inner {
  height: 76px;
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 28px;
}

.rev-brand {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  font-size: 23px;
  font-weight: 750;
  letter-spacing: -0.04em;
}

.rev-brand.small {
  font-size: 16px;
}

.rev-brand-mark {
  width: 34px;
  height: 34px;
  object-fit: contain;
}

.rev-menu {
  display: flex;
  gap: 34px;
  font-size: 14px;
  font-weight: 650;
}

.rev-nav .rev-btn {
  justify-self: end;
}

.rev-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 46px;
  padding: 0 22px;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 720;
  border: 1px solid var(--line);
  white-space: nowrap;
}

.rev-btn-primary {
  color: white;
  border-color: transparent;
  background: linear-gradient(135deg, var(--purple), var(--purple2));
  box-shadow: 0 14px 34px rgba(109, 40, 217, .24);
}

.rev-btn-secondary {
  background: white;
  color: var(--ink);
}

.rev-hero {
  padding: 56px 0 52px;
  border-bottom: 1px solid var(--line);
}

.rev-hero-grid {
  display: grid;
  grid-template-columns: .88fr 1.12fr;
  gap: 52px;
  align-items: center;
}

.rev-eyebrow {
  display: inline-flex;
  align-items: center;
  border: 1px solid rgba(109,40,217,.18);
  background: rgba(109,40,217,.05);
  color: var(--purple);
  border-radius: 999px;
  padding: 8px 13px;
  font-size: 12px;
  font-weight: 760;
  text-transform: uppercase;
  letter-spacing: .06em;
}

.rev-hero h1 {
  font-size: clamp(44px, 5vw, 70px);
  line-height: .98;
  letter-spacing: -0.065em;
  margin: 24px 0 22px;
}

.rev-hero h1 span {
  color: var(--purple);
}

.rev-hero p {
  max-width: 560px;
  color: #111827;
  font-size: 19px;
  line-height: 1.65;
}

.rev-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  margin-top: 30px;
}

.rev-quick {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  margin-top: 30px;
  color: #111827;
  font-size: 13px;
}

.rev-quick div {
  display: flex;
  align-items: center;
  gap: 8px;
}

.rev-dashboard {
  display: grid;
  grid-template-columns: 140px 1fr;
  min-height: 510px;
  background: white;
  border: 1px solid var(--line);
  border-radius: 18px;
  box-shadow: 0 34px 80px rgba(15, 23, 42, .1);
  overflow: hidden;
}

.rev-dash-sidebar {
  border-right: 1px solid var(--line);
  padding: 22px 14px;
}

.rev-dash-logo {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 760;
  margin-bottom: 28px;
}

.rev-side-item {
  padding: 10px 12px;
  border-radius: 9px;
  color: var(--muted);
  font-size: 13px;
  margin-bottom: 5px;
}

.rev-side-item.active {
  color: var(--purple);
  background: rgba(109,40,217,.08);
}

.rev-dash-main {
  padding: 28px;
}

.rev-dash-top,
.rev-metrics,
.rev-dash-grid {
  display: grid;
  gap: 16px;
}

.rev-dash-top {
  grid-template-columns: 1fr auto;
  align-items: center;
  margin-bottom: 18px;
}

.rev-dash-top h3 {
  margin: 0;
  font-size: 24px;
}

.rev-dash-top span {
  border: 1px solid var(--line);
  border-radius: 9px;
  padding: 10px 12px;
  font-size: 13px;
}

.rev-metrics {
  grid-template-columns: repeat(2, 1fr);
  margin-bottom: 16px;
}

.rev-metric,
.rev-table-card,
.rev-chart-card {
  border: 1px solid var(--line);
  border-radius: 14px;
  background: white;
}

.rev-metric {
  padding: 18px;
}

.rev-metric p {
  margin: 0 0 8px;
  font-size: 13px;
  font-weight: 700;
}

.rev-metric strong {
  display: block;
  color: var(--green);
  font-size: 28px;
  letter-spacing: -.04em;
}

.rev-metric span {
  color: var(--muted);
  font-size: 12px;
}

.rev-dash-grid {
  grid-template-columns: 1.3fr .85fr;
}

.rev-table-card,
.rev-chart-card {
  padding: 18px;
}

.rev-table-card h4,
.rev-chart-card h4 {
  margin: 0 0 14px;
}

.rev-table-row {
  display: grid;
  grid-template-columns: 20px 1fr auto auto;
  gap: 9px;
  align-items: center;
  font-size: 11px;
  padding: 8px 0;
  border-bottom: 1px solid #f1f3f8;
}

.rev-table-row p {
  margin: 0;
}

.rev-table-row strong {
  color: var(--green);
}

.rev-table-row em {
  font-style: normal;
  color: #a16207;
  background: #fef3c7;
  border-radius: 99px;
  padding: 3px 6px;
}

.rev-chart-lines {
  height: 140px;
}

.rev-chart-lines svg {
  width: 100%;
  height: 100%;
}

.rev-insight {
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 14px;
}

.rev-insight p {
  margin: 7px 0;
  color: var(--muted);
  font-size: 12px;
}

.rev-insight a {
  color: var(--purple);
  font-weight: 750;
  font-size: 12px;
}

.rev-section {
  padding: 54px 0;
}

.rev-center {
  text-align: center;
  font-size: clamp(28px, 3vw, 36px);
  letter-spacing: -.045em;
  margin: 0 0 28px;
}

.rev-team-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 16px;
}

.rev-team-card {
  background: white;
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 20px;
  min-height: 215px;
}

.rev-team-icon {
  width: 48px;
  height: 48px;
  display: grid;
  place-items: center;
  border-radius: 16px;
  background: #f3e8ff;
  font-size: 26px;
  margin-bottom: 14px;
}

.rev-team-title-row {
  min-height: 54px;
}

.rev-team-title-row h3 {
  margin: 0;
  font-size: 16px;
}

.rev-team-title-row span {
  display: inline-block;
  margin-top: 6px;
  padding: 5px 9px;
  border-radius: 999px;
  background: #fff7ed;
  color: #7c2d12;
  font-size: 11px;
}

.rev-team-card ul,
.rev-partner-card ul {
  list-style: none;
  padding: 0;
  margin: 12px 0 0;
  color: var(--muted);
  font-size: 13px;
  line-height: 1.9;
}

.rev-strip {
  margin: 24px auto 0;
  width: min(680px, 100%);
  display: flex;
  justify-content: center;
  gap: 30px;
  padding: 14px 20px;
  border-radius: 12px;
  background: rgba(109,40,217,.05);
  color: #111827;
  font-size: 14px;
  font-weight: 650;
}

.rev-how-grid {
  display: grid;
  grid-template-columns: 1.45fr .8fr;
  gap: 48px;
  align-items: center;
}

.rev-how-grid h2 {
  font-size: 34px;
  letter-spacing: -.04em;
}

.rev-steps {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 16px;
  margin-top: 28px;
}

.rev-step {
  text-align: center;
}

.rev-step div {
  margin: 0 auto 14px;
  width: 62px;
  height: 62px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: #f3e8ff;
  font-size: 25px;
}

.rev-step h3 {
  font-size: 14px;
  margin: 0 0 8px;
}

.rev-step p {
  margin: 0;
  color: #111827;
  font-size: 13px;
  line-height: 1.55;
}

.rev-partner-card {
  background: linear-gradient(135deg, rgba(139,92,246,.14), rgba(255,255,255,.88));
  border: 1px solid rgba(109,40,217,.16);
  border-radius: 18px;
  padding: 30px;
}

.rev-partner-card h2 {
  margin: 18px 0 12px;
  font-size: 30px;
}

.rev-partner-card p {
  color: #111827;
  line-height: 1.6;
}

.rev-testimonials {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.rev-quote {
  background: white;
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 26px;
}

.rev-quote b {
  color: var(--purple);
  font-size: 34px;
}

.rev-quote p {
  color: #111827;
  line-height: 1.6;
}

.rev-quote strong,
.rev-quote span {
  display: block;
}

.rev-quote span {
  color: var(--muted);
  margin-top: 4px;
}

.rev-final {
  margin-bottom: 42px;
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 28px;
  align-items: center;
  background: var(--navy);
  color: white;
  border-radius: 20px;
  padding: 34px 46px;
}

.rev-final-icon {
  width: 92px;
  height: 92px;
  display: grid;
  place-items: center;
  border-radius: 22px;
  background: linear-gradient(135deg, #312e81, #7c3aed);
  font-size: 38px;
}

.rev-final h2 {
  margin: 0 0 10px;
  font-size: 30px;
}

.rev-final p {
  color: #cbd5e1;
  margin: 0;
}

.rev-footer {
  border-top: 1px solid var(--line);
  padding: 22px 0;
}

.rev-footer-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.rev-footer-links {
  display: flex;
  gap: 20px;
  color: var(--muted);
}

.cookie-banner,
.cookie-panel {
  position: fixed;
  left: 50%;
  bottom: 34px;
  z-index: 80;
  width: min(720px, calc(100% - 32px));
  transform: translateX(-50%);
  background: white;
  border: 1px solid var(--line);
  box-shadow: 0 30px 80px rgba(8, 15, 36, 0.18);
}

.cookie-banner { padding: 30px 38px; }

.cookie-banner h2,
.cookie-panel h2 {
  margin: 0 0 14px;
  font-size: 26px;
  letter-spacing: -0.03em;
}

.cookie-banner p,
.cookie-panel p {
  margin: 0;
  color: var(--muted);
  font-size: 18px;
  line-height: 1.5;
}

.cookie-actions {
  display: flex;
  align-items: center;
  gap: 28px;
  margin-top: 28px;
}

.cookie-accept,
.cookie-confirm {
  border: 0;
  background: #000;
  color: white;
  font-weight: 850;
  font-size: 16px;
  padding: 16px 28px;
  cursor: pointer;
}

.cookie-settings,
.cookie-back {
  border: 0;
  background: transparent;
  color: #000;
  font-weight: 850;
  font-size: 16px;
  cursor: pointer;
}

.cookie-panel {
  padding: 28px;
  max-width: 440px;
}

.cookie-back {
  color: var(--muted);
  margin-bottom: 26px;
  padding: 0;
}

.cookie-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  border-top: 1px solid var(--line);
  padding: 18px 0;
  color: #111827;
}

.cookie-row:last-of-type { border-bottom: 1px solid var(--line); }

.cookie-required {
  color: var(--blue);
  font-size: 12px;
  white-space: nowrap;
}

.cookie-row input {
  width: 46px;
  height: 26px;
  accent-color: var(--navy);
}

.cookie-confirm {
  margin-top: 24px;
  padding: 13px 20px;
  font-size: 14px;
}

.legal-page,
.algorithm-hero {
  max-width: 980px;
  padding: 70px 0;
}

.legal-page h1,
.algorithm-hero h1 {
  font-size: clamp(42px, 6vw, 68px);
  line-height: 1;
  letter-spacing: -.06em;
}

.content-paper {
  background: white;
  border: 1px solid var(--line);
  border-radius: 24px;
  padding: 38px;
  margin-top: 24px;
}

.content-paper h2 {
  margin-top: 34px;
  font-size: 30px;
  letter-spacing: -.04em;
}

.content-paper h2:first-child { margin-top: 0; }

.content-paper p,
.content-paper li {
  color: var(--muted);
  line-height: 1.8;
}

.algorithm-callout {
  background: var(--navy);
  color: white;
  border-radius: 24px;
  padding: 32px;
  margin: 30px 0;
}

.algorithm-callout p { color: #cbd5e1; }

.algorithm-lead {
  color: var(--muted);
  font-size: 20px;
  line-height: 1.65;
}

@media (max-width: 980px) {
  .rev-container {
    width: min(100% - 32px, 720px);
  }

  .rev-nav-inner {
    grid-template-columns: 1fr auto;
  }

  .rev-menu {
    display: none;
  }

  .rev-hero-grid,
  .rev-how-grid,
  .rev-final {
    grid-template-columns: 1fr;
  }

  .rev-dashboard {
    grid-template-columns: 1fr;
  }

  .rev-dash-sidebar {
    display: none;
  }

  .rev-metrics,
  .rev-dash-grid,
  .rev-team-grid,
  .rev-testimonials,
  .rev-steps {
    grid-template-columns: 1fr;
  }

  .rev-strip {
    flex-direction: column;
    gap: 10px;
  }

  .rev-final {
    padding: 28px;
  }

  .rev-footer-inner {
    gap: 18px;
    flex-direction: column;
  }
}
''')

print("AI Revenue Manager homepage design applied.")
