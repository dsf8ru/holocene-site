import Link from "next/link";

export default function Page() {
  return (
    <main className="container simple-page">
      <Link className="btn btn-light" href="/">← Back</Link>
      <h1>Pricing</h1>
      <p>Holocene is currently free during MVP beta. Paid plans will be introduced after the beta period.</p>
    </main>
  );
}
