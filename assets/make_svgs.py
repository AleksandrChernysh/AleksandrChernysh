"""Generate the animated SVGs for the GitHub profile README.

header.svg  - name with an animated eye-tracking scanpath "reading" it
results.svg - key numbers from the signal-quality paper (arXiv:2610.32915)

Run with --static to also write *_static.svg (final frame, no animation) for previews.
"""
import sys
from pathlib import Path

OUT = Path(__file__).parent
STATIC = "--static" in sys.argv

BG1, BG2 = "#0b1220", "#132036"
ACCENT = "#4ea1ff"
ACCENT2 = "#7ee0c3"
TEXT = "#e6edf3"
MUTED = "#8b97a8"
FONT = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'SF Mono', Menlo, Consolas, 'DejaVu Sans Mono', monospace"

CYCLE = 9.0  # seconds per animation loop


def fade(begin, end_frac=0.86, peak=1.0, static=STATIC):
    """Opacity animation: invisible until `begin` (fraction of cycle), visible until end_frac."""
    if static:
        return "", f'opacity="{peak}"'
    a = max(begin, 0.001)
    b = min(a + 0.025, end_frac - 0.01)
    anim = (f'<animate attributeName="opacity" dur="{CYCLE}s" repeatCount="indefinite" '
            f'values="0;0;{peak};{peak};0" keyTimes="0;{a:.3f};{b:.3f};{end_frac};1"/>')
    return anim, 'opacity="0"'


def header(static=STATIC):
    w, h = 1200, 300
    # Fixations: (x, y, duration_ms). Reading order with one regression (fixation 5).
    fix = [(282, 118, 220), (372, 127, 260), (470, 121, 200), (566, 129, 300),
           (428, 124, 180), (716, 123, 240), (806, 130, 210), (902, 120, 280), (960, 128, 190)]
    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
                 f'role="img" aria-label="Aleksandr Chernysh - eye tracking, VR and eye-movement biometrics">')
    parts.append(f'''<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG1}"/><stop offset="1" stop-color="{BG2}"/></linearGradient>
  <radialGradient id="glow" cx="0.5" cy="0.45" r="0.6"><stop offset="0" stop-color="{ACCENT}" stop-opacity="0.16"/><stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/></radialGradient>
</defs>
<rect width="{w}" height="{h}" rx="18" fill="url(#bg)"/>
<rect width="{w}" height="{h}" rx="18" fill="url(#glow)"/>''')
    # calibration-grid dots
    dots = []
    for gx in range(80, w, 80):
        for gy in range(40, h, 55):
            dots.append(f'<circle cx="{gx}" cy="{gy}" r="1.3"/>')
    parts.append(f'<g fill="{MUTED}" opacity="0.18">{"".join(dots)}</g>')
    # 9-point calibration targets in the corners/edges (subtle)
    for cx, cy in [(60, 40), (1140, 40), (60, 260), (1140, 260)]:
        parts.append(f'<g stroke="{MUTED}" stroke-width="1.2" opacity="0.45" fill="none">'
                     f'<circle cx="{cx}" cy="{cy}" r="7"/><line x1="{cx-11}" y1="{cy}" x2="{cx+11}" y2="{cy}"/>'
                     f'<line x1="{cx}" y1="{cy-11}" x2="{cx}" y2="{cy+11}"/></g>')
    # name
    parts.append(f'<text x="600" y="150" text-anchor="middle" textLength="760" lengthAdjust="spacingAndGlyphs" '
                 f'font-family="{FONT}" font-size="74" font-weight="700" fill="{TEXT}">Aleksandr Chernysh</text>')
    # scanpath
    n = len(fix)
    start, step = 0.06, 0.075
    for i in range(n - 1):
        (x1, y1, _), (x2, y2, _) = fix[i], fix[i + 1]
        anim, op = fade(start + step * (i + 1) - 0.012, peak=0.6, static=static)
        regress = x2 < x1
        color = ACCENT2 if regress else ACCENT
        dash = ' stroke-dasharray="5 5"' if regress else ""
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.5"{dash} {op}>{anim}</line>')
    for i, (x, y, d) in enumerate(fix):
        r = 5 + d / 36
        anim, op = fade(start + step * i, static=static)
        parts.append(f'<g {op}>{anim}'
                     f'<circle cx="{x}" cy="{y}" r="{r:.1f}" fill="{ACCENT}" fill-opacity="0.35" stroke="{ACCENT}" stroke-width="1.6"/>'
                     f'<text x="{x}" y="{y - r - 5:.0f}" text-anchor="middle" font-family="{MONO}" font-size="11" font-weight="700" fill="{ACCENT}">{i + 1}</text></g>')
    # subtitle and labels
    parts.append(f'<text x="600" y="212" text-anchor="middle" font-family="{FONT}" font-size="23" fill="{MUTED}">'
                 f'Eye tracking  ·  VR headsets  ·  Eye-movement biometrics</text>')
    parts.append(f'<text x="600" y="246" text-anchor="middle" font-family="{FONT}" font-size="17" fill="{MUTED}" opacity="0.8">'
                 f'Data Science @ Texas State University  ·  OK Lab</text>')
    legend_anim, legend_op = fade(start + step * n, static=static)
    parts.append(f'<g {legend_op}>{legend_anim}<text x="1180" y="288" text-anchor="end" font-family="{MONO}" font-size="12" fill="{MUTED}">'
                 f'{n} fixations · {n - 1} saccades · 1 regression</text></g>')
    parts.append(f'<text x="20" y="288" font-family="{MONO}" font-size="12" fill="{MUTED}" opacity="0.8">● REC  gaze @ 90 Hz</text>')
    parts.append("</svg>")
    return "\n".join(parts)


def results(static=STATIC):
    w, h = 1200, 330
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
             f'aria-label="Key results: median participant mean error 1.04 degrees Quest Pro, 1.50 Pro Eye, 2.41 Focus Vision">']
    parts.append(f'''<defs><linearGradient id="bg2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG1}"/><stop offset="1" stop-color="{BG2}"/></linearGradient></defs>
<rect width="{w}" height="{h}" rx="18" fill="url(#bg2)"/>''')
    parts.append(f'<text x="40" y="52" font-family="{FONT}" font-size="25" font-weight="700" fill="{TEXT}">What mean error misses</text>')
    parts.append(f'<text x="40" y="80" font-family="{FONT}" font-size="15" fill="{MUTED}">30 participants · 3 VR headsets · one protocol · first author · arXiv:2610.32915</text>')
    # bars: median participant mean error (deg)
    parts.append(f'<text x="40" y="122" font-family="{FONT}" font-size="14" font-weight="600" fill="{MUTED}">MEDIAN PARTICIPANT MEAN ERROR</text>')
    bars = [("Meta Quest Pro", 1.04), ("HTC VIVE Pro Eye", 1.50), ("HTC VIVE Focus Vision", 2.41)]
    scale = 150  # px per degree
    for i, (name, val) in enumerate(bars):
        y = 145 + i * 52
        bw = val * scale
        parts.append(f'<text x="40" y="{y + 20}" font-family="{FONT}" font-size="16" fill="{TEXT}">{name}</text>')
        parts.append(f'<rect x="230" y="{y + 4}" width="{3 * scale}" height="22" rx="5" fill="{MUTED}" opacity="0.12"/>')
        if static:
            parts.append(f'<rect x="230" y="{y + 4}" width="{bw:.0f}" height="22" rx="5" fill="{ACCENT}"/>')
        else:
            parts.append(f'<rect x="230" y="{y + 4}" width="{bw:.0f}" height="22" rx="5" fill="{ACCENT}">'
                         f'<animate attributeName="width" from="0" to="{bw:.0f}" dur="1.2s" begin="{0.2 + i * 0.25:.2f}s" fill="freeze"/></rect>')
        parts.append(f'<text x="{230 + bw + 10:.0f}" y="{y + 20}" font-family="{MONO}" font-size="16" font-weight="700" fill="{TEXT}">{val:.2f}°</text>')
    # divider
    parts.append(f'<line x1="760" y1="110" x2="760" y2="295" stroke="{MUTED}" stroke-opacity="0.25"/>')
    stats = [("6.04 s", "longest Quest Pro pause hidden in the stream"),
             ("100%", "of Quest Pro samples flagged valid with eyes closed"),
             ("9.8×", "Focus Vision dispersion vs. sample-to-sample RMS")]
    for i, (big, small) in enumerate(stats):
        y = 130 + i * 64
        parts.append(f'<text x="790" y="{y + 10}" font-family="{FONT}" font-size="30" font-weight="700" fill="{ACCENT2}">{big}</text>')
        parts.append(f'<text x="790" y="{y + 32}" font-family="{FONT}" font-size="14" fill="{MUTED}">{small}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


if __name__ == "__main__":
    (OUT / "header.svg").write_text(header(static=False))
    (OUT / "results.svg").write_text(results(static=False))
    if STATIC:
        (OUT / "header_static.svg").write_text(header(static=True))
        (OUT / "results_static.svg").write_text(results(static=True))
    print("written")
