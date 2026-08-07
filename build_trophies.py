"""trophies.svg — trophy grid with pop-in and shine sweep"""
import os
OUT = os.path.dirname(os.path.abspath(__file__))

P1="#ff4da6"; P2="#c44dff"; CARD="#140022"; TEXT="#f0d8ff"; TEXT2="#c9a8e8"

trophies = [
    ("SSS", "Total Stars",    "42",  "#ffd700", "🏆"),
    ("SS",  "Commits",        "318", "#ff9900", "🥇"),
    ("S",   "Pull Requests",  "24",  "#c44dff", "⭐"),
    ("A+",  "Issues Solved",  "11",  "#ff4da6", "🎯"),
    ("A",   "Contributed To", "6",   "#00ccff", "🤝"),
    ("B",   "Repositories",   "12",  "#80ffcc", "📦"),
]

cells_svg = ""
cell_w, cell_h = 140, 140
cols = 6
for i,(rank,label,val,col,icon) in enumerate(trophies):
    cx_pos = 10 + i*(cell_w+10)
    cy_pos = 30
    delay = 0.15 + i*0.18
    cells_svg += f"""
  <!-- trophy {i}: {label} -->
  <g transform="translate({cx_pos},{cy_pos})" opacity="0">
    <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{delay:.2f}s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate"
      values="{cx_pos},{cy_pos+30};{cx_pos},{cy_pos}" dur="0.4s" begin="{delay:.2f}s" fill="freeze" additive="replace"/>

    <!-- cell bg -->
    <rect width="{cell_w}" height="{cell_h}" rx="14" ry="14"
          fill="rgba(30,0,50,0.8)" stroke="{col}" stroke-width="1.5" opacity="0.9"/>

    <!-- rank badge top -->
    <rect x="{cell_w//2 - 18}" y="8" width="36" height="18" rx="9"
          fill="{col}" opacity="0.25"/>
    <text x="{cell_w//2}" y="21" text-anchor="middle"
          font-family="'Courier New',monospace" font-weight="bold" font-size="10"
          fill="{col}">{rank}</text>

    <!-- icon -->
    <text x="{cell_w//2}" y="72" text-anchor="middle" font-size="28">{icon}</text>

    <!-- label -->
    <text x="{cell_w//2}" y="96" text-anchor="middle"
          font-family="'Segoe UI',Arial,sans-serif" font-size="9.5" fill="{TEXT2}">{label}</text>

    <!-- value -->
    <text x="{cell_w//2}" y="114" text-anchor="middle"
          font-family="'Courier New',monospace" font-weight="bold" font-size="18" fill="{col}">{val}</text>

    <!-- glowing border on hover approximation (pulse) -->
    <rect width="{cell_w}" height="{cell_h}" rx="14" ry="14"
          fill="none" stroke="{col}" stroke-width="2" opacity="0">
      <animate attributeName="opacity" values="0;0.6;0" dur="3s" begin="{delay+0.5:.2f}s" repeatCount="indefinite"/>
    </rect>
  </g>"""

total_w = 10 + cols*(cell_w+10)

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
  width="{total_w}" height="200" viewBox="0 0 {total_w} 200"
  role="img" aria-label="Harshita Yadav GitHub Trophies">
  <title>GitHub Trophies — Harshita Yadav</title>
  <defs>
    <linearGradient id="trophyTitleGrad" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="{P1}"/>
      <stop offset="100%" stop-color="{P2}"/>
    </linearGradient>
    <linearGradient id="shineGrad" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="white" stop-opacity="0"/>
      <stop offset="50%" stop-color="white" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="white" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="trophyClip">
      <rect width="{total_w}" height="200" rx="12"/>
    </clipPath>
    <filter id="trophyShadow" x="-3%" y="-3%" width="106%" height="112%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="{P2}" flood-opacity="0.3"/>
    </filter>
    <style>@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@700&amp;family=Share+Tech+Mono&amp;display=swap');</style>
  </defs>

  <rect width="{total_w}" height="200" rx="12" ry="12" fill="{CARD}" filter="url(#trophyShadow)"/>
  <rect x="1" y="1" width="{total_w-2}" height="198" rx="11" ry="11" fill="none"
        stroke="url(#trophyTitleGrad)" stroke-width="1.2" opacity="0.4"/>

  <!-- title -->
  <text x="{total_w//2}" y="22" text-anchor="middle"
        font-family="'Space Grotesk','Segoe UI',Arial,sans-serif"
        font-weight="700" font-size="13" fill="{TEXT}" letter-spacing="2">
    🏆 GitHub Trophies
  </text>

  {cells_svg}

  <!-- shine sweep across all trophies -->
  <g clip-path="url(#trophyClip)">
    <rect x="-200" y="0" width="180" height="200" fill="url(#shineGrad)">
      <animate attributeName="x" values="-200;{total_w+200}" dur="4s" begin="2s" repeatCount="indefinite"/>
    </rect>
  </g>
</svg>"""

with open(os.path.join(OUT, "trophies.svg"), "w", encoding="utf-8") as f:
    f.write(svg)
print("trophies.svg done!")
