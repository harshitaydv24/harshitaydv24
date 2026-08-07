"""stats.svg — animated rank ring + stat rows"""
import os
OUT = os.path.dirname(os.path.abspath(__file__))

P1="#ff4da6"; P2="#c44dff"; BG="#0d0011"; CARD="#140022"
TEXT="#f0d8ff"; TEXT2="#c9a8e8"; MONO="'Share Tech Mono','Courier New',monospace"

# Stats rows: label, value, max_bar_w (out of 200), color
stats = [
    ("⭐ Stars Earned",     "42",   88,  P1),
    ("🔁 Total Commits",    "318",  160, P2),
    ("🔀 Pull Requests",    "24",   48,  "#ff80cc"),
    ("🐛 Issues Opened",    "11",   22,  "#a0a0ff"),
    ("🤝 Contributed To",   "6",    12,  "#80ffcc"),
]

# Rank ring: circumference = 2π×54 ≈ 339
CIRC = 339
rank_dash = int(CIRC * 0.78)  # 78% filled = A++ rank

rows_svg = ""
for i,(label,val,bw,col) in enumerate(stats):
    y = 28 + i*36
    delay = 0.4 + i*0.25
    rows_svg += f"""
  <!-- row {i} -->
  <g opacity="0">
    <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{delay:.2f}s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate" values="-30,0;0,0" dur="0.4s" begin="{delay:.2f}s" fill="freeze" additive="sum"/>
    <text x="165" y="{y+16}" font-family="'Segoe UI',Arial,sans-serif" font-size="11" fill="{TEXT2}">{label}</text>
    <rect x="165" y="{y+20}" width="200" height="8" rx="4" fill="rgba(255,255,255,0.07)"/>
    <rect x="165" y="{y+20}" width="0" height="8" rx="4" fill="{col}">
      <animate attributeName="width" from="0" to="{bw}" dur="0.8s" begin="{delay+0.1:.2f}s" fill="freeze"/>
    </rect>
    <text x="372" y="{y+28}" font-family="'Courier New',monospace" font-size="10" fill="{col}" font-weight="bold">{val}</text>
  </g>"""

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
  width="490" height="220" viewBox="0 0 490 220"
  role="img" aria-label="Harshita Yadav GitHub Stats">
  <title>GitHub Stats — Harshita Yadav</title>
  <defs>
    <linearGradient id="rankGrad" x1="0" y1="0" x2="1" y2="1" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="{P1}">
        <animate attributeName="stop-color" values="{P1};{P2};{P1}" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="{P2}">
        <animate attributeName="stop-color" values="{P2};{P1};{P2}" dur="4s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="{P1}" flood-opacity="0.8"/>
      <feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="{P2}" flood-opacity="0.4"/>
    </filter>
    <filter id="cardShadow" x="-3%" y="-3%" width="106%" height="112%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="{P2}" flood-opacity="0.3"/>
    </filter>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&amp;family=Share+Tech+Mono&amp;display=swap');
    </style>
  </defs>

  <!-- card background -->
  <rect width="490" height="220" rx="16" ry="16" fill="{CARD}" filter="url(#cardShadow)"/>
  <rect x="1" y="1" width="488" height="218" rx="15" ry="15" fill="none"
        stroke="url(#rankGrad)" stroke-width="1.2" opacity="0.5"/>

  <!-- title -->
  <text x="20" y="28" font-family="'Space Grotesk','Segoe UI',Arial,sans-serif"
        font-weight="700" font-size="14" fill="{TEXT}" letter-spacing="1">GitHub Stats</text>
  <text x="20" y="44" font-family="'Courier New',monospace" font-size="10" fill="{P2}" opacity="0.7">harshitaydv24</text>

  <!-- rank ring (left side) -->
  <g transform="translate(82,120)">
    <!-- track -->
    <circle r="54" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="10"/>
    <!-- progress arc -->
    <circle r="54" fill="none" stroke="url(#rankGrad)" stroke-width="10"
            stroke-linecap="round" filter="url(#glow)"
            stroke-dasharray="{CIRC}" stroke-dashoffset="{CIRC}"
            transform="rotate(-90)">
      <animate attributeName="stroke-dashoffset" from="{CIRC}" to="{CIRC - rank_dash}"
               dur="1.5s" begin="0.2s" fill="freeze"/>
    </circle>
    <!-- rank label -->
    <text text-anchor="middle" y="-8"
          font-family="'Space Grotesk','Segoe UI',Arial,sans-serif"
          font-weight="700" font-size="28" fill="url(#rankGrad)" filter="url(#glow)">A+</text>
    <text text-anchor="middle" y="12" font-family="'Courier New',monospace" font-size="10" fill="{TEXT2}">Rank</text>
    <!-- percentage text -->
    <text text-anchor="middle" y="30" font-family="'Courier New',monospace" font-size="9" fill="{P1}">Top 15%</text>
  </g>

  <!-- stat rows (right side) -->
  <g transform="translate(0,0)">
    {rows_svg}
  </g>
</svg>"""

with open(os.path.join(OUT, "stats.svg"), "w", encoding="utf-8") as f:
    f.write(svg)
print("stats.svg done!")
