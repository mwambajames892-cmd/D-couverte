import sys, pathlib
from playwright.sync_api import sync_playwright
src = pathlib.Path.home()/'motion-design-claude-code/presentation/styleframes'
names = sys.argv[1:] or [p.stem for p in sorted(src.glob('*.html'))]
(src/'png').mkdir(exist_ok=True)
with sync_playwright() as p:
    exe = '/opt/pw-browsers/chromium'
    try: b = p.chromium.launch(executable_path=exe, args=['--no-sandbox'])
    except Exception as e:
        import glob; c = glob.glob('/opt/pw-browsers/chromium*/chrome-linux*/chrome'); print('fallback', c); b = p.chromium.launch(executable_path=c[0], args=['--no-sandbox'])
    pg = b.new_page(viewport={'width':1080,'height':1920}, device_scale_factor=1)
    for n in names:
        pg.goto((src/f'{n}.html').as_uri()); pg.wait_for_load_state('networkidle')
        pg.evaluate('document.fonts.ready.then(()=>true)'); pg.wait_for_timeout(300)
        pg.screenshot(path=str(src/'png'/f'{n}.png')); print('ok', n)
    b.close()
