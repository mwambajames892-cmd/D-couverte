import pathlib
ticks = ''
for sec in range(0, 37):
    x = 70 + 940*sec/36.68
    big = sec % 5 == 0
    h = 26 if big else 14
    ticks += f'<i class="h1-tick" style="left:{x:.1f}px;top:{176-h}px;height:{h}px"></i>'
    if big and sec: ticks += f'<b class="h1-tlab" style="left:{x+6:.1f}px">00:{sec:02d}</b>'
HEART='<svg width="58" height="58" viewBox="0 0 24 24" fill="none" stroke="#0B2229" stroke-width="2" stroke-linejoin="round"><path d="M12 21s-7.5-4.6-9.6-9.2C.9 8.4 2.6 4.5 6.4 4.5c2.2 0 3.7 1.2 5.6 3.3 1.9-2.1 3.4-3.3 5.6-3.3 3.8 0 5.5 3.9 4 7.3C19.5 16.4 12 21 12 21z"/></svg>'
COMM='<svg width="58" height="58" viewBox="0 0 24 24" fill="none" stroke="#0B2229" stroke-width="2" stroke-linejoin="round"><path d="M21 11.5a8.5 8.5 0 0 1-12.4 7.5L3 20.5l1.6-5.2A8.5 8.5 0 1 1 21 11.5z"/></svg>'
SEND='<svg width="58" height="58" viewBox="0 0 24 24" fill="none" stroke="#0B2229" stroke-width="2" stroke-linejoin="round"><path d="M22 2 11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg>'
def post(id_, name, img):
    return (f'<div id="{id_}" class="h1-post"><div class="h1-hd"><div class="h1-av"><i></i></div><div class="h1-nm">{name}<small>à l\'instant</small></div></div>'
            f'<div class="h1-media"><img src="assets/img/fx/{img}" alt=""></div><div class="h1-acts"><span class="h1-ic">{HEART}</span><span class="h1-ic">{COMM}</span><span class="h1-ic">{SEND}</span></div>'
            '<div class="h1-bar" style="width:92%"></div><div class="h1-bar" style="width:62%"></div></div>')
def w(t, txt, cls=''): return f'<span class="h1-sw {cls}" data-cue="{t:.2f}">{txt}</span>'
sub1 = w(0.00,'Pourquoi')+' '+w(0.30,'certaines')+' '+w(0.70,'vidéos')
sub2 = w(1.10,'te')+' '+w(1.30,'gardent')+' <span class="h1-ink"><i class="h1-inkbg" data-trace="1.58"></i><span class="h1-inktx">'+w(1.64,"jusqu'à",'inb')+' '+w(2.06,'la','inb')+' '+w(2.16,'fin','inb')+'</span></span> '+w(2.38,'?')
sub3 = w(2.98,'Et')+' '+w(3.06,"d'autres")+' <span class="h1-ink"><i class="h1-inkbg" data-trace="3.18"></i><span class="h1-inktx">'+w(3.26,'non.','inb')+'</span></span>'

CSS = r'''
@font-face { font-family: "Inter"; src: url("assets/fonts/Inter-Medium.otf") format("opentype"); font-weight: 500; }
@font-face { font-family: "Inter"; src: url("assets/fonts/Inter-Bold.otf") format("opentype"); font-weight: 700; }
@font-face { font-family: "Inter"; src: url("assets/fonts/Inter-ExtraBold.otf") format("opentype"); font-weight: 800; }
@font-face { font-family: "JetBrains Mono"; src: url("assets/fonts/JetBrainsMono-Bold.ttf") format("truetype"); font-weight: 700; }
#root { position: relative; width: 1080px; height: 1920px; overflow: hidden; font-family: "Inter", sans-serif; color: #0B2229; -webkit-font-smoothing: antialiased; }
.h1-layer { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; }
.h1-ground { background: radial-gradient(ellipse 1100px 1300px at 50% 30%, #FBF9F4 0%, #F1EEE7 55%, #E4DFD3 100%); }
.h1-vig { pointer-events: none; background: radial-gradient(ellipse at 50% 42%, rgba(11,34,41,0) 55%, rgba(11,34,41,.14) 100%); }
.h1-grain { pointer-events: none; opacity: .14; mix-blend-mode: multiply; background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>"); }
.h1-tick { position: absolute; width: 2px; background: rgba(11,34,41,.28); }
.h1-tlab { position: absolute; top: 118px; font: 700 19px "JetBrains Mono", monospace; color: rgba(11,34,41,.64); }
.h1-rail { position: absolute; left: 70px; top: 176px; width: 940px; height: 8px; border-radius: 5px; background: #D9E4E4; }
.h1-fill { position: absolute; left: 70px; top: 176px; width: 940px; height: 8px; border-radius: 5px; background: #0C7F8F; transform-origin: 0 50%; }
.h1-phw { position: absolute; left: 70px; top: 0; width: 0; height: 200px; }
.h1-ph { position: absolute; left: -2px; top: 96px; width: 4px; height: 104px; background: #0C7F8F; box-shadow: 0 0 18px rgba(12,127,143,.6); }
.h1-ph::before { content: ""; position: absolute; top: -6px; left: -12px; border-left: 14px solid transparent; border-right: 14px solid transparent; border-top: 20px solid #0C7F8F; }
.h1-tc { position: absolute; left: -48px; top: 56px; width: 96px; height: 40px; border-radius: 8px; background: #0C7F8F; }
.h1-tc b { position: absolute; left: 0; top: 0; width: 96px; text-align: center; font: 800 24px/40px "JetBrains Mono", monospace; color: #fff; opacity: 0; }
.h1-q { position: absolute; left: 520px; top: 200px; opacity: 0; }
.h1-post { box-sizing: border-box; position: absolute; left: 90px; width: 900px; background: #fff; border-radius: 44px; padding: 34px; box-shadow: 0 40px 90px rgba(11,34,41,.22), 0 0 0 2px rgba(11,34,41,.06); }
.h1-hd { display: flex; align-items: center; gap: 22px; height: 92px; }
.h1-av { width: 84px; height: 84px; border-radius: 50%; background: conic-gradient(from 200deg, #0C7F8F, #7fd0da, #0C7F8F); padding: 5px; flex: none; }
.h1-av i { display: block; width: 100%; height: 100%; border-radius: 50%; background: #0B2229; }
.h1-nm { font: 800 34px "Inter", sans-serif; color: #0B2229; }
.h1-nm small { display: block; font: 500 26px "Inter", sans-serif; color: #78898D; margin-top: 2px; }
.h1-media { position: relative; height: 560px; border-radius: 28px; overflow: hidden; margin-top: 6px; }
.h1-media img { width: 100%; height: 100%; object-fit: cover; display: block; }
.h1-acts { display: flex; gap: 34px; margin-top: 26px; align-items: center; }
.h1-ic { display: inline-block; opacity: .25; }
.h1-bar { height: 22px; border-radius: 12px; background: #E8E4DA; margin-top: 16px; transform-origin: 0 50%; }
.h1-chart { position: absolute; left: 560px; top: 960px; width: 430px; height: 310px; padding: 20px; border-radius: 26px; background: #fff; box-shadow: 0 26px 60px rgba(11,34,41,.28), 0 0 0 6px #fff; opacity: 0; }
.h1-sub { position: absolute; left: 0; top: 1420px; width: 1080px; text-align: center; font: 800 64px/77px "Inter", sans-serif; letter-spacing: -.01em; color: #0B2229; white-space: nowrap; }
.h1-sw { display: inline-block; opacity: 0; }
.h1-ink { position: relative; display: inline-block; margin: 0 14px; }
.h1-inkbg { position: absolute; left: -16px; right: -16px; top: 4px; bottom: 0; border-radius: 12px; background: #0C7F8F; transform-origin: 0 50%; transform: scaleX(0); }
.h1-inktx { position: relative; }
.h1-sw.inb { color: #fff; }
'''
BODY = f'''
  <div id="root" data-composition-id="01-hook" data-width="1080" data-height="1920" data-duration="3.98">
    <div id="h1-ground" class="clip h1-layer h1-ground" data-start="0" data-duration="3.98" data-track-index="0"></div>
    <div id="h1-header" class="clip h1-layer" data-start="0" data-duration="3.98" data-track-index="2" style="z-index:3">
      <div class="h1-rail"></div><div id="h1-fill" class="h1-fill"></div>{ticks}
      <div id="h1-phw" class="h1-phw"><div class="h1-ph"></div><div class="h1-tc"><b id="h1-t0">00:00</b><b id="h1-t1">00:01</b><b id="h1-t2">00:02</b><b id="h1-t3">00:03</b></div></div>
    </div>
    <div id="h1-world" class="clip h1-layer" data-start="0" data-duration="3.98" data-track-index="1" style="z-index:2">
      <svg id="h1-q" class="h1-q" width="560" height="1000" viewBox="0 0 560 1000" aria-hidden="true"><path d="M110,250 C110,50 470,50 470,290 C470,470 290,500 290,660" fill="none" stroke="#0C7F8F" stroke-width="40" stroke-linecap="round"/><circle cx="290" cy="830" r="36" fill="#0C7F8F"/></svg>
      {post('h1-postA','@createur','createur.jpg').replace('class="h1-post"','class="h1-post" style="top:270px"')}
      <div id="h1-chart" class="h1-chart"><svg width="390" height="270" viewBox="0 0 390 270">
        <defs><mask id="h1-mk" maskUnits="userSpaceOnUse" x="0" y="0" width="390" height="270"><path id="h1-mkp" d="M0,30 C80,40 120,150 190,200 S300,240 380,244" fill="none" stroke="#fff" stroke-width="14"/></mask></defs>
        <line x1="0" y1="250" x2="390" y2="250" stroke="#cfd8d8" stroke-width="3"/>
        <g id="h1-grey"><path d="M0,30 C80,40 120,150 190,200 S300,240 380,244" fill="none" stroke="#8aa0a4" stroke-width="6" stroke-linecap="round" stroke-dasharray="2 14" mask="url(#h1-mk)"/>
        <text id="h1-lab2" x="185" y="236" font-family="JetBrains Mono" font-weight="700" font-size="19" fill="#6c8387">LES AUTRES</text></g>
        <path id="h1-teal" d="M0,30 C80,34 220,44 380,56" fill="none" stroke="#0C7F8F" stroke-width="9" stroke-linecap="round"/>
        <circle id="h1-dot" cx="380" cy="56" r="13" fill="#0C7F8F" opacity="0"/>
        <text id="h1-lab1" x="150" y="112" font-family="JetBrains Mono" font-weight="700" font-size="19" fill="#0B5560" opacity="0">JUSQU'À LA FIN</text></svg></div>
      {post('h1-postB','@video.en.cours','cinema.jpg').replace('class="h1-post"','class="h1-post" style="top:1640px"')}
    </div>
    <div id="h1-subs" class="clip h1-layer" data-start="0" data-duration="3.98" data-track-index="3" style="z-index:4">
      <div id="h1-s1" class="h1-sub">{sub1}</div><div id="h1-s2" class="h1-sub">{sub2}</div><div id="h1-s3" class="h1-sub">{sub3}</div>
    </div>
    <div id="h1-vig" class="clip h1-layer h1-vig" data-start="0" data-duration="3.98" data-track-index="4" style="z-index:5"></div>
    <div id="h1-grain" class="clip h1-layer h1-grain" data-start="0" data-duration="3.98" data-track-index="5" style="z-index:6"></div>
  </div>
'''
JS = r'''
  <script src="assets/vendor/gsap-3.14.2.min.js"></script>
  <script>
    (function () {
      var FID = "01-hook", DUR = 3.98;
      var root = document.querySelector('[data-composition-id="' + FID + '"]');
      function $(n) { return root.querySelector("#h1-" + n); }
      function qa(sel) { return Array.prototype.slice.call(root.querySelectorAll(sel)); }
      var tl = gsap.timeline({ paused: true });
      function ft(el, a, b, t) { b.immediateRender = (t === 0 || t === 0.04); tl.fromTo(el, a, b, t); }
      function fl(el, a, b, t) { b.immediateRender = false; tl.fromTo(el, a, b, t); }

      // état de départ = handoff_in : le post « @createur » énorme et flou, la règle vide
      gsap.set($("postA"), { rotation: -1.2, transformOrigin: "50% 50%" });
      gsap.set($("chart"), { rotation: 4, transformOrigin: "50% 50%" });
      gsap.set($("postB"), { scale: 0.9, transformOrigin: "50% 0%", filter: "blur(7px)", opacity: 0.75 });
      gsap.set($("fill"), { scaleX: 0 });
      gsap.set($("t0"), { opacity: 1 });

      // ---------- la règle de temps : linéaire pendant toute la séquence (x 70 → 172 à 3.98 s) ----------
      tl.fromTo($("fill"), { scaleX: 0 }, { scaleX: 102 / 940, duration: DUR, ease: "none", immediateRender: true }, 0);
      tl.fromTo($("phw"), { x: 0 }, { x: 102, duration: DUR, ease: "none", immediateRender: true }, 0);
      [["t0", "t1", 1.0], ["t1", "t2", 2.0], ["t2", "t3", 3.0]].forEach(function (s) {
        tl.set($(s[0]), { opacity: 0 }, s[2]); tl.set($(s[1]), { opacity: 1 }, s[2]);
      });

      // ---------- dérive linéaire du fil : +30 u/s vers le haut, sous tout le monde ----------
      tl.fromTo($("world"), { y: 0 }, { y: -30 * DUR, duration: DUR, ease: "none", immediateRender: true }, 0);

      // ---------- scène 1 (0.00 à 1.10) : le post se pose sous le flou ----------
      ft($("postA"), { scale: 2.3, filter: "blur(14px)" }, { scale: 1, filter: "blur(0px)", duration: 0.4, ease: "expo.out" }, 0.04);
      fl($("q"), { opacity: 0 }, { opacity: 0.2, duration: 0.2, ease: "power1.out" }, 0.30);
      qa("#h1-postA .h1-ic").forEach(function (ic, i) { fl(ic, { opacity: 0.25 }, { opacity: 1, duration: 0.12, ease: "power1.out" }, 0.55 + 0.12 * i); });

      // ---------- scène 2 (1.10 à 2.98) : la carte de courbes tient jusqu'à la fin ----------
      fl($("chart"), { opacity: 0, scale: 1.6, x: 120, y: 120, filter: "blur(12px)" }, { opacity: 1, scale: 1, x: 0, y: 0, filter: "blur(0px)", duration: 0.35, ease: "expo.out" }, 1.30);
      var teal = $("teal"), len = teal.getTotalLength();
      gsap.set(teal, { strokeDasharray: len, strokeDashoffset: len });
      var mkp = $("mkp"), mlen = mkp.getTotalLength();
      gsap.set(mkp, { strokeDasharray: mlen, strokeDashoffset: mlen });
      gsap.set($("lab2"), { opacity: 0 });
      fl(mkp, { strokeDashoffset: mlen }, { strokeDashoffset: 0, duration: 0.7, ease: "power2.out" }, 1.60);
      fl($("lab2"), { opacity: 0 }, { opacity: 1, duration: 0.15, ease: "power1.out" }, 2.10);
      fl(teal, { strokeDashoffset: len }, { strokeDashoffset: 0, duration: 0.5, ease: "power2.out" }, 1.90);
      fl($("lab1"), { opacity: 0 }, { opacity: 1, duration: 0.15, ease: "power1.out" }, 2.20);
      fl($("dot"), { opacity: 0, scale: 0.4, transformOrigin: "380px 56px" }, { opacity: 1, scale: 1, duration: 0.12, ease: "expo.out" }, 2.38);
      fl($("dot"), { scale: 1 }, { scale: 1.6, duration: 0.15, ease: "sine.out" }, 2.50);
      fl($("dot"), { scale: 1.6 }, { scale: 1, duration: 0.15, ease: "sine.in" }, 2.65);
      var bars = qa("#h1-postA .h1-bar");
      fl(bars, { x: 0 }, { x: -30, duration: 0.3, ease: "power2.out" }, 2.55);
      // petit cran vers la carte (échelle 1 → 1,06)
      fl($("postA"), { scale: 1 }, { scale: 1.03, duration: 0.2, ease: "expo.out" }, 1.30);

      // ---------- scène 3 (2.98 à 3.98) : « non », la courbe grise tombe, le fil monte d'un cran ----------
      fl($("grey"), { y: 0 }, { y: 28, duration: 0.15, ease: "power2.in" }, 3.26);
      var old = [$("postA"), $("chart"), $("q")];
      fl(old, { y: 0 }, { y: -1500, duration: 0.5, ease: "power2.in" }, 3.40);
      fl([$("postA"), $("chart")], { filter: "blur(0px)" }, { filter: "blur(12px)", duration: 0.4, ease: "power1.in" }, 3.40);
      // le post suivant (« @video.en.cours ») monte d'un trait : linéaire, flou 10 px à la couture (media top y 700 à 3.98)
      fl($("postB"), { y: 0, scale: 0.9, filter: "blur(7px)", opacity: 0.75 }, { y: -953, scale: 1, filter: "blur(10px)", opacity: 1, duration: 0.46, ease: "none" }, 3.52);

      // ---------- la phrase : mot par mot (temps locaux), trois morceaux qui se remplacent ----------
      qa(".h1-sub .h1-sw").forEach(function (wd) {
        var t0 = parseFloat(wd.getAttribute("data-cue")), inb = wd.classList.contains("inb");
        fl(wd, { opacity: 0, y: 10, filter: "blur(6px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.14, ease: "power2.out" }, t0);
        if (!inb) fl(wd, { color: "rgba(11,34,41,0.35)" }, { color: "rgba(11,34,41,1)", duration: 0.2, ease: "power1.out" }, t0 + 0.08);
      });
      qa(".h1-inkbg").forEach(function (b) { fl(b, { scaleX: 0 }, { scaleX: 1, duration: 0.16, ease: "power3.out" }, parseFloat(b.getAttribute("data-trace"))); });
      function subOut(id, t0) {
        var els = qa("#h1-" + id + " .h1-sw").concat(qa("#h1-" + id + " .h1-inkbg"));
        fl(els, { opacity: 1, filter: "blur(0px)" }, { opacity: 0, filter: "blur(6px)", duration: 0.12, ease: "power2.in" }, t0);
      }
      subOut("s1", 1.02); subOut("s2", 2.84); subOut("s3", 3.74);

      tl.set({}, {}, DUR);
      window.__timelines = window.__timelines || {};
      window.__timelines[FID] = tl;
    })();
  </script>
'''
out = '<template>\n  <style>' + CSS + '</style>\n' + BODY + JS + '</template>\n'
pathlib.Path.home().joinpath('motion-design-claude-code/presentation/compositions/frames/01-hook.html').write_text(out, encoding='utf-8')
print(len(out))
