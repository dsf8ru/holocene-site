from pathlib import Path

Path("src/app/algorithm/page.tsx").write_text(r'''import Link from "next/link";

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

        <div className="content-paper">
          <h2>1. Value perception</h2>
          <p>
            Customers buy when their perceived value is equal to or higher than the price.
            That perception changes with competition, seasonality, product presentation,
            promotions, advertising pressure, and marketplace conditions.
          </p>

          <h2>2. Price elasticity</h2>
          <p>
            Every product reacts differently to price changes. Some products lose sales quickly
            after a small increase. Others remain stable. Holocene reviews historical price points
            and sales velocity to estimate how a product responds.
          </p>

          <h2>3. Evidence checks</h2>
          <p>
            Average sales can be misleading. Holocene checks whether there is enough recent history,
            order volume, price range, and meaningful price-point evidence before showing recommendations.
          </p>

          <h2>4. Revenue and profit separation</h2>
          <p>
            The best revenue price is not always the best profit price. Holocene separates revenue opportunity
            from profit opportunity once COGS, FBA fees, marketplace fees, and advertising context are available.
          </p>

          <h2>5. Pricing constraints</h2>
          <p>
            Recommendations must respect business constraints: cost structure, acceptable margin, price history,
            marketplace behavior, and seller-defined boundaries. This prevents optimization from becoming reckless repricing.
          </p>

          <h2>6. AI co-pilot workflow</h2>
          <p>
            Sellers can start in recommendation mode, review pricing evidence in Pricing Workspace,
            and later enable controlled automation when they are ready to let the system execute within defined limits.
          </p>
        </div>
      </section>
    </main>
  );
}
''')

print("Algorithm page fixed.")
