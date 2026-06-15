"use client";

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
