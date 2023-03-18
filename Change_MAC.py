#!/usr/bin/env python
"""Script on Linux
You must run the command with root rights"""

import subprocess as sb

MAC_ADDRESS = input('Write MAC-ADRESS, (format 00:11:22:33:44:55): ')

sb.call('ifconfig eth0 down', shell=True)
sb.call(f'ifconfig eth0 hw ether {MAC_ADDRESS}', shell=True)
sb.call(f'ifconfig eth0 up', shell=True)
print('Success!')
