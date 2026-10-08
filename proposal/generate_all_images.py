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

def draw_tech_blueprint():
    # 1024x1024 Tech Blueprint (Dark Minimalist)
    w, h = 1024, 1024
    img = Image.new("RGBA", (w, h), (18, 15, 12, 255))
    draw = ImageDraw.Draw(img)

    font_title = get_font(28, bold=True)
    font_sub = get_font(17)
    font_section = get_font(16, bold=True)
    font_card_title = get_font(15, bold=True)
    font_card_body = get_font(13)

    # Title
    draw.text((w/2, 45), "AURA THREE-LAYER SOVEREIGN ARCHITECTURE", fill=(245, 197, 115), font=font_title, anchor="mm")
    draw.text((w/2, 80), "Security Meets Scalability — Sovereign Industrial B2B Ecosystem", fill=(210, 195, 180), font=font_sub, anchor="mm")

    # Layer A
    draw.rounded_rectangle((50, 140, 974, 320), radius=12, fill=(28, 22, 16, 255), outline=(215, 145, 60), width=2)
    draw.rounded_rectangle((70, 155, 160, 185), radius=6, fill=(195, 133, 40, 255))
    draw.text((115, 170), "LAYER A", fill=(15, 12, 10), font=font_card_body, anchor="mm")
    draw.text((180, 170), "EUROHPC SUPERCOMPUTING & DATAHUB (BSC MARENOSTRUM V)", fill=(248, 250, 252), font=font_section, anchor="ls")

    draw.text((80, 220), "• MareNostrum V Supercomputing Access: Heavy industrial LLM / SLM fine-tuning & foundation training", fill=(220, 210, 200), font=font_card_body)
    draw.text((80, 250), "• Pan-European Industrial Datahub: Multimodal dataset curation, benchmarking, & open-source weights distribution", fill=(220, 210, 200), font=font_card_body)
    draw.text((80, 280), "• Key Partner Leadership: BSC MareNostrum (WP8 Leader) & Scientific Guidance (UA - WP2)", fill=(245, 197, 115), font=font_card_body)

    # Arrow Down
    draw.line([(512, 320), (512, 360)], fill=(215, 145, 60), width=3)
    draw.polygon([(504, 355), (520, 355), (512, 368)], fill=(215, 145, 60))

    # Layer B
    draw.rounded_rectangle((50, 370, 974, 550), radius=12, fill=(28, 22, 16, 255), outline=(215, 145, 60), width=2)
    draw.rounded_rectangle((70, 385, 160, 415), radius=6, fill=(184, 92, 55, 255))
    draw.text((115, 400), "LAYER B", fill=(255, 255, 255), font=font_card_body, anchor="mm")
    draw.text((180, 400), "24/7 LIVE GAIA-X SOVEREIGN CLOUD & SECTORAL ORACLES", fill=(248, 250, 252), font=font_section, anchor="ls")

    draw.text((80, 450), "• Core ISA-95 Ontology (Layer 1): Standardized industrial hierarchy & data models (INDElab / UvA - WP4)", fill=(220, 210, 200), font=font_card_body)
    draw.text((80, 480), "• Sectoral Oracles Track B (Layer 2): Regulatory & compliance knowledge (HACCP, REACH, CLP, OSHA)", fill=(220, 210, 200), font=font_card_body)
    draw.text((80, 510), "• Gaia-X Sovereign Cloud Infrastructure: 24/7 high-availability MLOps / AIOps pipelines (ESTEN - WP5)", fill=(245, 197, 115), font=font_card_body)

    # Sovereignty Boundary
    draw.line([(30, 590), (994, 590)], fill=(225, 29, 72, 255), width=3)
    draw.rounded_rectangle((180, 572, 844, 608), radius=6, fill=(20, 16, 12, 255), outline=(225, 29, 72, 255), width=1)
    draw.text((512, 590), "ABSOLUTE DATA SOVEREIGNTY BOUNDARY — PLANT TELEMETRY & RAW LOGS NEVER LEAVE FACTORY", fill=(255, 255, 255), font=font_card_body, anchor="mm")

    # Arrow Down
    draw.line([(250, 608), (250, 640)], fill=(225, 29, 72, 255), width=2)
    draw.polygon([(245, 635), (255, 635), (250, 645)], fill=(225, 29, 72, 255))
    draw.text((260, 625), "Unidirectional Downstream Model / API Push", fill=(230, 180, 180), font=get_font(11))

    # Layer C
    draw.rounded_rectangle((50, 650, 974, 980), radius=12, fill=(28, 22, 16, 255), outline=(215, 145, 60), width=2)
    draw.rounded_rectangle((70, 665, 160, 695), radius=6, fill=(160, 85, 50, 255))
    draw.text((115, 680), "LAYER C", fill=(255, 255, 255), font=font_card_body, anchor="mm")
    draw.text((180, 680), "ON-PREMISE INDUSTRIAL EDGE & TRL 5 PILOTS (VICKY FOODS & AKCOAT)", fill=(248, 250, 252), font=font_section, anchor="ls")

    # Pilot Boxes
    draw.rounded_rectangle((70, 715, 500, 840), radius=8, fill=(35, 26, 18, 255), outline=(215, 145, 60), width=1)
    draw.text((85, 735), "Pilot 1: Vicky Foods (Agro-Food / Bakery)", fill=(245, 197, 115), font=font_card_title)
    draw.text((85, 765), "• Continuous industrial bakery line telemetry\n• Viscosity, thermal baking curves & dough sensor logs\n• Real-time operator guidance & quality failure prevention", fill=(220, 210, 200), font=font_card_body)

    draw.rounded_rectangle((520, 715, 954, 840), radius=8, fill=(35, 26, 18, 255), outline=(225, 125, 85), width=1)
    draw.text((535, 735), "Pilot 2: AKCOAT (Chemicals & Materials)", fill=(255, 160, 140), font=font_card_title)
    draw.text((535, 765), "• Ceramic enamel & chemical coatings manufacturing\n• Physico-chemical rheology & thermal curing parameters\n• On-premise Edge GPU server for zero-latency inference", fill=(220, 210, 200), font=font_card_body)

    # Knowledge Graph box
    draw.rounded_rectangle((70, 855, 954, 960), radius=8, fill=(35, 26, 18, 255), outline=(215, 145, 60), width=1)
    draw.text((85, 875), "Private Knowledge Graph (Layer 3) & 4-Agent Cognitive Engine", fill=(248, 250, 252), font=font_card_title)
    draw.text((85, 905), "• Local SOPs, machinery manuals, operator logs & sensor data stored strictly inside factory walls", fill=(220, 210, 200), font=font_card_body)
    draw.text((85, 930), "• 4-Agent Architecture: Router Agent | Dual Graph-RAG | EU AI Act Explainability | Judge Evaluator", fill=(245, 197, 115), font=font_card_body)

    img.save("aura_three_layer_architecture_dark.png")
    print("Rendered aura_three_layer_architecture_dark.png")

def create_dual_projections():
    # Render dark blueprint
    draw_tech_blueprint()
    
    # Open Tech Dark Blueprint & Master Arch
    img_tech = Image.open("aura_three_layer_architecture_dark.png")
    img_exec = Image.open("aura_master_architecture.png")

    # Combine into Dual Projection (2048 x 1080)
    w, h = 2048, 1080
    dual_arch = Image.new("RGBA", (w, h), (12, 10, 8, 255))
    draw_dual = ImageDraw.Draw(dual_arch)

    font_hdr = get_font(26, bold=True)
    font_sub = get_font(16)

    # Header
    draw_dual.text((w/2, 35), "AURA DUAL ARCHITECTURE PROJECTION", fill=(245, 197, 115), font=font_hdr, anchor="mm")
    draw_dual.text((w/2, 65), "Technical Blueprint Specification (Left)  |  Executive B2B Infographic (Right)", fill=(210, 195, 180), font=font_sub, anchor="mm")

    # Resize images to 980x950
    t_resized = img_tech.resize((980, 950), Image.Resampling.LANCZOS)
    e_resized = img_exec.resize((980, 950), Image.Resampling.LANCZOS)

    dual_arch.paste(t_resized, (25, 95))
    dual_arch.paste(e_resized, (1043, 95))

    # Border highlights
    draw_dual.rounded_rectangle((20, 90, 1010, 1055), radius=10, fill=None, outline=(215, 145, 60), width=1)
    draw_dual.rounded_rectangle((1038, 90, 2028, 1055), radius=10, fill=None, outline=(215, 145, 60), width=1)

    dual_arch.save("aura_three_layer_dual_projection.png")
    print("Rendered aura_three_layer_dual_projection.png")

def patch_edge_engine_projections():
    # Make sure aura_edge_engine_4steps_dark.png is clean and fully English
    w, h = 1024, 1024
    img = Image.new("RGBA", (w, h), (18, 15, 12, 255))
    draw = ImageDraw.Draw(img)

    font_title = get_font(28, bold=True)
    font_sub = get_font(17)
    font_step = get_font(16, bold=True)
    font_card_title = get_font(18, bold=True)
    font_card_body = get_font(13)

    # Title
    draw.text((w/2, 45), "EDGE ENGINE: EMPOWERING THE HUMAN OPERATOR", fill=(245, 197, 115), font=font_title, anchor="mm")
    draw.text((w/2, 80), "4-Step Closed Loop: Converting Tacit Plant Knowledge into Explicit Private Graph Intelligence", fill=(210, 195, 180), font=font_sub, anchor="mm")

    # 4 Cards Grid
    steps = [
        ("STEP 1", "1. PREDICT", [
            "• Real-time sensor log analysis",
            "• Predictive AI anomaly detection",
            "• Machine failure anticipation (>2h)",
            "• Dough/enamel quality risk alerts",
            "• Local GPU edge inference"
        ], (215, 145, 60)),
        ("STEP 2", "2. GUIDE", [
            "• Dual Graph-RAG retrieval",
            "• Explainable step-by-step SOPs",
            "• Root-cause diagnostic evidence",
            "• EU AI Act compliant rationale",
            "• Contextual operator assistance"
        ], (225, 125, 85)),
        ("STEP 3", "3. ACT", [
            "• Human-at-the-Edge decision",
            "• Operator executes or overrides",
            "• Real-time plant line adjustment",
            "• Diagnostic outcome logging",
            "• Full human agency retained"
        ], (235, 165, 125)),
        ("STEP 4", "4. LEARN", [
            "• Tacit operator experience capture",
            "• Judge Agent validation & filtering",
            "• Private Graph dynamic update",
            "• Continuous AI model improvement",
            "• Zero data leakage outside plant"
        ], (245, 197, 115))
    ]

    cx = 50
    card_w = 210
    card_gap = 25

    for i, (s_num, s_title, items, border_col) in enumerate(steps):
        x1 = cx + i * (card_w + card_gap)
        x2 = x1 + card_w
        draw.rounded_rectangle((x1, 150, x2, 600), radius=10, fill=(28, 22, 16, 255), outline=border_col, width=2)
        
        # Step Tag
        draw.rounded_rectangle((x1 + 15, 165, x1 + 95, 195), radius=6, fill=(45, 32, 22, 255), outline=border_col, width=1)
        draw.text((x1 + 55, 180), s_num, fill=border_col, font=get_font(12, bold=True), anchor="mm")

        # Step Title
        draw.text((x1 + 15, 220), s_title, fill=(248, 250, 252), font=font_step)

        # Bullet items
        y_text = 270
        for item in items:
            draw.text((x1 + 12, y_text), item, fill=(220, 210, 200), font=font_card_body)
            y_text += 55

        # Connection Arrow
        if i < 3:
            ax = x2 + 5
            draw.line([(ax, 375), (ax + 15, 375)], fill=border_col, width=3)
            draw.polygon([(ax + 12, 370), (ax + 20, 375), (ax + 12, 380)], fill=border_col)

    # Feedback loop line bottom
    draw.line([(155, 640), (865, 640)], fill=(225, 29, 72, 255), width=3)
    draw.line([(865, 600), (865, 640)], fill=(225, 29, 72, 255), width=3)
    draw.line([(155, 600), (155, 640)], fill=(225, 29, 72, 255), width=3)
    draw.polygon([(150, 605), (160, 605), (155, 595)], fill=(225, 29, 72, 255))

    draw.rounded_rectangle((220, 622, 790, 658), radius=6, fill=(20, 16, 12, 255), outline=(225, 29, 72, 255), width=1)
    draw.text((505, 640), "CONTINUOUS TACIT-TO-EXPLICIT KNOWLEDGE FEEDBACK LOOP IN FACTORY PLANT", fill=(255, 255, 255), font=get_font(12, bold=True), anchor="mm")

    # Bottom Validation Box
    draw.rounded_rectangle((50, 700, 974, 820), radius=10, fill=(28, 22, 16, 255), outline=(215, 145, 60), width=1)
    draw.text((w/2, 735), "Validated at TRL 5 in On-Premise Industrial Edge Pilots:", fill=(245, 197, 115), font=font_card_title, anchor="mm")
    draw.text((w/2, 780), "Vicky Foods (Continuous Bakery Dough Telemetry)   |   AKCOAT (Chemical Rheology & Thermal Curing)", fill=(248, 250, 252), font=font_card_body, anchor="mm")

    img.save("aura_edge_engine_4steps_dark.png")
    print("Rendered aura_edge_engine_4steps_dark.png")

    # Combine Dual Projection for Edge Engine
    img_bucle = Image.open("aura_bucle_4_etapas.png")
    
    dual_edge = Image.new("RGBA", (2048, 1080), (12, 10, 8, 255))
    draw_de = ImageDraw.Draw(dual_edge)
    font_hdr = get_font(26, bold=True)
    draw_de.text((1024, 35), "THE AURA EDGE ENGINE — DUAL OPERATIONAL PROJECTION", fill=(245, 197, 115), font=font_hdr, anchor="mm")
    draw_de.text((1024, 65), "Technical 4-Step Closed Loop (Left)  |  Executive Operational Flow (Right)", fill=(210, 195, 180), font=font_sub, anchor="mm")

    e_left = img.resize((980, 950), Image.Resampling.LANCZOS)
    e_right = img_bucle.resize((980, 950), Image.Resampling.LANCZOS)

    dual_edge.paste(e_left, (25, 95))
    dual_edge.paste(e_right, (1043, 95))

    draw_de.rounded_rectangle((20, 90, 1010, 1055), radius=10, fill=None, outline=(215, 145, 60), width=1)
    draw_de.rounded_rectangle((1038, 90, 2028, 1055), radius=10, fill=None, outline=(215, 145, 60), width=1)

    dual_edge.save("aura_edge_engine_dual_projection.png")
    print("Rendered aura_edge_engine_dual_projection.png")

create_dual_projections()
patch_edge_engine_projections()
