import Link from "next/link";

export default function Page() {
  return (
    <main className="container simple-page">
      <Link className="btn btn-light" href="/">← Back</Link>
      <h1>Support</h1>
      <p>For support, contact the Holocene team at support@holocene.ee.</p>
    </main>
  );
}
