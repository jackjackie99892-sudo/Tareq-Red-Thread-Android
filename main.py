__version__ = '1.0.0'

from math import sin
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Ellipse, Line
from kivy.properties import BooleanProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

WHITE=(.93,.95,.97,1); DIM=(.62,.67,.73,1); TEAL=(.32,.75,.65,1); GOLD=(.91,.72,.31,1)
RED=(.8,.28,.31,1); BLUE=(.3,.52,.75,1); PURPLE=(.51,.38,.68,1); PANEL=(.09,.12,.17,1); PANEL2=(.14,.18,.24,1)

LEVELS=[
 dict(key='sheffield',episode=1,title='The Red Thread',institution='University of Sheffield',city='Sheffield, United Kingdom',year='2016',width=2500,palette='sheffield',exit_x=2380,required=['notebook','terminal','iraq_clue'],items=[
  dict(name="Professor's notebook",x=575,y=138,w=50,h=55,flag='notebook',required=None,color=GOLD,dialogue="NARRATOR|A notebook left in a lab archive contains a hand-drawn red symbol, three Arabic surnames, and one sentence: 'Patterns survive the people who create them.'"),
  dict(name='Prospect research terminal',x=1185,y=140,w=70,h=65,flag='terminal',required='notebook',color=TEAL,dialogue='TAREQ|The names surface in unrelated public records. The only shared connection is a shell company called ORCHID MERIDIAN.'),
  dict(name='Old envelope',x=1815,y=170,w=55,h=48,flag='iraq_clue',required='terminal',color=RED,dialogue="NARRATOR|Inside is a photograph taken in Baghdad. On the back: 'When your work takes you there, ask who signed twice.'")],npcs=[
  dict(name='Dr. Mara Vale',x=300,required=None,dialogue='VALE|Tareq, keep the notebook. You notice institutional patterns other people dismiss as coincidence.'),
  dict(name='Research colleague',x=1510,required='terminal',dialogue="COLLEAGUE|You're treating this like an investigation. It's prospect research, not a spy film.")]),
 dict(key='iraq',episode=2,title='The Signature',institution='International Commission on Missing Persons (ICMP)',city='Baghdad & Erbil, Iraq',year='2018',width=2600,palette='iraq',exit_x=2460,required=['crate','signature','seal'],items=[
  dict(name='Sealed evidence crate',x=520,y=145,w=76,h=58,flag='crate',required=None,color=GOLD,dialogue="TAREQ|The transfer number matches the number written in Vale's old notebook. That should be impossible."),
  dict(name='Transfer ledger',x=1035,y=160,w=72,h=55,flag='signature',required='crate',color=TEAL,dialogue='TAREQ|Two signatures. Same official. Three hours apart. The second entry was logged after the officer had already left the compound.'),
  dict(name='Black-seal photograph',x=2025,y=175,w=58,h=52,flag='seal',required='signature',color=RED,dialogue='NARRATOR|The same red-thread symbol appears in black wax beside the words ORCHID MERIDIAN.')],npcs=[
  dict(name='Faris',x=330,required=None,dialogue='FARIS|Mistakes are messy. This is too neat to be a mistake.'),
  dict(name='Field liaison',x=1690,required='signature',dialogue='LIAISON|Institutions survive on evidence, not intuition.')]),
 dict(key='hague',episode=3,title='The Map Room',institution='International Commission on Missing Persons (ICMP)',city='The Hague, Netherlands',year='2020',width=2600,palette='hague',exit_x=2470,required=['map','number','message'],items=[
  dict(name='Regional stakeholder map',x=585,y=145,w=72,h=66,flag='map',required=None,color=BLUE,dialogue='TAREQ|A routine MENA capability map recreates the same network shape: ports, laboratories, foundations, logistics companies.'),
  dict(name='Conference folder',x=1095,y=160,w=58,h=52,flag='number',required='map',color=GOLD,dialogue='NARRATOR|A business card bears the ORCHID MERIDIAN name. No website. No address. Only a number in Cairo.'),
  dict(name='Voicemail transcript',x=2115,y=165,w=58,h=52,flag='message',required='number',color=RED,dialogue="VALE|Don't investigate the institutions around it. Investigate the gaps between them.")],npcs=[
  dict(name='Programme colleague',x=350,required=None,dialogue="COLLEAGUE|You're staring at the stakeholder map like it insulted your family."),
  dict(name='Visiting expert',x=1700,required='map',dialogue='EXPERT|International systems create seams. Bad actors learn to hide inside them.')]),
 dict(key='cairo',episode=4,title='Five Years in Cairo',institution='UN Office on Drugs and Crime (UNODC)',city='Cairo, Egypt / MENA',year='2023',width=2800,palette='cairo',exit_x=2670,required=['network','company','office','email'],items=[
  dict(name='Training scenario laptop',x=485,y=145,w=70,h=58,flag='network',required=None,color=TEAL,dialogue='TAREQ|Dozens of synthetic voices resolve into only three true origins.'),
  dict(name='Partner screening file',x=1015,y=160,w=70,h=55,flag='company',required='network',color=GOLD,dialogue='TAREQ|A proposed subcontractor lists Orchid Meridian Strategic Services. Every director is a nominee.'),
  dict(name='Cairo phone number',x=2080,y=170,w=58,h=50,flag='office',required='company',color=RED,dialogue='NARRATOR|The number leads to a disused office near the river. Inside: maps, source lists, and red thread across five countries.'),
  dict(name='Unsent email',x=2485,y=145,w=58,h=50,flag='email',required='office',color=PURPLE,dialogue="VALE|Subject: 'You were never chasing a company.' Body: 'They manufacture context.'")],npcs=[
  dict(name='Regional counterpart',x=300,required=None,dialogue="COUNTERPART|Before lunch it's risk screening. After lunch it's urgent delivery."),
  dict(name='OSINT trainer',x=1550,required='network',dialogue="TRAINER|A hundred reposts can still be one source.")]),
 dict(key='icc',episode=5,title='The Situation Centre',institution='International Criminal Court (ICC) — Office of the Prosecutor Situation Centre',city='The Hague, Netherlands',year='2026',width=2800,palette='icc',exit_x=2690,required=['feed','graph','return','brief'],items=[
  dict(name='Incident feed',x=555,y=145,w=65,h=58,flag='feed',required=None,color=RED,dialogue='TAREQ|A fictional mission environment is flooded with reports of an attack. Thirty-eight accounts repeat the same claim.'),
  dict(name='Source graph',x=1090,y=155,w=70,h=58,flag='graph',required='feed',color=TEAL,dialogue='TAREQ|Thirty-eight accounts collapse into three origin clusters. One video is old. One is from another city. The third shows a road accident.'),
  dict(name='Orchid relay note',x=2145,y=165,w=65,h=52,flag='return',required='graph',color=GOLD,dialogue='NARRATOR|One origin account links back to the same fictional shell network: ORCHID MERIDIAN.'),
  dict(name='Flash brief',x=2510,y=150,w=65,h=55,flag='brief',required='return',color=BLUE,dialogue='TAREQ|Verified facts, confidence, potential impact, and what still needs confirmation. The manufactured crisis loses momentum.')],npcs=[
  dict(name='Duty officer',x=320,required=None,dialogue="DUTY OFFICER|I don't need the internet. I need the picture. What changed, what matters, and how sure are we?"),
  dict(name='Night analyst',x=1660,required='graph',dialogue="ANALYST|You look like you've seen this pattern before.")])
]

class World(Widget):
    left=BooleanProperty(False); right=BooleanProperty(False)
    def __init__(self,ui,**kw):
        super().__init__(**kw); self.ui=ui; self.i=0; self.level=LEVELS[0]; self.flags=set(); self.player_x=90.; self.player_y=112.; self.vy=0.; self.on_ground=True; self.camera=0.; self.facing=1; self.t=0.; self.auto=None; self.pending=None; self.dialogue=False; self.active=False
        Clock.schedule_interval(self.update,1/60)
    def start(self):
        self.i=0; self.level=LEVELS[0]; self.flags.clear(); self.player_x=90; self.player_y=112; self.vy=0; self.camera=0; self.active=True; self.ui.enter_game(); self.ui.chapter(self.level)
    def complete(self): return all(x in self.flags for x in self.level['required'])
    def jump(self):
        if self.active and not self.dialogue and self.on_ground: self.vy=390; self.on_ground=False
    def say(self,raw):
        sp,tx=(raw.split('|',1) if '|' in raw else ('NARRATOR',raw)); self.dialogue=True; self.ui.show_dialogue(sp,tx)
    def close_dialogue(self): self.dialogue=False; self.ui.hide_dialogue()
    def next_level(self):
        if self.i==len(LEVELS)-1: self.active=False; self.ui.ending(); return
        self.i+=1; self.level=LEVELS[self.i]; self.player_x=90; self.player_y=112; self.vy=0; self.camera=0; self.auto=None; self.pending=None; self.ui.chapter(self.level)
    def interact(self,obj,kind):
        req=obj.get('required')
        if req and req not in self.flags: self.say('NARRATOR|This makes more sense after you investigate something earlier in the chain.'); return
        self.say(obj['dialogue'])
        if kind=='item': self.flags.add(obj['flag']); self.ui.hud(self.level,self.flags)
    def update(self,dt):
        if not self.active or self.dialogue: self.redraw(); return
        d=(-1 if self.left else 0)+(1 if self.right else 0)
        if d: self.auto=None
        elif self.auto is not None:
            dx=self.auto-self.player_x
            if abs(dx)<15: self.auto=None
            else: d=1 if dx>0 else -1
        if d: self.player_x+=d*220*dt; self.facing=d; self.t+=dt*9
        self.player_x=max(20,min(self.level['width']-20,self.player_x))
        self.vy-=900*dt; self.player_y+=self.vy*dt
        if self.player_y<=112: self.player_y=112; self.vy=0; self.on_ground=True
        maxcam=max(0,self.level['width']-self.width); target=self.player_x-self.width*.45; self.camera += (max(0,min(maxcam,target))-self.camera)*min(1,dt*7)
        if self.pending:
            kind,obj=self.pending; tx=(obj['x']+obj['w']/2 if kind=='item' else obj['x'])
            if abs(self.player_x-tx)<85: self.pending=None; self.auto=None; self.interact(obj,kind)
        if self.complete() and self.player_x>=self.level['exit_x']: self.next_level()
        self.redraw()
    def on_touch_down(self,touch):
        if not self.active: return super().on_touch_down(touch)
        if self.dialogue: self.close_dialogue(); return True
        if touch.y<self.height*.18: return super().on_touch_down(touch)
        wx=touch.x+self.camera; wy=touch.y
        for obj in self.level['items']:
            if obj['x']-18<=wx<=obj['x']+obj['w']+18 and obj['y']-25<=wy<=obj['y']+obj['h']+35:
                self.pending=('item',obj); self.auto=obj['x']+obj['w']/2; return True
        for obj in self.level['npcs']:
            if obj['x']-45<=wx<=obj['x']+45 and 80<=wy<=250:
                self.pending=('npc',obj); self.auto=obj['x']; return True
        self.pending=None; self.auto=max(20,min(self.level['width']-20,wx)); return True
    def palette(self):
        p=self.level['palette']
        return {'sheffield':((.21,.25,.30,1),(.17,.16,.15,1)),'iraq':((.71,.56,.37,1),(.41,.30,.22,1)),'hague':((.24,.32,.41,1),(.18,.20,.23,1)),'cairo':((.76,.53,.35,1),(.42,.28,.20,1)),'icc':((.12,.17,.23,1),(.15,.17,.20,1))}[p]
    def redraw(self):
        self.canvas.clear();
        if not self.active:return
        top,ground=self.palette(); w,h=self.width,self.height
        with self.canvas:
            Color(*top); Rectangle(pos=self.pos,size=self.size)
            Color(.12,.16,.21,1)
            for j in range(18):
                x=j*170-(self.camera*.18)%170-80; bh=90+(j%5)*20; Rectangle(pos=(x,112),size=(125,bh))
            Color(*ground); Rectangle(pos=(0,0),size=(w,112)); Color(.38,.36,.34,1); Rectangle(pos=(0,108),size=(w,4))
            Color(.12,.16,.20,1)
            for xx in (250,900,1550,2200):
                x=xx-self.camera
                if -500<x<w+100: Rectangle(pos=(x,150),size=(420,150))
            for obj in self.level['items']:
                x=obj['x']-self.camera
                if -100<x<w+100:
                    col=obj['color'] if obj['flag'] not in self.flags else tuple(max(.15,c*.45) for c in obj['color'][:3])+(1,); Color(*col); Rectangle(pos=(x,obj['y']),size=(obj['w'],obj['h']))
                    if obj['flag'] not in self.flags: Color(*GOLD); Ellipse(pos=(x+obj['w']/2-5,obj['y']+obj['h']+10),size=(10,10))
            for npc in self.level['npcs']:
                x=npc['x']-self.camera
                if -80<x<w+80:
                    Color(.05,.06,.08,1); Ellipse(pos=(x-18,108),size=(36,9)); Color(.27,.29,.33,1); Rectangle(pos=(x-10,112),size=(8,35)); Rectangle(pos=(x+3,112),size=(8,35)); Color(.35,.42,.52,1); Rectangle(pos=(x-16,144),size=(32,42)); Color(.72,.53,.39,1); Rectangle(pos=(x-10,186),size=(20,22)); Color(.16,.12,.10,1); Rectangle(pos=(x-11,204),size=(22,8))
            x=self.player_x-self.camera; y=self.player_y; bob=sin(self.t)*2 if self.left or self.right or self.auto else 0
            Color(.04,.045,.06,1); Ellipse(pos=(x-21,y-5),size=(42,10)); Color(.18,.20,.24,1); Rectangle(pos=(x-12,y),size=(9,33)); Rectangle(pos=(x+3,y),size=(9,33)); Color(.18,.31,.42,1); Rectangle(pos=(x-17,y+30+bob),size=(34,42)); Rectangle(pos=(x-24,y+35+bob),size=(7,31)); Rectangle(pos=(x+17,y+35+bob),size=(7,31)); Color(.72,.53,.39,1); Rectangle(pos=(x-11,y+72+bob),size=(22,22)); Color(.15,.11,.09,1); Rectangle(pos=(x-12,y+90+bob),size=(24,9))
            ex=self.level['exit_x']-self.camera
            if -100<ex<w+100: Color(*(TEAL if self.complete() else DIM)); Rectangle(pos=(ex-18,112),size=(36,120)); Color(.05,.07,.10,1); Rectangle(pos=(ex-10,120),size=(20,100))

class UI(FloatLayout):
    def __init__(self,**kw):
        super().__init__(**kw); self.world=World(self,size_hint=(1,.80),pos_hint={'x':0,'y':.20}); self.add_widget(self.world)
        self.title=FloatLayout(size_hint=(1,1)); self.add_widget(self.title)
        self.title.add_widget(Label(text='[b]TAREQ: THE RED THREAD[/b]',markup=True,font_size='34sp',color=WHITE,size_hint=(.9,.12),pos_hint={'x':.05,'y':.72}))
        self.title.add_widget(Label(text='A FICTIONALISED CAREER DRAMA\n\nReal name. Real cities. Real institutions.\nInvented mystery, characters and operational events.',font_size='18sp',color=DIM,halign='center',size_hint=(.9,.30),pos_hint={'x':.05,'y':.38}))
        b=Button(text='START EPISODE 1',size_hint=(.42,.10),pos_hint={'x':.29,'y':.25},background_normal='',background_color=TEAL,color=(.03,.05,.07,1),font_size='20sp'); b.bind(on_release=lambda *_:self.world.start()); self.title.add_widget(b)
        self.title.add_widget(Label(text='Fiction inspired by real career milestones. It does not depict real institutional investigations or wrongdoing.',font_size='12sp',color=DIM,size_hint=(.96,.08),pos_hint={'x':.02,'y':.05}))
        self.controls=FloatLayout(size_hint=(1,.20),pos_hint={'x':0,'y':0},opacity=0); self.add_widget(self.controls)
        self.lb=self.btn('◀',.02,.10); self.rb=self.btn('▶',.14,.10); self.jb=self.btn('JUMP',.28,.16)
        self.lb.bind(on_press=lambda *_:setattr(self.world,'left',True),on_release=lambda *_:setattr(self.world,'left',False)); self.rb.bind(on_press=lambda *_:setattr(self.world,'right',True),on_release=lambda *_:setattr(self.world,'right',False)); self.jb.bind(on_press=lambda *_:self.world.jump())
        self.ep=Label(text='',font_size='15sp',color=WHITE,size_hint=(.50,.55),pos_hint={'x':.46,'y':.37},halign='left'); self.controls.add_widget(self.ep)
        self.pr=Label(text='',font_size='14sp',color=GOLD,size_hint=(.34,.25),pos_hint={'x':.46,'y':.12},halign='left'); self.controls.add_widget(self.pr)
        self.box=Button(text='',markup=True,font_size='17sp',halign='left',valign='middle',size_hint=(.90,.22),pos_hint={'x':.05,'y':.23},background_normal='',background_color=(.04,.06,.09,.98),color=WHITE,opacity=0); self.box.bind(size=lambda i,v:setattr(i,'text_size',(v[0]-30,v[1]-20))); self.box.bind(on_release=lambda *_:self.world.close_dialogue()); self.add_widget(self.box)
        self.card=Label(text='',markup=True,font_size='26sp',color=WHITE,halign='center',valign='middle',size_hint=(1,1),opacity=0); self.card.bind(size=lambda i,v:setattr(i,'text_size',(v[0]*.85,v[1]*.65))); self.add_widget(self.card)
        self.end=Label(text='',markup=True,font_size='20sp',color=WHITE,halign='center',valign='middle',size_hint=(1,1),opacity=0); self.end.bind(size=lambda i,v:setattr(i,'text_size',(v[0]*.84,v[1]*.82))); self.add_widget(self.end)
    def btn(self,text,x,w):
        b=Button(text=text,size_hint=(w,.62),pos_hint={'x':x,'y':.18},background_normal='',background_color=PANEL2,color=WHITE,font_size='18sp'); self.controls.add_widget(b); return b
    def enter_game(self): self.title.opacity=0; self.title.disabled=True; self.controls.opacity=1
    def hud(self,l,f):
        done=sum(x in f for x in l['required']); self.ep.text=f"EPISODE {l['episode']}: {l['title']}\n{l['institution']} • {l['city']} • {l['year']}"; self.pr.text=f"CLUES {done}/{len(l['required'])}"+(' • EXIT OPEN' if done==len(l['required']) else '')
    def show_dialogue(self,sp,tx): self.box.text=f"[color=e7b84f][b]{sp}[/b][/color]\n{tx}"; self.box.opacity=1
    def hide_dialogue(self): self.box.opacity=0
    def chapter(self,l):
        self.hud(l,self.world.flags); self.card.text=f"[color=cc474f]EPISODE {l['episode']}[/color]\n[b]{l['title']}[/b]\n\n[size=18sp]{l['institution']}[/size]\n[size=16sp]{l['city']} • {l['year']}[/size]"; self.card.opacity=1; Clock.schedule_once(lambda dt:setattr(self.card,'opacity',0),3.0)
    def ending(self):
        self.controls.opacity=0; self.box.opacity=0; self.end.opacity=1; self.end.text="[b][size=30sp]SEASON ONE: THE RED THREAD[/size][/b]\n\nThe fictional crisis collapses. The Situation Centre returns to normal. The report is filed.\n\nThe pattern that began in Sheffield has crossed ten years of Tareq's life: academia, evidence, international programmes, OSINT and intelligence.\n\n[color=cc474f]04:12 — UNKNOWN NUMBER\n'Tareq. Vale is alive. And the red thread is not finished.'[/color]\n\n[size=14sp]Fictional drama inspired by real career milestones; operational events and supporting characters are invented.[/size]"

class RedThreadApp(App):
    title='Tareq: The Red Thread'
    def build(self): Window.size=(960,540); return UI()

if __name__=='__main__': RedThreadApp().run()
