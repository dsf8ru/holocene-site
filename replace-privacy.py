
from pathlib import Path

Path("src/app/privacy/page.tsx").write_text(r'''import Link from "next/link";

export default function PrivacyPage() {

  return (

    <main className="container legal-page">

      <Link className="btn btn-secondary" href="/">← Back</Link>

      <h1>Privacy Policy</h1>

      <div className="content-paper">

        <p>

          The controller of the personal data is Holocene Services OÜ (registry code 16446910),

          located at Tööstuse tn 48, 10416, Tallinn, Estonia, phone +372 5740 8236 and

          e-mail info@holocene.ee.

        </p>

        <h2>1. Which personal data are processed?</h2>

        <ul>

          <li>Name, phone number and e-mail address</li>

          <li>Delivery address</li>

          <li>Bank account number</li>

          <li>Cost of goods and services and data related to payments (purchase history)</li>

          <li>Customer support data</li>

          <li>IP address</li>

        </ul>

        <h2>2. For which purposes are personal data processed?</h2>

        <p>

          Personal data is used to manage the customer’s orders and to deliver goods.

        </p>

        <p>

          Purchase history data (date of purchase, goods, quantity, customer data) are used to

          put together an overview of the goods and services purchased, to analyse customer

          preferences and, among other things, for the purposes of resolving consumer disputes.

        </p>

        <p>

          The bank account number is used to reimburse payments to the customer.

        </p>

        <p>

          Personal data such as the e-mail address, telephone number and name of the customer are

          processed to handle any issues relating to the provision of goods and services

          (customer support).

        </p>

        <p>

          E-mail is also used in order to forward invoices and the telephone number is used to

          notify the customer about their goods arriving in the parcel locker.

        </p>

        <p>

          The IP address or other online identifiers of users of the online shop are processed

          for the provision of the online shop as an information society service and for web use statistics.

        </p>

        <h2>3. Legal basis</h2>

        <p>

          The purpose of processing personal data is to fulfil the agreement entered into with

          the customer (managing the customer’s orders, delivery, returning goods and reimbursing payments).

        </p>

        <p>

          Personal data are processed in order to fulfil legal obligations (e.g. for accounting).

          The processing of personal data, i.e. the collection of purchase history data for the purposes

          of resolving potential consumer disputes, is necessary due to the controller’s legitimate interest.

        </p>

        <h2>4. Recipients of personal data</h2>

        <p>

          Personal data are forwarded to the customer support of the online shop in order to manage

          purchase history and resolve customer issues.

        </p>

        <p>

          Name, telephone number and e-mail address are forwarded to the transport service provider

          selected by the customer.

        </p>

        <p>

          If an outside service provider handles the accounting for the online shop, the personal data

          is forwarded to that service provider to perform the accounting operations.

        </p>

        <p>

          Personal data may be forwarded to IT service providers if this is needed to ensure the

          functionality of the online shop or to host data.

        </p>

        <h2>5. Security and access to data</h2>

        <p>

          Personal data are stored on the servers of a member state of the European Union or states

          of the European Economic Area.

        </p>

        <p>

          Personal data can be accessed by the staff of the online shop in order to resolve technical

          issues related to the use of the online shop and to provide customer support.

        </p>

        <p>

          Personal data are forwarded to processors on the basis of contracts between the online shop

          and processors.

        </p>

        <h2>6. Access to and rectification of personal data</h2>

        <p>

          Personal data can be accessed and rectified via the online shop’s user profile or customer support.

        </p>

        <h2>7. Withdrawal of consent</h2>

        <p>

          If personal data are processed with the customer’s consent, the customer has the right to

          withdraw their consent by making relevant changes in the user account’s settings or by

          notifying customer support via e-mail.

        </p>

        <h2>8. Storage</h2>

        <p>

          Personal data are erased upon deleting the online shop’s customer account, except for the

          personal data necessary for accounting or to resolve consumer disputes.

        </p>

        <p>

          The personal data in original accounting documents is stored for seven years.

        </p>

        <h2>9. Restriction</h2>

        <p>

          If the data are incorrect, incomplete or processed unlawfully, the customer has the right

          to request the restriction of the processing of their personal data.

        </p>

        <h2>10. Objections</h2>

        <p>

          The customer has the right to submit objections regarding the processing of their personal

          data if they have a reason to believe that there is no legal basis to process their personal data.

        </p>

        <h2>11. Erasure</h2>

        <p>

          For the erasure of personal data, customer support should be contacted by e-mail.

        </p>

        <h2>12. Transfer</h2>

        <p>

          Requests to transfer personal data submitted via e-mail are responded to within one month.

        </p>

        <h2>13. Direct marketing messages</h2>

        <p>

          The e-mail address and telephone number are used to send direct marketing messages if the

          customer has consented to receiving such messages.

        </p>

        <p>

          The customer has the right to object at any time both to the initial and further processing

          of their personal data related to direct marketing.

        </p>

        <h2>14. Resolution of disputes</h2>

        <p>

          Disputes concerning the processing of personal data are settled through customer support

          by email info@holocene.ee.

        </p>

        <p>

          The supervisory authority is the Estonian Data Protection Inspectorate (info@aki.ee).

        </p>

      </div>

    </main>

  );

}

''')

print("Privacy page replaced.")

