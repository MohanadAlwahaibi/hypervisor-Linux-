# hypervisor 
# has a type 1 and type 2 

# what is a hypervisor?
# a hypervisor is a software that creates and runs virtual machines (VMs)

# what is hypervisor type 1?
# a hypervisor type 1 runs directly on the host's hardware to control the hardware 
# and to manage guest operating systems (KVM, Xen, VMware ESXi)

# what is hypervisor type 2?# a hypervisor type 2 runs on a conventional operating system just as other computer programs do
# relies on the host OS for device support and management (virtualBox , vmware, oracle VM)

# ping is getting icmp
# if the ping is not reaching or packet loss 
# that means that ether the host is down or the firewall dropped it 

# the commands we usually use this:
# man {{manual to get information about a specific tool}}
# ls -al {{to show hidden files}}
# ps -aef | all with additional information
# ps -aef | grep "exercise.py" {{to check for "exersise.py"}}
# kill -9 3864 {{to end process}}


# echo %JAVA_APP%
# env

# CD ~ {{"~" go to home directory}}
# cp main.py ./yet_another_directory {{to copy a file}}

# mv main_app.py ../main_app.py {{move the file in documents}}

#mv main_app.py ./app.py {{to rename a file}}

#typing a command from windows it goes to ubentu then u will see the output
# first step to remote access a machine

# SSH Server APP
# OpenSSH

#states of the backgorund 

#systemctl enable ssh | disable | restart

#systemctl status ssh 

# -p 22 muhannad@192.168.100.236 {{to access using ssh with port 22}}

#winscp  for windows only {{it provides also a gui}}
#putty

#python3 location 
#whereis python3
#which python3
# what is sudo apt install python3-venev? {{to create a python environment}}

# python3 -m venv ./myvenv {{to run a module as a main script}}

# python3 -m venv ./.myvenv {{to run a module as a main script}}
# .myvenv is a hidden file
# shortcuts is called symlinks in linux

#pip freeze to check all the libraries and their versions
# u have to create a vertual python whenever u use a python

# echo "uvicorn " > requrements.txt

#source myvenv/bin/activate

# pip install -r requirements.txt {{to download all the packges}}

# deativate {{to go out from the venv}}

# pip install fastapi(all)

# api endpoint {{read about it}}

# what to do if there is a rebbot in the machine and u want to run it 24/7

#cronjob , systemctl 



# deactive {{to close the venv}}

# to copy any file from windows to linux
# we use scp 

#NGINX {{APPLICATION IS TO RUN ON PORT 80}}

# sudo apt install nginx {{server appliction by default it will be always enabled}}

#so basically it u can run http://192.168.100.245
# cd /var/www/html/
# 
#  su root {{it have all the priviliages}}

#sudo chown -R muhannad:muhannad html/ {{give ownership privilge to muhannad}}

#free bootstrap templets {{its free}}

#hosting a site 
# 1- rent a machine wiht ubentu 
# 2 - download nigx
# 3 - get a template
# 4 - copy the files conenets , into /var/www/html

#using a tool remote-ssh 
# ssh  (secure connection to remote shell)
#shell is terminal (ssh)

#AES-254(msg, key) {{encript the massage}}

#RSA ALGORITHM 

#public key cryptography {{RSA algorithm}}

#rebooting computing {{Read it , no jobs , no secure at all}}
#man in the middle attack {{read about it}}


#certificate is only public key 
# lets encript {read it }


#AWS lightsail {{to rend a machine}}
# when u regiester u will create instance 
#choose linux and ubentu 24.
# 2GB memory , 
# then name it 
# attach a static ip so that the ip addrs will not be changed
# we add also HTTPS PORT 443
# make sure its updated 
# u will get the private key by downloading it 
#first thing to do is to download nginx
#sudo apt install nginx
# to check its on 
#systemctl status nginx.service
#etc/nginx {{to disable like robots , and others}}
#linux administratation {"read about it "}
#copilot 3.7 thinking model is best for coding
#perplexity {{its like google, now pepople use this for search engine}}
#treafik and nginx are same
# we have to download this sudo apt install pyhton3-venv
#pydantic {{a library to define a class}}
#loadbalancer {{to disterbute loads , its a web server}}

