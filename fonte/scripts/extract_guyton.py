import pymupdf as fitz, re, json
d=fitz.open('/mnt/project-files/Tratado de Fisiologia Médica.pdf')
out={}
chaps=set(str(c) for c in list(range(9,21))+[23])
def figblocks(p):
    return [b for b in sorted(p.get_text('blocks'),key=lambda b:b[1]) if re.match(r'Figura\s*\d+\.\d+\s+[A-ZÀ-Ú]',b[4].strip())]
for i in range(362,900):
    p=d[i]
    for im in p.get_images(full=True):
        xref=im[0]; rects=p.get_image_rects(xref)
        if not rects: continue
        r=rects[0]
        cap=None
        for b in figblocks(p):
            if b[1]>=r.y1-5: cap=b[4]; break
        if not cap and i+1<d.page_count:
            nb=figblocks(d[i+1]); nimgs=d[i+1].get_images()
            if nb:
                ny=min([rr.y0 for x in nimgs for rr in d[i+1].get_image_rects(x[0])] or [9999])
                if nb[0][1]<ny: cap=nb[0][4]
        if not cap: continue
        cap=re.sub(r'\s+',' ',cap.strip())
        m=re.match(r'Figura\s*(\d+)\.(\d+)',cap)
        if m.group(1) not in chaps: continue
        key=f'g{m.group(1)}_{int(m.group(2)):02d}'
        if key in out: continue
        pix=fitz.Pixmap(d,xref)
        if pix.n-pix.alpha>=4: pix=fitz.Pixmap(fitz.csRGB,pix)
        if pix.alpha: pix=fitz.Pixmap(pix,0)
        pix.save(f'fig/guyton/{key}.png')
        out[key]=dict(page=i+1,w=pix.width,h=pix.height,caption=cap)
json.dump(out,open('fig/guyton/index.json','w'),ensure_ascii=False,indent=1)
print(len(out))
