from PIL import Image, ImageDraw, ImageFont
import os

def get_font(size, bold=False):
    paths = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNS.ttf"
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def render_master_architecture():
    w, h = 1024, 1024
    img = Image.new("RGBA", (w, h), (18, 15, 12, 255))
    draw = ImageDraw.Draw(img)

    font_title = get_font(28, bold=True)
    font_sub = get_font(17)
    font_section = get_font(15, bold=True)
    font_card_title = get_font(15, bold=True)
    font_card_body = get_font(13)
    font_vertical = get_font(13, bold=True)

    # Title
    draw.text((w/2, 45), "Project AURA | Master Technical Architecture", fill=(245, 197, 115), font=font_title, anchor="mm")
    draw.text((w/2, 80), "(Anticipatory Unified Real-time AI for Advanced Manufacturing)", fill=(210, 195, 180), font=font_sub, anchor="mm")

    # Left vertical labels (positioned correctly to avoid overlaps)
    draw.text((38, 280), "TOP LEVEL", fill=(245, 197, 115), font=font_vertical, anchor="mm")
    draw.text((38, 495), "MIDDLE BARRIER", fill=(245, 197, 115), font=font_vertical, anchor="mm")
    draw.text((38, 790), "BOTTOM LEVEL", fill=(245, 197, 115), font=font_vertical, anchor="mm")

    # 1. TOP LEVEL BOX (FEDERATED LEVEL)
    draw.rounded_rectangle((75, 160, 975, 405), radius=12, fill=(28, 22, 16, 255), outline=(215, 145, 60), width=2)
    draw.rounded_rectangle((95, 172, 955, 205), radius=6, fill=(15, 12, 10, 255))
    draw.text((525, 188), "FEDERATED LEVEL (Gaia-X Sovereign Cloud 24/7 & EuroHPC)", fill=(248, 250, 252), font=font_section, anchor="mm")

    # Top level Cards
    # Card 1: Layer 1
    draw.rounded_rectangle((98, 218, 290, 390), radius=10, fill=(195, 133, 40, 255), outline=(235, 175, 80), width=1)
    draw.text((194, 295), "Layer 1:\nCore Ontology\nISA-95", fill=(15, 12, 10), font=font_card_title, anchor="mm", align="center")

    # Card 2: Layer 2
    draw.rounded_rectangle((310, 218, 520, 390), radius=10, fill=(184, 92, 55, 255), outline=(225, 125, 85), width=1)
    draw.text((415, 295), "Layer 2:\nTrack B Domain\nOracles\n(HACCP/EFSA, REACH/CLP)", fill=(248, 250, 252), font=font_card_title, anchor="mm", align="center")

    # Card 3: EuroHPC BSC
    draw.rounded_rectangle((540, 218, 735, 390), radius=10, fill=(45, 32, 22, 255), outline=(180, 130, 80), width=1)
    draw.text((637, 295), "EuroHPC BSC\nMareNostrum V\nLLM Training", fill=(248, 250, 252), font=font_card_title, anchor="mm", align="center")

    # Card 4: MLOps Pipeline
    draw.rounded_rectangle((780, 218, 955, 390), radius=10, fill=(175, 95, 65, 255), outline=(215, 135, 105), width=1)
    draw.text((867, 295), "MLOps\nPipeline", fill=(248, 250, 252), font=font_card_title, anchor="mm", align="center")

    # 2. MIDDLE BARRIER (SOVEREIGNTY BOUNDARY)
    # Track A Oracles card left
    draw.rounded_rectangle((98, 440, 250, 505), radius=8, fill=(160, 85, 50, 255))
    draw.text((174, 472), "Track A Oracles\nPlant Integrators\n(Vicky Foods & AKCOAT)", fill=(248, 250, 252), font=font_card_body, anchor="mm", align="center")

    # Center Sovereignty Line
    draw.line([(75, 510), (975, 510)], fill=(225, 29, 72, 255), width=3)
    draw.rounded_rectangle((285, 492, 715, 528), radius=6, fill=(20, 16, 12, 255), outline=(225, 29, 72, 255), width=1)
    draw.text((500, 510), "ABSOLUTE DATA SOVEREIGNTY BOUNDARY", fill=(255, 255, 255), font=font_section, anchor="mm")

    # Right warning
    draw.text((865, 450), "Track B Oracles", fill=(230, 210, 190), font=font_card_body, anchor="mm")
    draw.text((865, 545), "Raw plant data\nNEVER leaves factory", fill=(255, 120, 120), font=font_card_body, anchor="mm", align="center")

    # 3. BOTTOM LEVEL BOX (LOCAL LEVEL)
    draw.rounded_rectangle((75, 610, 975, 975), radius=12, fill=(28, 22, 16, 255), outline=(215, 145, 60), width=2)
    draw.rounded_rectangle((285, 622, 715, 655), radius=6, fill=(15, 12, 10, 255))
    draw.text((500, 638), "LOCAL LEVEL (Factory Edge - TRL 5)", fill=(248, 250, 252), font=font_section, anchor="mm")

    # Bottom Level Cards
    # Factory GPU Server
    draw.rounded_rectangle((98, 675, 195, 955), radius=10, fill=(45, 32, 22, 255), outline=(160, 120, 80), width=1)
    draw.text((146, 815), "Factory\nGPU Server", fill=(248, 250, 252), font=font_card_title, anchor="mm", align="center")

    # Layer 3 Knowledge Graph
    draw.rounded_rectangle((215, 675, 420, 955), radius=10, fill=(35, 26, 18, 255), outline=(215, 145, 60), width=1)
    draw.text((317, 815), "Layer 3:\nPrivate Local\nKnowledge Graph\n(SOPs & Sensor Logs)", fill=(248, 250, 252), font=font_card_title, anchor="mm", align="center")

    # 4-Agent Cognitive Engine
    draw.rounded_rectangle((440, 675, 660, 955), radius=10, fill=(35, 26, 18, 255), outline=(215, 145, 60), width=1)
    draw.text((550, 695), "4-Agent Cognitive Engine", fill=(248, 250, 252), font=font_card_title, anchor="mm")
    
    # Sub-agents
    draw.rounded_rectangle((455, 720, 645, 760), radius=6, fill=(235, 125, 85, 255))
    draw.text((550, 740), "Router", fill=(15, 12, 10), font=font_card_title, anchor="mm")

    draw.rounded_rectangle((455, 775, 645, 815), radius=6, fill=(245, 165, 125, 255))
    draw.text((550, 795), "Dual Graph-RAG", fill=(15, 12, 10), font=font_card_title, anchor="mm")

    draw.rounded_rectangle((455, 830, 645, 880), radius=6, fill=(255, 185, 155, 255))
    draw.text((550, 855), "Explainable Analyst\nEU AI Act", fill=(15, 12, 10), font=font_card_body, anchor="mm", align="center")

    draw.rounded_rectangle((455, 895, 645, 935), radius=6, fill=(245, 165, 125, 255))
    draw.text((550, 915), "Evaluator Judge", fill=(15, 12, 10), font=font_card_title, anchor="mm")

    # Workflow loop right
    draw.rounded_rectangle((680, 675, 955, 955), radius=10, fill=(35, 26, 18, 255), outline=(160, 120, 80), width=1)
    draw.text((817, 695), "Human-in-the-Loop\nClosed-Loop Workflow", fill=(248, 250, 252), font=font_card_title, anchor="mm", align="center")

    draw.rounded_rectangle((740, 735, 895, 770), radius=6, fill=(245, 197, 115, 255))
    draw.text((817, 752), "1. Predict >2h", fill=(15, 12, 10), font=font_card_title, anchor="mm")

    draw.rounded_rectangle((695, 800, 790, 845), radius=6, fill=(245, 197, 115, 255))
    draw.text((742, 822), "2. Explain\n& Guide", fill=(15, 12, 10), font=font_card_body, anchor="mm", align="center")

    draw.rounded_rectangle((840, 800, 940, 845), radius=6, fill=(225, 125, 85, 255))
    draw.text((890, 822), "3. Operator\nAction", fill=(15, 12, 10), font=font_card_body, anchor="mm", align="center")

    draw.rounded_rectangle((740, 880, 895, 925), radius=6, fill=(245, 197, 115, 255))
    draw.text((817, 902), "4. Knowledge\nGraph Learning", fill=(15, 12, 10), font=font_card_body, anchor="mm", align="center")

    img.save("aura_master_architecture.png")
    print("Rendered clean English aura_master_architecture.png")

render_master_architecture()
