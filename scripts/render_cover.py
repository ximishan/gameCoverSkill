#!/usr/bin/env python3
import argparse
from pathlib import Path
from typing import List, Tuple
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

SIZE_PRESETS={
 "feed-4x5":(1080,1350),"portrait-3x4":(1080,1440),"vertical-9x16":(1080,1920),
 "square-1x1":(1080,1080),"landscape-16x9":(1920,1080),"landscape-16x10":(1600,1000)}
RATIOS={"4:5":SIZE_PRESETS["feed-4x5"],"3:4":SIZE_PRESETS["portrait-3x4"],"9:16":SIZE_PRESETS["vertical-9x16"],"1:1":SIZE_PRESETS["square-1x1"],"16:9":SIZE_PRESETS["landscape-16x9"],"16:10":SIZE_PRESETS["landscape-16x10"]}
FONTS=[r"C:\Windows\Fonts\msyhbd.ttc",r"C:\Windows\Fonts\msyh.ttc",r"C:\Windows\Fonts\simhei.ttf",r"C:\Windows\Fonts\Dengb.ttf","/System/Library/Fonts/PingFang.ttc","/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc","/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc","/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"]
W=(255,255,255,255); B=(0,0,0,255)
# template, panel shape, tag, panel1, panel2, accent, title shadow, version, stroke, brightness, contrast, saturation
THEMES={
 "general":("impact","brush",(220,20,24,235),(0,0,0,215),(35,35,35,215),(255,218,0,255),(220,20,24,255),(220,20,24,235),B,.86,1.08,1.08),
 "action":("impact","brush",(205,18,28,240),(5,5,5,220),(30,30,30,215),(255,219,0,255),(232,35,25,255),(205,18,28,240),B,.84,1.12,1.12),
 "roguelike":("impact","brush",(160,16,28,240),(8,8,12,225),(28,22,35,220),(255,205,0,255),(186,22,38,255),(126,18,30,240),B,.82,1.14,1.08),
 "shooter":("tactical","slant",(242,91,24,240),(12,18,22,225),(30,40,46,220),(255,178,25,255),(242,91,24,255),(242,91,24,240),B,.84,1.15,1.02),
 "rpg":("epic","frame",(108,72,180,235),(18,23,46,220),(28,35,64,215),(247,201,72,255),(103,63,168,255),(145,95,190,235),B,.88,1.08,1.08),
 "strategy":("command","frame",(150,110,35,235),(14,29,48,225),(24,44,66,220),(239,194,72,255),(145,105,35,255),(120,85,25,235),B,.88,1.10,.96),
 "casual":("bright","rounded",(32,149,243,235),(255,255,255,225),(255,244,214,225),(255,112,67,255),(32,125,220,255),(255,183,77,240),(38,66,92,255),.96,1.03,1.18),
 "horror":("horror","brush",(125,0,14,245),(0,0,0,232),(28,20,22,228),(220,38,38,255),(120,0,12,255),(95,0,12,240),B,.70,1.20,.78),
 "racing":("speed","slant",(0,185,220,240),(9,14,24,222),(24,30,42,218),(255,125,35,255),(0,170,210,255),(255,102,35,240),B,.90,1.15,1.18),
 "simulation":("clean","rounded",(30,145,124,235),(12,54,52,215),(23,72,68,210),(255,210,78,255),(21,122,112,255),(44,155,136,235),B,.92,1.06,1.04),
 "survival":("rugged","brush",(111,88,38,240),(25,28,20,225),(45,45,34,220),(226,151,55,255),(104,73,33,255),(92,77,39,240),B,.80,1.14,.92),
 "anime":("neon","rounded",(231,66,152,235),(36,18,58,218),(23,38,72,215),(82,224,255,255),(231,66,152,255),(118,81,210,235),(24,18,38,255),.92,1.08,1.20),
 "retro":("retro","pixel",(117,64,180,240),(24,18,48,225),(48,32,72,220),(255,91,179,255),(73,211,255,255),(73,84,170,240),B,.92,1.10,1.22)}
KEYWORDS={
 "roguelike":["roguelike","肉鸽","地牢","重生细胞","dead cells","哈迪斯","hades"],"shooter":["射击","fps","tps","枪战","火力掩护","cover fire","使命召唤","战地"],"horror":["恐怖","惊悚","丧尸","僵尸","horror","生化危机"],"racing":["赛车","竞速","漂移","racing","forza","极品飞车"],"strategy":["策略","slg","塔防","文明","帝国","strategy"],"simulation":["模拟","经营","建造","农场","城市","simulator","tycoon"],"survival":["生存","末日","荒野","饥荒","survival","craft"],"anime":["二次元","动漫","少女","anime","gacha","忍者","超忍机"],"retro":["像素","复古","pixel","retro","8-bit","16-bit"],"casual":["休闲","益智","消除","卡牌","扑克牌","dice","puzzle","casual"],"rpg":["rpg","角色扮演","幻想","魔法","最终幻想","勇者","冒险"],"action":["动作","act","格斗","战斗","类魂","souls","boss","英雄"]}

def find_font(p=None):
 if p and Path(p).exists(): return p
 for f in FONTS:
  if Path(f).exists(): return f
 raise FileNotFoundError("No Chinese font found. Pass --font with a local Chinese font path.")
def parse_size(v):
 s=v.lower().replace("×","x")
 try:w,h=map(int,s.split("x",1))
 except:raise argparse.ArgumentTypeError("Size must look like 1080x1350")
 if min(w,h)<320: raise argparse.ArgumentTypeError("Both dimensions must be >=320")
 return w,h
def out_size(size,preset,ratio): return size or SIZE_PRESETS.get(preset) or RATIOS.get(ratio) or SIZE_PRESETS["feed-4x5"]
def crop(im,size):
 tw,th=size; sw,sh=im.size; s=max(tw/sw,th/sh); nw,nh=int(sw*s),int(sh*s); im=im.resize((nw,nh),Image.Resampling.LANCZOS); return im.crop(((nw-tw)//2,(nh-th)//2,(nw+tw)//2,(nh+th)//2))
def lines(text,n):
 text=(text or "").strip()
 if not text:return []
 if "\n" in text:return [x.strip() for x in text.splitlines() if x.strip()]
 return [text[i:i+n] for i in range(0,len(text),n)]
def tsize(d,t,f,s=0):
 b=d.textbbox((0,0),t,font=f,stroke_width=s); return b[2]-b[0],b[3]-b[1]
def fit(d,ls,font,maxw,start,minsz,stroke):
 for sz in range(start,minsz-1,-4):
  f=ImageFont.truetype(font,sz)
  if max(tsize(d,x,f,stroke)[0] for x in (ls or [" "]))<=maxw:return f
 return ImageFont.truetype(font,minsz)
def genre_for(title,tag,features,g):
 g=(g or "auto").lower()
 if g!="auto":return g if g in THEMES else "general"
 text=" ".join([title or "",tag or "",*(features or [])]).lower()
 for k,ws in KEYWORDS.items():
  if any(w.lower() in text for w in ws):return k
 return "general"
def panel(d,r,theme,fill):
 x1,y1,x2,y2=map(int,r); shape=theme[1]; h=y2-y1
 if shape=="brush":
  n=max(5,int(h*.16)); d.polygon([(x1,y1+n),(x1+n,y1),(x2-2*n,y1+n//2),(x2,y1+n),(x2-n,y2),(x1+2*n,y2-n//2),(x1,y2-n)],fill=fill)
 elif shape=="slant":
  s=max(10,int(h*.34)); d.polygon([(x1+s,y1),(x2,y1),(x2-s,y2),(x1,y2)],fill=fill)
 elif shape=="rounded": d.rounded_rectangle((x1,y1,x2,y2),radius=max(12,int(h*.24)),fill=fill)
 elif shape=="frame": d.rectangle((x1,y1,x2,y2),fill=fill,outline=theme[5],width=max(3,int(h*.08)))
 elif shape=="pixel":
  q=max(5,int(h*.12)); d.rectangle((x1+q,y1,x2-q,y2),fill=fill); d.rectangle((x1,y1+q,x2,y2-q),fill=fill)
 else:d.rectangle((x1,y1,x2,y2),fill=fill)
def readability(im,theme):
 w,h=im.size; ov=Image.new("RGBA",(w,h),(0,0,0,0)); p=ov.load(); bright=theme[0] in {"bright","clean"}
 for y in range(h):
  a=int(min(180,(42 if bright else 72)*max(0,1-y/(h*.42))+(95 if bright else 155)*max(0,(y-h*.62)/(h*.38))**1.5))
  if a:
   for x in range(w):p[x,y]=(0,0,0,a)
 im.alpha_composite(ov); return im
def tag_draw(d,text,font,w,h,t):
 if not text:return
 sz=max(30,int(min(w,h)*.045)); f=ImageFont.truetype(font,sz); st=max(3,int(sz*.09)); tw,th=tsize(d,text,f,st); px,py=int(sz*.4),int(sz*.2); x,y=int(w*.045),int(h*.035); r=(x,y,x+tw+2*px,y+th+2*py); panel(d,r,t,t[2]); fill=B if t[0]=="bright" else W; d.text((x+px,y+py-2),text,font=f,fill=fill,stroke_width=st,stroke_fill=t[8])
def title_draw(d,text,font,w,h,t):
 ls=lines(text,7)
 if not ls:return int(h*.12)
 st=max(7,int(w*(.010 if t[0]=="bright" else .012))); f=fit(d,ls,font,int(w*.92),int(w*(.136 if t[0] in {"bright","clean","neon"} else .145)),int(w*.07),st); y=int(h*.085)
 for x in ls:
  tw,th=tsize(d,x,f,st); xx=(w-tw)//2; sh=max(4,int(w*.006)); d.text((xx+sh,y+sh),x,font=f,fill=t[6],stroke_width=st,stroke_fill=t[8]); d.text((xx,y),x,font=f,fill=W,stroke_width=st,stroke_fill=t[8]); y+=th+int(h*.01)
 return y
def features_draw(d,fs,ver,font,w,h,y,t):
 y=max(y,int(h*.30)); x=int(w*.045); maxw=int(w*.72); st=max(4,int(w*.006))
 for i,txt in enumerate(fs[:3]):
  ls=lines(txt,10); f=fit(d,ls,font,maxw,max(34,int(w*.066)),int(w*.046),st)
  for ln in ls:
   tw,th=tsize(d,ln,f,st); px,py=int(f.size*.34),int(f.size*.18); r=(x,y,x+min(maxw,tw+2*px),y+th+2*py); panel(d,r,t,t[3] if i%2==0 else t[4]); fill=(25,50,75,255) if t[0]=="bright" else (t[5] if i%2==0 else W); d.text((x+px,y+py-2),ln,font=f,fill=fill,stroke_width=st,stroke_fill=t[8]); y=r[3]+int(h*.012)
 if ver:
  txt=ver if ver.startswith("版本") else f"版本号 {ver}"; f=ImageFont.truetype(font,max(28,int(w*.048))); tw,th=tsize(d,txt,f,st); px,py=int(f.size*.3),int(f.size*.16); r=(x,y,min(w-int(w*.045),x+tw+2*px),y+th+2*py); panel(d,r,t,t[7]); d.text((x+px,y+py-2),txt,font=f,fill=B if t[0]=="bright" else W,stroke_width=st,stroke_fill=t[8])
def accent_draw(d,text,font,w,h,t):
 if not text:return
 ls=lines(text,7); st=max(8,int(w*(.010 if t[0]=="bright" else .013))); f=fit(d,ls,font,int(w*.92),int(w*.165),int(w*.08),st); hs=[tsize(d,x,f,st)[1] for x in ls]; y=h-int(h*.05)-sum(hs)-max(0,len(ls)-1)*int(h*.008); top=max(int(h*.60),y-int(h*.025)); panel(d,(int(w*.02),top,int(w*.98),h-int(h*.025)),t,(255,255,255,215) if t[0]=="bright" else t[2])
 for ln,th in zip(ls,hs):
  tw,_=tsize(d,ln,f,st); d.text(((w-tw)//2,y),ln,font=f,fill=t[5],stroke_width=st,stroke_fill=t[8]); y+=th+int(h*.008)
def render(inp,out,title,tag,fs,ver,accent,size,font,darken,read,genre):
 g=genre_for(title,tag,fs,genre); t=THEMES[g]; im=crop(Image.open(inp).convert("RGB"),size)
 if darken: im=ImageEnhance.Color(ImageEnhance.Contrast(ImageEnhance.Brightness(im).enhance(t[9])).enhance(t[10])).enhance(t[11])
 im=im.convert("RGBA"); im=readability(im,t) if read else im; d=ImageDraw.Draw(im); w,h=im.size; tag_draw(d,tag,font,w,h,t); y=title_draw(d,title,font,w,h,t); features_draw(d,fs,ver,font,w,h,y+int(h*.02),t); accent_draw(d,accent,font,w,h,t); p=Path(out); p.parent.mkdir(parents=True,exist_ok=True); im.convert("RGB").save(p,quality=95,optimize=True) if p.suffix.lower() in {".jpg",".jpeg"} else im.save(p,optimize=True); print(f"genre={g} template={t[0]} output={p.resolve()}")
def main():
 ap=argparse.ArgumentParser(description="Render a genre-aware Chinese game-sharing cover with exact text."); ap.add_argument("input"); ap.add_argument("--output","-o",default="game-cover.png"); ap.add_argument("--title",required=True); ap.add_argument("--tag",default="游戏分享"); ap.add_argument("--feature",action="append",default=[]); ap.add_argument("--version",default=""); ap.add_argument("--accent",default="手游分享"); ap.add_argument("--genre",choices=["auto",*THEMES.keys()],default="auto"); ap.add_argument("--preset",choices=SIZE_PRESETS.keys()); ap.add_argument("--ratio",choices=RATIOS.keys()); ap.add_argument("--size",type=parse_size); ap.add_argument("--font"); ap.add_argument("--no-darken",action="store_true"); ap.add_argument("--no-readability-layer",action="store_true"); a=ap.parse_args(); render(a.input,a.output,a.title,a.tag,a.feature,a.version,a.accent,out_size(a.size,a.preset,a.ratio),find_font(a.font),not a.no_darken,not a.no_readability_layer,a.genre)
if __name__=="__main__":main()
