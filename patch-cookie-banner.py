from pathlib import Path

components = Path("src/components")
components.mkdir(exist_ok=True)

Path("src/components/cookie-banner.tsx").write_text(r'''"use client";

import { useEffect, useState } from "react";

type Consent = {
  essential: true;
  analytics: boolean;
  advertising: boolean;
};

const STORAGE_KEY = "holocene_cookie_consent";

export default function CookieBanner() {
  const [visible, setVisible] = useState(false);
  const [settingsOpen, setSettingsOpen] = useState(false);
  const [analytics, setAnalytics] = useState(false);
  const [advertising, setAdvertising] = useState(false);

  useEffect(() => {
    const saved = window.localStorage.getItem(STORAGE_KEY);

    if (!saved) {
      setVisible(true);
      return;
    }

    try {
      const parsed = JSON.parse(saved) as Consent;
      setAnalytics(Boolean(parsed.analytics));
      setAdvertising(Boolean(parsed.advertising));
    } catch {
      setVisible(true);
    }
  }, []);

  function save(next: Consent) {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
    setVisible(false);
    setSettingsOpen(false);
  }

  if (!visible) return null;

  if (settingsOpen) {
    return (
      <div className="cookie-panel" role="dialog" aria-label="Cookie settings">
        <button className="cookie-back" type="button" onClick={() => setSettingsOpen(false)}>
          ← Cookies managing
        </button>

        <h2>Cookie Settings</h2>

        <p>
          Cookies necessary for the correct operation of the site are always enabled.
          Other cookies are configurable.
        </p>

        <div className="cookie-row">
          <div>
            <strong>Essential cookies</strong>
          </div>
          <span className="cookie-required">Always allowed</span>
        </div>

        <label className="cookie-row">
          <span>
            <strong>Analytics cookies</strong>
          </span>
          <input
            type="checkbox"
            checked={analytics}
            onChange={(event) => setAnalytics(event.target.checked)}
          />
        </label>

        <label className="cookie-row">
          <span>
            <strong>Advertising cookies</strong>
          </span>
          <input
            type="checkbox"
            checked={advertising}
            onChange={(event) => setAdvertising(event.target.checked)}
          />
        </label>

        <button
          className="cookie-confirm"
          type="button"
          onClick={() =>
            save({
              essential: true,
              analytics,
              advertising,
            })
          }
        >
          Confirm
        </button>
      </div>
    );
  }

  return (
    <div className="cookie-banner" role="dialog" aria-label="Cookies managing">
      <div>
        <h2>Cookies managing</h2>
        <p>We use cookies to provide the best site experience.</p>
      </div>

      <div className="cookie-actions">
        <button
          className="cookie-accept"
          type="button"
          onClick={() =>
            save({
              essential: true,
              analytics: true,
              advertising: true,
            })
          }
        >
          Accept All
        </button>

        <button className="cookie-settings" type="button" onClick={() => setSettingsOpen(true)}>
          Cookie Settings
        </button>
      </div>
    </div>
  );
}
''')

css = Path("src/app/globals.css")
s = css.read_text()

s += r'''

.cookie-banner,
.cookie-panel {
  position: fixed;
  left: 50%;
  bottom: 34px;
  z-index: 80;
  width: min(720px, calc(100% - 32px));
  transform: translateX(-50%);
  background: white;
  border: 1px solid var(--line);
  box-shadow: 0 30px 80px rgba(8, 15, 36, 0.18);
}

.cookie-banner {
  padding: 30px 38px;
}

.cookie-banner h2,
.cookie-panel h2 {
  margin: 0 0 14px;
  font-size: 26px;
  letter-spacing: -0.03em;
}

.cookie-banner p,
.cookie-panel p {
  margin: 0;
  color: var(--muted);
  font-size: 18px;
  line-height: 1.5;
}

.cookie-actions {
  display: flex;
  align-items: center;
  gap: 28px;
  margin-top: 28px;
}

.cookie-accept,
.cookie-confirm {
  border: 0;
  background: #000;
  color: white;
  font-weight: 850;
  font-size: 16px;
  padding: 16px 28px;
  cursor: pointer;
}

.cookie-settings,
.cookie-back {
  border: 0;
  background: transparent;
  color: #000;
  font-weight: 850;
  font-size: 16px;
  cursor: pointer;
}

.cookie-panel {
  padding: 28px;
  max-width: 440px;
}

.cookie-back {
  color: var(--muted);
  margin-bottom: 26px;
  padding: 0;
}

.cookie-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  border-top: 1px solid var(--line);
  padding: 18px 0;
  color: #111827;
}

.cookie-row:last-of-type {
  border-bottom: 1px solid var(--line);
}

.cookie-required {
  color: var(--blue);
  font-size: 12px;
  white-space: nowrap;
}

.cookie-row input {
  width: 46px;
  height: 26px;
  accent-color: var(--navy);
}

.cookie-confirm {
  margin-top: 24px;
  padding: 13px 20px;
  font-size: 14px;
}

@media (max-width: 720px) {
  .cookie-banner {
    padding: 24px;
  }

  .cookie-actions {
    flex-direction: column;
    align-items: stretch;
    gap: 14px;
  }

  .cookie-accept,
  .cookie-settings {
    width: 100%;
    justify-content: center;
  }
}
'''
css.write_text(s)

layout = Path("src/app/layout.tsx")
l = layout.read_text()

if 'import CookieBanner from "@/components/cookie-banner";' not in l:
    l = l.replace('import "./globals.css";', 'import "./globals.css";\nimport CookieBanner from "@/components/cookie-banner";')

l = l.replace("<body>{children}</body>", "<body>{children}<CookieBanner /></body>")

layout.write_text(l)

print("Cookie banner added.")
