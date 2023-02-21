import os,time,sys,datetime 
from urllib.parse import unquote
codedate=str(datetime.date.today()).split('-')
tmp=1
for a in codedate:
  tmp=tmp*int(a)
codedate=tmp
tmp=0
#bs4,requests
time1=time.time()
ip=sys.argv[2].split('.')
#ip='255.255.255.255'.split('.')
uniqueid=int(ip[0])
for a in ip:
  uniqueid=uniqueid*int(a)
arg=str(sys.argv[1])
arg=unquote(arg.replace('&','=').replace('+',' ')).replace('\r','').replace('\n','')
arg=arg.split('?')
arg=arg[1:]
db='/home/pxki/database/'
activecolour=(119, 221, 119,1)
deadcolour=(0,0,0,1)
offlinecolour=(246, 114, 128,1)
logindir=db+'accounts/'
profiledir=db+'profiles/'
commentsdir=db+'comments/'
badgesdir=db+'badges/'
logintext='Login or Sign Up (You are '+str(uniqueid)+')'
maxslots=50
maxtime=2592000
badges=['Admin','Developer','From the Beginning','Da Master','osu! Player','Programmer']
if  not os.path.isdir(commentsdir):
  os.mkdir(commentsdir)
if  not os.path.isdir(logindir):
  os.mkdir(logindir)
if  not os.path.isdir(profiledir):
  os.mkdir(profiledir)
if  not os.path.isdir(badgesdir):
  os.mkdir(badgesdir)
user=''
if os.path.isfile(logindir+str(uniqueid)):
  sign=True
  user=open(logindir+str(uniqueid)).read().replace('\n','')
  if not os.path.isfile(logindir+str(uniqueid)+'.active'):
    open(logindir+str(uniqueid)+'.active','w').close()
  if os.path.isfile(logindir+str(uniqueid)+'.offline'):
    os.remove(logindir+str(uniqueid)+'.offline')
  if not os.path.isfile(profiledir+user+'uid'):
    x=open(profiledir+user+'/uid','w')
    x.write(str(uniqueid))
    x.close()
  if os.path.isfile(logindir+str(uniqueid)+'.offline'):
    os.remove(logindir+str(uniqueid)+'.remove')
  logintext='Logged in as '+str(user)
  loginurl='/?viewprofile='+str(user)
else:
  sign=False
  loginurl='/?login'
if os.path.isfile(logindir+str(uniqueid)+'.isverified'):
  isverified='1'
else:
  isverified='0'
if len(arg)>10:
  print('Too Many Arguments')
  exit()
search=''
version=1
database='/home/pxki/database/posts/'
style=open('/home/pxki/web/styles.css').read()
home=open('/home/pxki/web/home.html').read()
debug=False
if debug:
  debug=open('/home/pxki/web/debug.html').read()
else:
  debug=''
def trail(file):
  return file.replace('+extratitle+',title).replace('+hometitle+',hometitle).replace('+style+',style).replace('+version+',str(version)+' '+str(arg)+'='+str(len(arg))).replace('+search+',search).replace('+uniqueid+',str(uniqueid)).replace('+loginbutton+',logintext).replace('+loginlink+',loginurl)
#if not arg.replace('/','')=='openpost':
def isveri(value):
  if value=='1':
    return ' class="verified"'
  else:
    return ' class="nveri"'
def form(data,bypass,ispost):
  if not len(data)<1:
    extrasteps=''
    data=data.split(';')
    pver=int(data[0])
    pmature=data[1]
    ptime=data[2]
    pname=data[3]
    puid=pname
    if os.path.isfile(logindir+data[3]):
      pname=open(logindir+data[3]).read().replace('\n','')
    if os.path.isfile(logindir+data[3]+'.isverified'):
      pverified='1'
    else:
      pverified='0'
    ptext=data[5]
    if "[img]" in ptext:
      tet=ptext.find('[img]')
      tets=ptext[:tet]
      ptext=ptext[tet:]
      ptext=ptext.replace('[img]','').split('[/img]')
      urltmp=ptext[0]
      tmp=ptext
      ptext='<p>'+tets+'</p><img style="margin:20px 0px 20px 0px;" src="'+urltmp
      ptext+='"></img>'
      for a in tmp[1:]:
        ptext+='<p>'+str(a)+'</p>'
    else:
      ptext='<p>'+ptext+'</p>'
    if os.path.isfile(logindir+puid+'.color'):
      hcolor=open(logindir+puid+'.color').read().replace('\n','')
      colortime=' style="background-color:'
      colortime+=hcolor+';"'
    else:
      colortime=''
    if os.path.isfile(logindir+puid+'.active'):
      activestatus='Active '
      extrasteps='style="background-color: rgba'
      extrasteps+=str(activecolour)+';"'
    elif os.path.isfile(logindir+puid+'.offline'):
      if time.time()-os.stat(logindir+puid+'.offline').st_mtime>maxtime:
        activestatus=' Dead  '
        extrasteps='style="background-color: rgba'
        extrasteps+=str(deadcolour)+';"'
      else:
        activestatus='Offline'
        extrasteps='style="background-color: rgba'
        extrasteps+=str(offlinecolour)+';"'
    else:
      activestatus='  N/A  '
      extrasteps='style="background-color: rgba'
      extrasteps+=str(deadcolour)+';"'
    if pmature=='1' and bypass==False:
      ptext='<p>This may contain Mature Content that is not suitable for younger audiences</p>'
    if ispost:
      extra='<a href="/?read=+data+">'
      extra2='</a>'
    else:
      extra=''
      extra2=''
    tmp='<div class="contentblock"><a href="/?viewprofile='+str(pname)
    tmp+='"><h3'+str(colortime)+isveri(pverified)+'>'+pname+' </h3></a><div '+extrasteps+' class="active">'+activestatus+'</div><p>Created at '+datetime.datetime.fromtimestamp(int(ptime)).strftime('%d/%m/%Y %H:%M')+'</p>'+extra+'<div class="datablock"><center>'+ptext+'</center></div>'+extra2+'</div>'
    return tmp
  else:
    return ''

def postnot():
  print('<div class="contentblock"><h3>The Post does not exist</h3></div>')

if len(arg)==0:
  search=''
else:
  if arg[0].split('=')[0]=='search':
    search=arg[0].split('=')[1]
  else:
    search=''
#print(arg[0].split('=')[1])
#exit()
title='Dub9'
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
if os.path.isdir(profiledir+user):
  if os.path.isfile(profiledir+'uid'):
    if open(profiledir+'uid').read().replace('\n','') !=uniqueid:
      print('<div class="contentblock"><h3 style="color:white;">Your account has been banned, sorry it had to be like this :<</h3></div>')
if isverified=='1':
  hometitle='<h1 class="hiddensecret" >Dub9</h1><h3 style="display:inherit;margin:-10px 0px 0px 10px;" class="verititle">Premium</h3>'
else:
  hometitle='<h1 class="hiddensecret" >Dub9</h1>'
if len(arg)==0:
  print(trail(home))
  axe=1
  try:
    for a in range(len(os.listdir(database)),0,-1):
      if not axe>49:
        print(form(open(database+str(a)).read().rstrip("\n"),False,True).replace('+data+',str(a)))
        axe+=1
      else:
        break
  except Exception as error:
    print('<div class="contentblock"><h3 style="color:red;">'+str(error)+'</h3></div>')
    
  print('<div class="contentblock"><h3>Congrats You Caught Up!</h3></div>')
else:
  try:
    arg=arg[0].split('=')
    if arg[0]=='search':
      print(trail(home))
      for a in range(len(os.listdir(database)),0,-1):
        an=str(a)
        data=open(database+an).read()
        #print(form('0;Andrew Tate;1;HELL'))
        if arg[1].lower() in data.lower():
          print(form(data,False,True).replace('+data+',an))
    elif arg[0]=='loginas':
      if len(arg)==1:
        print('<meta http-equiv="refresh" content="0; url=/" />')
      else:
        username=str(unquote(arg[1])).replace(';','').replace('+',' ').replace('/','').replace('\\','')
        if os.path.isdir(profiledir+str(username)):
          print('This User already exist dude <meta http-equiv="refresh" content="3; url=/" />')
        else:
          print('Welcome, '+str(username)+' <3')
          if not os.path.isfile(logindir+str(uniqueid)):
            x=open(logindir+str(uniqueid),'w')
            x.write(str(username))
            x.close()
            os.mkdir(profiledir+str(username))
          print('<meta http-equiv="refresh" content="0; url=/" />')
    elif arg[0]=='viewprofile':
      if len(arg)==1:
        print('<meta http-equiv="refresh" content="0; url=/" />')
      else:
        print(trail(home))
        username=unquote(arg[1]).replace('+',' ')
        if os.path.isdir(profiledir+username):
          uid=open(profiledir+username+'/uid').read().replace('\n','')
          if os.path.isfile(logindir+uid+'.isverified'):
            pverified='1'
          else:
            pverified='0'
          if os.path.isfile(logindir+uid+'.bio'):
            bio=open(logindir+uid+'.bio').read().replace('\n','').replace('+',' ')
          else:
            bio='No infomation for the bio *sadface*'
          if os.path.isfile(logindir+uid+'.color'):
            hcolor=open(logindir+uid+'.color').read().replace('\n','')
            colortime=' style="background-color:'
            colortime+=hcolor+';"'
          else:
            colortime=''
          if os.path.isfile(logindir+uid+'.active'):
            activestatus='Active '
            extrasteps='style="background-color: rgba'
            extrasteps+=str(activecolour)+';"'
          elif os.path.isfile(logindir+uid+'.offline'):
            if time.time()-os.stat(logindir+uid+'.offline').st_mtime>maxtime:
              activestatus=' Dead  '
              extrasteps='style="background-color: rgba'
              extrasteps+=str(deadcolour)+';"'
            else:
              activestatus='Offline'
              extrasteps='style="background-color: rgba'
              extrasteps+=str(offlinecolour)+';"'
          else:
            activestatus='  N/A  '
            extrasteps='style="background-color: rgba'
            extrasteps+=str(deadcolour)+';"'
          if os.path.isfile(badgesdir+uid):
            ptext=''  
            for a in open(badgesdir+uid).readlines():
              tmp=a.replace('\n','')
              try:
                ptext+='<h3 style="margin:0px 0px 0px 10px;" class="verified">'+str(badges[int(tmp)-1])+'</h3>'
              except Exception as error:
                break
          else:
            ptext='This Person does not have any badges'
          print(str('<div class="contentblock" style="height:80%;"><h3'+str(colortime)+isveri(pverified)+'>'+username+' </h3><div '+extrasteps+' class="active">'+activestatus+'</div><p>'+bio+'</p>'+ptext+'<p>User ID:'+str(uid)+'</p>'))
          if sign:
            if username==user:
              if isverified=='1':
                print('<a href="/?changecolor"><button class="butt">Change Color of your Profile (Premium Only)</button></a><br><a href="/?redeem"><button class="butt">Redeem Code</button></a><br>')
              else:
                print('<a href="/?redeem"><button class="butt">Redeem Code for Premium</button></a><br>')
              print('<a href="/?changebio"><button class="butt">Change Bio</button></a><br>')
          print('</center></div></div>')
        else:
          print('<div class="contentblock"><h3 style="display: inline-block;">'+username+' does not exist</h3></div>')
    elif arg[0]=='read':
      slots=maxslots
      if os.path.isfile(commentsdir+arg[1]):
        slots-=len(open(commentsdir+arg[1]).readlines())
      print(trail(home))
      if len(arg)==1:
        postnot()
      else:
        if not os.path.isfile(database+arg[1]):
          postnot()
        else:
          try:
            print(form(open(database+str(arg[1])).read().rstrip("\n"),True,False))
            print('<div class="contentblock"><h3 style="text-align:left;margin:0px 0px 0px 20px;padding:20px 0px;">Comments ('+str(slots)+' slots left):</h3><div style="margin:0px 0px 20px 0px;"><form><input type="text" maxlength="100" class="seobar"  name="comment='+str(arg[1]))
            print('"></input><button class="seo">Comment</button></form></div></div>')
            if not os.path.isfile(commentsdir+arg[1]):
              open(commentsdir+arg[1],'w').close()
            if os.path.isfile(commentsdir+arg[1]):
              if len(open(commentsdir+arg[1]).readlines())==0:
                print('<div class="contentblock"><h3>Be the first to comment on this Post!</h3></div>')
              else:
                for a in open(commentsdir+arg[1]).readlines():
                  if not len(a)<2:
                    print(form(a,True,False))
          except Exception:
            print('<div class="contentblock"><h3 style="color:red;">The post is hidden for security purposes</h3></div>')
    elif arg[0]=='comment':
      if len(arg)<3:
        print('<meta http-equiv="refresh" content="0; url=/" />')
      else:
        if sign:
          if maxslots-len(open(commentsdir+arg[1]).readlines())<1:
            print('You can not post anymore comment on this Post<meta http-equiv="refresh" content="3; url=/" />')
          else:
            badwords=['pussy','dick','vagina','penis','nigga','queer']
          #print(arg)
            comments=arg[2]
            for a in badwords:
              comments=comments.lower().replace(a,'____')
            if str(uniqueid) in open(commentsdir+arg[1]).read():
              print('You can only comment one per post<meta http-equiv="refresh" content="3; url=/?read='+arg[1])
              print('" />')
            else:
              x=open(commentsdir+arg[1],'a')
              x.write('1;0;'+str(int(time.time()))+';'+str(uniqueid)+';0;'+str(comments)+'\n')
              print('<meta http-equiv="refresh" content="0; url=/?read='+arg[1])
              print('" />')
        else:
          print('<meta http-equiv="refresh" content="0; url=/" />')

    elif arg[0]=='changebio':
      if len(arg)==1:
        if sign:
          print(trail(home))
          print('<div class="contentblock"><h3>Enter a text for ya bio :></h3><form><input type="text" maxlength="255" class="seobar"  name="changebio"></input><button class="seo">Change Bio</button></div>')
        else:
          print('<meta http-equiv="refresh" content="0; url=/" />')
      else:
        if sign:
          code=str(unquote(arg[1])).replace('<','').replace('>','')
          if not code=='':
            print('<meta http-equiv="refresh" content="0; url=/" />')
            x=open(logindir+str(uniqueid)+'.bio','w')
            x.write(code.replace('+',' '))
            x.close()
          else:
            print('<meta http-equiv="refresh" content="0; url=/?changebio" />')
#          else:
 #           print('<meta http-equiv="refresh" content="0; url=/" />')
    elif arg[0]=='changecolor':
      if len(arg)==1:
        if sign:
          print(trail(home))
          print('<div class="contentblock"><h3>Enter a color via html code</h3><form><input type="text" maxlength="7" class="seobar"  name="changecolor"></input><button class="seo">Change Color</button></div>')
        else:
          print('<meta http-equiv="refresh" content="0; url=/" />')
      else:
        if sign:
          if isverified=='1':
            code=str(unquote(arg[1]))
            if code[0]=='#':
              print('<meta http-equiv="refresh" content="0; url=/" />')
              x=open(logindir+str(uniqueid)+'.color','w')
              x.write(code)
              x.close()
            else:
              print('<meta http-equiv="refresh" content="0; url=/?changecolor" />')
          else:
            print('<meta http-equiv="refresh" content="0; url=/" />')
    elif arg[0]=='redeem':
      if len(arg)==1:
        if sign:
          print(trail(home))
          print('<div class="contentblock"><h3>Enter Code</h3><form><input type="text" maxlength="7" class="seobar"  name="redeem"></input><button class="seo">Redeem</button></div>')
        else:
          print('<meta http-equiv="refresh" content="0; url=/" />')
      else:
        if sign:
          code=str(unquote(arg[1]))
          if code==str(codedate):
            print('<meta http-equiv="refresh" content="0; url=/" />')
            open(logindir+str(uniqueid)+'.isverified','w').close()
          elif code=='P4O6RAM':
            x=open(badgesdir+str(uniqueid),'a')
            x.write('6\n')
            x.close()
            print('<meta http-equiv="refresh" content="0; url=/" />')
          elif code=='P3PPY':
            x=open(badgesdir+str(uniqueid),'a')
            x.write('5\n')
            x.close()
            print('<meta http-equiv="refresh" content="0; url=/" />')
          else:
            print('<meta http-equiv="refresh" content="0; url=/?redeem" />')
    elif arg[0]=='create':
      if len(arg)==1:
        print(trail(home))
        print(trail(open('/home/pxki/web/create.htm').read()))
      else:
        if sign:
          if '1'=='1':
            x=open(database+str(len(os.listdir(database))+1),'w')
          if "ismature" in arg:
            ismature='1'
          else:
            ismature='0'
          if '1'=='1':
            x.write(str(version)+';'+str(ismature)+';'+str(int(time.time()))+';'+str(uniqueid)+';'+str(isverified)+';'+str(str(unquote(arg[1])).replace(';','').replace('+',' ').replace('<','').replace('>',''))[:100])
            x.close()
            print('<meta http-equiv="refresh" content="0; url=/" />')
          else:
            print(arg)
        else:
          print('<meta http-equiv="refresh" content="0; url='+str(loginurl))
          print('" />')
    elif arg[0]=='login':
      print(trail(open('/home/pxki/web/loginpage.htm').read()))
    else:
      print(arg)
  except Exception as error:
    print(error)
#print(open('/home/pxki/web/beta.htm').read())
#for a in range(1,100):
  #print('<div class="contentblock"><h3>Content Goes Here #'+str(a)+'</h3></div>')