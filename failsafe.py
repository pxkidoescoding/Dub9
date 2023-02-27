import os,sys
sys.argv=sys.argv[1:]
test=False
try:
    exec(open(sys.argv[0]).read())
except Exception as error:
    print('<h1>'+str(error)+'</h1>')