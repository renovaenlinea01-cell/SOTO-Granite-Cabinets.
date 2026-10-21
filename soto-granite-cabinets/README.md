# SOTO Granite & Cabinets

Responsive, bilingual, multi-page static website for SOTO Granite & Cabinets. It describes kitchen and bathroom remodeling, cabinets and countertops, wood-look tile and laminate flooring, drywall, painting, electrical work and general home repairs. The portfolio retains all 41 owner-provided project photos and groups them into browsable project cards, with a lightbox and category filters. A separate generated electrical photo is labeled as illustrative and is not included as a SOTO project.

## Preview locally

Open `index.html` in a browser, or run a small local server from this folder:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Update the connected Vercel site

The Vercel project is connected to the GitHub `main` branch. Replace the website files in the repository with the contents of this folder, keep the `assets/` directory structure, and commit the changes to `main`. Vercel will create a deployment automatically. Check **Deployments** in Vercel and wait for the new deployment to show **Ready**.

No build step or package installation is required. All page links and assets use relative paths.

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
- Facebook: [SOTO Facebook link](https://www.facebook.com/share/19r1S9o8NU/)

The Facebook link above was supplied by the owner and is linked directly. No Instagram link was confirmed. WhatsApp is not assumed. No physical address, email, license, warranties, reviews, prices, inventory, dates or project locations have been invented.

## Before launch

- The inquiry form opens the visitor's email app with the message prepared. It does not submit to a server or save information. Add a verified company email and a secure form service or backend before describing the form as delivered to SOTO.
- Confirm flooring materials, the electrical work scope, service area availability, and the preferred contact email before quoting.
- The portfolio photos in `assets/projects/` were supplied by the owner. They show kitchen and bathroom updates, repairs, cabinets, countertops, wood-look tile installation and drywall preparation. The design rendering is labeled as a concept, work-in-progress photos are labeled accordingly, and the generated electrical image is marked as illustrative. Only the outdoor countertop photos are marked before/after because they show the same work area at different stages.
- The CSS loads DM Sans and Playfair Display from Google Fonts; system fallbacks are included.
- Update privacy language if analytics, uploads, cookies, CRM or third-party form processing are added.
- Add the public domain and a sitemap after the deployment URL is known.

## Files

- `index.html`, `services.html`, `projects.html`, `about.html`, `contact.html`
- `bakersfield.html`, `paso-robles.html`, `privacy.html`
- `styles.css`, `script.js`
- `assets/favicon.svg`, `assets/soto-tiktok-qr.svg`, `assets/electrical-work-illustrative.png`
- `work/make_qr.py` QR generator
