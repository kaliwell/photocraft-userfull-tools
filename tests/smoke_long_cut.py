"""Real native cutter smoke test in an isolated editor; never targets a user's document."""
from pathlib import Path
from io import BytesIO
import argparse
import json
import sys
import time
import zipfile
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from PIL import Image, ImageGrab
from photocraft_ai.bridge import ControlClient, PhotoCraftBridge


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--runtime',type=Path,required=True)
    p.add_argument('--port',type=int,default=17980)
    p.add_argument('--expect-restored',action='store_true')
    args=p.parse_args();r=args.runtime.resolve()
    c=ControlClient(args.port,r/'control.token',timeout=30)
    for _ in range(60):
        if c.alive():break
        time.sleep(.25)
    bridge=PhotoCraftBridge(c,r/'exchange',r)
    assert not bridge.documents(), 'Use a clean isolated QA editor'
    image=Image.new('RGBA',(240,1200))
    image.putdata([(x%256,y%256,120,128 if y<300 else 255) for y in range(1200) for x in range(240)])
    raw=BytesIO();image.save(raw,format='PNG')
    bridge.new_image_from_pngs([raw.getvalue()],'Long cut QA',None)
    c.run('select.rect',x=20,y=20,width=30,height=30)
    before=c.run('document.inspect')
    c.call('ui.menu.invoke',id='tools.longCut.open')
    state=c.call('ui.inspect')['longCut']
    restored=state['cuts']
    if args.expect_restored:assert restored==[82,120,210],restored
    x,y,w,h=state['sourceRect']
    c.call('ui.click',x=x+w/2,y=y+h*10/1200)
    assert len(c.call('ui.inspect')['longCut']['cuts'])==len(restored)+1
    x,y,w,h=c.call('ui.inspect')['longCut']['sourceRect']
    c.call('ui.move',x=x+w/2,y=y+h*10/1200)
    c.call('ui.key',key='Z',command=True)
    assert c.call('ui.inspect')['longCut']['cuts']==restored
    x,y,w,h=c.call('ui.inspect')['longCut']['sourceRect']
    c.call('ui.move',x=x+w/2,y=y+h*20/1200)
    c.call('ui.key',key='S')
    assert len(c.call('ui.inspect')['longCut']['cuts'])==len(restored)+1
    c.call('ui.key',key='Delete')
    assert c.call('ui.inspect')['longCut']['cuts']==restored
    after=c.run('document.inspect')
    for k in ['revision','history','hasSelection','selectionBounds','layers']:
        assert before.get(k)==after.get(k),k
    c.call('ui.screenshot',path='long-cut-verified.png')
    report={'restored':restored,'click_S_Delete_undo':True,'document_and_selection_preserved':True}
    if (r/'slices.zip').exists():
        c.call('ui.menu.invoke',id='file.export.clipboard')
        full=ImageGrab.grabclipboard().convert('RGBA')
        with zipfile.ZipFile(r/'slices.zip') as z:
            assert z.testzip() is None
            pieces=[Image.open(BytesIO(z.read(n))).convert('RGBA') for n in z.namelist()]
        joined=Image.new('RGBA',full.size);row=0
        for piece in pieces:
            assert piece.width==full.width
            joined.paste(piece,(0,row));row+=piece.height
        assert row==full.height and joined.tobytes()==full.tobytes()
        report.update(zip_crc=True,exact_rgba_reconstruction=True,pieces=[p.size for p in pieces])
    (r/'long-cut-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report))


if __name__=='__main__':main()
