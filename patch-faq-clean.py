from pathlib import Path

css = Path("src/app/globals.css")
s = css.read_text()

s += """

.faq-list {
  background: white;
  border: 1px solid var(--line);
  border-radius: 28px;
  padding: 12px 30px;
}

.faq-item {
  background: transparent !important;
  border: 0 !important;
  border-radius: 0 !important;
  padding: 24px 0 !important;
  border-bottom: 1px solid var(--line) !important;
}

.faq-item:last-child {
  border-bottom: 0 !important;
}

.faq-item h3 {
  margin-bottom: 8px;
}

.faq-item p {
  margin: 0;
}
"""

css.write_text(s)

print("FAQ cleaned.")
