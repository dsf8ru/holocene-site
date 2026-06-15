
from pathlib import Path

p = Path("src/app/globals.css")

s = p.read_text()

s += """

/* badge tuning */

.badges-section {

  padding-top: 18px !important;

  padding-bottom: 64px !important;

  margin-top: 0 !important;

}

.badges-row {

  gap: 24px !important;

  align-items: center !important;

}

.badge-img {

  height: 52px !important;

  width: auto !important;

}

.badge-link:first-child .badge-img {

  height: 68px !important;

}

@media (max-width: 980px) {

  .badge-img {

    height: 40px !important;

  }

  .badge-link:first-child .badge-img {

    height: 50px !important;

  }

}

"""

p.write_text(s)

print("Badges tuned.")

