#! /usr/bin/env/python3
import os
from time import sleep as timeout
#===================================#
W='\033[1;32m'
A='\033[1;33m'
B='\033[1;30m'
V= '\033[;36m'
D='\033[;0m'
VM='\033[1;31m'
M='\033[1;30m'
P='\033[1;31m'
G='\033[1;34m'
C='\033[36m'
H='\033[1;35m'


# interface de usuário é banner #
#==================================#
os.system("clear")
def menu():
	print(f"""
    {C}
▒▄█▀▀█▒▐█▀▀█▌░▐█▀█▐██░░▄█▀▄─▒██░░░
▒▀▀█▄▄▒▐█▄▒█▌░▐█──░█▌░▐█▄▄▐█▒██░░░
▒█▄▄█▀▒▐██▄█▌░▐█▄█▐██░▐█─░▐█▒██▄▄█
{G}
:::::::::  :::            :::      ::::::::  :::    :::
:+:    :+: :+:          :+: :+:   :+:    :+: :+:   :+:
+:+    +:+ +:+         +:+   +:+  +:+        +:+  +:+
+#++:++#+  +#+        +#++:++#++: +#+        +#++:++
{H}+#+    +#+ +#+        +#+     +#+ +#+        +#+  +#+
#+#    #+# #+#        #+#     #+# #+#    #+# #+#   #+#
{P}#########  ########## ###     ###  ########  ###    ###
{V}
 *==========================================+
 * {W}CRIADOR ~》Clay404                     {C}  *
 * {W}Telegram ~》 https://t.me/Clayy404{C}	    *
 * {W}Parceiro ~》Abaddon Morningstar       {C}   *
 +===========================+==============+
 *   {A}[1]{C}╠➥$Kali linux
 *   {A}[2]{C}╠➥$Configuração termux
 *   {A}[3]{C}╠➥$Koroni
 *   {A}[4]{C}╠➥$Zphisher
 *   {A}[5]{C}╠➥$FotoSploit
 *   {A}[6]{C}╠➥$Weeman
 *   {A}[7]{C}╠➥$Splmap
 *   {A}[8]{C}╠➥$Impulse
 *   {A}[9]{C}╠➥$Urlspoof
 *  {A}[10]{C}╠➥$Lazymux
 *  {A}[11]{C}╠➥$Wifite
 *  {A}[12]{C}╠➥$Fbi
 *  {A}[13]{C}╠➥$Kali nethunter
 *  {A}[14]{C}╠➥$Kiny painel
 *  {A}[15]{C}╠➥$Spamwa
 *  {A}[16]{C}╠➥$Wifi-hacker
 *  {A}[17]{C}╠➥$SocialFish
 *  {A}[18]{C}╠➥$Routersploit
 *  {A}[19]{C}╠➥$Nexphisher
 *  {A}[20]{C}╠➥$Ps.ngrok
 *  {A}[21]{C}╠➥$Anon-msg
 *  {A}[22]{C}╠➥$Tstyling
 *  {A}[23]{C}╠➥$Metasploit-framework
 *  {A}[24]{C}╠➥$LazyFiglet
 *  {A}[25]{C}╠➥$RED_HAWK
 *  {A}[26]{C}╠➥$Spamrito
 *  {A}[27]{C}╠➥$Tool-X
 *  {A}[28]{C}╠➥$DDOS
 *  {A}[29]{C}╠➥$torshammer
 *  {A}[30]{C}╠➥$clis
 *  {A}[31]{C}╠➥$AIOPhish
+===========================+=============+
* {A}[90$╠➥$Atualizar termux] {C}    {P}0$╠➥$SAIR{C}  *
+=========================================+

""") 
menu()
def sair_do_programar():
	print(f"""
	
 {C}   __________
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║
  ╔════════════╗
  ╚════════════╝{V}
 {B} ║██████████╚╗
  ║██{P}╔══╗{B}█{P}╔═╗{B}█║
  ║██{P}║╬╔╝{B}█{P}╚╗║{B}█║
  ║██{P}╚═╝{B}█║█{P}╚╝{B}█║
  ╚╗█████████═╝
     ╚╗║╠╩╩╩╩╩╝[D404RBLACK]
        ║║┈┈┈█{C}▐█████{P}▒.｡oO
       {B} ║██╠╦╦╦╗
        ╚╗██████
           ╚════╝{B}
[VOLTE SEMPRE BROW]
""")


#construção da ferramenta
while True:
    print(" ")
    opcao = input (f"""{C}  > set_install~>: """)
   
        
    if opcao == "90":
                    def confg():
                        os.system("apt update -y")
                        os.system("pkg upgrade -y")
                        os.system("pkg install python -y")
                        os.system("pkg install python2 -y")
                        os.system("pkg install pip -y")
                        os.system("pkg install pip2 -y")
                        os.system("pkg install pip3 -y")
                        os.system("pkg install nano -y")
                        os.system("pkg install perl -y")
                        os.system("pkg install npm -y")
                        print("~"*27)
                        print(f"{P}Instalação concluída...");timeout(3);
                        print(f"{H}[99] ~> Para voltar ao menu")
                    confg()
                    
    elif opcao == "1":
                    def kali():
                        os.system("apt update -y")
                        os.system("pkg upgrade -y")
                        os.system("pkg install wget -y")
                        os.system("pkg install wget proot -y && wget https://raw.githubusercontent.com/MasterDevX/KaliTermux/master/InstallKali.sh && bash InstallKali.sh")
                        os.system("mv InstallKali.sh /data/data/com.termux/files/home")
                        os.system("mv kali-binds /data/data/com.termux/files/home")
                        os.system("mv start-kali.sh /data/data/com.termux/files/home")
                        os.system ("mv kali-fs /data/data/com.termux/files/home")
                        print(f"{P}Instalação concluída...");timeout(3);
                        print("~"*27)
                        print(f"{H}[99] ~> Para voltar ao menu")
                    kali()
                   
    elif opcao == "2":
                    def confg():
                        os.system("apt update -y")
                        os.system("pkg upgrade -y")
                        os.system("pkg install git -y")
                        os.system("git clone https://github.com/403ForbiddenF1/configurar_termux")
                        print(f"{P}Instalação concluída...");timeout(3);
                        print(f"{P}Instalação concluída...");timeout(3);
                        print("~"*27)
                        print(f"{H}[99] ~> Para voltar ao menu")
                    confg()
	                 
    elif opcao == "3":
                    def koroni():
                        os.system ("termux-setup-storage")
                        os.system("apt update -y")
                        os.system("pkg upgrade -y")
                        os.system ("pkg install git -y")
                        os.system("pkg install php -y")
                        os.system("git clone https://github.com/DeepSociety/koroni")
                        print(f"{P}Instalação concluída...");timeout(3);
                        print("~"*27)
                        print(f"{H}[99] ~> Para voltar ao menu")
                    koroni ()
                    
    elif opcao == "4":
                    def zphisher():
                        os.system("apt update -y")
                        os.system("pkg upgrade -y") 
                        os.system("pkg install git -h")
                        os.system("pkg install php -y")
                        os.system("git clone  git://github.com/htr-tech/zphisher.git")
                        os.system("mv zphisher /data/data/com.termux/files/home")
                        print(f"{P}Instalação concluída...");timeout(3);                        print("~"*27)
                        print(f"{H}[99] ~> Para voltar ao menu")
                    zphisher()
                    
    elif opcao == "5":
                    def fotosploit():
                        os.system ("apt update -y")
                        os.system ("pkg upgrade -y")
                        os.system ("pkg install git -y")
                        os.system("pkg install php -y")
                        os.system("git clone https://github.com/Cesar-Hack-Gray/FotoSploit")
                        os.system("mv FotoSploit /data/data/com.termux/files/home")
                        print(f"{P}Instalação concluída...");timeout(3);
                        print("~"*27)
                        print(f"{H}[99] ~> Para voltar ao menu")
                    fotosploit()
               
    elif opcao == "6":
                    def weeman():
                        os.system("apt update -y")
                        os.system("pkg upgrade -y")
                        os.system("pkg install git -y")
                        os.system("pkg install python -y")
                        os.system("git clone https://github.com/evait-security/weeman")
                        os.system("mv weeman /data/data/com.termux/files/home")
                        print(f"{P}Instalação concluída...");timeout(3);
                        print("~"*27)
                        print(f"{H}[99] ~> Para voltar ao menu")
                    weeman()
                
    elif opcao == "7":
                    def sqlmap():
                        os.system("apt update -y")
                        os.system("pkg upgrade -y")
                        os.system("pkg install git -y")
                        os.system("git clone https://github.com/sqlmapproject/sqlmap")
                        os.system("mv sqlmap /data/data/com.termux/files/home")
                        print(f"{P}Instalação concluída...");timeout(3);
                        print("~"*27)
                        print(f"{H}[99] ~> Para voltar ao menu")
                    sqlmap()
                    
    elif opcao =="8":
                    def impulse():
                        os.system("clear")
                        os.system("apt update -y")
                        os.system("pkg upgrade -y")
                        os.system("pkg install python -y")
                        os.system ("pkg install python2 -y")
                        os.system("pkg install git -y")
                        os.system("git clone https://github.com/LimerBoy/Impulse")
                        os.system("mv Impulse /data/data/com.termux/files/home")
                        print(f"{P}Instalação concluída...");timeout(3);
                        print("~"*27)
                        print(f"{H}[99] ~> Para voltar ao menu")
                    impulse() 
                      
    elif opcao == "9":
             def urlspoof():
                 os.system("apt update -y")
                 os.system("pkg upgrade -y")
                 os.system("pkg install python -y")
                 os.system("pkg install git -y")
                 os.system("git clone https://github.com/Darkmux/URLSpoof")
                 os.system("mv URLSpoof /data/data/com.termux/files/home")
                 print(f"{P}Instalação concluída...");timeout(3);
                 print("~"*27)
                 print(f"{H}[99] ~> Para voltar ao menu")
             urlspoof()
             
    elif opcao == "10":
             def lazymux():
                 os.system("apt update -y")
                 os.system("pkg upgrade -y")
                 os.system("pkg install python -y")
                 os.system("pkg install python2 -y")
                 os.system("git clone https://github.com/Gameye98/Lazymux")
                 os.system("mv Lazymux /data/data/com.termux/files/home")
                 os.system("mv lazymux.conf /data/data/com.termux/files/home")
                 print(f"{P}Instalação concluída...");timeout(3);
                 print("~"*27)
                 print(f"{H}[99] ~> Para voltar ao menu")
             lazymux()
             
    elif opcao == "11":
                    def wifite():
                        os.system("apt update -y")
                        os.system("pkg upgrade -y")
                        os.system("pkg install python -y")
                        os.system("pkg install python2 -y")
                        os.system("pkg install git -y")
                        os.system(" git clone https://github.com/derv82/wifite")
                        os.system("mv wifite /data/data/com.termux/files/home")
                        print(f"{P}Instalação concluída...");timeout(3);
                        print("~"*27)
                        print(f"{H}[99] ~> Para voltar ao menu")
                    wifite()
                                     
    elif opcao =="12":
           def fbi():
               os.system("apt update -y")
               os.system("cd ..")
               os.system("pkg upgrade -y")
               os.system("pkg install python -y")
               os.system("pkg install python2 -y")
               os.system("pkg install git -y")
               os.system("git clone https://github.com/xHak9x/fbi.git")
               os.system("mv fbi /data/data/com.termux/files/home")
               print(f"{P}Instalação concluída...");timeout(3);
               print("~"*27)
               print(f"{H}[99] ~> Para voltar ao menu")
           fbi()

    elif opcao =="13":
                      def kali_nethunter():
                          print("="*26)
                          print("AVISO:")
                          print (f"{P}Essa função requer 16GB De armazenamento livres É 2GB Ram.\nSe não tive esse requesito recomendo não prosseguir essa ação. ")
                          print(" ")
                          print("[S]im\n[N]ão\n----------")
                          op = input (f"{A}Desejar prosseguir ~~>: ")
                          if op == "N":
                              def opc():
                                 print(f"{G}Voltando ao menu...");timeout(2);
                                 os.system("clear")
                                 menu()
                              opc()
                                 
                          elif op =="S":
                              def install():
                                  os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh")
                                  print(f"{P}Instalação concluída...");timeout(3);
                                  print("~"*27)
                                  print(f"{H}[99] ~> Para voltar ao menu")
                              install()
                              
                          else:print(f"{C}~~>Opção inválida");timeout(3);
                      kali_nethunter()
                      
    elif opcao == "14":
                      def  kiny():
                          os.system("apt update -y")
                          os.system("pkg upgrade -y")
                          os.system("pkg install python -y")
                          os.system("pkg install python2 -y")
                          os.system("pkg install git -y")
                          os.system("git clone https://github.com/Kiny-Kiny/Kiny-Painel")
                          os.system("mv Kiny-Painel /data/data/com.termux/files/home")
                          print(f"{P}Instalação concluída...");timeout(3);
                          print("~"*27)
                          print(f"{H}[99] ~> Para voltar ao menu")
                      kiny()
                      
    elif opcao == "15":
                      def spamwa():
                          os.system("apt update -y")
                          os.system("pkg upgrade -y")
                          os.system("pkg install git -y")
                          os.system("pkg install python -y")
                          os.system("pkg install python2- y")
                          os.system("git clone https://github.com/sandiwijayani1/SpamWa")
                          os.system("mv SpamWa /data/data/com.termux/files/home")
                          print(f"{P}Instalação concluída...");timeout(3);
                          print("~"*27)
                          print(f"{H}[99] ~> Para voltar ao menu")
                      spamwa()
                           
    elif opcao == "16":
                     def hacker_wifi():
                            os.system ("apt update -y")
                            os.system("pkg upgrade -y")
                            os.system ("pkg install git -y")
                            os.system("git clone https://github.com/esc0rtd3w/wifi-hacker")
                            os.system("mv wifi-hacker /data/data/com.termux/files/home")
                            print(f"{P}Instalação concluída...");timeout(3);
                            print("~"*27)
                            print(f"{H}[99] ~> Para voltar ao menu")
                     hacker_wifi()
       
    elif opcao == "17":
                      def fish():
                             os.system ("apt update -y")
                             os.system("pkg upgrade -y")
                             os.system("pkg install python2 -y")
                             os.system("git clone https://github.com/UndeadSec/SocialFish")
                             os.system("mv SocialFish /data/data/com.termux/files/home")
                             print(f"{P}Instalação concluída...");timeout(3);
                             print("~"*27)
                             print(f"{H}[99] ~> Para voltar ao menu")
                      fish()
                      
    elif opcao == "18":
                       def Routersploit():
                            os.system("apt update -y")
                            os.system("pkg upgrade -y")
                            os.system("termux-setup-storage")
                            os.system ("pkg install python git clang -y")
                            os.system("pkg install -y")
                            os.system("pkg install make -y")
                            os.system ("pkg install python -y")
                            os.system ("git clone https://github.com/threat9/routersploit")
                            os.system("mv routersploit /data/data/com.termux/files/home")
                            print(f"{P}Instalação concluída...");timeout(3);
                            print("~"*27)
                            print(f"{H}[99] ~> Para voltar ao menu")
                       Routersploit()
        
    elif opcao =="19":
                      def nexphisher():
                            os.system("apt update -y")
                            os.system("pkg upgrade -y")
                            os.system("pkg install git -y")
                            os.system("git clone https://github.com/htr-tech/nexphisher")
                            os.system("mv nexphisher /data/data/com.termux/files/home")
                            print(f"{P}Instalação concluída...");timeout(3);
                            print("~"*27)
                            print(f"{H}[99] ~> Para voltar ao menu")
                      nexphisher()
        
    elif opcao =="20":
                       def ps_ngrok():
                            os.system("apt upgrade -y")
                            os.system("pkg upgrade -y")
                            os.system("pkg install git -y")
                            os.system("git clone https://github.com/PSecurity/ps.ngrok")
                            os.system("mv ps.ngrok /data/data/com.termux/files/home")
                            print(f"{P}Instalação concluída...");timeout(3);
                            print("~"*27)
                            print(f"{H}[99] ~> Para voltar ao menu")
                       ps_ngrok()
        
    elif opcao =="21":
                       def anon_msg():
                           os.system("apt update -y")
                           os.system("pkg upgrade -y")
                           os.system("pkg install python -y")
                           os.system("pkg install python2 -y")
                           os.system("pkg install git -y")
                           os.system("git clone https://github.com/Detrew/Anon-msg")
                           os.system("mv Anon-msg /data/data/com.termux/files/home")
                           print(f"{P}Instalação concluída...");timeout(3);
                           print("~"*27)
                           print(f"{H}[99] ~> Para voltar ao menu")
                       anon_msg()
        
    elif opcao == "22":
                      def banner():
                          os.system("apt update -y")
                          os.system("pkg upgrade -y")
                          os.system("pkg install git -y")
                          os.system("git clone https://github.com/darkwarrior3/tstyling")
                          os.system("mv tstyling /data/data/com.termux/files/home")
                          print(f"{P}Instalação concluída...");timeout(3);
                          print("~"*27)
                          print(f"{H}[99] ~> Para voltar ao menu")
                      banner()
   
    elif opcao =="23":
                      def metasploit():
                          os.system("apt update -y")
                          os.system ("pkg upgrade -y")
                          os.system("pkg install git -y")
                          os.system("git clone https://github.com/rapid7/metasploit-framework")
                          os.system("mv metasploit-framework /data/data/com.termux/files/home")
                          print(f"{P}Instalação concluída...");timeout(3);
                          print("~"*27)
                          print(f"{H}[99] ~> Para voltar ao menu")
                      metasploit()
    
    elif opcao =="24":
        def LazyFiglet():
            os.system("apt update -y")
            os.system("pkg upgrade -y")
            os.system("pkg install git -y")
            os.system("git clone https://github.com/TechnicalMujeeb/LazyFiglet.git")
            os.system("mv LazyFiglet /data/data/com.termux/files/home")
            print(f"{P}Instalação concluída...");timeout(3);
            print("~"*27)
            print(f"{H}[99] ~> Para voltar ao menu")     
        LazyFiglet()

    elif opcao == "25":
        def  RED_HAWK():
            os.system("apt update -y")
            os.system("pkg upgrade -y")
            os.system("pkg install git -y")
            os.system("pkg install php -y")
            os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
            os.system("mv RED_HAWK /data/data/com.termux/files/home")
            print(f"{P}Instalação concluída...");timeout(3);
            print("~"*27)
            print(f"{H}[99] ~> Para voltar ao menu")
        RED_HAWK()
    
    elif opcao == "26":
           def spamrito():
               os.system("apt update -y")
               os.system("pkg upgrade -y")
               os.system("pkg install git -y")
               os.system("git clone https://github.com/MisterIot/spamrito")
               os.system("mv spamrito /data/data/com.termux/files/home")
               print(f"{P}Instalação concluída...");timeout(3);
               print("~"*27)
               print(f"{H}[99] ~> Para voltar ao menu")
           spamrito()
   
    elif opcao == "27":
           def Tool():
               os.system("apt update -y")
               os.system("pkg upgrade -y")
               os.system("pkg install git -y")
               os.system("git clone https://github.com/rajkumardusad/Tool-X")
               os.system("mv Tool-X /data/data/com.termux/files/home")
               print(f"{P}Instalação concluída...");timeout(3);
               print("~"*27)
               print(f"{H}[99] ~> Para voltar ao menu")
           Tool()

    elif opcao =="28":
        def ddos():
            os.system ("apt update -y && pkg upgrade -y")
            os.system("pkg install python -y")
            os.system("pkg install python2 -y")
            os.system("pkg install git -y")
            os.system("git clone https://github.com/pembriahmad/DDOS")
            os.system("mv DDOS /data/data/com.termux/files/home")
            print(f"{P}Instalação concluída...");timeout(3);
            print("~"*27)
            print(f"{H}[99] ~> Para voltar ao menu")
        ddos()

    elif opcao == "29":
             def torshammer():
                 os.system("apt update -y && pkg upgrade -y")
                 os.system("pkg install python -y")
                 os.system("pkg install python2 -y")
                 os.system("pkg install git -y")
                 os.system("git clone https://github.com/dotfighter/torshammer")
                 os.system("mv torshammer /data/data/com.termux/files/home")
                 print(f"{P}Instalação concluída...");timeout(3);
                 print("~"*27)
                 print(f"{H}[99] ~> Para voltar ao menu")
             torshammer()

    elif opcao == "30":
            def clis():
                os.system("apt update -y && pkg upgrade -y")
                os.system("pkg install git -y")
                os.system("git clone https://github.com/Olliv3r/clis")
                os.system("mv clis /data/data/com.termux/files/home")
                print(f"{P}Instalação concluída...");timeout(3);
                print("~"*27)
                print(f"{H}[99] ~> Para voltar ao menu")
            clis()

    elif opcao =="31":
            def aiophish():
                 os.system("apt update -y && pkg upgrade -y")
                 os.system("pkg install git -y")
                 os.system("git clone https://github.com/DeepSociety/AIOPhish")
                 os.system("mv AIOPhish /data/data/com.termux/files/home")
                 print(f"{P}Instalação concluída...");timeout(3);
                 print("~"*27)
                 print(f"{H}[99] ~> Para voltar ao menu")
            aiophish()

    elif opcao == "0":
                     def sair():
                         os.system("clear")
                         sair_do_programar()
                         print("SAINDO DO PROGRAMAR....");timeout(3);                
                         exit()
                     sair()
                             
    elif opcao == "99":
                        print(f"{G}Voltando ao menu...");timeout(2);
                        os.system("clear")
                        menu()
                               
    else: 
          print("~"*25)
          print(f"{P}Opção Inválida :(");timeout(3);
          print(f"{C}~"*25)
          os.system ("clear")
          menu()

