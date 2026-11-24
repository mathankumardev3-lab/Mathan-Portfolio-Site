# TRILLION GAME — Creative Digital Agency & Engineering Studio

A digital agency portfolio inspired by the high-velocity startup ethos of **Trillion Game**. Designed with editorial typography, tactile motion choreography, and high-performance native browser primitives.

---

## ⚡ Tech Stack & Architecture

This project is built **strictly** without any front-end frameworks, build tools, or server runtimes:

- **HTML5**: Semantic layout structure (`<header>`, `<main>`, `<section>`, `<article>`, `<footer>`).
- **CSS3 & Tailwind CSS**: Modern typography, custom layout grids, and brand variables via Tailwind CDN + custom `assets/css/style.css`.
- **Vanilla JavaScript (ES6+)**: Modular client-side interactions, project category filter, mobile drawer, and dynamic enquiry generation.
- **GSAP & ScrollTrigger**: Hardware-accelerated motion choreography and scroll reveals.
- **Three.js**: Interactive 3D WebGL core featuring an obsidian polyhedron with orbit drag controls.
- **Lucide Icons**: Crisp vector UI icons.
- **GitHub Pages Ready**: 100% static client-side asset delivery with zero backend requirements.

---

## 🎨 Color Palette & Design System

- **Warm Cream**: `#FAF7F2` (Background & tactile foundation)
- **Obsidian Black**: `#0B0C0E` (Surface & strong contrast text)
- **Trillion Orange**: `#FF5A1F` (Energy accents, cursor highlight, and CTAs)
- **Forest Green**: `#0D2818` (Editorial prestige, badges, and primary buttons)
- **Typography**: 
  - Display: *Syne* (Bold, modern geometric)
  - Body: *Plus Jakarta Sans* (Clean, legible sans-serif)
  - Editorial: *Playfair Display* (Editorial luxury italic)

---

## 📂 Project Showcase (All 6 Included)

The portfolio highlights six client deliverables with high-fidelity screenshots:

1. **Kaveri Bridal & Beauty Studio** — Luxury HD bridal makeup, hair styling, and mehendi studio.
2. **CarePlus Clinic** — Multispecialty clinic, 24/7 OPD routing, diagnostics catalog, and family care.
3. **Taste & Thyme** — Artisan bistro and botanical dining experience with seasonal menus.
4. **Haven Properties** — Ultra-prime architectural residences, penthouses, and waterfront estates.
5. **Vertex Infra** — Heavy civil engineering, mega structures, high-speed rail, and BIM infrastructure.
6. **StockFlow** — High-velocity enterprise multi-depot inventory automation SaaS platform.

---

## 📁 File Structure

```
trillion-game-portfolio/
│
├── index.html                  # Semantic single-page HTML
├── assets/
│   ├── css/
│   │   └── style.css           # Custom styling, palette variables & cursor
│   ├── js/
│   │   └── script.js           # Three.js 3D hero, GSAP & Vanilla JS logic
│   ├── images/
│   │   ├── projects/           # High-resolution screenshots of all 6 projects
│   │   │   ├── kaveri-bridal.png
│   │   │   ├── careplus-clinic.png
│   │   │   ├── taste-thyme.png
│   │   │   ├── haven-properties.png
│   │   │   ├── vertex-infra.png
│   │   │   └── stockflow.png
│   │   └── general/
│   └── models/
│
├── generate_screenshots.py     # Clean renderer generating project previews
└── README.md
```

---

## 🚀 Deployment Instructions (GitHub Pages)

Because this repository contains zero build steps or server requirements, deploying takes less than 60 seconds:

1. Push this directory to your GitHub repository:
   ```bash
   git init
   git add .
   git commit -m "feat: complete Trillion Game vanilla portfolio"
   git branch -M main
   git remote add origin https://github.com/mathankumardev3-lab/<your-repo-name>.git
   git push -u origin main
   ```
2. In your GitHub repository:
   - Navigate to **Settings** > **Pages**.
   - Under **Build and deployment**, set **Source** to **Deploy from a branch**.
   - Select `main` branch and `/ (root)` folder.
   - Click **Save**.
3. Your portfolio is live instantly at:
   `https://mathankumardev3-lab.github.io/<your-repo-name>/`

---

## 📞 Direct Inquiries & Contact Configuration

All contact points are fully static with zero third-party form services:
- **WhatsApp Direct**: Pre-formatted WhatsApp links with configurable phone numbers and message generation (`assets/js/script.js`).
- **Email Client**: Standard `mailto:` handlers pre-filling inquiry subject and project classifications.
- **Socials**: Direct links to GitHub and Instagram.
