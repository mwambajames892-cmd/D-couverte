#!/usr/bin/env python3
"""Mixage du film « James Framotion » (44,68 s) : voix + musique + bruitages -> assets/audio/mix-<option>.wav
Usage : python3 tools-mix.py [A B C]   (sans argument : les trois options)
Voix : assets/audio/voix.mp3 posée à 0 s (aucune coupe : 36,68 s). Musique : assets/music/blueprint_for_progress.mp3, démarrée à 34,48 s
de son propre temps pour que son drop (46,78 s) tombe sur « Moi, c'est James » (12,3 s du film). Bruitages : ceux du storyboard (lignes SON).
"""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
SFX = os.path.join('..', '.claude', 'skills', 'media-use', 'audio', 'assets', 'sfx')
VOICE, MUSIC = 'assets/audio/voix.mp3', 'assets/music/blueprint_for_progress.mp3'
TOTAL, VOICE_END, LOGO_AT = 44.68, 36.68, 38.68
MUSIC_START = 46.78 - 12.30          # le drop du morceau tombe à 12.3 s du film
# [nom, temps du film, gain, (durée gardée pour un riser)]
EVENTS = [
 ['whoosh-short', 0.04, .50], ['ping', 1.30, .30], ['pop', 2.38, .40], ['whoosh', 3.55, .45],
 ['notification', 5.40, .50], ['whoosh-short', 7.22, .50], ['riser', 8.38, .30, 1.20],
 ['impact-bass-1', 9.68, .55], ['impact-bass-1', 12.26, .70], ['ping', 12.73, .32], ['pop', 13.18, .38],
 ['click', 14.16, .35], ['whoosh-short', 14.21, .45], ['click', 15.08, .35], ['click', 15.88, .35], ['whoosh-short', 16.06, .40],
 ['ping', 16.70, .30], ['click', 17.60, .35], ['click', 18.22, .35], ['pop', 18.46, .40],
 ['whoosh', 19.46, .45], ['pop', 20.21, .40], ['riser', 22.36, .22, 0.55],
 ['ping', 22.90, .30], ['pop', 23.00, .38], ['pop', 23.76, .38], ['pop', 24.52, .38], ['pop', 25.82, .45], ['pop', 26.68, .38], ['pop', 27.50, .38], ['pop', 28.14, .40], ['whoosh', 28.20, .45],
 ['pop', 28.86, .38], ['pop', 29.04, .38], ['pop', 29.22, .38], ['whoosh', 31.12, .45], ['ping', 31.76, .32],
 ['impact-bass-1', 32.06, .55], ['ping', 32.46, .30], ['pop', 33.86, .36], ['pop', 33.96, .36], ['pop', 34.06, .36], ['pop', 34.16, .36],
 ['notification', 34.70, .50], ['pop', 35.36, .40], ['click', 36.26, .40],
 ['ping', 36.86, .30], ['ping', 37.11, .30], ['ping', 37.36, .30], ['ping', 37.61, .30], ['riser', 37.96, .35, 0.70],
 ['impact-bass-1', 38.63, .75], ['whoosh-cinematic', 38.98, .45], ['ping', 39.88, .35], ['pop', 40.98, .40], ['sparkle', 41.88, .38], ['pop', 42.68, .40],
]
OPTIONS = {
 'A': dict(nom="La musique porte tout le film", music_gain=0.55, logo_gain=0.90, music_from=0.0, sfx=1.0),
 'B': dict(nom="Musique douce, bruitages en avant", music_gain=0.16, logo_gain=0.55, music_from=0.0, sfx=1.40),
 'C': dict(nom="Silence jusqu'au pivot, la musique entre sur « Moi, c'est James »", music_gain=0.45, logo_gain=0.90, music_from=9.4, sfx=1.10),
}
def dur(p):
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True,check=True).stdout)
def build(key):
    o = OPTIONS[key]
    inputs = ['-i', VOICE, '-i', MUSIC]
    graph = []
    # voix : 12,6 dB pour viser -16 LUFS, puis bornée
    graph.append(f"[0:a]aresample=44100,volume=12.6dB,alimiter=limit=0.89,apad=whole_dur={TOTAL},atrim=0:{TOTAL}[voice]")
    graph.append("[voice]asplit=2[vmix][vsc]")
    # musique : démarre à MUSIC_START, gain voix -> gain logo (rampe 2 s), duck sous la voix, entrée à music_from
    mg, lg = o['music_gain'], o['logo_gain']
    vol = f"if(lt(t,{VOICE_END}),{mg},if(lt(t,{LOGO_AT}),{mg}+({lg}-{mg})*(t-{VOICE_END})/{LOGO_AT-VOICE_END},{lg}))"
    fin = f",afade=t=in:st={o['music_from']}:d=0.9" if o['music_from'] > 0 else ",afade=t=in:st=0:d=0.5"
    graph.append(f"[1:a]aresample=44100,atrim=start={MUSIC_START:.3f}:duration={TOTAL},asetpts=PTS-STARTPTS,volume='{vol}':eval=frame{fin},afade=t=out:st={TOTAL-1.6}:d=1.6[mraw]")
    graph.append("[mraw][vsc]sidechaincompress=threshold=0.03:ratio=5:attack=20:release=450:makeup=1[mduck]")
    labels = ['[vmix]', '[mduck]']
    for i, ev in enumerate(EVENTS):
        name, t, g = ev[0], ev[1], ev[2]
        path = os.path.join(SFX, name + '.mp3')
        inputs += ['-i', path]
        idx = i + 2
        trim = ''
        if name == 'riser':
            L = ev[3]; trim = f"atrim=start={max(0, dur(path)-L):.3f},asetpts=PTS-STARTPTS,afade=t=in:st=0:d={min(0.2, L/2):.2f},"
        ms = int(round(t*1000))
        graph.append(f"[{idx}:a]aresample=44100,{trim}volume={g*o['sfx']:.3f},adelay={ms}|{ms},apad=whole_dur={TOTAL},atrim=0:{TOTAL}[s{i}]")
        labels.append(f"[s{i}]")
    graph.append(''.join(labels) + f"amix=inputs={len(labels)}:normalize=0:dropout_transition=0,alimiter=limit=0.89[pre]")
    graph.append("[pre]loudnorm=I=-16:TP=-1.5:LRA=11,aresample=44100,atrim=0:%.2f[out]" % TOTAL)
    out = f'assets/audio/mix-{key}.wav'
    cmd = ['ffmpeg','-v','error','-y'] + inputs + ['-filter_complex', ';'.join(graph), '-map', '[out]', '-ar', '44100', '-ac', '2', out]
    subprocess.run(cmd, check=True)
    return out
if __name__ == '__main__':
    keys = [k for k in sys.argv[1:] if k in OPTIONS] or list(OPTIONS)
    for k in keys:
        print(k, OPTIONS[k]['nom'], '->', build(k))
