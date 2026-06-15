
from pathlib import Path

# 1. Подменяем favicon

# Лучше использовать уже очищенный HS logo.

# Если logo-mark.png есть — берём его, иначе logo-transparent.png.

logo = Path("public/logo-mark.png")

if not logo.exists():

    logo = Path("public/logo-transparent.png")

if not logo.exists():

    raise SystemExit("No logo file found: public/logo-mark.png or public/logo-transparent.png")

# Создаем favicon.ico через ImageMagick convert

import subprocess

subprocess.run([

    "convert",

    str(logo),

    "-resize",

    "64x64",

    "src/app/favicon.ico",

], check=True)

# 2. Обновляем metadata

Path("src/app/layout.tsx").write_text(r'''import type { Metadata } from "next";

import "./globals.css";

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

      <body>{children}</body>

    </html>

  );

}

''')

# 3. Добавляем разные title для страниц

pages = {

    "src/app/algorithm/page.tsx": '''export const metadata = {

  title: "ML Pricing Algorithm",

  description: "How the Holocene AI Pricing Co-Pilot evaluates pricing behavior, evidence, revenue, and profit.",

};

''',

    "src/app/privacy/page.tsx": '''export const metadata = {

  title: "Privacy Policy",

  description: "Privacy Policy for Holocene Services OÜ.",

};

''',

    "src/app/terms/page.tsx": '''export const metadata = {

  title: "Terms of Service",

  description: "Terms of Service for Holocene Services OÜ.",

};

''',

}

for file, meta in pages.items():

    p = Path(file)

    s = p.read_text()

    if "export const metadata" not in s:

        s = s.replace('import Link from "next/link";\n\n', 'import Link from "next/link";\n\n' + meta)

        p.write_text(s)

print("Favicon and metadata updated.")

