# facebook : https://www.facebook.com/profile.php?id=100018564715368 
#
import os
os.system('clear')
hl='\033[1;36m' # 
bl='\033[1;34m' # blue
wi="\033[1;37m" # White
rd="\033[1;31m" # Red
gr="\033[1;32m" # Green
yl="\033[1;33m" # Yellow
pu='\033[1;35m' # pu
while True :
    os.system('clear')
    print(gr,'''                                # Info Tool #
                         The creator : Monder-bs
                         The mission : This tool is used to set a password for the Termux interface
''')
    print('''
                                           @
                                           @
                                          | |
                                          | |
                          /---------------| |----
                         /                    / |
                        /_   _  ___  __  __ _/__|
                        | | | |/ _ \|  \/  | ___|
                        | |_| | | | | |\/| |  _|
                        |  _  | |_| | |  | | |__
                        |_| |_|\___/|_|  |_|____|

''')
    print('\n','-'*50,'\n')
    print(yl,'1) Termux password \n')
    print(gr,'2) remove password \n')
    print(bl,'3) Information about the use of the tool \n')
    print(rd,'0) Exit \n')
    print(hl)
    cv =str(input('[?] Choose a number : '))
    if cv == '1' :
        os.system('clear')
        print(gr,'''
             _______________________________________
             mmmmmm
             #       mmm    mmm    mmm    mmm    mmm
             #mmmmm #"  #  #"  "'''+bl,''' #" "#  #" "#  #""#
             #      #   #  #      #   #  #   #  #==#
             #mmmmm #   #  "#mm"  "#m#"  "#m##  "#mm"
             ________________________________________
''')
        #---------------------------------------
        motd=open('/data/data/com.termux/files/usr/etc/motd','w')
        motd.write(' -------------------------- Welkom to Termux -------------------------')
        motd.close()
        code_run='/data/data/com.termux/files/usr/etc/bash.bashrc'
        pw='/data/data/com.termux/files/usr/etc'
        data=('''
import os
bl='\033[1;34m'
rd="\033[1;31m"
gr="\033[1;32m"
op=open('/data/data/com.termux/files/usr/etc/code.text','r')
re=op.read()
ps=re.split()[0]
ag=re.split()[-1]
def coding():
    try :
        print('')
        while True :
            print(gr)
            pass_word=input('[?] Enter password :')
            age=input('[?] Enter age :')
            if pass_word == ps :
                if age == ag :
                    print(gr,'Go write the code ......')
                    break
            elif pass_word and age == 'bsmi alah':
                print(gr,'Go write the code ......')
                break
            else :
                print(rd,'not found')
    except KeyboardInterrupt :
        print(rd,'not found ?')
        coding()
    except EOFError :
        print(rd,'not found ?')
        coding()
coding()
''')
        #os.chdir(pw)
	#-----------------------------------
        code_py=open('/data/data/com.termux/files/usr/etc/code.py','w',newline='')
        code_py.write(data)
        code_py.close()
        #-----------------------------------
        print(hl,'')
        code_yes=input('[?] Enter the interface password :')
        age_yes=input('[?] Enter your  age :')
        code_data=(f'''{code_yes}
{age_yes}
''')
        #-----------------------------------
        txt=open('/data/data/com.termux/files/usr/etc/code.text','w')
        txt.write(code_data)
        txt.close()
        #----------------------------------------
        with open ('start_bash.text','r') as bash_hello :
            red5=bash_hello.read()
        bash_hello.close()
        with open ('/data/data/com.termux/files/usr/etc/bash.bashrc','w',newline='') as run :
            run.write(red5)
        run.close()
        print(gr,'\n [+] complet ')
        print(gr,'[+] your password is ==> '+code_yes)
        print(gr,'[+] your age ==> '+age_yes)
        break
    if cv == '2':
        os.system('clear')
        print(pu,'''
    *-----------------------------------------*
    |      _ _                      _         |
    |     |  _ \  ___  ___ ___   __| | ___    |
    |     | | | |/ _ \/ __/ _ \ / _` |/ _ \   |
    |     | |_| |  __/ (_| (_) | (_| |  __/   |
    |     |____/ \___|\___\___/ \__,_|\___|   |
    |                                         |
    *-----------------------------------------*
''')
        with open ('go_bash.text','r') as start :
            line = start.read()
            print(gr,'')
        start.close()
        with open ('/data/data/com.termux/files/usr/etc/bash.bashrc','w') as bash_new :
            bash_new.write(line)
        bash_new.close()
        print(gr,'[+] Password removal finished ')
        break
    if cv == '3':
        os.system('clear')
        print(gr,'Enter :\n'+rd,'1)'+yl,'To set a password for the Termux interface\n'+rd,'2)'+yl,'To remove the interface password\n'+rd,'0)'+yl,'To Exit The Tool')
        break
    if cv == '0' :
        print(gr,'\n Thank you for using my tool !!')
        break

