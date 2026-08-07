"""
Build script - generates all SVG files for harshitaydv24 GitHub profile.
Run from the project directory.
"""
import os, sys

# ── Load base64 character image ──────────────────────────────────────────────
with open("char_b64.txt") as f:
    CHAR_B64 = f.read().strip()
CHAR_W, CHAR_H = 400, 533
IMG_DATA = f"data:image/png;base64,{CHAR_B64}"
OUT = os.path.dirname(os.path.abspath(__file__))

# ─────────────────────────────────────────────────────────────────────────────
#  BANNER.SVG  (1280 × 740)
# ─────────────────────────────────────────────────────────────────────────────
def build_banner(dark=True):
    # Color theme
    if dark:
        BG       = "#0d0011"
        BG2      = "#150020"
        CARD     = "rgba(255,255,255,0.04)"
        CARD_S   = "#2a0040"
        TEXT     = "#f0d8ff"
        TEXT2    = "#c9a8e8"
        MONO     = "#e8c8ff"
        TERM_BG  = "#0a0015"
        TERM_FX  = "#ff66bb"
        P1       = "#ff4da6"   # hot pink
        P2       = "#c44dff"   # purple
        P3       = "#ff80cc"   # light pink
        NEON1    = "#ff38a8"
        NEON2    = "#cc44ff"
        SCAN_C   = "#00ffe0"
        EDITOR_BG= "#0e001a"
        PILL_BG  = "rgba(180,0,120,0.18)"
        PILL_BD  = "#ff4da6"
        BAR_BG   = "rgba(255,255,255,0.08)"
        BAR_FX   = "url(#barGrad)"
        STAR_C   = "#ff99dd"
        HEART_C  = "#ff4da6"
    else:
        BG       = "#fdf0f8"
        BG2      = "#f5e0f5"
        CARD     = "rgba(120,0,80,0.06)"
        CARD_S   = "#f0d0f0"
        TEXT     = "#2a0035"
        TEXT2    = "#5a1070"
        MONO     = "#3a0055"
        TERM_BG  = "#f0e0f8"
        TERM_FX  = "#aa0060"
        P1       = "#c0006a"
        P2       = "#7700cc"
        P3       = "#d060a0"
        NEON1    = "#aa0060"
        NEON2    = "#7700cc"
        SCAN_C   = "#0088cc"
        EDITOR_BG= "#ede0f8"
        PILL_BG  = "rgba(150,0,90,0.10)"
        PILL_BD  = "#c0006a"
        BAR_BG   = "rgba(0,0,0,0.08)"
        BAR_FX   = "url(#barGrad)"
        STAR_C   = "#aa0060"
        HEART_C  = "#c0006a"

    skills = [
        ("Photoshop","#ff6eb4"),("Canva","#ff4da6"),("Figma","#c44dff"),
        ("Python","#ffdd57"),("Java","#f89820"),("C/C++","#a8e6ff"),
        ("HTML","#f06529"),("CSS","#2965f1"),("Vibe Coding","#ff80cc"),
    ]

    roles = ["Student","Designer","Vibe Coder","Creative Builder","Open Source Enthusiast"]
    code_lines = [
        'const buildDreams = () => {',
        '  const skills = ["Design","Code","Create"];',
        '  return skills.map(s => <Dream key={s} power={s} />);',
        '};',
        '',
        'export default buildDreams;',
    ]

    # ── pill rows ─────────────────────────────────────────────────────────────
    pill_svg = ""
    pill_w, pill_h, pill_gap = 110, 26, 8
    row_start_x, row_start_y = 490, 435
    per_row = 5
    for i,(sk,col) in enumerate(skills):
        col_i = i % per_row
        row_i = i // per_row
        px = row_start_x + col_i*(pill_w+pill_gap)
        py = row_start_y + row_i*(pill_h+pill_gap+2)
        delay = 0.05 + i*0.12
        pill_svg += f"""
    <g opacity="0" transform="translate({px},{py})">
      <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{delay:.2f}s" fill="freeze"/>
      <rect rx="13" ry="13" width="{pill_w}" height="{pill_h}" fill="{PILL_BG}" stroke="{col}" stroke-width="1.2"/>
      <text x="{pill_w//2}" y="{pill_h//2+5}" text-anchor="middle" font-family="'Courier New',monospace" font-size="10.5" fill="{col}">{sk}</text>
    </g>"""

    # ── code editor lines ──────────────────────────────────────────────────────
    code_svg = ""
    cx0, cy0 = 760, 590
    for li, line in enumerate(code_lines):
        lx = cx0 + 25
        ly = cy0 + 16 + li*16
        cover_w = 460
        delay_s = 1.0 + li*0.5
        dur_s   = max(0.3, len(line)*0.055)
        col = "#c44dff" if line.startswith("const") or line.startswith("export") else (
              "#ff80cc" if line.startswith("  return") else
              "#a8e6ff" if "skills" in line else
              "#e8c8ff")
        if line.strip() == "":
            continue
        code_svg += f"""
    <!-- code line {li} -->
    <text x="{lx}" y="{ly}" font-family="'Courier New',monospace" font-size="11.5" fill="{col}">{line.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')}</text>
    <rect x="{lx-2}" y="{ly-12}" width="{cover_w}" height="16" fill="{EDITOR_BG}">
      <animate attributeName="width" from="{cover_w}" to="0" dur="{dur_s:.2f}s" begin="{delay_s:.2f}s" fill="freeze"/>
    </rect>"""

    # ── cycling roles ──────────────────────────────────────────────────────────
    n_roles = len(roles)
    role_dur = 2.8
    total_dur = n_roles * role_dur
    role_svg = ""
    for ri, role in enumerate(roles):
        t0 = ri * role_dur
        t1 = t0 + 0.15
        t2 = t0 + role_dur - 0.15
        t3 = t0 + role_dur
        # Build keyTimes/values cycling over total_dur
        # Simplified: just chain visible windows
        vis_start = t0 / total_dur
        vis_end   = t3 / total_dur
        on_s  = t1 / total_dur
        off_s = t2 / total_dur
        # Full cycle values
        vals = "0"
        kts  = "0"
        for ri2, _ in enumerate(roles):
            s = ri2 * role_dur / total_dur
            e = (ri2+1) * role_dur / total_dur
            on2  = (ri2*role_dur+0.15) / total_dur
            off2 = (ri2*role_dur+role_dur-0.15) / total_dur
            if ri2 == ri:
                vals += f";0;1;1;0"
            else:
                vals += f";0;0;0;0"
            kts  += f";{s:.4f};{on2:.4f};{off2:.4f};{e:.4f}"
        role_svg += f"""
    <text x="490" y="330" font-family="'Segoe UI',Arial,sans-serif" font-size="16" fill="{P3}" opacity="0" letter-spacing="2">
      &gt; {role}
      <animate attributeName="opacity" values="{vals}" keyTimes="{kts}" dur="{total_dur:.1f}s" repeatCount="indefinite"/>
    </text>"""

    # ── terminal typing ────────────────────────────────────────────────────────
    TERM_TEXT = "user@dev:~$ cat README.md"
    term_cover_w = len(TERM_TEXT) * 8.5  # monospace estimate

    # ── floating hearts ────────────────────────────────────────────────────────
    hearts_svg = ""
    hpos = [(60,680),(120,700),(200,660),(280,690),(350,710),(1100,680),(1160,700),(1220,660)]
    for hi,(hx,hy) in enumerate(hpos):
        delay = hi * 0.8
        hearts_svg += f"""
    <text x="{hx}" y="{hy}" font-size="16" fill="{HEART_C}" opacity="0">♥
      <animate attributeName="opacity" values="0;0.9;0" dur="4s" begin="{delay:.1f}s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="translate" values="0,0;{5 if hi%2==0 else -5},-80" dur="4s" begin="{delay:.1f}s" repeatCount="indefinite" additive="sum"/>
    </text>"""

    # ── twinkling sparkles ─────────────────────────────────────────────────────
    sparks_svg = ""
    spos = [(80,100),(160,200),(240,80),(1050,90),(1150,150),(1200,220),(900,60),(800,700),(1000,680)]
    for si,(sx,sy) in enumerate(spos):
        delay = si * 0.4
        sparks_svg += f"""
    <text x="{sx}" y="{sy}" font-size="{12+si%4*2}" fill="{STAR_C}" opacity="0">✦
      <animate attributeName="opacity" values="0;1;0" dur="{1.5+si%3*0.5:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="scale" values="0.5,0.5;1.2,1.2;0.5,0.5" dur="{1.5+si%3*0.5:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite" additive="sum"/>
    </text>"""

    # ── rising particles ──────────────────────────────────────────────────────
    particles_svg = ""
    ppos = [(50,750),(130,730),(210,760),(320,740),(420,750),(1050,740),(1130,750),(1200,730),(900,750),(700,760)]
    for pi,(px,py) in enumerate(ppos):
        delay = pi * 0.7
        r = 2 + pi%2
        col = P1 if pi%2==0 else P2
        particles_svg += f"""
    <circle cx="{px}" cy="{py}" r="{r}" fill="{col}" opacity="0">
      <animate attributeName="cy" from="{py}" to="{py-200}" dur="{5+pi%3:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;0.7;0" keyTimes="0;0.2;1" dur="{5+pi%3:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite"/>
    </circle>"""

    # ── ambient orbs ─────────────────────────────────────────────────────────
    orbs_svg = f"""
    <circle cx="100" cy="150" r="120" fill="{P1}" opacity="0.04">
      <animate attributeName="r" values="100;140;100" dur="7s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.04;0.08;0.04" dur="7s" repeatCount="indefinite"/>
    </circle>
    <circle cx="1200" cy="600" r="150" fill="{P2}" opacity="0.05">
      <animate attributeName="r" values="120;170;120" dur="9s" begin="1s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.05;0.09;0.05" dur="9s" begin="1s" repeatCount="indefinite"/>
    </circle>
    <circle cx="650" cy="740" r="100" fill="{P1}" opacity="0.04">
      <animate attributeName="r" values="80;120;80" dur="6s" begin="2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="1050" cy="100" r="80" fill="{P2}" opacity="0.04">
      <animate attributeName="r" values="60;100;60" dur="8s" begin="3s" repeatCount="indefinite"/>
    </circle>"""

    # ── stats bar ─────────────────────────────────────────────────────────────
    stats_items = [("Commits","██████████████",78),("PRs","█████",32),("Stars","████████",55)]
    stats_svg = ""
    for si2,(label,_,pct) in enumerate(stats_items):
        bar_x, bar_y = 490, 600 + si2*26
        bar_maxw = 170
        bar_w = int(bar_maxw * pct / 100)
        delay = 0.5 + si2*0.3
        stats_svg += f"""
    <text x="{bar_x}" y="{bar_y+13}" font-family="'Courier New',monospace" font-size="10" fill="{TEXT2}">{label}</text>
    <rect x="{bar_x+65}" y="{bar_y+2}" width="{bar_maxw}" height="14" rx="7" fill="{BAR_BG}"/>
    <rect x="{bar_x+65}" y="{bar_y+2}" width="0" height="14" rx="7" fill="url(#barGrad)">
      <animate attributeName="width" from="0" to="{bar_w}" dur="1s" begin="{delay:.1f}s" fill="freeze"/>
    </rect>
    <text x="{bar_x+65+bar_maxw+6}" y="{bar_y+13}" font-family="'Courier New',monospace" font-size="9" fill="{TEXT2}">{pct}%</text>"""

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
  width="1280" height="740" viewBox="0 0 1280 740"
  role="img" aria-label="Harshita Yadav GitHub Profile Banner">
  <title>Harshita Yadav — Student | Designer | Developer</title>
  <defs>
    <!-- ── gradients ────────────────────────────────── -->
    <linearGradient id="bgGrad" x1="0" y1="0" x2="1" y2="1" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="{BG}"/>
      <stop offset="100%" stop-color="{BG2}"/>
    </linearGradient>
    <linearGradient id="nameGrad" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="{P1}">
        <animate attributeName="stop-color" values="{P1};{P2};{P1}" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="{P2}">
        <animate attributeName="stop-color" values="{P2};{P1};{P2}" dur="4s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    <linearGradient id="barGrad" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="{P1}"/>
      <stop offset="100%" stop-color="{P2}"/>
    </linearGradient>
    <linearGradient id="scanGrad" x1="0" y1="0" x2="0" y2="1" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="{SCAN_C}" stop-opacity="0"/>
      <stop offset="40%" stop-color="{SCAN_C}" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="{SCAN_C}" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="{SCAN_C}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="neonGrad" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="{NEON1}"/>
      <stop offset="50%" stop-color="{NEON2}"/>
      <stop offset="100%" stop-color="{NEON1}"/>
    </linearGradient>
    <linearGradient id="divGrad" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="{P1}" stop-opacity="0"/>
      <stop offset="30%" stop-color="{P1}"/>
      <stop offset="70%" stop-color="{P2}"/>
      <stop offset="100%" stop-color="{P2}" stop-opacity="0"/>
    </linearGradient>

    <!-- ── clip paths ───────────────────────────────── -->
    <clipPath id="bannerClip">
      <rect width="1280" height="740" rx="18" ry="18"/>
    </clipPath>
    <clipPath id="charClip">
      <rect x="0" y="0" width="430" height="740"/>
    </clipPath>
    <clipPath id="holoReveal">
      <rect x="0" y="0" width="430" height="0">
        <animate attributeName="height" from="0" to="760" dur="1.8s" begin="0.2s" fill="freeze"/>
      </rect>
    </clipPath>

    <!-- ── filters ──────────────────────────────────── -->
    <filter id="neonGlow" x="-30%" y="-80%" width="160%" height="260%">
      <feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="{P1}" flood-opacity="0.9"/>
      <feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="{P2}" flood-opacity="0.6"/>
    </filter>
    <filter id="textGlow" x="-10%" y="-40%" width="120%" height="180%">
      <feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="{P1}" flood-opacity="0.7"/>
    </filter>
    <filter id="scanGlow" x="-5%" y="-200%" width="110%" height="500%">
      <feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="{SCAN_C}" flood-opacity="1"/>
      <feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="{SCAN_C}" flood-opacity="0.5"/>
    </filter>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="{P2}" flood-opacity="0.25"/>
    </filter>

    <!-- ── styles ───────────────────────────────────── -->
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Pacifico&amp;family=Space+Grotesk:wght@300;400;600;700&amp;family=Share+Tech+Mono&amp;display=swap');

      .neon-sign {{
        font-family: 'Share Tech Mono', 'Courier New', monospace;
        font-size: 19px;
        fill: url(#neonGrad);
        filter: url(#neonGlow);
        animation: flicker 0.15s linear 2.5s 6, steadyGlow 1s ease-out 3.5s forwards;
        opacity: 0;
      }}
      @keyframes flicker {{
        0%,100% {{ opacity:1; }}
        25%,75% {{ opacity:0.3; }}
        50% {{ opacity:0.8; }}
      }}
      @keyframes steadyGlow {{
        from {{ opacity:0.3; }} to {{ opacity:1; }}
      }}
      .term-cursor {{
        animation: blink 1s step-end infinite;
        fill: {TERM_FX};
      }}
      @keyframes blink {{
        0%,100% {{ opacity:1; }} 50% {{ opacity:0; }}
      }}
      .heart-float {{
        animation: floatUp 4s ease-out infinite;
      }}
      @keyframes floatUp {{
        0% {{ transform:translateY(0); opacity:0; }}
        20% {{ opacity:0.9; }}
        100% {{ transform:translateY(-120px); opacity:0; }}
      }}
    </style>
  </defs>

  <!-- ── background ───────────────────────────────────────────────────────── -->
  <g clip-path="url(#bannerClip)">
    <rect width="1280" height="740" fill="url(#bgGrad)"/>

    <!-- grid overlay -->
    <line x1="0" y1="0" x2="1280" y2="0" stroke="{P1}" stroke-opacity="0.04"/>
    <line x1="0" y1="185" x2="1280" y2="185" stroke="{P1}" stroke-opacity="0.04"/>
    <line x1="0" y1="370" x2="1280" y2="370" stroke="{P1}" stroke-opacity="0.04"/>
    <line x1="0" y1="555" x2="1280" y2="555" stroke="{P1}" stroke-opacity="0.04"/>
    <line x1="430" y1="0" x2="430" y2="740" stroke="{P1}" stroke-opacity="0.04"/>
    <line x1="855" y1="0" x2="855" y2="740" stroke="{P1}" stroke-opacity="0.04"/>

    {orbs_svg}
    {particles_svg}
    {sparks_svg}
    {hearts_svg}

    <!-- ── character image (left panel) ──────────────────────────────────── -->
    <g clip-path="url(#charClip)">
      <!-- character reveal with hologram clipPath -->
      <g clip-path="url(#holoReveal)">
        <image href="{IMG_DATA}"
               x="15" y="107" width="{CHAR_W}" height="{CHAR_H}"
               preserveAspectRatio="xMidYMid meet"
               image-rendering="high-quality"/>
        <!-- scanline overlay on image for hologram feel -->
        <rect x="0" y="0" width="430" height="740"
              fill="none"
              stroke="{SCAN_C}" stroke-width="0"
              style="background: repeating-linear-gradient(0deg, transparent, transparent 3px, rgba(0,255,224,0.03) 4px)"/>
      </g>

      <!-- initial reveal scan line (moves with reveal) -->
      <rect x="0" y="0" width="430" height="6" fill="url(#scanGrad)" filter="url(#scanGlow)">
        <animate attributeName="y" from="0" to="740" dur="1.8s" begin="0.2s" fill="freeze"/>
        <animate attributeName="opacity" from="1" to="0" dur="0.3s" begin="2s" fill="freeze"/>
      </rect>

      <!-- continuous scanner every 3.5s after initial reveal -->
      <rect x="0" y="-6" width="430" height="6" fill="url(#scanGrad)" filter="url(#scanGlow)">
        <animate attributeName="y" values="-6;746" dur="3.5s" begin="2.5s" repeatCount="indefinite"/>
      </rect>

      <!-- hologram tint overlay on character -->
      <rect x="0" y="0" width="430" height="740" fill="{SCAN_C}" opacity="0">
        <animate attributeName="opacity" values="0.08;0;0.04;0;0.06;0" dur="1.8s" begin="0.2s" fill="freeze"/>
      </rect>

      <!-- vignette on character sides -->
      <linearGradient id="vigL" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
        <stop offset="0%" stop-color="{BG}" stop-opacity="0.5"/>
        <stop offset="40%" stop-color="{BG}" stop-opacity="0"/>
      </linearGradient>
      <linearGradient id="vigR" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
        <stop offset="60%" stop-color="{BG}" stop-opacity="0"/>
        <stop offset="100%" stop-color="{BG}" stop-opacity="0.6"/>
      </linearGradient>
      <rect x="0" y="0" width="430" height="740" fill="url(#vigL)"/>
      <rect x="0" y="0" width="430" height="740" fill="url(#vigR)"/>

      <!-- bottom vignette -->
      <linearGradient id="vigB" x1="0" y1="0" x2="0" y2="1" gradientUnits="objectBoundingBox">
        <stop offset="70%" stop-color="{BG}" stop-opacity="0"/>
        <stop offset="100%" stop-color="{BG}" stop-opacity="0.8"/>
      </linearGradient>
      <rect x="0" y="0" width="430" height="740" fill="url(#vigB)"/>
    </g>

    <!-- divider line -->
    <rect x="440" y="30" width="1" height="680" fill="url(#divGrad)" opacity="0.3"/>

    <!-- ── RIGHT PANEL — text content ────────────────────────────────────── -->

    <!-- terminal card -->
    <rect x="490" y="32" width="768" height="52" rx="10" ry="10" fill="{TERM_BG}" filter="url(#cardShadow)"/>
    <circle cx="508" cy="58" r="5" fill="#ff5f57"/>
    <circle cx="523" cy="58" r="5" fill="#febc2e"/>
    <circle cx="538" cy="58" r="5" fill="#28c840"/>
    <text x="555" y="63" font-family="'Share Tech Mono','Courier New',monospace" font-size="12.5" fill="{MONO}" opacity="0">user@dev:~$ cat README.md
      <animate attributeName="opacity" from="0" to="1" dur="0.01s" begin="0.3s" fill="freeze"/>
    </text>
    <!-- typing cover reveals the text -->
    <rect x="555" y="47" width="{int(len('user@dev:~$ cat README.md')*7.8)}" height="22" fill="{TERM_BG}">
      <animate attributeName="width" from="{int(len('user@dev:~$ cat README.md')*7.8)}" to="0" dur="1.6s" begin="0.3s" fill="freeze"/>
    </rect>
    <!-- blinking cursor -->
    <rect class="term-cursor" x="750" y="49" width="8" height="18" rx="1" opacity="0">
      <animate attributeName="opacity" from="0" to="1" dur="0.01s" begin="1.9s" fill="freeze"/>
      <animate attributeName="x" from="555" to="750" dur="1.6s" begin="0.3s" fill="freeze"/>
    </rect>

    <!-- ── NAME ──────────────────────────────────────────────────────────── -->
    <text x="490" y="155" font-family="'Pacifico','Georgia','Times New Roman',serif"
          font-size="52" fill="url(#nameGrad)" filter="url(#textGlow)" opacity="0"
          letter-spacing="1">
      HARSHITA YADAV
      <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="1.8s" fill="freeze"/>
    </text>
    <!-- letter by letter reveal cover -->
    <rect x="490" y="105" width="760" height="62" fill="{BG}">
      <animate attributeName="width" from="760" to="0" dur="1.2s" begin="1.8s" fill="freeze"/>
    </rect>

    <!-- ── subtitle / role line ──────────────────────────────────────────── -->
    <text x="490" y="195" font-family="'Space Grotesk','Segoe UI',Arial,sans-serif"
          font-size="14" fill="{TEXT2}" letter-spacing="3" opacity="0">
      ✦ STUDENT · DESIGNER · DEVELOPER ✦
      <animate attributeName="opacity" from="0" to="0.8" dur="0.5s" begin="3s" fill="freeze"/>
    </text>

    <!-- separator -->
    <rect x="490" y="208" width="0" height="1.5" rx="1" fill="url(#divGrad)">
      <animate attributeName="width" from="0" to="760" dur="0.8s" begin="3.2s" fill="freeze"/>
    </rect>

    <!-- ── cycling roles ─────────────────────────────────────────────────── -->
    {role_svg}

    <!-- ── tagline quote box ─────────────────────────────────────────────── -->
    <rect x="490" y="343" width="0" height="62" rx="10" ry="10"
          fill="{PILL_BG}" stroke="{P1}" stroke-width="1.2" opacity="0.8">
      <animate attributeName="width" from="0" to="760" dur="0.6s" begin="3.5s" fill="freeze"/>
      <animate attributeName="opacity" from="0" to="0.8" dur="0.6s" begin="3.5s" fill="freeze"/>
    </rect>
    <text x="502" y="368" font-family="'Share Tech Mono','Courier New',monospace"
          font-size="11" fill="{TEXT2}" opacity="0">
      // tagline
      <animate attributeName="opacity" from="0" to="1" dur="0.01s" begin="4.1s" fill="freeze"/>
    </text>
    <text x="502" y="390" font-family="'Space Grotesk','Segoe UI',Arial,sans-serif"
          font-size="13" fill="{TEXT}" opacity="0" font-style="italic">
      "designing intuitive experiences through creativity and code"
      <animate attributeName="opacity" from="0" to="1" dur="0.01s" begin="4.2s" fill="freeze"/>
    </text>
    <!-- tagline typing cover -->
    <rect x="502" y="376" width="740" height="20" fill="{BG}" opacity="0">
      <animate attributeName="opacity" from="1" to="1" dur="0.01s" begin="4.2s" fill="freeze"/>
      <animate attributeName="width" from="740" to="0" dur="1.5s" begin="4.2s" fill="freeze"/>
    </rect>

    <!-- ── tech pills label ───────────────────────────────────────────────── -->
    <text x="490" y="418" font-family="'Space Grotesk','Segoe UI',Arial,sans-serif"
          font-size="11" fill="{P2}" letter-spacing="2" opacity="0">
      ⟨ TECH STACK ⟩
      <animate attributeName="opacity" from="0" to="0.9" dur="0.3s" begin="5.2s" fill="freeze"/>
    </text>

    {pill_svg}

    <!-- ── about me lines ────────────────────────────────────────────────── -->
    <text x="490" y="518" font-family="'Space Grotesk','Segoe UI',Arial,sans-serif"
          font-size="12.5" fill="{TEXT}" opacity="0">
      👩‍💻  Harshita Yadav · harshitaydv24 · harshitaydv1024@gmail.com
      <animate attributeName="opacity" from="0" to="0.9" dur="0.4s" begin="6.5s" fill="freeze"/>
      <animateTransform attributeName="transform" type="translate" values="-20,0;0,0" dur="0.4s" begin="6.5s" fill="freeze" additive="sum"/>
    </text>
    <text x="490" y="536" font-family="'Space Grotesk','Segoe UI',Arial,sans-serif"
          font-size="12" fill="{TEXT2}" opacity="0">
      🎨  Graphic Design  ·  Photoshop  ·  Figma  ·  Canva
      <animate attributeName="opacity" from="0" to="0.85" dur="0.4s" begin="6.8s" fill="freeze"/>
      <animateTransform attributeName="transform" type="translate" values="-20,0;0,0" dur="0.4s" begin="6.8s" fill="freeze" additive="sum"/>
    </text>
    <text x="490" y="554" font-family="'Space Grotesk','Segoe UI',Arial,sans-serif"
          font-size="12" fill="{TEXT2}" opacity="0">
      💻  Python  ·  Java  ·  C/C++  ·  HTML  ·  CSS  ·  Vibe Coding
      <animate attributeName="opacity" from="0" to="0.85" dur="0.4s" begin="7.1s" fill="freeze"/>
      <animateTransform attributeName="transform" type="translate" values="-20,0;0,0" dur="0.4s" begin="7.1s" fill="freeze" additive="sum"/>
    </text>

    <!-- ── stats bar section ─────────────────────────────────────────────── -->
    <text x="490" y="582" font-family="'Space Grotesk','Segoe UI',Arial,sans-serif"
          font-size="10.5" fill="{P2}" letter-spacing="2" opacity="0">
      ⟨ ACTIVITY ⟩
      <animate attributeName="opacity" from="0" to="0.8" dur="0.3s" begin="7.4s" fill="freeze"/>
    </text>
    {stats_svg}

    <!-- ── code editor card ───────────────────────────────────────────────── -->
    <rect x="750" y="575" width="480" height="116" rx="12" ry="12"
          fill="{EDITOR_BG}" stroke="{P2}" stroke-width="1" stroke-opacity="0.5"
          filter="url(#cardShadow)" opacity="0">
      <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="8.5s" fill="freeze"/>
    </rect>
    <!-- editor tab -->
    <rect x="750" y="575" width="100" height="20" rx="6" ry="6" fill="{PILL_BG}"/>
    <text x="755" y="589" font-family="'Share Tech Mono','Courier New',monospace"
          font-size="10" fill="{P3}" opacity="0">
      ▶ buildDreams.jsx
      <animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="8.5s" fill="freeze"/>
    </text>
    <!-- line numbers -->
    <text x="758" y="606" font-family="'Share Tech Mono','Courier New',monospace"
          font-size="10" fill="{P2}" opacity="0.4">
      <tspan x="758" dy="0">1</tspan>
      <tspan x="758" dy="16">2</tspan>
      <tspan x="758" dy="16">3</tspan>
      <tspan x="758" dy="16">4</tspan>
      <tspan x="758" dy="16">5</tspan>
      <tspan x="758" dy="16">6</tspan>
      <animate attributeName="opacity" from="0" to="0.4" dur="0.3s" begin="8.7s" fill="freeze"/>
    </text>
    {code_svg}

    <!-- ── neon sign ──────────────────────────────────────────────────────── -->
    <text x="490" y="726" class="neon-sign" opacity="0"
          font-family="'Share Tech Mono','Courier New',monospace"
          font-size="18" fill="url(#neonGrad)" filter="url(#neonGlow)"
          letter-spacing="3">
      ✦ KEEP CODING  KEEP GROWING ✦
      <animate attributeName="opacity" from="0" to="0" dur="2.5s" begin="0s" fill="freeze"/>
      <animate attributeName="opacity" values="0;0.3;1;0.3;1;0.4;1" dur="1.2s" begin="2.5s" fill="freeze"/>
    </text>

    <!-- outer glow border -->
    <rect x="1" y="1" width="1278" height="738" rx="17" ry="17"
          fill="none" stroke="url(#divGrad)" stroke-width="1.5" opacity="0.4"/>
  </g>
</svg>"""
    return svg

# Write banner files
print("Writing banner.svg...")
with open(os.path.join(OUT, "banner.svg"), "w", encoding="utf-8") as f:
    f.write(build_banner(dark=True))

print("Writing banner-light.svg...")
with open(os.path.join(OUT, "banner-light.svg"), "w", encoding="utf-8") as f:
    f.write(build_banner(dark=False))

print("Banner files done!")
