import zipfile,os,sys,threading,time

"""
Recode Can't Make You The Real Programmer
"""

os.system("clear")
berhasil = []
count = 0
banner = """
 ___ZIP__
|   //   |
|   \\\   | > Zip Cracker v1
|   //   | > Author : H1B1K1_404
|   \\\   | > Team : LaughSec
|   //   | > Greetz : All Admins And Members
|___\\\___|
"""
print banner
def main(file,pas):
  global counts,count
  try:
   zip = zipfile.ZipFile(file)
   zip.extractall("result",pwd=pas)
   berhasil.append("[+] "+pas)
  except:
   pass
  count +=1
  print "\r[!] Cracking -%s/%s"%(count,counts),;sys.stdout.flush()
def x():
 try:
  global counts,count
  print
  f = raw_input("[+] File (.zip) : ")
  pasq = raw_input("[+] Wordlist : ")
  pas = open(pasq,"r").read().split("\n")
  counts = len(pas)
  for i in pas:
   t = threading.Thread(target=main,args=(f,i))
   t.start()
   if len(berhasil) !=0:
    time.sleep(7)
    print "\n[+] Password Found"
    for x in berhasil:
     print x
    os.system("rm -rf result")
    sys.exit()
  time.sleep(7)
  os.system("rm -rf result")
  print "\n[-] Password Not Found"
 except KeyboardInterrupt:
  os.system("rm -rf result")
  time.sleep(5)
  print "\n[-] Closed By User"
 except IOError:
  time.sleep(5)
  print "\n[!] File Not Found"
x()
