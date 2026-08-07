"""
Build lanyard.svg + stat cards + trophies for harshitaydv24.
"""
import os, sys

with open("char_b64.txt") as f:
    CHAR_B64 = f.read().strip()
IMG_DATA = f"data:image/png;base64,{CHAR_B64}"
OUT = os.path.dirname(os.path.abspath(__file__))

# ─────────────────────────────────────────────────────────────────────────────
#  LANYARD.SVG
# ─────────────────────────────────────────────────────────────────────────────
def build_lanyard():
    # Swing: damped oscillation encoded as discrete SMIL values
    # 18 frames over 2s then gentle sway
    swing_angles = [
        -35, 20, -12, 7, -4, 2.5, -1.5, 0.8, -0.5, 0.3, -0.2, 0.1, 0
    ]
    vals   = ";".join(str(a) for a in swing_angles)
    ktimes = ";".join(f"{i/(len(swing_angles)-1):.3f}" for i in range(len(swing_angles)))

    # gentle sway after damping (small amplitude)
    sway_vals = "0;1.5;0;-1.5;0"
    sway_kts  = "0;0.25;0.5;0.75;1"

    # Barcode strips (alternating widths, 50 strips)
    import random
    random.seed(42)
    bx = 50
    bc_strips = ""
    for _ in range(50):
        bw = random.choice([1,1,2,1,1,2,3,1])
        bc_strips += f'<rect x="{bx}" y="0" width="{bw}" height="28" fill="white"/>'
        bx += bw + random.choice([1,2])

    # Avatar circle: crop character centered on face area
    # Character is 400x533; face is roughly top 40% centered
    # We'll show y=0 to y=220, x=100 to x=300 → 200x220 cropped
    # In SVG, use clipPath circle + image positioned to show face

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
  width="280" height="520" viewBox="0 0 280 520"
  role="img" aria-label="Harshita Yadav ID Badge">
  <title>Harshita Yadav — Lanyard Badge</title>
  <defs>
    <!-- gradients -->
    <linearGradient id="strapGrad" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="#c0006a"/>
      <stop offset="50%" stop-color="#ff4da6"/>
      <stop offset="100%" stop-color="#c44dff"/>
    </linearGradient>
    <linearGradient id="claspGrad" x1="0" y1="0" x2="0" y2="1" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="#e0e0e0"/>
      <stop offset="50%" stop-color="#aaaaaa"/>
      <stop offset="100%" stop-color="#cccccc"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0" y1="0" x2="0" y2="1" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="#1a0028"/>
      <stop offset="100%" stop-color="#0d0018"/>
    </linearGradient>
    <linearGradient id="avatarRingGrad" x1="0" y1="0" x2="1" y2="1" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="#ff4da6">
        <animate attributeName="stop-color" values="#ff4da6;#c44dff;#ff4da6" dur="3s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#c44dff">
        <animate attributeName="stop-color" values="#c44dff;#ff4da6;#c44dff" dur="3s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    <linearGradient id="holoShine" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="white" stop-opacity="0"/>
      <stop offset="40%" stop-color="white" stop-opacity="0.18"/>
      <stop offset="60%" stop-color="white" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="white" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="barcodeGrad" x1="0" y1="0" x2="0" y2="1" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="#ff4da6" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#c44dff" stop-opacity="0.3"/>
    </linearGradient>

    <!-- clip paths -->
    <clipPath id="avatarCircle">
      <circle cx="140" cy="82" r="48"/>
    </clipPath>
    <clipPath id="cardClip">
      <rect x="25" y="98" width="230" height="310" rx="16" ry="16"/>
    </clipPath>
    <clipPath id="lanyardClip">
      <rect x="0" y="0" width="280" height="520"/>
    </clipPath>

    <!-- filters -->
    <filter id="avatarGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="#ff4da6" flood-opacity="0.9"/>
      <feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="#c44dff" flood-opacity="0.5"/>
    </filter>
    <filter id="cardGlow" x="-8%" y="-5%" width="116%" height="115%">
      <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#ff4da6" flood-opacity="0.4"/>
      <feDropShadow dx="0" dy="0" stdDeviation="4"  flood-color="#c44dff" flood-opacity="0.3"/>
    </filter>
    <filter id="strapShadow" x="-20%" y="-5%" width="140%" height="110%">
      <feDropShadow dx="2" dy="0" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- ── drop + swing animation group ─────────────────────────────────────── -->
  <!-- Drop from top, then swing with damped physics -->
  <g id="wholeCard">
    <!-- Initial drop from y=-520 to y=0 -->
    <animateTransform attributeName="transform" type="translate"
      values="0,-520;0,0" keyTimes="0;1" dur="0.8s" begin="0s" fill="freeze" additive="replace"/>

    <!-- Damped swing after drop, pivot at strap top center (140,0) -->
    <animateTransform attributeName="transform" type="rotate"
      values="{vals}" keyTimes="{ktimes}"
      dur="2.0s" begin="0.8s" fill="freeze" additive="sum"/>

    <!-- Gentle sway after damping -->
    <animateTransform attributeName="transform" type="rotate"
      values="{sway_vals}" keyTimes="{sway_kts}"
      dur="3s" begin="2.8s" repeatCount="indefinite" additive="sum"/>
  </g>

  <!-- ── STRAP ──────────────────────────────────────────────────────────── -->
  <!-- Left strap leg -->
  <polygon points="130,0 150,0 148,115 132,115" fill="url(#strapGrad)" filter="url(#strapShadow)"/>
  <!-- Strap text repeated -->
  <text font-family="'Courier New',monospace" font-size="7" fill="rgba(255,255,255,0.3)" transform="rotate(-90)">
    <tspan x="-110" y="142.5">HARSHITA YADAV · STUDENT · DESIGNER</tspan>
  </text>

  <!-- ── METAL CLASP ────────────────────────────────────────────────────── -->
  <rect x="123" y="96" width="34" height="22" rx="4" ry="4" fill="url(#claspGrad)"/>
  <ellipse cx="140" cy="107" rx="10" ry="10" fill="url(#claspGrad)" stroke="#888" stroke-width="0.5"/>
  <!-- Ring bolt -->
  <circle cx="140" cy="92" r="7" fill="none" stroke="url(#claspGrad)" stroke-width="3"/>
  <circle cx="140" cy="92" r="4" fill="#bbbbbb"/>

  <!-- ── CARD BODY ──────────────────────────────────────────────────────── -->
  <rect x="25" y="108" width="230" height="310" rx="16" ry="16"
        fill="url(#cardGrad)" filter="url(#cardGlow)"
        stroke="#3a0058" stroke-width="1.5"/>

  <!-- card inner glow border -->
  <rect x="27" y="110" width="226" height="306" rx="15" ry="15"
        fill="none" stroke="url(#avatarRingGrad)" stroke-width="0.8" opacity="0.5"/>

  <!-- ── AVATAR ───────────────────────────────────────────────────────────── -->
  <!-- Glowing avatar ring -->
  <circle cx="140" cy="170" r="52" fill="none" stroke="url(#avatarRingGrad)" stroke-width="3"
          filter="url(#avatarGlow)">
    <animate attributeName="stroke-width" values="3;5;3" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="140" cy="170" r="49" fill="#0d0018"/>
  <!-- Character image clipped to circle, showing upper body/face -->
  <clipPath id="avatarClip2">
    <circle cx="140" cy="170" r="48"/>
  </clipPath>
  <image href="{IMG_DATA}"
         x="52" y="141" width="220" height="293"
         clip-path="url(#avatarClip2)"
         preserveAspectRatio="xMidYMin slice"/>

  <!-- ── NAME ──────────────────────────────────────────────────────────── -->
  <text x="140" y="238" text-anchor="middle"
        font-family="'Segoe UI','Arial',sans-serif"
        font-weight="700" font-size="14.5"
        fill="white" letter-spacing="1">HARSHITA YADAV</text>

  <!-- ── ROLE ──────────────────────────────────────────────────────────── -->
  <rect x="80" y="244" width="120" height="18" rx="9" fill="rgba(255,77,166,0.2)" stroke="#ff4da6" stroke-width="0.8"/>
  <text x="140" y="257" text-anchor="middle"
        font-family="'Courier New',monospace" font-size="9.5"
        fill="#ff80cc" letter-spacing="1.5">STUDENT</text>

  <!-- ── HANDLE ─────────────────────────────────────────────────────────── -->
  <text x="140" y="278" text-anchor="middle"
        font-family="'Courier New',monospace" font-size="10"
        fill="#c44dff">@harshitaydv24</text>

  <!-- ── SKILLS ─────────────────────────────────────────────────────────── -->
  <text x="140" y="298" text-anchor="middle"
        font-family="'Segoe UI','Arial',sans-serif" font-size="9"
        fill="rgba(255,255,255,0.5)">Design · Code · Create</text>

  <!-- divider -->
  <rect x="50" y="307" width="180" height="1" fill="url(#avatarRingGrad)" opacity="0.4"/>

  <!-- ── EMAIL ──────────────────────────────────────────────────────────── -->
  <text x="140" y="323" text-anchor="middle"
        font-family="'Courier New',monospace" font-size="8.5"
        fill="rgba(255,255,255,0.4)">harshitaydv1024@gmail.com</text>

  <!-- ── BARCODE ─────────────────────────────────────────────────────────── -->
  <rect x="45" y="330" width="190" height="38" rx="4" fill="rgba(255,77,166,0.05)"/>
  <g transform="translate(45,334)">
    {bc_strips}
  </g>
  <text x="140" y="378" text-anchor="middle"
        font-family="'Courier New',monospace" font-size="7.5"
        fill="rgba(255,255,255,0.25)" letter-spacing="2">2024-HYADAV-GH24</text>

  <!-- ── ID label ───────────────────────────────────────────────────────── -->
  <rect x="50" y="388" width="180" height="16" rx="3" fill="rgba(196,77,255,0.1)"/>
  <text x="140" y="400" text-anchor="middle"
        font-family="'Courier New',monospace" font-size="8" letter-spacing="2"
        fill="rgba(196,77,255,0.6)">GITHUB DEVELOPER ID</text>

  <!-- ── HOLOGRAPHIC SHINE SWEEP ─────────────────────────────────────────── -->
  <g clip-path="url(#cardClip)">
    <rect x="25" y="108" width="80" height="310" fill="url(#holoShine)" opacity="0">
      <animate attributeName="x" values="25;220" dur="3s" begin="1s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;0.9;0" keyTimes="0;0.5;1" dur="3s" begin="1s" repeatCount="indefinite"/>
    </rect>
  </g>
</svg>"""
    return svg

print("Writing lanyard.svg...")
with open(os.path.join(OUT, "lanyard.svg"), "w", encoding="utf-8") as f:
    f.write(build_lanyard())
print("Done!")
