from pathlib import Path
import re

app = Path("src/app")

# CSS polish
css = app / "globals.css"
s = css.read_text()

s += r"""

/* content polish */

.hero .lead {
  max-width: 520px;
}

.legal-page {
  background: transparent;
}

.legal-intro {
  color: var(--muted);
  font-size: 18px;
  line-height: 1.7;
  margin-bottom: 32px;
}

.legal-card {
  background: white;
  border: 1px solid var(--line);
  border-radius: 24px;
  padding: 30px;
  margin-top: 18px;
}

.legal-card h2 {
  margin-top: 0;
}

.algorithm-hero {
  padding: 72px 0 42px;
}

.algorithm-lead {
  max-width: 760px;
  color: var(--muted);
  font-size: 20px;
  line-height: 1.65;
}

.algorithm-callout {
  background: var(--navy);
  color: white;
  border-radius: 30px;
  padding: 34px;
  margin: 34px 0;
}

.algorithm-callout p {
  color: #c5d0e2;
  line-height: 1.65;
}

@media (max-width: 980px) {
  .legal-card {
    padding: 22px;
  }
}
"""
css.write_text(s)

# Home page: shorter hero, better FAQ
page = app / "page.tsx"
p = page.read_text()

p = p.replace(
'''              <h1>Amazon pricing analytics for better price decisions.</h1>
              <p className="lead">
                Holocene AI Pricing Co-Pilot analyzes Seller Central and Amazon Ads data to show pricing activity,
                pricing evidence, revenue opportunity, and profit opportunity by product.
              </p>''',
'''              <h1>Amazon pricing analytics for Private Label sellers.</h1>
              <p className="lead">
                See where pricing behavior may be leaving revenue or profit on the table using Seller Central and Amazon Ads data.
              </p>'''
)

p = p.replace(
'''              <div className="faq-item">
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
              </div>''',
'''              <div className="faq-item">
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
              </div>'''
)

page.write_text(p)

# Algorithm page
(app / "algorithm" / "page.tsx").write_text(r'''import Link from "next/link";

export default function AlgorithmPage() {
  return (
    <main>
      <section className="container algorithm-hero">
        <Link className="btn btn-secondary" href="/">← Back</Link>

        <h1>How the ML pricing algorithm works</h1>
        <p className="algorithm-lead">
          Holocene translates pricing history, sales behavior, advertising context, and product economics
          into evidence-aware pricing recommendations for Amazon Private Label sellers.
        </p>

        <div className="algorithm-callout">
          <h2>Pricing is not only about changing numbers.</h2>
          <p>
            A price is a signal of value perception. When customers react to a price change,
            the seller learns how demand, revenue, and profit may move at that price point.
            Holocene turns those historical signals into a structured pricing workflow.
          </p>
        </div>
      </section>

      <section className="container section">
        <div className="algorithm-grid">
          <section className="algorithm-card">
            <h2>1. Value perception</h2>
            <p>
              Customers buy when their perceived value is equal to or higher than the price.
              That perception changes with competition, seasonality, product presentation, promotions,
              advertising pressure, and marketplace conditions.
            </p>
          </section>

          <section className="algorithm-card">
            <h2>2. Price elasticity</h2>
            <p>
              Every product reacts differently to price changes. Some products lose sales quickly after a small increase.
              Others remain stable. Holocene reviews historical price points and sales velocity to estimate how a product responds.
            </p>
          </section>

          <section className="algorithm-card">
            <h2>3. Evidence checks</h2>
            <p>
              Average sales can be misleading. Holocene checks whether there is enough recent history, order volume,
              price range, and meaningful price-point evidence before showing recommendations.
            </p>
          </section>

          <section className="algorithm-card">
            <h2>4. Revenue and profit separation</h2>
            <p>
              The best revenue price is not always the best profit price. Holocene separates revenue opportunity from profit
              opportunity once COGS, FBA fees, marketplace fees, and advertising context are available.
            </p>
          </section>

          <section className="algorithm-card">
            <h2>5. Pricing constraints</h2>
            <p>
              Recommendations must respect business constraints: cost structure, acceptable margin, price history,
              marketplace behavior, and seller-defined boundaries. This prevents optimization from becoming reckless repricing.
            </p>
          </section>

          <section className="algorithm-card">
            <h2>6. AI co-pilot workflow</h2>
            <p>
              Sellers can start in recommendation mode, review pricing evidence in Pricing Workspace,
              and later enable controlled automation when they are ready to let the system execute within defined limits.
            </p>
          </section>
        </div>
      </section>
    </main>
  );
}
''')

# Privacy page: card format
privacy = app / "privacy" / "page.tsx"
pv = privacy.read_text()
pv = pv.replace('<p>\n        The controller', '<p className="legal-intro">\n        The controller')
pv = re.sub(r'\n      <h2>(.*?)</h2>\n      ([\s\S]*?)(?=\n      <h2>|\n    </main>)',
            lambda m: f'\n      <section className="legal-card">\n        <h2>{m.group(1)}</h2>\n        {m.group(2).strip()}\n      </section>',
            pv)
privacy.write_text(pv)

# Terms page: card format
terms = app / "terms" / "page.tsx"
tv = terms.read_text()
tv = tv.replace('<p>\n        Originally published', '<p className="legal-intro">\n        Originally published')
tv = re.sub(r'\n      <h2>(.*?)</h2>\n      ([\s\S]*?)(?=\n      <h2>|\n    </main>)',
            lambda m: f'\n      <section className="legal-card">\n        <h2>{m.group(1)}</h2>\n        {m.group(2).strip()}\n      </section>',
            tv)
terms.write_text(tv)

print("Content polish patch applied.")
