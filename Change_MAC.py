#!/usr/bin/env python
import subprocess as sb

MAC_ADDRESS = input('Write MAC-ADRESS, (format 00:11:22:33:44:55): ')

sb.call('ifconfig')
