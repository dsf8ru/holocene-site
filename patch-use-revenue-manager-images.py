from pathlib import Path
import re

p = Path("src/app/page.tsx")
s = p.read_text()

old = '''            <DashboardMock />'''

new = '''            <div className="rev-product-shot">
              <picture>
                <source media="(max-width: 720px)" srcSet="/revenue-manager-mobile.webp" />
                <img
                  src="/revenue-manager-desktop.webp"
                  alt="Holocene AI Revenue Manager dashboard overview"
                />
              </picture>
            </div>'''

if old not in s:
    raise SystemExit("Could not find <DashboardMock /> in page.tsx")

s = s.replace(old, new)

p.write_text(s)

css = Path("src/app/globals.css")
c = css.read_text()

c += r'''

.rev-product-shot {
  background: white;
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 10px;
  box-shadow: 0 34px 80px rgba(15, 23, 42, .12);
  overflow: hidden;
}

.rev-product-shot img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 14px;
}

@media (max-width: 720px) {
  .rev-product-shot {
    padding: 8px;
    border-radius: 18px;
  }

  .rev-product-shot img {
    border-radius: 12px;
  }
}
'''
css.write_text(c)

print("Revenue manager images enabled.")
