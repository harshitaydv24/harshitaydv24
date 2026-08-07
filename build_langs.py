"""langs.svg — animated skill/language bars"""
import os
OUT = os.path.dirname(os.path.abspath(__file__))

P1="#ff4da6"; P2="#c44dff"; BG="#0d0011"; CARD="#140022"
TEXT="#f0d8ff"; TEXT2="#c9a8e8"

# Skills: label, pct, color
skills = [
    ("Graphic Design", 85, "#ff4da6"),
    ("Figma",          80, "#c44dff"),
    ("Adobe Photoshop",75, "#ff6eb4"),
    ("Canva",          90, "#ff80cc"),
    ("Python",         70, "#ffdd57"),
    ("HTML/CSS",       78, "#f06529"),
    ("Java",           55, "#f89820"),
    ("C/C++",          60, "#a8e6ff"),
    ("Vibe Coding",    95, "#80ffdd"),
]

bars_svg = ""
max_bar = 340
for i,(sk,pct,col) in enumerate(skills):
    y = 46 + i*32
    bw = int(max_bar * pct / 100)
    delay = 0.1 + i*0.15
    bars_svg += f"""
  <g opacity="0">
    <animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="{delay:.2f}s" fill="freeze"/>
    <text x="18" y="{y+11}" font-family="'Segoe UI',Arial,sans-serif" font-size="11.5" fill="{TEXT2}">{sk}</text>
    <text x="{18+max_bar+8}" y="{y+11}" font-family="'Courier New',monospace" font-size="10" fill="{col}">{pct}%</text>
    <rect x="18" y="{y+14}" width="{max_bar}" height="9" rx="4.5" fill="rgba(255,255,255,0.07)"/>
    <rect x="18" y="{y+14}" width="0"  height="9" rx="4.5" fill="{col}" opacity="0.85">
      <animate attributeName="width" from="0" to="{bw}" dur="0.9s" begin="{delay+0.05:.2f}s" fill="freeze"/>
    </rect>
  </g>"""

CIRC_TOTAL = sum(p for _,p,_ in skills)
pie_pieces = ""
cx, cy, r = 405, 145, 68
angle = -90.0
for i,(sk,pct,col) in enumerate(skills):
    sweep = pct / CIRC_TOTAL * 360
    import math
    x1 = cx + r * math.cos(math.radians(angle))
    y1 = cy + r * math.sin(math.radians(angle))
    angle2 = angle + sweep
    x2 = cx + r * math.cos(math.radians(angle2))
    y2 = cy + r * math.sin(math.radians(angle2))
    large = 1 if sweep > 180 else 0
    delay = 0.1 + i*0.15
    pie_pieces += f"""
  <path d="M{cx:.1f},{cy:.1f} L{x1:.1f},{y1:.1f} A{r},{r} 0 {large},1 {x2:.1f},{y2:.1f} Z"
        fill="{col}" opacity="0" stroke="#140022" stroke-width="1">
    <animate attributeName="opacity" from="0" to="0.85" dur="0.4s" begin="{delay:.2f}s" fill="freeze"/>
  </path>"""
    angle = angle2

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
  width="490" height="340" viewBox="0 0 490 340"
  role="img" aria-label="Harshita Yadav Skills">
  <title>Skills — Harshita Yadav</title>
  <defs>
    <linearGradient id="titleGrad" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="{P1}"/>
      <stop offset="100%" stop-color="{P2}"/>
    </linearGradient>
    <filter id="cardShadow2" x="-3%" y="-2%" width="106%" height="108%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="{P2}" flood-opacity="0.3"/>
    </filter>
    <style>@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&amp;family=Share+Tech+Mono&amp;display=swap');</style>
  </defs>
  <rect width="490" height="340" rx="16" ry="16" fill="#140022" filter="url(#cardShadow2)"/>
  <rect x="1" y="1" width="488" height="338" rx="15" ry="15" fill="none"
        stroke="url(#titleGrad)" stroke-width="1.2" opacity="0.45"/>
  <text x="18" y="26" font-family="'Space Grotesk','Segoe UI',Arial,sans-serif"
        font-weight="700" font-size="14" fill="{TEXT}" letter-spacing="1">Skills &amp; Tools</text>
  <text x="18" y="40" font-family="'Courier New',monospace" font-size="10" fill="{P2}" opacity="0.7">harshitaydv24</text>
  {bars_svg}
</svg>"""

with open(os.path.join(OUT, "langs.svg"), "w", encoding="utf-8") as f:
    f.write(svg)
print("langs.svg done!")
