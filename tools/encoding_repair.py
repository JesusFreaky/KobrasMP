#!/usr/bin/env python3
import base64, hashlib, json, zlib
from pathlib import Path

ROOT = Path("Kobras")
PATCH_DIR = Path("tools/encoding_patch")
ORIGINAL = {'common/cultures/00_cultures.txt': '6154176a95aed6566b403ab88e19b77b9d3fe9a1', 'events/FlavorTUR.txt': '996ccf45f010fead7818bad654c12d074d943d51', 'events/estate_janissaries.txt': '487cb733fcb46bbce000a2c6551713de7f615580', 'missions/DOM_French_Missions.txt': 'da704216e3433fcb52676e4af37ba81dc702a835', 'common/event_modifiers/00_event_modifiers.txt': '744c3cd30a0e8302155a5f35b57226f55c691c3e', 'history/countries/TEU - Teutonic Order.txt': 'ba7b648c41efefb50123ce20b878458b704a8a94', 'history/countries/COR - Corsica.txt': '70c4b522eb30180a0282eec6b876323f8b875737', 'common/great_projects/01_monuments.txt': 'a6b90e064c6581f702aeaaf09cfb75c833f65331'}
TARGET = {'common/cultures/00_cultures.txt': 'dc5426c3acbcb2ab62cb0238b33155a740043bfb', 'events/FlavorTUR.txt': '8daf9bac05b6def6897785a06f3012ab541f8dc7', 'events/estate_janissaries.txt': 'dda6d745f991f5f4d1991f6f9988e58e7ec5254b', 'missions/DOM_French_Missions.txt': 'fa1a6075cf60e883180e73e257f16ecc02b98fdd', 'common/event_modifiers/00_event_modifiers.txt': '0e55604bce12ff78239993023cac0b7018411f7b', 'history/countries/TEU - Teutonic Order.txt': '15cfa8037eb744bd1d08d6e5f8a0273fe6d2e787', 'history/countries/COR - Corsica.txt': '6575d639957ed5a576f95f12214e15d40edcefb9', 'common/great_projects/01_monuments.txt': '4ed963d308405e8b49cf9d4e55323fcd3302f2ef'}

def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

payload = "".join(p.read_text().strip() for p in sorted(PATCH_DIR.glob("chunk_*.txt")))
manifest = json.loads(zlib.decompress(base64.b64decode(payload)))

for rel, expected in ORIGINAL.items():
    p = ROOT / rel
    data = p.read_bytes()
    actual = git_blob_sha(data)
    if actual != expected:
        raise SystemExit(f"SOURCE SHA MISMATCH {rel}: {actual} != {expected}")

for rel, spec in manifest.items():
    p = ROOT / rel
    data = p.read_bytes()
    if isinstance(spec, dict):
        if spec.get("strip_bom"):
            if not data.startswith(b"\xef\xbb\xbf"):
                raise SystemExit(f"EXPECTED BOM MISSING: {rel}")
            data = data[3:]
            p.write_bytes(data)
        continue
    had_final_nl = data.endswith(b"\n")
    lines = data.splitlines()
    for idx, encoded in spec:
        lines[idx] = base64.b64decode(encoded)
    out = b"\n".join(lines) + (b"\n" if had_final_nl else b"")
    p.write_bytes(out)

for rel, expected in TARGET.items():
    actual = git_blob_sha((ROOT / rel).read_bytes())
    if actual != expected:
        raise SystemExit(f"TARGET SHA MISMATCH {rel}: {actual} != {expected}")
    print(f"OK {rel} {actual}")
