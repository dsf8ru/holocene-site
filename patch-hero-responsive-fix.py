from pathlib import Path

p = Path("src/app/globals.css")
s = p.read_text()

s += """

/* hero responsive fix */

.rev-hero-grid {
  grid-template-columns: minmax(420px, 0.78fr) minmax(620px, 1.22fr) !important;
  gap: 48px !important;
  overflow: hidden;
}

.rev-hero h1 {
  font-size: 56px !important;
  line-height: 0.98 !important;
  max-width: 620px;
}

.rev-hero p {
  max-width: 560px;
}

.rev-product-shot {
  min-width: 0;
}

@media (min-width: 1280px) {
  .rev-hero h1 {
    font-size: 58px !important;
  }
}

@media (max-width: 1180px) {
  .rev-hero-grid {
    grid-template-columns: 1fr !important;
  }

  .rev-hero h1 {
    font-size: clamp(40px, 8vw, 56px) !important;
    max-width: 760px;
  }
}

@media (max-width: 720px) {
  .rev-hero h1 {
    font-size: 42px !important;
  }
}
"""

p.write_text(s)
print("Hero responsive fix applied.")
