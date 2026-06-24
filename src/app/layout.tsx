import type { Metadata } from "next";

import "./globals.css";
import CookieBanner from "@/components/cookie-banner";

export const metadata: Metadata = {

  title: {

    default: "Holocene AI Revenue Manager",

    template: "%s | Holocene",

  },

  description:

    "AI Revenue Manager for Amazon Private Label sellers. Find pricing, advertising, revenue, and profit opportunities in one place.",

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

