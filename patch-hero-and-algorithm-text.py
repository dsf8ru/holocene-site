from pathlib import Path

# Hero title + subtitle
home = Path("src/app/page.tsx")
s = home.read_text()

s = s.replace(
'''              <h1>Amazon pricing analytics for Private Label sellers.</h1>
              <p className="lead">
                See where pricing behavior may be leaving revenue or profit on the table using Seller Central and Amazon Ads data.
              </p>''',
'''              <h1>Holocene AI Pricing Co-Pilot</h1>
              <p className="lead">
                Understand how pricing behavior impacts revenue and profit. Analyze Seller Central and Amazon Ads data to identify pricing opportunities, evaluate pricing evidence, and make better pricing decisions.
              </p>'''
)

home.write_text(s)

# Algorithm CSS tuning
css = Path("src/app/globals.css")
c = css.read_text()

c += """

/* algorithm article tuning */

.content-paper h2 {
  font-size: 34px;
  line-height: 1.15;
  letter-spacing: -0.04em;
}

.content-paper p {
  max-width: 980px;
}

.algorithm-callout h2 {
  font-size: 38px;
  line-height: 1.1;
}

.algorithm-callout p {
  max-width: 980px;
}

@media (max-width: 980px) {
  .content-paper h2 {
    font-size: 28px;
  }

  .algorithm-callout h2 {
    font-size: 30px;
  }
}
"""
css.write_text(c)

# Algorithm page expanded text
Path("src/app/algorithm/page.tsx").write_text(r'''import Link from "next/link";

export default function AlgorithmPage() {
  return (
    <main>
      <section className="container algorithm-hero">
        <Link className="btn btn-secondary" href="/">← Back</Link>

        <h1>How the ML pricing algorithm works</h1>
        <p className="algorithm-lead">
          Holocene uses pricing history, sales behavior, advertising context, and product economics
          to help Amazon Private Label sellers understand how price changes may affect revenue and profit.
        </p>

        <div className="algorithm-callout">
          <h2>Pricing decisions are decisions about value perception.</h2>
          <p>
            A price is not only a number in Seller Central. It is a signal that customers compare
            against the value they believe the product provides. Holocene uses historical pricing behavior,
            sales velocity, advertising data, and cost structure to estimate how customers may respond
            to future price changes.
          </p>
        </div>

        <div className="content-paper">
          <h2>1. Value perception</h2>
          <p>
            Customers do not buy products because of price alone. Every purchase is the result of a
            comparison between the perceived value of a product and the price being asked.
          </p>
          <p>
            When perceived value is higher than the asking price, demand can stay strong or increase.
            When perceived value falls below the asking price, demand weakens. This is why two products
            with the same price can perform very differently.
          </p>
          <p>
            Perceived value changes over time. Competition, reviews, advertising activity, seasonality,
            marketplace ranking, product images, promotions, and brand trust can all change how customers
            respond to the same price.
          </p>
          <p>
            Holocene treats pricing as a measurement problem rather than a guessing problem. The goal is
            to understand how customers have historically responded to different prices and use that evidence
            to support future pricing decisions.
          </p>

          <h2>2. Price elasticity</h2>
          <p>
            Price elasticity describes how demand changes when price changes. Some products are highly
            sensitive: a small price increase can reduce unit sales quickly. Other products are more stable:
            customers continue buying even after a moderate price increase.
          </p>
          <p>
            This relationship is different for every product. A seller cannot safely assume that all SKUs
            should be priced with the same rule, the same margin target, or the same discount strategy.
          </p>
          <p>
            Holocene reviews historical price points and sales velocity to understand whether previous price
            changes created meaningful differences in revenue or demand. The system looks for price behavior
            that has enough sales evidence behind it to be useful.
          </p>
          <p>
            The goal is not simply to raise prices or lower prices. The goal is to identify price ranges where
            the product can generate stronger revenue, stronger profit, or better evidence for the next pricing test.
          </p>

          <h2>3. Historical evidence and probability</h2>
          <p>
            One day of sales means very little. Ten days mean more. Sixty days provide a stronger recent signal.
            Holocene uses recent sales behavior to avoid making recommendations from isolated events.
          </p>
          <p>
            Marketplace sales are noisy. A product may sell more because of advertising, ranking movement,
            seasonality, a promotion, or random demand fluctuation. A single strong or weak day does not prove
            that a price is good or bad.
          </p>
          <p>
            This is why Holocene uses evidence checks. The system evaluates recent history, order volume,
            price range, and meaningful price points before treating a pricing signal as reliable.
          </p>
          <p>
            The algorithm does not try to predict the future perfectly. It estimates the probability that a
            price candidate can improve the seller’s outcome based on the evidence available. More history and
            more meaningful price points usually create stronger pricing evidence.
          </p>

          <h2>4. Revenue versus profit</h2>
          <p>
            The best revenue price is not always the best profit price. A price that maximizes revenue can still
            produce weaker profit if margin, fees, product costs, or advertising spend are ignored.
          </p>
          <p>
            Holocene separates revenue opportunity from profit opportunity. Sellers can start with revenue analysis
            even before product costs are entered. Once COGS, FBA fees, marketplace fees, and advertising context
            are available, the system can estimate profit impact as well.
          </p>
          <p>
            This separation is important because different sellers optimize for different outcomes. Some may want
            growth and velocity. Others may want margin expansion. Others may want to test whether discounts are
            hiding weak pricing behavior.
          </p>
          <p>
            Pricing Workspace shows recommended revenue prices and recommended profit prices separately so the seller
            can evaluate the trade-off before changing anything in Amazon.
          </p>

          <h2>5. Pricing constraints</h2>
          <p>
            A pricing algorithm should not behave like uncontrolled repricing. Real sellers operate with constraints:
            minimum margin, acceptable price range, cost structure, advertising pressure, marketplace position, and
            customer expectations.
          </p>
          <p>
            Holocene uses pricing evidence, pricing activity, cost completeness, and recent marketplace behavior to
            decide how much confidence a recommendation should receive. If the evidence is weak, the system should not
            pretend that the recommendation is certain.
          </p>
          <p>
            Constraints also protect the seller from overreacting to noise. A short-term sales spike does not always
            justify a new price. A temporary drop does not always mean the price is wrong. The system is designed to
            make price decisions more deliberate.
          </p>

          <h2>6. AI co-pilot workflow</h2>
          <p>
            Holocene starts with visibility. The dashboard shows whether pricing behavior may be leaving revenue or
            profit on the table, how active pricing has been, and whether enough evidence exists for recommendations.
          </p>
          <p>
            The next step is review. Pricing Workspace lets the seller inspect product-level recommendations,
            historical price points, pricing evidence, advertising context, and expected impact.
          </p>
          <p>
            After review, the seller can apply recommendations manually or continue monitoring. This is the safest
            starting point because the seller stays in control while the system learns from recent pricing behavior.
          </p>
          <p>
            Controlled automation is the final step. The AI co-pilot workflow is designed to operate within defined
            limits, using evidence-aware recommendations rather than aggressive price changes. The objective is not
            to replace the seller, but to help the seller make and execute better pricing decisions.
          </p>
        </div>
      </section>
    </main>
  );
}
''')

print("Hero and algorithm text updated.")
