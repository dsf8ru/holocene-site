from pathlib import Path
import re

css = Path("src/app/globals.css")
s = css.read_text()

# убираем старые классы если есть
for cls in [
    ".algorithm-grid",
    ".algorithm-card",
    ".legal-card",
]:
    pos = s.find(cls)
    if pos != -1:
        end = s.find("}", pos)
        if end != -1:
            s = s[:pos] + s[end+1:]

s += """

.content-paper {
  background: white;
  border: 1px solid var(--line);
  border-radius: 28px;
  padding: 40px;
  margin-top: 24px;
}

.content-paper h2 {
  margin-top: 42px;
}

.content-paper h2:first-child {
  margin-top: 0;
}

.content-paper p,
.content-paper li {
  color: var(--muted);
  line-height: 1.8;
}

@media (max-width: 980px) {
  .content-paper {
    padding: 24px;
  }
}
"""

css.write_text(s)

# ---------- algorithm ----------
algo = Path("src/app/algorithm/page.tsx")
if algo.exists():
    a = algo.read_text()

    a = a.replace(
        '<div className="algorithm-grid">',
        '<div className="content-paper">'
    )

    a = a.replace(
        '</div>\n      </section>\n    </main>',
        '</div>\n      </section>\n    </main>'
    )

    a = a.replace(
        '<section className="algorithm-card">',
        ''
    )
    a = a.replace(
        '</section>',
        ''
    )

    algo.write_text(a)

# ---------- privacy ----------
privacy = Path("src/app/privacy/page.tsx")
if privacy.exists():
    p = privacy.read_text()

    p = p.replace(
        '<p className="legal-intro">',
        '<div className="content-paper">\n      <p className="legal-intro">'
    )

    p = p.replace(
        '</main>',
        '</div>\n    </main>'
    )

    p = re.sub(
        r'<section className="legal-card">',
        '',
        p
    )
    p = p.replace('</section>', '')

    privacy.write_text(p)

# ---------- terms ----------
terms = Path("src/app/terms/page.tsx")
if terms.exists():
    t = terms.read_text()

    t = t.replace(
        '<p className="legal-intro">',
        '<div className="content-paper">\n      <p className="legal-intro">'
    )

    t = t.replace(
        '</main>',
        '</div>\n    </main>'
    )

    t = re.sub(
        r'<section className="legal-card">',
        '',
        t
    )
    t = t.replace('</section>', '')

    terms.write_text(t)

print("Document layout patch applied.")
