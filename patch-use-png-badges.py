from pathlib import Path

p = Path("src/app/page.tsx")
s = p.read_text()

s = s.replace(
    '/badges/amazon-ads.svg',
    '/badges/amazon-ads.png'
)

s = s.replace(
    '/badges/amazon-appstore.svg',
    '/badges/amazon-appstore.png'
)

s = s.replace(
    '/badges/shopify-appstore.svg',
    '/badges/shopify-appstore.png'
)

p.write_text(s)

print("PNG badges enabled")
