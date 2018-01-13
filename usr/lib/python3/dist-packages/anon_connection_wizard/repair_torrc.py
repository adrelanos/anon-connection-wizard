#!/usr/bin/python3 -u

import fileinput, os, shutil


'''repair_torrc() function will be called when we want to gurantee the existence of:
1. /etc/tor/torrc file
2. /etc/tor/torrc.anondist file
3. /etc/tor/torrc is exactly the same with /etc/tor/torrc.anondist
'''
def repair_torrc():
    repair_torrc_d()
    repair_torrc_anondist()
    shutil.copyfile('/etc/tor/torrc.anondist', '/etc/tor/torrc')

'''
repair_torrc_d() will gurantee the existence of /etc/torrc.d
'''
def repair_torrc_d():
    if not os.path.exists('/etc/torrc.d/'):
        os.makedirs('/etc/torrc.d/')

'''
repair_torrc_anondist() will gurantee the existence of /etc/tor/torrc.anondist
However, maintainer need to manually update its content when
any changes is made to  /etc/tor/torrc.anondist
''' 
def repair_torrc_anondist():
    if not os.path.exists('/etc/tor/torrc.anondist'):
        with open('/etc/tor/torrc.anondist', "w") as f:
            f.write("\
            ## Do not edit this file!\n\
            ## Add modifications to the following file instead:\n\
            ## /usr/local/etc/torrc.d/50_user.torrc\n\
            \n\
            %include /etc/torrc.d\n")

