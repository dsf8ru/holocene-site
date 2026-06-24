from pathlib import Path

p = Path("src/app/globals.css")
s = p.read_text()

s += """

/* typography tuning */

.brand-title {
  font-weight: 700 !important;
}

.nav-links {
  font-weight: 600 !important;
}

.btn {
  font-weight: 700 !important;
}

.eyebrow {
  font-weight: 650 !important;
}

.hero h1 {
  font-size: clamp(34px, 4.4vw, 58px) !important;
}

.faq h2 {
  font-size: 46px !important;
}

.cta h2 {
  font-size: 44px !important;
}

.footer-brand span {
  font-weight: 700 !important;
}
"""

p.write_text(s)

print("Typography patch applied.")
