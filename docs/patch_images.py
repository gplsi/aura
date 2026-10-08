from PIL import Image, ImageDraw, ImageFont
import os

# Helper to load system fonts
def get_font(size):
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNS.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf"
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except Exception:
                pass
    return ImageFont.load_default()

def patch_master_architecture(filename):
    if not os.path.exists(filename):
        return
    img = Image.open(filename).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, h = img.size

    # Background color samples from the image:
    # Header dark banner: #16120e / #1e1914 / #181410
    # Yellow card header/bg: #c9882a / #3d2a10
    # Orange card header/bg: #b85c37 / #3d2015
    # Red line background: #181410
    # Bottom card header/bg: #16120e / #2e1c14

    # 1. 'NIVEL FEDERADO (Gaia-X Sovereign Cloud 24/7 & EuroHPC)'
    # Top banner area: y ~ 170..210, x ~ 190..830
    draw.rectangle([(195, 175), (830, 205)], fill=(22, 18, 14, 255))
    font_top = get_font(18)
    draw.text((512, 190), "FEDERATED LEVEL (Gaia-X Sovereign Cloud 24/7 & EuroHPC)", fill=(248, 250, 252), font=font_top, anchor="mm")

    # 2. 'Capa 1:' inside yellow box (x ~ 125..255, y ~ 290..315)
    draw.rectangle([(125, 292), (255, 314)], fill=(195, 133, 40, 255))
    font_capa = get_font(18)
    draw.text((190, 303), "Layer 1:", fill=(15, 12, 10), font=font_capa, anchor="mm")

    # 3. 'Capa 2:' inside orange box (x ~ 335..480, y ~ 290..315)
    draw.rectangle([(335, 292), (480, 314)], fill=(184, 92, 55, 255))
    draw.text((407, 303), "Layer 2:", fill=(15, 12, 10), font=font_capa, anchor="mm")

    # 4. 'FRONTERA DE SOBERANÍA ABSOLUTA' across middle red bar (x ~ 285..710, y ~ 485..520)
    draw.rectangle([(290, 488), (705, 516)], fill=(20, 16, 12, 255))
    font_bar = get_font(17)
    draw.text((497, 502), "ABSOLUTE DATA SOVEREIGNTY BOUNDARY", fill=(248, 250, 252), font=font_bar, anchor="mm")

    # 5. 'NIVEL LOCAL (Edge en Planta - TRL 5)' (x ~ 280..710, y ~ 605..640)
    draw.rectangle([(285, 608), (710, 638)], fill=(22, 18, 14, 255))
    draw.text((497, 623), "LOCAL LEVEL (Factory Edge - TRL 5)", fill=(248, 250, 252), font=font_top, anchor="mm")

    # 6. 'Capa 3:' inside bottom left box (x ~ 265..365, y ~ 790..815)
    draw.rectangle([(265, 792), (365, 814)], fill=(22, 18, 14, 255))
    draw.text((315, 803), "Layer 3:", fill=(248, 250, 252), font=font_capa, anchor="mm")

    img.save(filename)
    print(f"Patched {filename} successfully.")

patch_master_architecture("aura_master_architecture.png")
