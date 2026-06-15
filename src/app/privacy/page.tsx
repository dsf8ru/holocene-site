import Link from "next/link";

export const metadata = {

  title: "Privacy Policy",

  description: "Privacy Policy for Holocene Services OÜ.",

};

export default function PrivacyPage() {
  return (
    <main className="container legal-page">
      <Link className="btn btn-secondary" href="/">← Back</Link>

      <h1>Privacy Policy</h1>
      <div className="content-paper">
      <p className="legal-intro">
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
      
    </div>
    </main>
  );
}
