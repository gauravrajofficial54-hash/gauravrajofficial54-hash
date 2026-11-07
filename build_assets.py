#!/usr/bin/env python3
"""Generates all animated SVG assets for Gaurav's GitHub profile.

Usage:
    python3 build_assets.py                 # builds everything with a placeholder photo
    python3 build_assets.py my_photo.jpg    # builds everything with YOUR photo embedded
"""
import base64, math, mimetypes, os, sys

OUT = "assets"
os.makedirs(OUT, exist_ok=True)

GOLD, GREEN, DARK, DEEP = "#F5B301", "#22C55E", "#0B1210", "#052e16"


# ------------------------------------------------------------------ HEADER
def header():
    cubes = ""
    spots = [(120, 70, 34, 7), (880, 90, 42, 9), (230, 235, 24, 6), (790, 225, 30, 8), (500, 40, 20, 5)]
    for i, (x, y, s, d) in enumerate(spots):
        h = s * 0.5
        cubes += f"""
  <g transform="translate({x} {y})">
    <g>
      <animateTransform attributeName="transform" type="translate" values="0 0;0 -16;0 0" dur="{d}s" repeatCount="indefinite" calcMode="spline" keySplines=".4 0 .6 1;.4 0 .6 1" keyTimes="0;.5;1"/>
      <g>
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="{d*3}s" repeatCount="indefinite"/>
        <polygon points="0,{-s} {s*0.87},{-h} 0,0 {-s*0.87},{-h}" fill="url(#top)"/>
        <polygon points="{-s*0.87},{-h} 0,0 0,{s} {-s*0.87},{s-h}" fill="url(#left)"/>
        <polygon points="{s*0.87},{-h} 0,0 0,{s} {s*0.87},{s-h}" fill="url(#right)"/>
      </g>
    </g>
  </g>"""
    grid = ""
    for i in range(-10, 11):
        grid += f'<line x1="{500 + i*30}" y1="190" x2="{500 + i*130}" y2="300" stroke="{GREEN}" stroke-opacity=".35"/>'
    for k in range(6):
        y = 190 + (k ** 1.7) * 6.2
        grid += f'<line x1="0" y1="{y:.1f}" x2="1000" y2="{y:.1f}" stroke="{GREEN}" stroke-opacity=".3"/>'
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300" width="1000" height="300">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{DEEP}"/><stop offset=".5" stop-color="{DARK}"/><stop offset="1" stop-color="#166534"/>
  </linearGradient>
  <linearGradient id="txt" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#fff"/><stop offset=".5" stop-color="{GOLD}"/><stop offset="1" stop-color="#fff"/>
    <animate attributeName="x1" values="-1;1" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="x2" values="0;2" dur="4s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="top" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{GOLD}"/><stop offset="1" stop-color="#ffe08a"/></linearGradient>
  <linearGradient id="left" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#166534"/><stop offset="1" stop-color="{DEEP}"/></linearGradient>
  <linearGradient id="right" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{GREEN}"/><stop offset="1" stop-color="#166534"/></linearGradient>
  <filter id="glow"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="1000" height="300" fill="url(#bg)" rx="18"/>
<g>{grid}</g>
<rect y="190" width="1000" height="2" fill="{GOLD}" opacity=".6"><animate attributeName="opacity" values=".2;.9;.2" dur="3s" repeatCount="indefinite"/></rect>
{cubes}
<g filter="url(#glow)">
  <text x="500" y="135" text-anchor="middle" font-family="'Segoe UI',Arial,sans-serif" font-weight="900" font-size="78" letter-spacing="8" fill="url(#txt)">GAURAV KUMAR</text>
</g>
<text x="500" y="178" text-anchor="middle" font-family="'Courier New',monospace" font-size="22" fill="{GOLD}" letter-spacing="3">
  Tech Enthusiast • Student • Lifelong Learner
  <animate attributeName="opacity" values="0;1;1;1" keyTimes="0;.2;.9;1" dur="5s" repeatCount="indefinite"/>
</text>
</svg>
"""


# ------------------------------------------------------------------ PHOTO FRAME
def photo_frame(photo_path=None):
    if photo_path:
        mime = mimetypes.guess_type(photo_path)[0] or "image/jpeg"
        b64 = base64.b64encode(open(photo_path, "rb").read()).decode()
        photo = f'<image href="data:{mime};base64,{b64}" x="0" y="0" width="260" height="320" preserveAspectRatio="xMidYMid slice"/>'
    else:
        photo = f"""<rect width="260" height="320" fill="#10201a"/>
      <circle cx="130" cy="125" r="52" fill="#1d3a2d"/>
      <path d="M30 320 Q130 190 230 320Z" fill="#1d3a2d"/>
      <text x="130" y="295" text-anchor="middle" font-family="Arial" font-size="14" fill="{GOLD}">YOUR PHOTO HERE</text>"""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 460" width="400" height="460">
<defs>
  <linearGradient id="ring" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{GOLD}"/><stop offset="1" stop-color="{GREEN}"/></linearGradient>
  <clipPath id="card"><rect width="260" height="320" rx="26"/></clipPath>
  <radialGradient id="aura"><stop offset="0" stop-color="{GOLD}" stop-opacity=".35"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient>
  <linearGradient id="shine" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".35"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
  </linearGradient>
</defs>
<circle cx="200" cy="215" r="190" fill="url(#aura)"><animate attributeName="r" values="170;195;170" dur="5s" repeatCount="indefinite"/></circle>

<!-- 3D orbit rings -->
<g transform="translate(200 215)" fill="none" stroke="url(#ring)" stroke-width="2">
  <ellipse rx="185" ry="48" opacity=".7"><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="14s" repeatCount="indefinite"/></ellipse>
  <ellipse rx="185" ry="48" opacity=".5" transform="rotate(60)"><animateTransform attributeName="transform" type="rotate" from="60" to="420" dur="18s" repeatCount="indefinite"/></ellipse>
  <ellipse rx="185" ry="48" opacity=".5" transform="rotate(-60)"><animateTransform attributeName="transform" type="rotate" from="-60" to="-420" dur="22s" repeatCount="indefinite"/></ellipse>
</g>

<!-- floating + 3D tilting photo card -->
<g transform="translate(70 55)">
  <animateTransform attributeName="transform" type="translate" values="70 55;70 43;70 55" dur="4.5s" repeatCount="indefinite" calcMode="spline" keySplines=".4 0 .6 1;.4 0 .6 1" keyTimes="0;.5;1"/>
  <rect x="14" y="22" width="260" height="320" rx="26" fill="#000" opacity=".35"/>
  <g>
    <animateTransform attributeName="transform" type="skewY" values="-3;3;-3" dur="6s" repeatCount="indefinite"/>
    <g clip-path="url(#card)">
      {photo}
      <rect x="-300" width="140" height="320" fill="url(#shine)" transform="skewX(-20)">
        <animate attributeName="x" values="-300;420" dur="4s" repeatCount="indefinite"/>
      </rect>
    </g>
    <rect width="260" height="320" rx="26" fill="none" stroke="url(#ring)" stroke-width="5"/>
  </g>
</g>

<!-- orbiting sparks -->
<g>
  <circle r="7" fill="{GOLD}"><animateMotion dur="7s" repeatCount="indefinite" path="M200,215 m-185,0 a185,48 0 1,0 370,0 a185,48 0 1,0 -370,0"/></circle>
  <circle r="5" fill="{GREEN}"><animateMotion dur="9s" repeatCount="indefinite" begin="-3s" path="M200,215 m-185,0 a185,48 0 1,0 370,0 a185,48 0 1,0 -370,0"/></circle>
</g>
<text x="200" y="445" text-anchor="middle" font-family="'Courier New',monospace" font-size="18" fill="{GOLD}" letter-spacing="2">&lt; GAURAV KUMAR /&gt;</text>
</svg>
"""


# ------------------------------------------------------------------ SKILL ORBIT
def orbit():
    skills = [("Python", "#3776AB"), ("HTML", "#E34F26"), ("CSS", "#1572B6"), ("JS", "#F7DF1E"), ("Git", "#F05032"), ("GitHub", "#8b949e"), ("C", "#00599C")]
    n, dur = len(skills), 14
    path = "M500,170 m-330,0 a330,95 0 1,0 660,0 a330,95 0 1,0 -660,0"
    nodes = ""
    for i, (name, col) in enumerate(skills):
        begin = -dur * i / n
        txt = "#000" if name == "JS" else "#fff"
        nodes += f"""
<g>
  <animateMotion dur="{dur}s" repeatCount="indefinite" begin="{begin:.2f}s" path="{path}"/>
  <g>
    <animateTransform attributeName="transform" type="scale" values="1.25;.8;.55;.8;1.25" keyTimes="0;.25;.5;.75;1" dur="{dur}s" repeatCount="indefinite" begin="{begin:.2f}s"/>
    <circle r="36" fill="{col}" stroke="#fff" stroke-opacity=".5" stroke-width="3"/>
    <text y="6" text-anchor="middle" font-family="Arial" font-weight="800" font-size="16" fill="{txt}">{name}</text>
  </g>
</g>"""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 340" width="1000" height="340">
<defs><radialGradient id="core"><stop offset="0" stop-color="{GOLD}"/><stop offset="1" stop-color="#b57f00"/></radialGradient></defs>
<ellipse cx="500" cy="170" rx="330" ry="95" fill="none" stroke="{GREEN}" stroke-opacity=".4" stroke-dasharray="6 8"/>
<circle cx="500" cy="170" r="46" fill="url(#core)"><animate attributeName="r" values="42;50;42" dur="3s" repeatCount="indefinite"/></circle>
<text x="500" y="177" text-anchor="middle" font-family="'Courier New',monospace" font-weight="800" font-size="18" fill="{DARK}">SKILLS</text>
{nodes}
</svg>
"""


# ------------------------------------------------------------------ DIVIDER
def divider():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 24" width="1000" height="24">
<defs><linearGradient id="d" x1="0" x2="1"><stop offset="0" stop-color="{GREEN}" stop-opacity="0"/><stop offset=".5" stop-color="{GOLD}"/><stop offset="1" stop-color="{GREEN}" stop-opacity="0"/></linearGradient></defs>
<rect x="0" y="11" width="1000" height="2" fill="url(#d)"/>
<circle cy="12" r="5" fill="{GOLD}"><animate attributeName="cx" values="0;1000" dur="4s" repeatCount="indefinite"/></circle>
</svg>
"""


def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    photo = sys.argv[1] if len(sys.argv) > 1 else None
    write("header.svg", header())
    write("photo-frame.svg", photo_frame(photo))
    write("skills-orbit.svg", orbit())
    write("divider.svg", divider())
    print("Built assets" + (f" with photo: {photo}" if photo else " (placeholder photo)"))

