# SOTO Granite & Cabinets

Responsive, bilingual, multi-page static website prepared for GitHub Pages.

## Preview locally

Open `index.html` in a browser, or run a small local server from this folder:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Publish with GitHub Pages

1. Create a GitHub repository and add these project files.
2. In **Settings → Pages**, choose **Deploy from a branch**, select `main` and `/ (root)`, then save.
3. GitHub will show the public URL after deployment. Add that URL to the repository description and replace the QR destination as described below if you want flyer scans to open the website.

No build step or package installation is required. All page links and assets use relative paths, so the site works from a GitHub Pages project URL.

## QR code for flyers

`assets/soto-tiktok-qr.svg` is a vector QR code linking to the TikTok profile supplied by the owner: `https://www.tiktok.com/@sotogranitecabinets`. It can be placed directly in a flyer or printed. It currently links to TikTok because the website has not been published and has no confirmed public URL yet.

To point the QR at the published website, edit `URL` in `work/make_qr.py`, then run:

```bash
python work/make_qr.py
```

The script overwrites the SVG QR asset with the new destination. Keep the QR black on white with a clear margin when laying out the flyer.

## Confirmed company details used

- Name: SOTO Granite & Cabinets
- Sign tagline: Commercial & Residential
- Main phone: +1 (661) 345-4539
- Cell phone: +1 (805) 280-8756
- Service areas shown on company sign: Bakersfield and Paso Robles, California
- TikTok: [@sotogranitecabinets](https://www.tiktok.com/@sotogranitecabinets)

Facebook and Instagram profiles could not be verified from public search, so they are not linked. WhatsApp is not assumed. No physical address, email, license, warranties, reviews, prices, inventory or completed SOTO projects have been invented.

## Before launch

- The inquiry form opens the visitor's email app with the message prepared. It does not submit to a server or save information. Add a verified company email and a secure form service or backend before describing the form as delivered to SOTO.
- Confirm which services and materials the company currently offers, the areas served, and the preferred contact email.
- The inspiration gallery uses remote Unsplash editorial imagery and labels it as inspiration, not company project photography. Replace these with approved company photos when available.
- The CSS loads DM Sans and Playfair Display from Google Fonts; system fallbacks are included.
- Update privacy language if analytics, uploads, cookies, CRM or third-party form processing are added.
- Add the public domain and a sitemap after the deployment URL is known.

## Files

- `index.html`, `services.html`, `projects.html`, `about.html`, `contact.html`
- `bakersfield.html`, `paso-robles.html`, `privacy.html`
- `styles.css`, `script.js`
- `assets/favicon.svg`, `assets/soto-tiktok-qr.svg`
- `work/make_qr.py` QR generator
