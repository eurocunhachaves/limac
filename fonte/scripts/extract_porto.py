import pymupdf as fitz, re, json
d=fitz.open('/mnt/project-files/Semiologia Médica.pdf')
out={}
def figblocks(p):
    return [b for b in sorted(p.get_text('blocks'),key=lambda b:b[1]) if re.match(r'Figura\s*\d+\.\d+',b[4].strip())]
for i in range(519,690):
    p=d[i]
    for im in p.get_images(full=True):
        xref=im[0]; rects=p.get_image_rects(xref)
        if not rects or im[2]<120: continue
        r=rects[0]
        cap=None
        for b in figblocks(p):
            if b[1]>=r.y1-8: cap=b[4]; break
        if not cap and i+1<d.page_count:
            nb=figblocks(d[i+1])
            if nb and nb[0][1]<200: cap=nb[0][4]
        if not cap: 
            print('nocap',i+1,im[2],im[3]); continue
        cap=re.sub(r'\s+',' ',cap.strip()).replace('­','-')
        m=re.match(r'Figura\s*(\d+)\.(\d+)',cap)
        key=f'p{m.group(1)}_{int(m.group(2)):02d}'
        k2=key; n=0
        while k2 in out: n+=1; k2=f'{key}{chr(96+n)}'
        pix=fitz.Pixmap(d,xref)
        if pix.n-pix.alpha>=4: pix=fitz.Pixmap(fitz.csRGB,pix)
        if pix.alpha: pix=fitz.Pixmap(pix,0)
        pix.save(f'fig/porto/{k2}.png')
        out[k2]=dict(page=i+1,w=pix.width,h=pix.height,caption=cap)
json.dump(out,open('fig/porto/index.json','w'),ensure_ascii=False,indent=1)
print(len(out))
for k,v in out.items(): print(k,v['page'],v['w'],v['h'],v['caption'][:120])
