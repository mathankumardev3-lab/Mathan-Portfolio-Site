import cairo
import math

WIDTH = 1280
HEIGHT = 800

def draw_browser_chrome(ctx, title, url):
    # Top bar background
    ctx.set_source_rgb(0.12, 0.13, 0.15)
    ctx.rectangle(0, 0, WIDTH, 48)
    ctx.fill()
    
    # Window controls (mac style)
    colors = [(0.98, 0.36, 0.35), (0.99, 0.73, 0.22), (0.16, 0.79, 0.38)]
    for i, col in enumerate(colors):
        ctx.set_source_rgb(*col)
        ctx.arc(24 + i * 20, 24, 6, 0, 2 * math.pi)
        ctx.fill()
        
    # URL bar
    ctx.set_source_rgb(0.18, 0.20, 0.24)
    # rounded rectangle
    x, y, w, h, r = 160, 10, 800, 28, 6
    ctx.arc(x + r, y + r, r, math.pi, 1.5 * math.pi)
    ctx.arc(x + w - r, y + r, r, 1.5 * math.pi, 2 * math.pi)
    ctx.arc(x + w - r, y + h - r, r, 0, 0.5 * math.pi)
    ctx.arc(x + r, y + h - r, r, 0.5 * math.pi, math.pi)
    ctx.close_path()
    ctx.fill()
    
    # Padlock icon hint & URL text
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(12)
    ctx.set_source_rgb(0.4, 0.8, 0.4)
    ctx.move_to(175, 28)
    ctx.show_text("🔒 https://")
    ctx.set_source_rgb(0.85, 0.88, 0.92)
    ctx.show_text(url)
    
    # Title
    ctx.set_source_rgb(0.6, 0.65, 0.7)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(11)
    ctx.move_to(WIDTH - 220, 28)
    ctx.show_text(title)

# 1. Kaveri Bridal & Beauty Studio
def render_kaveri(filename):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surf)
    
    # Background - warm luxurious blush/rose/cream
    pat = cairo.LinearGradient(0, 48, WIDTH, HEIGHT)
    pat.add_color_stop_rgb(0, 0.98, 0.94, 0.92)
    pat.add_color_stop_rgb(1, 0.94, 0.88, 0.86)
    ctx.set_source(pat)
    ctx.rectangle(0, 48, WIDTH, HEIGHT - 48)
    ctx.fill()
    
    # Nav bar
    ctx.set_source_rgba(1, 1, 1, 0.9)
    ctx.rectangle(0, 48, WIDTH, 65)
    ctx.fill()
    
    ctx.select_font_face("DejaVu Serif", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_source_rgb(0.35, 0.12, 0.18)
    ctx.set_font_size(22)
    ctx.move_to(80, 88)
    ctx.show_text("KAVERI")
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(10)
    ctx.move_to(180, 88)
    ctx.show_text("BRIDAL & BEAUTY STUDIO")
    
    # Nav links
    ctx.set_font_size(13)
    ctx.set_source_rgb(0.3, 0.25, 0.25)
    links = ["Bridal Packages", "Makeovers", "Hair & Spa", "Portfolio", "Testimonials"]
    for i, link in enumerate(links):
        ctx.move_to(560 + i * 110, 86)
        ctx.show_text(link)
        
    # Book Button
    ctx.set_source_rgb(0.78, 0.25, 0.35)
    ctx.rectangle(WIDTH - 180, 62, 120, 36)
    ctx.fill()
    ctx.set_source_rgb(1, 1, 1)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(12)
    ctx.move_to(WIDTH - 165, 84)
    ctx.show_text("Book Now")
    
    # Hero section - Luxury editorial layout
    # Left Hero Text
    ctx.select_font_face("DejaVu Serif", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_source_rgb(0.78, 0.25, 0.35)
    ctx.set_font_size(13)
    ctx.move_to(80, 180)
    ctx.show_text("CELEBRATING HER HERITAGE & GRACE")
    
    ctx.set_source_rgb(0.18, 0.08, 0.12)
    ctx.set_font_size(44)
    ctx.move_to(80, 240)
    ctx.show_text("Exquisite Bridal")
    ctx.move_to(80, 295)
    ctx.show_text("Artistry & Luxury")
    ctx.move_to(80, 350)
    ctx.show_text("Makeover Studio")
    
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_source_rgb(0.4, 0.35, 0.35)
    ctx.set_font_size(14)
    ctx.move_to(80, 395)
    ctx.show_text("Crafting timeless wedding elegance with premium HD makeup,")
    ctx.move_to(80, 420)
    ctx.show_text("traditional royal mehendi, and signature aesthetic styling.")
    
    # CTA Buttons
    ctx.set_source_rgb(0.78, 0.25, 0.35)
    ctx.rectangle(80, 460, 170, 48)
    ctx.fill()
    ctx.set_source_rgb(1, 1, 1)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(14)
    ctx.move_to(110, 490)
    ctx.show_text("View Gallery  →")
    
    ctx.set_source_rgb(0.35, 0.12, 0.18)
    ctx.rectangle(265, 460, 180, 48)
    ctx.set_line_width(1.5)
    ctx.stroke()
    ctx.move_to(285, 490)
    ctx.show_text("Consult Artist")
    
    # Stats badge
    ctx.set_source_rgba(1, 1, 1, 0.85)
    ctx.rectangle(80, 560, 420, 85)
    ctx.fill()
    stats = [("1,500+", "Weddings Styled"), ("15+", "Years Experience"), ("4.9★", "Google Rating")]
    for i, (num, label) in enumerate(stats):
        ctx.set_source_rgb(0.78, 0.25, 0.35)
        ctx.set_font_size(20)
        ctx.select_font_face("DejaVu Serif", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.move_to(100 + i * 140, 595)
        ctx.show_text(num)
        ctx.set_source_rgb(0.45, 0.4, 0.4)
        ctx.set_font_size(11)
        ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        ctx.move_to(100 + i * 140, 620)
        ctx.show_text(label)

    # Right Hero Cards (Visual Gallery)
    # Main hero card
    ctx.set_source_rgb(0.85, 0.72, 0.70)
    ctx.rectangle(580, 150, 320, 440)
    ctx.fill()
    # Gold border
    ctx.set_source_rgb(0.85, 0.65, 0.35)
    ctx.set_line_width(3)
    ctx.rectangle(590, 160, 300, 420)
    ctx.stroke()
    
    # Internal decorative elements
    ctx.set_source_rgb(0.45, 0.15, 0.22)
    ctx.select_font_face("DejaVu Serif", cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(24)
    ctx.move_to(630, 360)
    ctx.show_text("The Royal Bride")
    ctx.set_font_size(13)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.move_to(650, 390)
    ctx.show_text("Signature Couture 2026")
    
    # Secondary floating card
    ctx.set_source_rgb(0.95, 0.9, 0.88)
    ctx.rectangle(930, 220, 270, 360)
    ctx.fill()
    ctx.set_source_rgb(0.8, 0.6, 0.4)
    ctx.rectangle(940, 230, 250, 340)
    ctx.stroke()
    ctx.set_source_rgb(0.35, 0.12, 0.18)
    ctx.select_font_face("DejaVu Serif", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(18)
    ctx.move_to(960, 380)
    ctx.show_text("Bridal Mehndi & Spa")
    ctx.set_font_size(12)
    ctx.set_source_rgb(0.5, 0.4, 0.4)
    ctx.move_to(960, 410)
    ctx.show_text("Organic henna & treatments")
    
    # Bottom banner / ticker
    ctx.set_source_rgb(0.35, 0.12, 0.18)
    ctx.rectangle(0, 720, WIDTH, 80)
    ctx.fill()
    ctx.set_source_rgb(0.95, 0.85, 0.75)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(14)
    ctx.move_to(80, 765)
    ctx.show_text("✦ LUXURY HD BRIDAL MAKEUP   ✦ MEHENDI CEREMONY   ✦ PRE-WEDDING SKINCARE   ✦ HAIRSTYLING MASTERCLASS")
    
    draw_browser_chrome(ctx, "Kaveri Bridal & Beauty Studio", "kaveri-bridal.studio")
    surf.write_to_png(filename)
    print("Saved", filename)

# 2. CarePlus Clinic
def render_careplus(filename):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surf)
    
    # Background clean clinical white/slate
    ctx.set_source_rgb(0.97, 0.98, 0.99)
    ctx.rectangle(0, 48, WIDTH, HEIGHT - 48)
    ctx.fill()
    
    # Header
    ctx.set_source_rgb(1, 1, 1)
    ctx.rectangle(0, 48, WIDTH, 70)
    ctx.fill()
    ctx.set_source_rgb(0.88, 0.91, 0.95)
    ctx.set_line_width(1)
    ctx.move_to(0, 118)
    ctx.line_to(WIDTH, 118)
    ctx.stroke()
    
    # Logo
    ctx.set_source_rgb(0.08, 0.45, 0.82)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(24)
    ctx.move_to(80, 92)
    ctx.show_text("CarePlus")
    ctx.set_source_rgb(0.12, 0.72, 0.55)
    ctx.show_text("+")
    ctx.set_source_rgb(0.4, 0.45, 0.52)
    ctx.set_font_size(11)
    ctx.move_to(200, 92)
    ctx.show_text("MULTISPECIALTY MEDICAL CLINIC")
    
    # Menu
    ctx.set_font_size(13)
    ctx.set_source_rgb(0.3, 0.35, 0.42)
    menu = ["Specialties", "Doctors", "Diagnostics", "Online Booking", "Emergency"]
    for i, item in enumerate(menu):
        ctx.move_to(560 + i * 115, 90)
        ctx.show_text(item)
        
    ctx.set_source_rgb(0.08, 0.45, 0.82)
    ctx.rectangle(WIDTH - 190, 64, 130, 38)
    ctx.fill()
    ctx.set_source_rgb(1, 1, 1)
    ctx.move_to(WIDTH - 170, 88)
    ctx.show_text("Call 24/7 OPD")
    
    # Hero section
    ctx.set_source_rgb(0.08, 0.45, 0.82)
    ctx.rectangle(80, 150, 140, 26)
    ctx.fill()
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(11)
    ctx.move_to(92, 167)
    ctx.show_text("NABH ACCREDITED")
    
    ctx.set_source_rgb(0.08, 0.15, 0.25)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(42)
    ctx.move_to(80, 230)
    ctx.show_text("Compassionate Care,")
    ctx.move_to(80, 285)
    ctx.show_text("Advanced Medicine.")
    
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_source_rgb(0.38, 0.42, 0.48)
    ctx.set_font_size(15)
    ctx.move_to(80, 335)
    ctx.show_text("Complete family healthcare, pediatric diagnostics, cardiology,")
    ctx.move_to(80, 360)
    ctx.show_text("and digital patient records with zero wait time.")
    
    # Search / Quick appointment bar
    ctx.set_source_rgb(1, 1, 1)
    ctx.rectangle(80, 400, 520, 60)
    ctx.fill()
    ctx.set_source_rgb(0.85, 0.88, 0.92)
    ctx.rectangle(80, 400, 520, 60)
    ctx.stroke()
    ctx.set_source_rgb(0.5, 0.55, 0.6)
    ctx.set_font_size(13)
    ctx.move_to(110, 436)
    ctx.show_text("🔍 Find specialty, doctor, or health checkup...")
    ctx.set_source_rgb(0.12, 0.72, 0.55)
    ctx.rectangle(480, 410, 110, 40)
    ctx.fill()
    ctx.set_source_rgb(1, 1, 1)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(505, 435)
    ctx.show_text("Search")
    
    # 3 Service Cards on Right
    cards = [
        ("Cardiology & Heart Care", "Comprehensive ECG, 2D Echo & preventive screenings.", (0.9, 0.95, 1.0), (0.08, 0.45, 0.82)),
        ("Pediatrics & Wellness", "Vaccinations, newborn care & child nutrition clinic.", (0.92, 0.98, 0.95), (0.12, 0.72, 0.55)),
        ("Digital Diagnostics Lab", "Fully automated lab with same-day digital reports.", (0.98, 0.95, 0.92), (0.9, 0.45, 0.15))
    ]
    for i, (head, desc, bg, acc) in enumerate(cards):
        cy = 160 + i * 140
        ctx.set_source_rgb(*bg)
        ctx.rectangle(660, cy, 540, 120)
        ctx.fill()
        ctx.set_source_rgb(*acc)
        ctx.rectangle(660, cy, 6, 120)
        ctx.fill()
        
        ctx.set_source_rgb(0.1, 0.15, 0.22)
        ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(17)
        ctx.move_to(690, cy + 45)
        ctx.show_text(head)
        
        ctx.set_source_rgb(0.35, 0.4, 0.45)
        ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        ctx.set_font_size(13)
        ctx.move_to(690, cy + 78)
        ctx.show_text(desc)
        
        ctx.set_source_rgb(*acc)
        ctx.set_font_size(12)
        ctx.move_to(1110, cy + 65)
        ctx.show_text("Book →")
        
    # Doctor stats panel
    ctx.set_source_rgb(0.08, 0.15, 0.25)
    ctx.rectangle(80, 520, 520, 160)
    ctx.fill()
    ctx.set_source_rgb(1, 1, 1)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(16)
    ctx.move_to(110, 560)
    ctx.show_text("Need Immediate Medical Assistance?")
    ctx.set_source_rgb(0.75, 0.8, 0.88)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(13)
    ctx.move_to(110, 590)
    ctx.show_text("Our on-call medical staff and triage team are ready.")
    ctx.set_source_rgb(0.12, 0.72, 0.55)
    ctx.set_font_size(20)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(110, 640)
    ctx.show_text("📞 +91 98400 12345 / 044-2456-7890")
    
    draw_browser_chrome(ctx, "CarePlus Clinic - Multispecialty Healthcare", "careplusclinic.org")
    surf.write_to_png(filename)
    print("Saved", filename)

# 3. Taste & Thyme
def render_taste_thyme(filename):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surf)
    
    # Warm dark gourmet atmosphere
    ctx.set_source_rgb(0.08, 0.07, 0.06)
    ctx.rectangle(0, 48, WIDTH, HEIGHT - 48)
    ctx.fill()
    
    # Navigation
    ctx.set_source_rgba(0.12, 0.1, 0.09, 0.8)
    ctx.rectangle(0, 48, WIDTH, 75)
    ctx.fill()
    
    ctx.set_source_rgb(0.94, 0.78, 0.45) # Gold/Amber
    ctx.select_font_face("DejaVu Serif", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(24)
    ctx.move_to(80, 95)
    ctx.show_text("TASTE & THYME")
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(10)
    ctx.set_source_rgb(0.7, 0.65, 0.6)
    ctx.move_to(280, 95)
    ctx.show_text("ARTISAN BISTRO & BOTANICAL CAFE")
    
    nav = ["Seasonal Menu", "Farm-to-Table", "Private Dining", "Wine Cellar", "Reservations"]
    ctx.set_font_size(13)
    for i, n in enumerate(nav):
        ctx.move_to(600 + i * 110, 93)
        ctx.show_text(n)
        
    ctx.set_source_rgb(0.94, 0.78, 0.45)
    ctx.rectangle(WIDTH - 170, 68, 110, 36)
    ctx.fill()
    ctx.set_source_rgb(0.1, 0.08, 0.05)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(12)
    ctx.move_to(WIDTH - 150, 90)
    ctx.show_text("Reserve Table")
    
    # Left Hero Text
    ctx.set_source_rgb(0.94, 0.78, 0.45)
    ctx.set_font_size(13)
    ctx.move_to(80, 185)
    ctx.show_text("ELEVATED GASTRONOMY • SUSTAINABLE SOURCING")
    
    ctx.set_source_rgb(0.96, 0.94, 0.9)
    ctx.select_font_face("DejaVu Serif", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(46)
    ctx.move_to(80, 245)
    ctx.show_text("Flavors Forged in")
    ctx.move_to(80, 305)
    ctx.show_text("Nature's Finest Hearth")
    
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_source_rgb(0.7, 0.68, 0.65)
    ctx.set_font_size(15)
    ctx.move_to(80, 360)
    ctx.show_text("An intimate culinary experience marrying wood-fired botanical")
    ctx.move_to(80, 385)
    ctx.show_text("infusions, heritage sourdough, and hand-crafted pairings.")
    
    # Buttons
    ctx.set_source_rgb(0.94, 0.78, 0.45)
    ctx.rectangle(80, 430, 170, 48)
    ctx.fill()
    ctx.set_source_rgb(0.1, 0.08, 0.05)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(13)
    ctx.move_to(105, 460)
    ctx.show_text("Explore Menu ➔")
    
    ctx.set_source_rgb(0.94, 0.78, 0.45)
    ctx.rectangle(265, 430, 170, 48)
    ctx.stroke()
    ctx.move_to(285, 460)
    ctx.show_text("Chef's Story")
    
    # Menu Highlights Grid
    dishes = [
        ("Truffle & Forest Thyme Tart", "Smoked chanterelles, goat cheese crème, organic thyme oil", "$24"),
        ("Ember-Roasted Heritage Lamb", "Parsnip velvet, blackberry reduction, garden rosemary", "$38"),
        ("Wild Berry Lavender Pavlova", "Cardamom chantilly, candied citrus peel, local honey", "$16")
    ]
    for i, (title, sub, price) in enumerate(dishes):
        dx = 640
        dy = 180 + i * 130
        ctx.set_source_rgb(0.14, 0.12, 0.11)
        ctx.rectangle(dx, dy, 560, 110)
        ctx.fill()
        ctx.set_source_rgb(0.25, 0.2, 0.17)
        ctx.rectangle(dx, dy, 560, 110)
        ctx.stroke()
        
        ctx.set_source_rgb(0.94, 0.78, 0.45)
        ctx.select_font_face("DejaVu Serif", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(17)
        ctx.move_to(dx + 25, dy + 42)
        ctx.show_text(title)
        
        ctx.set_source_rgb(0.94, 0.78, 0.45)
        ctx.move_to(dx + 490, dy + 42)
        ctx.show_text(price)
        
        ctx.set_source_rgb(0.65, 0.62, 0.58)
        ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        ctx.set_font_size(12)
        ctx.move_to(dx + 25, dy + 75)
        ctx.show_text(sub)
        
    # Bottom quotes
    ctx.set_source_rgb(0.94, 0.78, 0.45)
    ctx.select_font_face("DejaVu Serif", cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(14)
    ctx.move_to(80, 560)
    ctx.show_text('"An ethereal dining landmark where rustic simplicity meets culinary poetry." — Michelin Guide Review')
    
    draw_browser_chrome(ctx, "Taste & Thyme | Fine Artisan Bistro", "tasteandthyme.dining")
    surf.write_to_png(filename)
    print("Saved", filename)

# 4. Haven Properties
def render_haven(filename):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surf)
    
    # Clean warm modern luxury architectural style
    ctx.set_source_rgb(0.94, 0.94, 0.92)
    ctx.rectangle(0, 48, WIDTH, HEIGHT - 48)
    ctx.fill()
    
    # Header
    ctx.set_source_rgb(0.12, 0.14, 0.16)
    ctx.rectangle(0, 48, WIDTH, 75)
    ctx.fill()
    
    ctx.set_source_rgb(0.92, 0.92, 0.9)
    ctx.select_font_face("DejaVu Serif", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(24)
    ctx.move_to(80, 95)
    ctx.show_text("HAVEN")
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(11)
    ctx.set_source_rgb(0.6, 0.75, 0.7)
    ctx.move_to(190, 95)
    ctx.show_text("LUXURY RESIDENTIAL & ESTATES")
    
    nav = ["Estates", "Penthouse Living", "Private Island", "Development", "Advisory"]
    ctx.set_font_size(13)
    ctx.set_source_rgb(0.8, 0.85, 0.88)
    for i, n in enumerate(nav):
        ctx.move_to(560 + i * 115, 93)
        ctx.show_text(n)
        
    ctx.set_source_rgb(0.2, 0.48, 0.42) # Forest Emerald
    ctx.rectangle(WIDTH - 180, 68, 120, 36)
    ctx.fill()
    ctx.set_source_rgb(1, 1, 1)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(12)
    ctx.move_to(WIDTH - 162, 90)
    ctx.show_text("Private Inquiry")
    
    # Left Hero Text
    ctx.set_source_rgb(0.2, 0.48, 0.42)
    ctx.set_font_size(12)
    ctx.move_to(80, 180)
    ctx.show_text("ARCHITECTURAL EXCELLENCE • PRIME GLOBAL LOCATIONS")
    
    ctx.set_source_rgb(0.12, 0.15, 0.18)
    ctx.select_font_face("DejaVu Serif", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(44)
    ctx.move_to(80, 240)
    ctx.show_text("Sanctuaries of")
    ctx.move_to(80, 295)
    ctx.show_text("Timeless Distinction.")
    
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_source_rgb(0.35, 0.38, 0.42)
    ctx.set_font_size(15)
    ctx.move_to(80, 345)
    ctx.show_text("Curating the most extraordinary residences, waterfront villas,")
    ctx.move_to(80, 370)
    ctx.show_text("and private retreats for discerning collectors worldwide.")
    
    # Search Box
    ctx.set_source_rgb(1, 1, 1)
    ctx.rectangle(80, 420, 480, 64)
    ctx.fill()
    ctx.set_source_rgb(0.8, 0.82, 0.85)
    ctx.rectangle(80, 420, 480, 64)
    ctx.stroke()
    ctx.set_source_rgb(0.5, 0.55, 0.6)
    ctx.set_font_size(13)
    ctx.move_to(105, 458)
    ctx.show_text("Location, Villa Style, or Price Range...")
    ctx.set_source_rgb(0.2, 0.48, 0.42)
    ctx.rectangle(440, 430, 110, 44)
    ctx.fill()
    ctx.set_source_rgb(1, 1, 1)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(465, 458)
    ctx.show_text("Explore")
    
    # Property Showcase Cards on Right
    props = [
        ("The Glass Pavilion, Bel Air", "6 Beds • 9 Baths • 14,200 sq.ft • $28,500,000", (0.2, 0.22, 0.25)),
        ("Azure Cliffside Villa, Amalfi", "5 Beds • Infinity Horizon Pool • €19,800,000", (0.28, 0.32, 0.35)),
        ("Skyline Crown Penthouse, London", "Duplex • Private Helipad • £22,000,000", (0.18, 0.26, 0.28))
    ]
    for i, (title, meta, bg) in enumerate(props):
        px = 620
        py = 160 + i * 165
        ctx.set_source_rgb(*bg)
        ctx.rectangle(px, py, 580, 145)
        ctx.fill()
        
        ctx.set_source_rgb(0.9, 0.8, 0.6)
        ctx.select_font_face("DejaVu Serif", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(18)
        ctx.move_to(px + 30, py + 50)
        ctx.show_text(title)
        
        ctx.set_source_rgb(0.8, 0.85, 0.9)
        ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        ctx.set_font_size(13)
        ctx.move_to(px + 30, py + 85)
        ctx.show_text(meta)
        
        ctx.set_source_rgb(0.6, 0.85, 0.75)
        ctx.set_font_size(12)
        ctx.move_to(px + 30, py + 115)
        ctx.show_text("VIEW ARCHITECTURAL SPECIFICATION ➔")
        
    draw_browser_chrome(ctx, "Haven Properties | Ultra Luxury Real Estate", "havenproperties.estate")
    surf.write_to_png(filename)
    print("Saved", filename)

# 5. Vertex Infra
def render_vertex(filename):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surf)
    
    # Industrial high-tech deep slate background
    ctx.set_source_rgb(0.06, 0.08, 0.11)
    ctx.rectangle(0, 48, WIDTH, HEIGHT - 48)
    ctx.fill()
    
    # Modern grid background lines
    ctx.set_source_rgba(0.15, 0.22, 0.3, 0.4)
    ctx.set_line_width(1)
    for gx in range(0, WIDTH, 80):
        ctx.move_to(gx, 48)
        ctx.line_to(gx, HEIGHT)
        ctx.stroke()
    for gy in range(48, HEIGHT, 80):
        ctx.move_to(0, gy)
        ctx.line_to(WIDTH, gy)
        ctx.stroke()
        
    # Header
    ctx.set_source_rgba(0.08, 0.11, 0.15, 0.9)
    ctx.rectangle(0, 48, WIDTH, 75)
    ctx.fill()
    
    ctx.set_source_rgb(0.95, 0.45, 0.12) # High-vis industrial orange
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(24)
    ctx.move_to(80, 95)
    ctx.show_text("VERTEX")
    ctx.set_source_rgb(0.8, 0.85, 0.9)
    ctx.show_text(" INFRA")
    
    nav = ["Civil Engineering", "Mega Structures", "Green Energy", "BIM & Smart Cities", "Investors"]
    ctx.set_font_size(13)
    ctx.set_source_rgb(0.7, 0.78, 0.85)
    for i, n in enumerate(nav):
        ctx.move_to(540 + i * 115, 93)
        ctx.show_text(n)
        
    ctx.set_source_rgb(0.95, 0.45, 0.12)
    ctx.rectangle(WIDTH - 180, 68, 120, 36)
    ctx.fill()
    ctx.set_source_rgb(1, 1, 1)
    ctx.move_to(WIDTH - 165, 90)
    ctx.show_text("Project Portal")
    
    # Left Hero Text
    ctx.set_source_rgb(0.95, 0.45, 0.12)
    ctx.set_font_size(12)
    ctx.move_to(80, 185)
    ctx.show_text("TIER-1 INFRASTRUCTURE & CAPITAL PROJECTS")
    
    ctx.set_source_rgb(0.95, 0.97, 1.0)
    ctx.set_font_size(44)
    ctx.move_to(80, 245)
    ctx.show_text("Engineering the Next")
    ctx.move_to(80, 305)
    ctx.show_text("Century's Skyline.")
    
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_source_rgb(0.65, 0.72, 0.8)
    ctx.set_font_size(15)
    ctx.move_to(80, 360)
    ctx.show_text("From high-speed transit corridors to carbon-neutral smart cities,")
    ctx.move_to(80, 385)
    ctx.show_text("Vertex delivers heavy civil engineering with unmatched precision.")
    
    # Metric Counters
    stats = [("$4.2B+", "Active Projects"), ("350km", "High-Speed Rail"), ("100%", "Safety Compliance")]
    for i, (m, lbl) in enumerate(stats):
        bx = 80 + i * 165
        ctx.set_source_rgb(0.12, 0.16, 0.22)
        ctx.rectangle(bx, 440, 150, 80)
        ctx.fill()
        ctx.set_source_rgb(0.95, 0.45, 0.12)
        ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(22)
        ctx.move_to(bx + 15, 475)
        ctx.show_text(m)
        ctx.set_source_rgb(0.7, 0.75, 0.82)
        ctx.set_font_size(11)
        ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        ctx.move_to(bx + 15, 502)
        ctx.show_text(lbl)
        
    # Interactive Project Blueprint Right Box
    ctx.set_source_rgb(0.1, 0.14, 0.2)
    ctx.rectangle(630, 160, 570, 480)
    ctx.fill()
    ctx.set_source_rgb(0.95, 0.45, 0.12)
    ctx.set_line_width(2)
    ctx.rectangle(630, 160, 570, 480)
    ctx.stroke()
    
    ctx.set_source_rgb(0.95, 0.97, 1.0)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(20)
    ctx.move_to(660, 210)
    ctx.show_text("Project Polaris: 12-Lane Smart Expressway")
    
    ctx.set_source_rgb(0.65, 0.72, 0.8)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(13)
    ctx.move_to(660, 240)
    ctx.show_text("BIM Level 3 • Real-time IoT sensor telemetry • Automated Toll Grid")
    
    # Schematic visuals
    ctx.set_source_rgba(0.2, 0.35, 0.5, 0.6)
    ctx.set_line_width(1.5)
    for l in range(5):
        ctx.move_to(660, 280 + l * 40)
        ctx.line_to(1170, 280 + l * 40)
        ctx.stroke()
        
    ctx.set_source_rgb(0.95, 0.45, 0.12)
    ctx.set_font_size(13)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(660, 520)
    ctx.show_text("STATUS: COMMISSIONING PHASE 2 (92% COMPLETE)")
    
    ctx.set_source_rgb(0.15, 0.75, 0.45)
    ctx.rectangle(660, 545, 450, 14)
    ctx.fill()
    ctx.set_source_rgb(0.25, 0.35, 0.45)
    ctx.rectangle(1110, 545, 40, 14)
    ctx.fill()
    
    draw_browser_chrome(ctx, "Vertex Infra | Global Heavy Infrastructure", "vertexinfra.build")
    surf.write_to_png(filename)
    print("Saved", filename)

# 6. StockFlow
def render_stockflow(filename):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surf)
    
    # SaaS Dashboard dark/sleek theme
    ctx.set_source_rgb(0.07, 0.08, 0.11)
    ctx.rectangle(0, 48, WIDTH, HEIGHT - 48)
    ctx.fill()
    
    # Sidebar
    ctx.set_source_rgb(0.1, 0.12, 0.16)
    ctx.rectangle(0, 48, 220, HEIGHT - 48)
    ctx.fill()
    
    ctx.set_source_rgb(0.35, 0.55, 0.98) # Electric SaaS Blue
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(20)
    ctx.move_to(25, 95)
    ctx.show_text("StockFlow")
    
    # Sidebar items
    items = ["📊 Live Dashboard", "📦 Inventory Ledger", "🚚 Multi-Warehouse", "🤖 AI Demand Forecast", "📑 Invoicing & GST", "⚙️ Integration API"]
    ctx.set_font_size(12)
    for i, itm in enumerate(items):
        if i == 0:
            ctx.set_source_rgb(0.18, 0.24, 0.35)
            ctx.rectangle(12, 130 + i * 44, 196, 36)
            ctx.fill()
            ctx.set_source_rgb(0.35, 0.55, 0.98)
        else:
            ctx.set_source_rgb(0.65, 0.7, 0.78)
        ctx.move_to(25, 154 + i * 44)
        ctx.show_text(itm)
        
    # Top bar
    ctx.set_source_rgb(0.1, 0.12, 0.16)
    ctx.rectangle(220, 48, WIDTH - 220, 60)
    ctx.fill()
    
    ctx.set_source_rgb(0.9, 0.92, 0.95)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(16)
    ctx.move_to(250, 84)
    ctx.show_text("Enterprise Inventory Intelligence")
    
    ctx.set_source_rgb(0.35, 0.55, 0.98)
    ctx.rectangle(WIDTH - 180, 62, 130, 34)
    ctx.fill()
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(12)
    ctx.move_to(WIDTH - 165, 84)
    ctx.show_text("+ New Shipment")
    
    # Dashboard KPI Cards
    kpis = [
        ("Total SKU Value", "$12,480,290", "+14.2% vs last mo", (0.15, 0.75, 0.45)),
        ("Low Stock Alerts", "14 Items", "Action Required", (0.95, 0.45, 0.15)),
        ("Fulfillment Rate", "99.84%", "Auto-dispatched", (0.35, 0.55, 0.98)),
        ("Turnover Ratio", "8.4x", "Industry top 5%", (0.7, 0.45, 0.95))
    ]
    for i, (head, val, sub, col) in enumerate(kpis):
        kx = 250 + i * 240
        ctx.set_source_rgb(0.13, 0.15, 0.20)
        ctx.rectangle(kx, 130, 225, 110)
        ctx.fill()
        
        ctx.set_source_rgb(0.65, 0.7, 0.78)
        ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        ctx.set_font_size(11)
        ctx.move_to(kx + 16, 158)
        ctx.show_text(head)
        
        ctx.set_source_rgb(0.95, 0.97, 1.0)
        ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(20)
        ctx.move_to(kx + 16, 192)
        ctx.show_text(val)
        
        ctx.set_source_rgb(*col)
        ctx.set_font_size(10)
        ctx.move_to(kx + 16, 220)
        ctx.show_text(sub)
        
    # Real-time Table / Chart Area
    ctx.set_source_rgb(0.13, 0.15, 0.20)
    ctx.rectangle(250, 265, 960, 460)
    ctx.fill()
    
    ctx.set_source_rgb(0.95, 0.97, 1.0)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(16)
    ctx.move_to(275, 305)
    ctx.show_text("Automated Reorder Pipeline & Real-Time Logistics")
    
    # Table header
    ctx.set_source_rgb(0.18, 0.22, 0.28)
    ctx.rectangle(275, 330, 910, 36)
    ctx.fill()
    ctx.set_source_rgb(0.7, 0.75, 0.82)
    ctx.set_font_size(12)
    cols = [(290, "BATCH ID"), (420, "PRODUCT DESCRIPTION"), (640, "DEPOT LOCATION"), (790, "STOCK LEVEL"), (940, "STATUS")]
    for cx, ch in cols:
        ctx.move_to(cx, 353)
        ctx.show_text(ch)
        
    # Table rows
    rows = [
        ("BT-9902-A", "High-Torque Servo Stepper X4", "Rotterdam Hub Alpha", "4,200 / 5,000", "In Stock (Optimal)"),
        ("BT-9844-C", "Lithium Polymer Pack 48V", "Singapore Bay 2", "120 / 2,500", "Reorder Triggered"),
        ("BT-9712-F", "Optical Transceiver 100G", "Dallas North Logistics", "1,850 / 2,000", "In Stock (Optimal)"),
        ("BT-9605-B", "Titanium Alloy Rod 12mm", "Tokyo Haneda Dep.", "3,400 / 3,500", "In Transit"),
        ("BT-9520-K", "Precision Ceramic Bearing 8mm", "Frankfurt Central", "890 / 1,000", "In Stock (Optimal)")
    ]
    for r_idx, r in enumerate(rows):
        ry = 380 + r_idx * 52
        ctx.set_source_rgb(0.15, 0.18, 0.23)
        ctx.rectangle(275, ry, 910, 42)
        ctx.fill()
        
        ctx.set_source_rgb(0.85, 0.88, 0.92)
        ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        ctx.set_font_size(12)
        ctx.move_to(290, ry + 26)
        ctx.show_text(r[0])
        ctx.move_to(420, ry + 26)
        ctx.show_text(r[1])
        ctx.move_to(640, ry + 26)
        ctx.show_text(r[2])
        ctx.move_to(790, ry + 26)
        ctx.show_text(r[3])
        
        if "Triggered" in r[4]:
            ctx.set_source_rgb(0.95, 0.45, 0.15)
        elif "Transit" in r[4]:
            ctx.set_source_rgb(0.35, 0.55, 0.98)
        else:
            ctx.set_source_rgb(0.15, 0.75, 0.45)
        ctx.move_to(940, ry + 26)
        ctx.show_text("● " + r[4])
        
    draw_browser_chrome(ctx, "StockFlow SaaS | Real-time Inventory Automation", "app.stockflow.io")
    surf.write_to_png(filename)
    print("Saved", filename)

if __name__ == "__main__":
    render_kaveri("assets/images/projects/kaveri-bridal.png")
    render_careplus("assets/images/projects/careplus-clinic.png")
    render_taste_thyme("assets/images/projects/taste-thyme.png")
    render_haven("assets/images/projects/haven-properties.png")
    render_vertex("assets/images/projects/vertex-infra.png")
    render_stockflow("assets/images/projects/stockflow.png")
