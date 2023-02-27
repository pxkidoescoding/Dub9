import os,time,sys,datetime 
from urllib.parse import unquote
codedate=str(datetime.date.today()).split('-')
track=time.time()
tmp=1
for a in codedate:
  tmp=tmp*int(a)
codedate=tmp
tmp=0
#bs4,requests
time1=time.time()
ip=sys.argv[2].split('.')
#ip='255.255.255.255'.split('.')
try:
  uniqueid=sys.argv[3]
except Exception:
  uniqueid='Guest'
arg=str(sys.argv[1])
arg=unquote(arg.replace('&','=').replace('+',' ')).replace('\r','').replace('\n','')
arg=arg.split('?')
arg=arg[1:]
if not "test" in globals():
  test=False
if test:
  db='/home/pxki/tdb/'
  adb='/home/pxki/database/'
else:
  db='/home/pxki/database/'
  adb=db

activecolour=(119, 221, 119,1)
deadcolour=(0,0,0,1)
bancolour=(255,255,0,1)
offlinecolour=(246, 114, 128,1)
logindir=adb+'accounts/'
reportsdir=db+'reports/'
profiledir=adb+'profiles/'
commentsdir=db+'comments/'
badgesdir=db+'badges/'
loveddir=db+'loved/'
logintext='Login or Sign Up'
maxslots=50
maxtime=2592000
paused=False
badges=['Admin','Developer','From the Beginning','Da Master','osu! Player','Programmer','Friends of Dub9']
if  not os.path.isdir(commentsdir):
  os.mkdir(commentsdir)
if  not os.path.isdir(logindir):
  os.mkdir(logindir)
if  not os.path.isdir(profiledir):
  os.mkdir(profiledir)
if  not os.path.isdir(badgesdir):
  os.mkdir(badgesdir)
if  not os.path.isdir(reportsdir):
  os.mkdir(reportsdir)
user=''
if os.path.isfile(logindir+str(uniqueid)):
  if not uniqueid=='Guest':
    sign=True
    user=uniqueid
    if not os.path.isfile(logindir+str(uniqueid)+'.active'):
      open(logindir+str(uniqueid)+'.active','w').close()
    if os.path.isfile(logindir+str(uniqueid)+'.offline'):
      os.remove(logindir+str(uniqueid)+'.offline')
#  if not os.path.isfile(profiledir+user+'uid'):
#    x=open(profiledir+user+'/uid','w')
#    x.write(str(uniqueid))
#    x.close()
    if os.path.isfile(logindir+str(uniqueid)+'.offline'):
      os.remove(logindir+str(uniqueid)+'.remove')
    if not os.path.isdir(profiledir+str(user)):
      os.mkdir(profiledir+str(user))
    logintext='Logged in as '+str(user)
    loginurl='/?viewprofile='+str(user)
  else:
    sign=False
    loginurl='/?login'
else:
  sign=False
  loginurl='/?login'
#if uniqueid==3400:
#  sign=True
#  logintext=str(sys.argv)
#  user='Pxki LLC.'
#  loginurl='/'

if os.path.isfile(logindir+str(uniqueid)+'.premium'):
  ispremium='1'
else:
  ispremium='0'
if len(arg)>10:
  print('Too Many Arguments')
  exit()
search=''
version=1
database=db+'posts/'
if "classicmode" in sys.argv:
  style='<head><link href="/classic.css" rel="stylesheet"></head>'
else:
  style='<head><link href="/styles.css" rel="stylesheet"></head>'
home=open('/home/pxki/web/home.html').read()
if os.path.isfile(logindir+str(uniqueid)+'.banned'):
  banned=True
  home+='<div class="bannerblock" style="background-color:#550000;color:red;"><h3>Due to complaints, your account is unfortunately banned. Meaning you can not interact to posts, or make one.</h3></div>'
else:
  banned=False
if  not os.path.isdir(database):
  os.mkdir(database)
debug=False
if debug:
  debug=open('/home/pxki/web/debug.html').read()
else:
  debug=''
def trail(file):
  return file.replace('+extratitle+',title).replace('+hometitle+',hometitle).replace('+style+',style).replace('+version+',str(version)+' '+str(arg)+'='+str(len(arg))).replace('+search+',search).replace('+uniqueid+',str(uniqueid)).replace('+loginbutton+',logintext).replace('+loginlink+',loginurl).replace('+extrabuttons+',extras)
#if not arg.replace('/','')=='openpost':
def isveri(value):
  if value=='1':
    return ' class="pfcolor"'
  else:
    return ' class="nveri"'
#datetime.datetime.fromtimestamp(int(ptime)).strftime('%d/%m/%Y %H:%M')
def timeform(data):
  data=int(time.time()-int(data))
  if data>=31557600*2:
    return str(int((data)//31557600 ))+' Years Ago'
  elif data>=31557600:
    return str(int((data)//31557600 ))+' Year Ago'
  elif data>=2629800*2:
    return str(int((data)//2629800))+' Months Ago'
  elif data>=2629800:
    return str(int((data)//2629800))+' Month Ago'
  elif data>1209599:
    return str(int((data)//604800))+' Weeks Ago'
  elif data>604799:
    return str(int((data)//604800))+' Week Ago'
  elif data>86399*2:
    return str(int((data)//86400))+' Days Ago'
  elif data>86399:
    return str(int((data)//86400))+' Day Ago'
  elif data>7199:
    return str(int((data)//3600))+' Hours Ago'
  elif data>3599:
    return str(int((data)//3600))+' Hour Ago'
  elif data>119:
    return str(int((data)//60))+' Minutes Ago'
  elif data>59:
    return str(int((data)//60))+' Minute Ago'
  elif data<60:
    return 'Just Now'
def checkstatus(puid):
  ban=False
  if os.path.isfile(logindir+puid+'.banned'):
    ban=True
    activestatus='Banned'
    extrasteps='style="background-color: rgba'
    extrasteps+=str(bancolour)+';"'
  elif os.path.isfile(logindir+puid+'.bot'):
    activestatus='Automated'
    extrasteps='style="background-color: #95BDFF;"'
  elif os.path.isfile(logindir+puid+'.active'):
    activestatus='Online'
    extrasteps='style="background-color: rgba'
    extrasteps+=str(activecolour)+';"'
  elif os.path.isfile(logindir+puid+'.offline'):
    if time.time()-os.stat(logindir+puid+'.offline').st_mtime>maxtime:
      activestatus='Abandoned'
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
  return extrasteps, activestatus,ban
def form(data,bypass,ispost,likeable,id=0):
  if not len(data)<1:
    extrasteps=''
    data=data.split(';')
    pver=int(data[0])
    pmature=data[1]
    ptime=data[2]
    timeduh=timeform(ptime)
    pname=data[3]
    puid=pname
    if os.path.isfile(logindir+data[3]+'.premium'):
      ppremium='1'
    else:
      ppremium='0'
    if os.path.isfile(logindir+data[3]+'.verified'):
      verified=True
    else:
      verified=False
    ptext=data[5]
    raw=ptext
    if "hitler" in raw.lower():
      return ''
    if id==100:
      getswon=True
    else:
      getswon=False
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
      c=hex_to_rgb(hcolor)
    else:
      colortime=''
    ban=False
    extrasteps, activestatus,ban= checkstatus(puid)
    if pmature=='1' and bypass==False:
      ptext='<p>This may contain Mature Content that is not suitable for younger audiences</p>'
    if ispost:
      extra='<a href="/?read=+data+">'
      extra2='</a>'
    else:
      extra=''
      extra2=''
    disabled=''
    if not admin:
      if ban:
        raw=''
        disabled='disabled'
        ptext='<p>This Post is hidden due to this Profile being Banned</p>'
    tmp='<div'
    tmp+=' class="contentblock"><a href="/?viewprofile='+str(pname)+'">'
    tmp+='<h3'+str(colortime)+isveri(ppremium)+'>'+pname+' </h3></a>'
    if verified:
      tmp+='<div style="background-color:#E7D27C;" class="notel">Verified User</div>'
    if getswon:
      tmp+='<div style="background-color:rgb(100,100,300);" class="notel">100th Post</div>'
    tmp+='<div '+extrasteps+' class="active">'+activestatus+'</div>'
    tmp+='<p>'+timeduh+'</p>'+extra+'<div class="datablock"><center>'+ptext+'</center></div>'+extra2
    if likeable:
      tmp+='<button style="margin:5px 0px 5px 0px;" disabled class="butt">Love</button><a href="/?create='+str(raw)+'"><button '+disabled+' style="margin:5px 0px 5px 0px;" class="butt">Repost</button></a><a href="?report='+str(id)+'"><button '+disabled+' style="margin:5px 0px 5px 0px;" class="butt">Report</button></a>'
      tmp+=getadmin(pname)
      if admin or uniqueid ==pname:
        tmp+='<a href="?delete='+str(id)+'"><button style="margin:5px 0px 5px 0px;" class="butt">Delete Post</button></a>'
    tmp+='</div>'
    return tmp
  else:
    return ''
def getadmin(nameuser):
  if admin:
   return '<a href="?banuser='+str(nameuser)+'"><button style="margin:5px 0px 5px 0px;" class="butt">Ban</button></a><a href="?unbanuser='+str(nameuser)+'"><button style="margin:5px 0px 5px 0px;" class="butt">Unban</button></a>'
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
if sign:
  extras='<a href="/?create"><button class="butt">Create</button></a>'
else:
  extras=''
extras=extras+'<a href="'+str(loginurl)+'"><button class="butt">'+logintext+'</button></a><a href="/wiki/"><button class="butt">Wiki</button></a></a>'
if os.path.isfile(logindir+str(uniqueid)+'.admin'):
  extras=extras+'<a href="/admin/"><button class="butt">Admin Panel</button></a>'
  admin=True
else:
  admin=False
#if str(uniqueid)=='Dub9':
#  admin=True
#elif str(uniqueid)=='AlphaWolf':
#  admin=True
#else:
#  admin=False
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
if os.path.isdir(profiledir+user):
  if os.path.isfile(profiledir+'uid'):
    if open(profiledir+'uid').read().replace('\n','') !=uniqueid:
      print('<div class="contentblock"><h3 style="color:white;">Your account has been banned, sorry it had to be like this :<</h3></div>')
if ispremium=='1':
  hometitle='<h1 class="hiddensecret" >Dub9</h1><h3 style="display:inherit;margin:-10px 0px 0px 10px;" class="verititle">Premium</h3>'
else:
  hometitle='<h1 class="hiddensecret" >Dub9</h1>'
if len(arg)==0:
  print(trail(home))
  print('<meta http-equiv="refresh" content="0; url=/?home" />')
else:
  try:
    arg=arg[0].split('=')
    if arg[0]=='home':
      print(trail(home))
    #print('<div style="background-color:yellow;color:white;text-shadow: 0px 0px 10px red;" class="bannerblock"><h3 style="background-color:black;">We might reset the database occasionally to sustain stability</h3></div>')
      axe=0
      try:
        for a in range(len(os.listdir(database))+1,0,-1):
          if os.path.isfile(database+str(a)):
            if not axe>49:
              print(form(open(database+str(a)).read().rstrip("\n"),False,True,True,id=a).replace('+data+',str(a)))
              axe+=1
            else:
              break
      except Exception as error:
        print('<div class="contentblock"><h3 style="color:red;">'+str(error)+'</h3></div>')  
      print('<div class="contentblock"><h3>There are '+str(len(os.listdir(database))+1)+' Posts Created! ('+str(int((time.time()-track)/0.01))+'ms)</h3></div>')
    elif arg[0]=='search':
      print(trail(home))
      axe=0
      for a in range(len(os.listdir(database)),0,-1):
        if not axe>49:
          if os.path.isfile(database+str(a)):
            an=str(a)
            data=open(database+an).read()
            #print(form('0;Andrew Tate;1;HELL'))
            if arg[1].lower() in data.lower():
              print(form(data,False,True,True,id=str(a)).replace('+data+',an))
              axe+=1
        else:
          break
      print('<div class="contentblock"><h3>'+str(axe)+' Posts  ('+str(int((time.time()-track)/0.01))+'ms)</h3></div>')
    elif arg[0]=='report':
      if len(arg)==1:
        print('<meta http-equiv="refresh" content="0; url=/" />')
      else:
        x=open(reportsdir+str(len(os.listdir(reportsdir))+1),'w')
        x.write(str(arg[1])+';'+str(uniqueid))
        x.close()
        print('<script>alert("This Post has been reported to our team :)");</script><meta http-equiv="refresh" content="0; url=/" />')

    elif arg[0]=='delete':
      if len(arg)==1:
        print('<meta http-equiv="refresh" content="0; url=/" />')
      else:
        tmp=open(database+arg[1]).read().split(";")
        if uniqueid==tmp[3] or admin:
          if os.path.isfile(database+arg[1]):
            w=open(database+arg[1],'w')
            w.write('1;0;'+str(int(time.time()))+';Deleted;0;[deleted post]')
            if os.path.isfile(commentsdir+arg[1]):
              open(database+arg[1],'w').close()
            print('<script>alert("Delete Successful");</script>')
        print('<meta http-equiv="refresh" content="0; url=/" />')
    elif arg[0]=='settings':
      print(trail(home))
      if len(arg)==1:
          print(str('<div class="contentblock" ><h3>Settings</h3>'))
          if "classicmode" in sys.argv:
            print('<a href="/api/modern.php"><button class="butt">Switch Back To Modern</button></a><br>')
          else:
            print('<a href="/api/classic.php"><button class="butt">Switch To Classic</button></a><br>')
    elif arg[0]=='viewprofile':
      if len(arg)==1:
        print('<meta http-equiv="refresh" content="0; url=/" />')
      else:
        print(trail(home))
        username=unquote(arg[1]).replace('+',' ')
        if os.path.isdir(profiledir+username):
          uid=username
          if os.path.isfile(logindir+uid+'.premium'):
            ppremium='1'
          else:
            ppremium='0'
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
          ban=False
          extrasteps, activestatus,ban= checkstatus(uid)
          if os.path.isfile(badgesdir+uid):
            ptext=''  
            for a in open(badgesdir+uid).readlines():
              tmp=a.replace('\n','')
              try:
                ptext+='<h3 style="margin:0px 0px 0px 10px;" class="pfcolor">'+str(badges[int(tmp)-1])+'</h3>'
              except Exception as error:
                break
          else:
            ptext='This Person does not have any badges'
          print(str('<div class="contentblock" >'))
          if os.path.isfile(profiledir+username+'/pfpurl'):
            print('<center><img style="margin:10px 0px 0px 0px;width:128px;height:128px;" src="'+str(open(profiledir+username+'/pfpurl').read().rstrip("\n"))+'"/></center>')
          print(str('<h3'+str(colortime)+isveri(ppremium)+'>'+username+' </h3><div '+extrasteps+' class="active">'+activestatus+'</div><p>'+bio+'</p>'+ptext+'<p></p>'))
          if sign:
            if username==user:
              if ispremium=='1':
                print('<a href="/?changecolor"><button class="butt">Change Color of your Profile (Premium Only)</button></a><br><a href="/?redeem"><button class="butt">Redeem Code</button></a><br>')
              else:
                print('<a href="/?redeem"><button class="butt">Redeem Code for Premium</button></a><br>')
              print('<a href="/?changebio"><button class="butt">Change Bio</button></a><br>')
              print('<a href="/?changepassword"><button class="butt">Change Password</button></a><br>')
              #print('<input type = "button" onclick = "eraseCookie(usr)" value = "Sign Out">')
              print('<a href="/?settings"><button class="butt">More Settings</button></a><br>')
              print('<a href="/api/destruct.php"><button class="butt">Sign Out</button></a><br>')
            print(getadmin(username))
          print('</center></div></div>')
        else:
          print('<div class="contentblock"><h3 style="display: inline-block;">'+username+' does not exist</h3></div>')
    elif arg[0]=='unbanuser':
      if admin:
        if not len(arg)==1:
          if os.path.isfile(logindir+arg[1]+'.banned'):
            os.remove(logindir+arg[1]+'.banned')
      print('<meta http-equiv="refresh" content="0; url=/" />')
    elif arg[0]=='banuser':
      if admin:
        if not len(arg)==1:
          if not os.path.isfile(logindir+arg[1]+'.banned'):
            open(logindir+arg[1]+'.banned','w').close()
      print('<meta http-equiv="refresh" content="0; url=/" />')

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
            tmp=open(database+str(arg[1])).read().rstrip("\n")
            ban=False
            try:
              if os.path.isfile(logindir+tmp.split(';')[3]+'.banned'):
                ban=True
            except Exception:
              ban=True
            print(form(tmp,True,False,True,id=arg[1]))
            if not ban:
              print('<div class="contentblock"><h3 style="text-align:left;margin:0px 0px 0px 20px;padding:20px 0px;"><a href="/?viewdev='+arg[1]+'">Comments</a> ('+str(slots)+' slots left):</h3><div style="margin:0px 0px 20px 0px;"><form><input type="text" maxlength="100" class="seobar"  name="comment='+str(arg[1]))
              print('"></input><button class="seo">Comment</button></form></div></div>')
      #      else:
            if not os.path.isfile(commentsdir+arg[1]):
              open(commentsdir+arg[1],'w').close()
            if os.path.isfile(commentsdir+arg[1]):
              if len(open(commentsdir+arg[1]).readlines())==0:
                if not ban:
                  print('<div class="contentblock"><h3>Be the first to comment on this Post!</h3></div>')
              else:
                if ban:
                  print('<div class="contentblock"><p>Comments are Archived because "'+tmp.split(';')[3]+'" is in a archived state</p></div>')
                for a in open(commentsdir+arg[1]).readlines():
                  if not len(a)<2:
                    print(form(a,True,False,False))
                      
          except Exception as error:
            print('<div class="contentblock"><h3 style="color:red;">The post is hidden for security purposes</h3></div>')
            print(error)
    elif arg[0]=='comment':
      if banned:
        print('<meta http-equiv="refresh" content="0; url=/" />')
        exit()
      if len(arg)<3:
        print('<meta http-equiv="refresh" content="0; url=/" />')
      else:
        if sign:
          if maxslots-len(open(commentsdir+arg[1]).readlines())<1:
            print('alert("You can not post anymore Comments on this Post");<meta http-equiv="refresh" content="3; url=/" />')
          else:
          #print(arg)
            comments=arg[2]
            if 1==2:
              pass
#            if str(uniqueid) in open(commentsdir+arg[1]).read():
#              print('You can only comment one per post<meta http-equiv="refresh" content="3; url=/?read='+arg[1])
#              print('" />')
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
    elif arg[0]=='changepassword':
      if len(arg)==1:
        if sign:
          print(trail(home))
          print('<div class="contentblock"><h3>Here your New Password</h3><form><input type="text" maxlength="255" class="seobar"  name="changepassword"></input><button class="seo">Change</button></div>')
        else:
          print('<meta http-equiv="refresh" content="0; url=/" />')
      else:
        if sign:
          code=str(unquote(arg[1])).replace('<','').replace('>','')
          if not code=='':
            print('<meta http-equiv="refresh" content="0; url=/" />')
            x=open(logindir+str(uniqueid),'w')
            x.write(code.replace('+',''))
            x.close()
          else:
            print('<meta http-equiv="refresh" content="0; url=/?changepassword" />')
#          else:
 #           print('<meta http-equiv="refresh" content="0; url=/" />')
    elif arg[0]=='changecolor':
      if len(arg)==1:
        if sign:
          print(trail(home))
          colors=['#000000','#FF0000','#00FF00','#0000FF','#CCF1FF','#E0D7FF','#FFCCE1','#D7EEFF','#FAFFC7','#C85EFF','#34568B','#FF6F61','#6B5B95','#88B04B','F7CAC9','#92A8D1','#B565A7','#009B77','#D65076','#5B5EA6','#9B2335','#BC243C']
          print('<div class="contentblock"><center><h3>Choose your Color</h3>')
          if os.path.isfile(logindir+str(uniqueid)+'.color'):
            tmp=open(logindir+str(uniqueid)+'.color').read().replace('\n','')
          else:
            tmp='#248977'
          for a in colors:
            if tmp==a:
              clicked=True
            else:
              clicked=False
            def va():
              if clicked:
                return 'border:2px solid white;'
              else:
                return ''
            print('<a href="/?changecolor='+str(a.replace('#','%23'))+'"><button style="'+str(va())+'cursor: pointer;background-color:'+str(a)+';padding:20px 20px;border-radius:40px;"></button></a>')
          print('</center><h3>Or You Want to Choose your own Color (html code only)</h3><form><input type="text" maxlength="7" class="seobar"  name="changecolor"></input><button class="seo">Change Color</button></div>')
        else:
          print('<meta http-equiv="refresh" content="0; url=/" />')
      else:
        if sign:
          if ispremium=='1':
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
    elif arg[0]=='viewdev':
      if len(arg)==1:
        print('<meta http-equiv="refresh" content="0; url=/" />')
      else:
        print(trail(home))
        tmp=open(database+str(arg[1])).read().rstrip("\n").split(';')
        print('<div class="contentblock"><h3>Post Version:'+str(tmp[0])+'</h3><h3>ismature:'+str(tmp[1])+'</h3><h3>Time in Unix Time:'+str(tmp[2])+'</h3><h3>Creator:'+str(tmp[3])+'</h3><h3>ispremium:'+str(tmp[4])+'</h3><h3>Raw Text:'+str(tmp[5])+'</h3>')


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
            open(logindir+str(uniqueid)+'.premium','w').close()
          elif code=='P4O6RAM':
            x=open(badgesdir+str(uniqueid),'a')
            x.write('6\n')
            x.close()
            print('<meta http-equiv="refresh" content="0; url=/" />')
          elif code=='bantest':
            open(logindir+str(uniqueid)+'.banned','w').close()
            print('<meta http-equiv="refresh" content="0; url=/" />')
          elif code=='P3PPY':
            x=open(badgesdir+str(uniqueid),'a')
            x.write('5\n')
            x.close()
            print('<meta http-equiv="refresh" content="0; url=/" />')
          else:
            print('<meta http-equiv="refresh" content="0; url=/?redeem" />')
    elif arg[0]=='create':
      if banned:
        print('<meta http-equiv="refresh" content="0; url=/" />')
        exit()
      if len(arg)==1:
        print(trail(home))
        print(trail(open('/home/pxki/web/create.htm').read()))
      else:
        if sign:
          if not paused:
            scotty=len(os.listdir(database))+1
            if os.path.isfile(database+str(scotty)):
              a=1
              scotty=scotty+1
              while a:
                if os.path.isfile(database+str(scotty)):
                  scotty=scotty+1
                else:
                  a=0
            x=open(database+str(scotty),'w')
          if "ismature" in arg:
            ismature='1'
          else:
            ismature='0'
          if not paused:
            x.write(str(version)+';'+str(ismature)+';'+str(int(time.time()))+';'+str(uniqueid)+';'+str(ispremium)+';'+str(str(unquote(arg[1])).replace(';','').replace('+',' ').replace('<','').replace('>',''))[:100])
            x.close()
            print('<meta http-equiv="refresh" content="0; url=/" />')
          else:
            print('<script>alert("Right Now, we have paused Creating Posts. Sorry for the inconvience :(");</script><meta http-equiv="refresh" content="0; url=/" />')
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
