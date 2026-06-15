from pathlib import Path

app = Path("src/app")
(app / "algorithm").mkdir(exist_ok=True)
(app / "privacy").mkdir(exist_ok=True)
(app / "terms").mkdir(exist_ok=True)

css = app / "globals.css"
s = css.read_text()

s = s.replace("scroll-behavior: smooth;", "scroll-behavior: smooth;\n  scroll-padding-top: 92px;")
s = s.replace("min-height: 76px;", "min-height: 64px;")
s = s.replace("width: 238px;", "width: 205px;")
s = s.replace("padding: 34px 0;", "padding: 24px 0;")
s += """

#how,
#faq,
#integrations {
  scroll-margin-top: 110px;
}

.legal-page {
  max-width: 920px;
  padding: 72px 0;
}

.legal-page h1 {
  font-size: clamp(40px, 6vw, 64px);
  letter-spacing: -0.06em;
}

.legal-page h2 {
  font-size: 26px;
  margin-top: 42px;
  letter-spacing: -0.035em;
}

.legal-page p,
.legal-page li {
  color: var(--muted);
  line-height: 1.75;
}

.algorithm-grid {
  display: grid;
  gap: 18px;
}

.algorithm-card {
  background: white;
  border: 1px solid var(--line);
  border-radius: 24px;
  padding: 26px;
}
"""
css.write_text(s)

(app / "page.tsx").write_text(r'''import Image from "next/image";

const loginUrl = "https://app.holocene.ee/login";
const registerUrl = "https://app.holocene.ee/register";

function Header() {
  return (
    <header className="nav">
      <div className="container nav-inner">
        <a href="/" aria-label="Holocene home">
          <Image className="logo-img" src="/logo-transparent.png" alt="Holocene AI Pricing Co-Pilot" width={760} height={190} priority />
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
        <Image className="logo-img" src="/logo-transparent.png" alt="Holocene AI Pricing Co-Pilot" width={760} height={190} />
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
                Holocene AI Pricing Co-Pilot analyzes Seller Central and Amazon Ads data to show pricing activity,
                pricing evidence, revenue opportunity, and profit opportunity by product.
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

        <section className="section" id="integrations">
          <div className="container">
            <div className="section-head">
              <h2>Amazon Seller Central and Amazon Ads data.</h2>
              <p>
                Holocene is built around the data sources Amazon sellers already use:
                sales and product data from Seller Central, plus advertising performance from Amazon Ads.
              </p>
            </div>

            <div className="cards-3">
              <div className="feature">
                <h3>Seller Central</h3>
                <p>Orders, SKUs, marketplaces, product sales, and pricing history.</p>
              </div>
              <div className="feature">
                <h3>Amazon Ads</h3>
                <p>Advertising spend, clicks, impressions, ROAS, and TACOS context.</p>
              </div>
              <div className="feature">
                <h3>Pricing Analytics</h3>
                <p>Revenue opportunity, profit opportunity, pricing evidence, and price-level recommendations.</p>
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
                <h3>What data does Holocene use?</h3>
                <p>Holocene uses connected Seller Central and Amazon Ads data to analyze sales, pricing behavior, advertising context, and product-level opportunity.</p>
              </div>
              <div className="faq-item">
                <h3>How often is the system updated?</h3>
                <p>The system analyzes the last 60 days of data and is designed around a weekly refresh cadence.</p>
              </div>
              <div className="faq-item">
                <h3>Do I need product costs?</h3>
                <p>You can start with revenue opportunity without COGS. Profit opportunity becomes available after product costs and fees are added.</p>
              </div>
              <div className="faq-item">
                <h3>Does Holocene change prices automatically?</h3>
                <p>Holocene starts with analytics, recommendations, and Pricing Workspace review. Pricing automation is planned as a controlled co-pilot workflow.</p>
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
''')

(app / "algorithm" / "page.tsx").write_text(r'''import Link from "next/link";

export default function AlgorithmPage() {
  return (
    <main className="container legal-page">
      <Link className="btn btn-secondary" href="/">← Back</Link>

      <h1>How the ML pricing algorithm works</h1>
      <p>
        Holocene uses pricing behavior, sales history, advertising context, and product economics
        to help sellers understand how price changes may affect revenue and profit.
      </p>

      <div className="algorithm-grid">
        <section className="algorithm-card">
          <h2>1. Price is a signal of value perception</h2>
          <p>
            A customer buys when their perception of product value is equal to or higher than the seller’s price.
            Pricing strategy starts with understanding how that value perception changes over time.
          </p>
        </section>

        <section className="algorithm-card">
          <h2>2. Every product has its own elasticity</h2>
          <p>
            Some products lose sales quickly after a small price increase. Others barely react.
            Holocene analyzes historical price points to understand how demand responded at different prices.
          </p>
        </section>

        <section className="algorithm-card">
          <h2>3. Average sales are not enough</h2>
          <p>
            Marketplace sales are volatile. One or two days of sales can be misleading.
            Holocene uses recent history and evidence checks to estimate whether a price point is meaningful enough
            to support a recommendation.
          </p>
        </section>

        <section className="algorithm-card">
          <h2>4. Pricing recommendations need constraints</h2>
          <p>
            COGS, fees, advertising spend, seasonality, competition, and price history all affect whether a price is useful.
            Holocene separates revenue opportunity from profit opportunity so sellers can avoid optimizing the wrong metric.
          </p>
        </section>

        <section className="algorithm-card">
          <h2>5. AI co-pilot workflow</h2>
          <p>
            Sellers can start in recommendation mode, review pricing evidence, and make price changes manually.
            Controlled automation can later apply pricing decisions within defined boundaries.
          </p>
        </section>
      </div>
    </main>
  );
}
''')

(app / "privacy" / "page.tsx").write_text(r'''import Link from "next/link";

export default function PrivacyPage() {
  return (
    <main className="container legal-page">
      <Link className="btn btn-secondary" href="/">← Back</Link>

      <h1>Privacy Policy</h1>
      <p>
        The controller of personal data is Holocene Services OÜ, registry code 16446910,
        located at Tööstuse tn 48, 10416, Tallinn, Estonia. Contact: info@holocene.ee.
      </p>

      <h2>1. Which data are processed?</h2>
      <ul>
        <li>Account data: name, email address, authentication and session data.</li>
        <li>Customer support data: messages, requests, and technical support history.</li>
        <li>Amazon Seller Central data: orders, SKUs, marketplaces, product sales, pricing history, and related product data.</li>
        <li>Amazon Ads data: campaign metrics, clicks, impressions, advertising spend, and related advertising performance data.</li>
        <li>User-provided business data: COGS, fees, pricing settings, and optimization preferences.</li>
        <li>Technical data: IP address, browser information, cookies, device and usage information.</li>
      </ul>

      <h2>2. Purposes of processing</h2>
      <p>
        Personal and business data are processed to provide Holocene pricing analytics, dashboard reporting,
        pricing recommendations, product-level analysis, customer support, billing, security, and service improvement.
      </p>

      <h2>3. Amazon data usage</h2>
      <p>
        Holocene accesses Amazon Seller Central and Amazon Ads data only to provide pricing analytics,
        reporting, recommendation generation, and pricing optimization services requested by the user.
        Holocene does not sell Amazon data to third parties and does not use Amazon data for third-party advertising.
      </p>

      <h2>4. Legal basis</h2>
      <p>
        Data are processed to perform the service agreement, comply with legal obligations, protect legitimate business interests,
        provide security, and where applicable, based on user consent.
      </p>

      <h2>5. Recipients of data</h2>
      <p>
        Data may be processed by hosting providers, database providers, analytics providers, payment providers,
        customer support providers, and other IT service providers required to operate Holocene.
      </p>

      <h2>6. Security and access</h2>
      <p>
        Access to data is limited to authorized personnel and processors who need access to provide, maintain,
        secure, or support the service. Processors are required to apply appropriate safeguards under GDPR.
      </p>

      <h2>7. Storage and deletion</h2>
      <p>
        Data are stored for as long as needed to provide the service, comply with legal obligations, resolve disputes,
        and maintain security. Users may request deletion of their account and associated data by contacting support@holocene.ee.
      </p>

      <h2>8. User rights</h2>
      <p>
        Users may request access, rectification, restriction, erasure, portability, or object to processing of their personal data.
        Requests should be sent to info@holocene.ee or support@holocene.ee.
      </p>

      <h2>9. Direct marketing</h2>
      <p>
        Holocene may send product updates or marketing messages only where permitted by law or consented to by the user.
        Users may unsubscribe or object to such processing at any time.
      </p>

      <h2>10. Disputes</h2>
      <p>
        Disputes concerning personal data are settled through customer support by email at info@holocene.ee.
        The supervisory authority is the Estonian Data Protection Inspectorate: info@aki.ee.
      </p>
    </main>
  );
}
''')

(app / "terms" / "page.tsx").write_text(r'''import Link from "next/link";

export default function TermsPage() {
  return (
    <main className="container legal-page">
      <Link className="btn btn-secondary" href="/">← Back</Link>

      <h1>Terms of Service</h1>
      <p>
        Originally published on July 01, 2024. The controller of these Terms of Service is Holocene Services OÜ,
        registry code 16446910, located at Tööstuse tn 48, 10416, Tallinn, Estonia.
        Contact: info@holocene.ee.
      </p>

      <h2>1. Overview</h2>
      <p>
        This website and service are operated by Holocene Services OÜ. By accessing the website or using the service,
        you agree to these Terms of Service.
      </p>

      <h2>2. Service use</h2>
      <p>
        You may use Holocene only for lawful business analytics purposes and only for accounts, stores, marketplaces,
        and data sources that you are authorized to connect.
      </p>

      <h2>3. Account information</h2>
      <p>
        You agree to provide current, complete, and accurate account information and to keep your login credentials secure.
      </p>

      <h2>4. Modifications, prices, and subscription plans</h2>
      <p>
        We reserve the right to modify or discontinue the service, subscription plans, features, or pricing at any time.
        If paid plans are introduced or changed, applicable pricing and billing terms will be made available to users.
      </p>

      <h2>5. Third-party services</h2>
      <p>
        Holocene may connect to third-party services such as Amazon Seller Central, Amazon Ads, payment providers,
        hosting providers, and analytics systems. Your use of third-party services may be subject to their own terms.
      </p>

      <h2>6. Prohibited uses</h2>
      <p>
        You may not use the service for unlawful purposes, to violate intellectual property rights, to transmit malicious code,
        to scrape or abuse the service, or to interfere with security features.
      </p>

      <h2>7. Disclaimer of warranties</h2>
      <p>
        The service is provided “as is” and “as available.” We do not guarantee that the service will be uninterrupted,
        error-free, or that the results obtained from the service will be accurate or reliable.
      </p>

      <h2>8. Limitation of liability</h2>
      <p>
        To the maximum extent permitted by law, Holocene Services OÜ shall not be liable for indirect, incidental,
        special, consequential, or punitive damages, including lost profits, lost revenue, loss of data, or business interruption.
      </p>

      <h2>9. Termination</h2>
      <p>
        You may stop using the service at any time. We may suspend or terminate access if we believe these Terms have been violated.
      </p>

      <h2>10. Governing law</h2>
      <p>
        These Terms of Service and any separate agreements whereby we provide services shall be governed by the laws of Estonia.
      </p>

      <h2>11. Changes to Terms</h2>
      <p>
        We reserve the right to update these Terms by posting changes on this website.
        Continued use of the website or service after changes are posted constitutes acceptance of those changes.
      </p>

      <h2>12. Contact</h2>
      <p>Questions about the Terms of Service should be sent to info@holocene.ee.</p>
    </main>
  );
}
''')

print("Patch v5 applied.")
