import pandas as pd
from datetime import date,datetime,timedelta
import pandas as pd
import pandas as pd
dflist=[]
wdfz=pd.read_csv("https://nhlelos.ontheroadtovote.repl.co/p.csv")


teamz=set(wdfz.Team.tolist())

for i in range(2011,2023):
  
  for team in teamz:
  
    wdf=wdfz[(wdfz.Team==team)]
                
    coln='pts'+str(i)    
    
          
        
    vegp=float(wdf[coln].sum())
      
    fn="points/"+str(coln)+team+".txt"
    file=open(fn,"w")
    file.write(str(vegp))
    file.close()
import numpy as np
import math

np.seterr(divide = 'ignore') 
import os
class Elo:
   
  def __init__(self,k,g=1,homefield = 50):
    self.ratingDict   = {}  
    self.k        = k
    self.g        = g
    self.homefield    = homefield

  def addPlayer(self,name,rating = 1500):
    self.ratingDict[name] = rating
    
  def gameOver(self, winner, loser, winnerHome,home,wins,loses,playoff,hb):
   
    global result
    global play
    neutral=home
    play=playoff
    if winnerHome==True and home==0:
      result = self.expectResult(self.ratingDict[winner]+hb + self.homefield, self.ratingDict[loser])
    if winnerHome!=True and home==0:
      result = self.expectResult(self.ratingDict[winner], hb+self.ratingDict[loser] + self.homefield)
    if winnerHome!=True and home!=0:
      result = self.expectResult(self.ratingDict[winner], self.ratingDict[loser])
    tie=False
    if wins==loses:
        tie=True
    if tie:
        mult=((0.6686*0+0.8048)*( 2.05 / (1 * 0.001 + 2.05)))
        shift=(self.k*mult)  *(0.5 - result) 
        self.ratingDict[winner] +=shift
        self.ratingDict[loser]-=shift
      
    
    if tie!=True:
        win=eloLeague.ratingDict[winner]
        if winnerHome and neutral!=1:
            
            win=eloLeague.ratingDict[winner]+50
        lose=eloLeague.ratingDict[loser]
        if winnerHome!=True and neutral!=1:
            
            lose=eloLeague.ratingDict[loser]+50
        
          
        z=win-lose
          
        mult=((0.6686*math.log(wins-loses)+0.8048)*( 2.05 / ( z * 0.001 + 2.05)))
        shift=(self.k*mult)  *(1 - result) 
        self.ratingDict[winner] +=shift
        self.ratingDict[loser]-=shift
        
      
    
  def expectResult(self, p1, p2):
    if play!=1:
      exp = (p2-p1)/400.0
      return 1/((10.0**(exp))+1)
    if play==1:
      
      exp = ((p2-p1)*1.25)/400.0
      return 1/((10.0**(exp))+1)




today = date.today()
tomorrow = today + timedelta(1)
import os.path
dfz=pd.read_csv("https://projects.fivethirtyeight.com/nhl-api/nhl_elo.csv",low_memory=False).fillna(0)
from20000=dfz
df=dfz[dfz.date<str(today)]






from2000  = df
allTeams  = set(df.home_team.tolist())
allTeamss  = set(df.away_team.tolist())
f2000=from2000[from2000.season>1999]
currTeams=set(f2000.home_team.tolist())
eloLeague   = Elo(k = 6,homefield=50)

from2000=from2000.sort_values(by='date')



for team in allTeams:
    eloLeague.addPlayer(team,rating=1380)
for team in allTeamss:
    eloLeague.addPlayer(team,rating=1380)
currSeason=1918

eloLeague.addPlayer('Toronto Maple Leafs',rating=1380.0)
eloLeague.addPlayer('DetroitRedWings',rating=1380.0)
eloLeague.addPlayer('Calgary Flames',rating=1380.0)
eloLeague.addPlayer('New Jersey Devils',rating=1380.0)
eloLeague.addPlayer('Oakland Seals',rating=1380.0)
eloLeague.addPlayer('Corado Avalanche',rating=1380.0)
eloLeague.addPlayer('St. Louis Eagles',rating=1380.0)
eloLeague.addPlayer('New York Islanders',rating=1380.0)
eloLeague.addPlayer('Quebec Athletic Club/Bulldogs',rating=1380.0)
eloLeague.addPlayer('Edmonton Oilers',rating=1380.0)
eloLeague.addPlayer('Anaheim Ducks',rating=1380.0)
eloLeague.addPlayer('Columbus Blue Jackets',rating=1380.0)
eloLeague.addPlayer('Pittsburgh Penguins',rating=1380.0)
eloLeague.addPlayer('Winnipeg Jets',rating=1380.0)
eloLeague.addPlayer('Vancouver Canucks',rating=1380.0)
eloLeague.addPlayer('Minnesota Wild',rating=1380.0)
eloLeague.addPlayer('New York Americans',rating=1380.0)
eloLeague.addPlayer('Carolina Hurricanes',rating=1380.0)
eloLeague.addPlayer('Vegas Golden Knights',rating=1490.0)
eloLeague.addPlayer('Ottawa Senators',rating=1380.0)
eloLeague.addPlayer('Nashville Predators',rating=1380.0)
eloLeague.addPlayer('Montreal Wanderers',rating=1380.0)
eloLeague.addPlayer('Philadelphia Flyers',rating=1380.0)
eloLeague.addPlayer('San Jose Sharks',rating=1380.0)
eloLeague.addPlayer('St. Louis Blues',rating=1380.0)
eloLeague.addPlayer('Dallas Stars',rating=1380.0)
eloLeague.addPlayer('Buffalo Sabres',rating=1380.0)
eloLeague.addPlayer('Los Angeles Kings',rating=1380.0)
eloLeague.addPlayer('Pittsburgh Pirates',rating=1380.0)
eloLeague.addPlayer('Arizona Coyotes',rating=1380.0)
eloLeague.addPlayer('Florida Panthers',rating=1380.0)
eloLeague.addPlayer('Seattle Kraken',rating=1489.80412134286)
eloLeague.addPlayer('Montreal Canadiens',rating=1380.0)
eloLeague.addPlayer('Montreal Maroons',rating=1380.0)
eloLeague.addPlayer('New York Rangers',rating=1380.0)
eloLeague.addPlayer('Boston Bruins',rating=1380.0)
eloLeague.addPlayer('Philadelphia Quakers',rating=1380.0)
eloLeague.addPlayer('Washington Capitals',rating=1380.0)
eloLeague.addPlayer('Chicago Blackhawks',rating=1380.0)
eloLeague.addPlayer('Tampa Bay Lightning',rating=1380.0)
w=0
l=0
z=0
zz=0
ms=[]
global p538
global veg
a538=[]
aveg=[]
from2000['hb']=0
for row in from2000.itertuples():
    if 'Colorado Avalanche' in str(row):
        from2000.at[row.Index,'hb']=5
    
for game in from2000.itertuples():
  
  
  if game.season > currSeason:
    done=0
    vega=[]
    wz=[]
    if game.season==2006:
      currSeason+=1
      
      for key in eloLeague.ratingDict.keys():
        
        eloz=eloLeague.ratingDict[key]
        if((eloz==1500)or(eloz==1490)or(eloz==1380)or(eloz==1489.80412134286)):
         
          my=[]
        else:
          eloLeague.ratingDict[key] = eloLeague.ratingDict[key] - ((eloLeague.ratingDict[key] - 1505) * (0.3)) 
      currSeason+=1
    else:    
      for key in eloLeague.ratingDict.keys():
        eloz=eloLeague.ratingDict[key]
        if(0>1):
           my=[]
        else:
          
          if(key=='Carolina Hurricanes'):
            davenname="wins/nhl"+"Carrolina Hurricanes"+str(game.season)+".txt"
          else:
            davenname="wins/nhl"+key+str(game.season)+".txt"
          if ((game.season>2017)&(os.path.exists(davenname)!=True)):
            pm=1
          wins=0
          vegp=1000
          if(os.path.exists(davenname)):
            if(game.season==2019):
              z='wins/nhl'
              y=key
              if(y=='Carolina Hurricanes'):
                f="Carrolina Hurricanes"
                davenname="wins/nhl"+f+str(2019)+".txt"
              if(y!='Carolina Hurricanes'):
                
                
                  
                davenname=z+y+str(2019)+".txt"
            
              davenf=open(davenname)
              davenw=davenf.readlines()
              davenw=str(davenw)
              davenw=davenw.replace('[','')
              davenw=davenw.replace(']','')
              davenw=davenw.replace("'",'')
              davenwz=davenw.replace('"','')
      
              davenwz=davenwz
            
              davenw=float(davenwz)
              wins=(28-davenw)*-6
              
            if(game.season!=2019):
              
              
              z='wins/nhl'
              y=key
              if(y=='Carolina Hurricanes'):
                f="Carrolina Hurricanes"
                davenname="wins/nhl"+f+str(game.season)+".txt"
              if(y!='Carolina Hurricanes'):
                
                
                  
                davenname=z+y+str(game.season)+".txt"
            
              davenf=open(davenname)
              davenw=davenf.readlines()
              davenw=str(davenw)
              davenw=davenw.replace('[','')
              davenw=davenw.replace(']','')
              davenw=davenw.replace("'",'')
              davenwz=davenw.replace('"','')
      
              davenwz=davenwz
              
              davenw=float(davenwz)
              wins=(41-davenw)*-6
            
          wz.append(wins)
          pn="points/pts"+str(game.season)+key+".txt"
            
          vegp=1000
            
          if(os.path.exists(pn)==True) and done!=1:
              
            cdf=from2000[from2000.season==game.season]
            x=set(cdf.home_team.tolist())
            for team in x:
              sea=str(game.season)
              pu="points/pts"+sea+team+".txt"
              pf=open(pu)
              pw=pf.readlines()
              pw=str(pw)
              if(len(pw)>0):
                pw=pw.replace('[','')
                pw=pw.replace(']','')
                pw=pw.replace("'",'')
                pw=pw.replace('"','')
                pw=pw
                pw=float(pw)
                if(pw!=89):
                  
                  vega.append(round(pw))
                if(pw==89):
                  vegp=1000
                  
            done=1
          if(os.path.exists(pn)==True):
              
                
            pf=open(pn)
            pw=pf.readlines()
            pw=str(pw)
              
            if(os.path.getsize(pn)==0):
              vegp=1000
            if(os.path.getsize(pn)>0):
              pw=pw.replace('[','')
              pw=pw.replace(']','')
              pw=pw.replace("'",'')
              pw=pw.replace('"','')
              pw=pw
              pw=float(pw)
              if(pw!=89):
                  
                vegp=round(pw)-round(np.mean(vega))
              if(pw==89):
                vegp=1000
           
                
                
                
            
            
        ek=eloLeague.ratingDict[key]
            
        if(vegp!=1000):
              
          wins=(round(wins)*0.70)+(round(vegp)*0.70)
        if(vegp==1000):
          wins=round(wins)*0.70
            
              
            
                
              
        eloLeague.ratingDict[key]=ek+((wins))
           
            
        elor=eloLeague.ratingDict[key]
        if(elor==1490 or elor==1500 or elor==1380 or elor==1489.80412134286):
            
          m=1
        else:
          eloLeague.ratingDict[key] = (eloLeague.ratingDict[key] *0.70)+(1505*0.30)
      currSeason += 1
  if game.home_team_score > game.away_team_score:   
    eloLeague.gameOver(game.home_team, game.away_team, True,game.neutral,game.home_team_score,game.away_team_score,game.playoff,row.hb)
  if game.away_team_score>game.home_team_score:
    eloLeague.gameOver(game.away_team, game.home_team, False,game.neutral,game.away_team_score,game.home_team_score,game.playoff,row.hb)
  if game.home_team_score==game.away_team_score:
    eloLeague.gameOver(game.home_team, game.away_team, True,game.neutral,game.home_team_score,game.away_team_score,game.playoff,row.hb)
print("{")

for team in eloLeague.ratingDict.keys():
    if team in currTeams:
      
      print ('"',team,'"',":",eloLeague.ratingDict[team],",")
      
    else:
      m=1

print('"','Team','"',':','20')
def Average(lst):
    sum_of_list = 0
    for i in range(len(lst)):
        sum_of_list += lst[i]
    average = sum_of_list/len(lst)
    return average
  
print("}")

mf=open("msqe.txt","w")
mf.write(str(Average(ms)))
mf.close()
def _sum(arr):
 
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
    sum = 0
 
    # iterate through the array
    # and add each element to the sum variable
    # one at a time
    for i in arr:
        sum = sum + i
 
    return(sum)
acc=100/(w+l)*w
af=open("acc.txt","w")
af.write(str(acc))
af.close()
sorted_dict = {}
sorted_keys = sorted(eloLeague.ratingDict, key=eloLeague.ratingDict.get)  # [1, 3, 2]

for w in sorted_keys:
    
    sorted_dict[w] = [w]
y=[]
for x in list(reversed(list(sorted_dict))):
    
    y.append(x)
file=open("power.txt","w")
file.write(str(y))
file.close()
global cs
import pandas as pd
from20000=pd.read_csv("https://projects.fivethirtyeight.com/nhl-api/nhl_elo.csv").fillna(0)
from20000.sort_values(by='date')

csdf=pd.DataFrame(from20000.iloc[-1:])
global opr
global t1r
for row in csdf.itertuples():
    cs=row.season
allTeams=set(from20000.home_team.tolist())

wins={}
pdz={}
global spread
for team in allTeams:
    w=0
    l=0
    spread=0
    teamdf=from20000[(from20000.season==cs)&((from20000.home_team==team)|(from20000.away_team==team))]
    teamudf=teamdf[(teamdf.away_team_score==0)|(teamdf.home_team_score==0)]
    teamdff=teamdf[(teamdf.home_team_score>0)|(teamdf.away_team_score>0)]
    for row in teamdff.itertuples():
        if(row.home_team==team) and (row.away_team_score<row.home_team_score):
            spread+=(row.home_team_score-row.away_team_score)
            w+=1
        if(row.home_team==team) and (row.away_team_score>row.home_team_score):
            spread+=(row.home_team_score-row.away_team_score)
            l+=1
        if(row.away_team==team) and (row.away_team_score>row.home_team_score):
            spread+=(row.away_team_score-row.home_team_score)
            w+=1
        if(row.away_team==team) and (row.away_team_score<row.home_team_score):
            l+=1
            spread+=(row.away_team_score-row.home_team_score)
        
    for row in teamudf.itertuples():
        global tr
        global opr
        if(row.neutral==True):
            tr=eloLeague[team]
            if(team==row.home_team):
                opr=eloLeague.ratingDict[row.away_team]
            if(team==row.away_team):
                opr=eloLeague.ratingDict[row.home_team]
            if(tr>opr):
                teams=(tr-opr)/50
                teams=round(teams)
                spread+=teams
                w+=1
            if(tr<opr):
                teams=(tr-opr)/50
                teams=round(teams)
                spread+=teams
                l+=1
                
            
            
        if(row.neutral!=True):
            if(team in row.home_team):
                tr=eloLeague.ratingDict[team]+50
                if(team=='Colorado Avalanche'):
                    tr=eloLeague.ratingDict[team]+55
                opr=eloLeague.ratingDict[row.away_team]
            if(team in row.away_team):
                opr=eloLeague.ratingDict[row.home_team]+50
                tr=eloLeague.ratingDict[team]
                if(row.home_team=='Colorado Avalanche'):
                    opr=eloLeague.ratingDict[row.home_team]+55
                   
            if(tr>opr):
                teams=(tr-opr)/50
                teams=round(teams)
                w+=1
                spread+=teams
            if(tr<opr):
                teams=(tr-opr)/50
                teams=round(teams)
                spread+=teams
                l+=1
        wins[team]=w
        pdz[team]=spread
f=open("wins.json","w")
f.write(str(wins))
f.close()
fz=open("pds.json","w")
fz.write(str(pdz))
fz.close()
