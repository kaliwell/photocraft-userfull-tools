"""Exercise real Windows clipboard export in an isolated editor; no AI generation."""
from __future__ import annotations

import argparse
from io import BytesIO
import json
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from PIL import Image, ImageDraw, ImageGrab
from photocraft_ai.bridge import ControlClient, PhotoCraftBridge


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=17980)
    parser.add_argument('--runtime', type=Path, required=True)
    parser.add_argument('--titlebar', action='store_true')
    args = parser.parse_args()
    runtime = args.runtime.resolve()
    exchange = runtime / 'exchange'
    client = ControlClient(args.port, runtime / 'control.token', timeout=30)
    for _ in range(60):
        if client.alive():
            break
        time.sleep(.25)
    else:
        raise RuntimeError('Isolated QA editor did not become ready')
    bridge = PhotoCraftBridge(client, exchange, runtime)
    source = Image.new('RGBA', (320, 200), (0, 0, 0, 0))
    draw = ImageDraw.Draw(source)
    draw.rectangle((30, 30, 140, 130), fill=(255, 0, 0, 128))
    draw.rectangle((200, 80, 290, 170), fill=(0, 80, 255, 255))
    png = BytesIO()
    source.save(png, format='PNG')
    bridge.new_image_from_pngs([png.getvalue()], 'Clipboard export QA', None)
    client.run('select.rect', x=40, y=40, width=30, height=20)
    before = client.run('document.inspect')
    files_before = {p.name for p in exchange.iterdir()}
    menus = client.call('ui.menu.list')
    if isinstance(menus, dict):
        menus = menus.get('items', menus.get('menus', []))
    item = next(m for m in menus if m.get('id') == 'file.export.clipboard')
    assert item['enabled'], item
    if args.titlebar:
        import ctypes
        user32 = ctypes.windll.user32
        assert user32.OpenClipboard(None), 'Clipboard is busy before button test'
        try:
            assert user32.EmptyClipboard(), 'Could not clear test clipboard'
        finally:
            user32.CloseClipboard()
        button = client.call('ui.inspect')['clipboardExport']
        assert button and button['enabled'], button
        x, y, w, h = button['rect']
        client.call('ui.click', x=x+w/2, y=y+h/2)
        result = {'trigger': 'titlebar', 'button': button}
    else:
        result = client.call('ui.menu.invoke', id='file.export.clipboard')
        assert result == {'width': 320, 'height': 200, 'copied': True}, result
    copied = None
    for _ in range(10):
        copied = ImageGrab.grabclipboard()
        if isinstance(copied, Image.Image):
            break
        time.sleep(.1)
    assert isinstance(copied, Image.Image), type(copied)
    copied = copied.convert('RGBA')
    assert copied.size == source.size, copied.size
    assert copied.getpixel((0, 0))[3] == 0, copied.getpixel((0, 0))
    red = copied.getpixel((60, 60))
    assert red[:3] == (255, 0, 0) and abs(red[3] - 128) <= 1, red
    assert copied.getpixel((240, 120)) == (0, 80, 255, 255), copied.getpixel((240, 120))
    assert {p.name for p in exchange.iterdir()} == files_before, 'Export created a file'
    after = client.run('document.inspect')
    for field in ('revision', 'history', 'hasSelection', 'selectionBounds', 'activeLayer', 'layers'):
        assert after.get(field) == before.get(field), (field, before.get(field), after.get(field))
    client.call('ui.set', fit=True)
    client.call('ui.screenshot', path='clipboard-export-verified.png')
    copied.save(runtime / 'clipboard-readback.png')
    report = {'result': result, 'menu': item, 'transparent_pixel': copied.getpixel((0, 0)),
              'semi_transparent_pixel': red, 'outside_selection_pixel': copied.getpixel((240, 120)),
              'selection_and_document_preserved': True, 'no_export_file_created': True,
              'real_system_clipboard_readback': True, 'live_ai': False}
    (runtime / 'clipboard-export-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=True))


if __name__ == '__main__':
    main()
