with open('banner.svg', encoding='utf-8') as f:
    c = f.read()

checks = {
    'Dark BG (#0d0011)':        '#0d0011' in c,
    'Name HARSHITA YADAV':      'HARSHITA YADAV' in c,
    'Pacifico font':            'Pacifico' in c,
    'Name gradient animated':   'nameGrad' in c and 'stop-color' in c,
    'Terminal text':            'user@dev' in c,
    'Blinking cursor':          'term-cursor' in c,
    'Role Student':             'Student' in c,
    'Role Designer':            'Designer' in c,
    'Tagline':                  'designing intuitive experiences' in c,
    'Tech pill Figma':          'Figma' in c,
    'Tech pill Python':         'Python' in c,
    'About Me email':           'harshitaydv1024@gmail.com' in c,
    'Code editor buildDreams':  'buildDreams' in c,
    'Neon sign KEEP CODING':    'KEEP CODING' in c,
    'Neon flicker CSS':         'flicker' in c,
    'Hearts floating':          '\u2665' in c,
    'Sparkles twinkling':       '\u2726' in c,
    'Rising particles (circle)':'<circle' in c,
    'Ambient orbs pulsing':     'orb' in c.lower() or ('<circle' in c and 'indefinite' in c),
    'Character base64 PNG':     'data:image/png;base64,' in c,
    'Hologram reveal clipPath': 'holoReveal' in c,
    'Scan line gradient':       'scanGrad' in c,
    'Continuous scanner 3.5s':  '3.5s' in c,
    'Stats bar animated':       'barGrad' in c,
    'Banner clip rounded':      'bannerClip' in c,
    'No JavaScript':            '<script' not in c,
    'SMIL animate (90+ tags)':  c.count('<animate ') >= 90,
    'animateTransform (18+ tags)': c.count('animateTransform') >= 18,
    'CSS @keyframes':           '@keyframes' in c,
    'Vignette grads in defs':   c.index('id="vigL"') < c.index('</defs>'),
    'Handle harshitaydv24':     'harshitaydv24' in c,
}

ok = all(checks.values())
print('=== BANNER.SVG CHECKS ===')
for k,v in checks.items():
    print(f'  {"[OK]" if v else "[FAIL]"} {k}')
print(f'\nALL PASS: {ok}')

# Also check lanyard
with open('lanyard.svg', encoding='utf-8') as f:
    l = f.read()
lc = {
    'Barcode':          'barcode' in l.lower() or 'rect x=' in l,
    'Avatar circle':    'avatarClip' in l,
    'Holographic shine':'holoShine' in l,
    'Swing animation':  'animateTransform' in l,
    'Drop animation':   'translate' in l and '-520' in l,
    'Gentle sway':      'sway' in l.lower() or ('3s' in l and 'indefinite' in l),
    'Name on card':     'HARSHITA YADAV' in l,
    'Handle on card':   'harshitaydv24' in l,
    'Email on card':    'harshitaydv1024' in l,
    'ID label':         'DEVELOPER ID' in l or 'GITHUB' in l,
    'Character image':  'data:image/png;base64,' in l,
    'No script':        '<script' not in l,
}
print('\n=== LANYARD.SVG CHECKS ===')
for k,v in lc.items():
    print(f'  {"[OK]" if v else "[FAIL]"} {k}')
print(f'\nALL PASS: {all(lc.values())}')
