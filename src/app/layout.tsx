import type { Metadata } from "next";

import "./globals.css";
import CookieBanner from "@/components/cookie-banner";

export const metadata: Metadata = {

  title: {

    default: "Holocene AI Pricing Co-Pilot",

    template: "%s | Holocene",

  },

  description:

    "Amazon pricing analytics and AI Pricing Co-Pilot for Private Label sellers.",

  icons: {

    icon: "/favicon.ico",

    shortcut: "/favicon.ico",

    apple: "/favicon.ico",

  },

};

export default function RootLayout({

  children,

}: Readonly<{

  children: React.ReactNode;

}>) {

  return (

    <html lang="en">

      <body>{children}<CookieBanner /></body>

    </html>

  );

}

