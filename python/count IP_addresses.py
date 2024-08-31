'''
https://www.codewars.com/kata/526989a41034285187000de4

DESCRIPTION:
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them
(including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater
than the first one.

Examples:
* With input "10.0.0.0", "10.0.0.50"  => return   50 
* With input "10.0.0.0", "10.0.1.0"   => return  256 
* With input "20.0.0.10", "20.0.1.0"  => return  246
'''

def ips_between(start, end):
    start_parts = list(map(int, start.split('.')))
    end_parts = list(map(int, end.split('.')))
    
    return (end_parts[0] - start_parts[0]) * 256**3 + \
           (end_parts[1] - start_parts[1]) * 256**2 + \
           (end_parts[2] - start_parts[2]) * 256 + \
           (end_parts[3] - start_parts[3])

# Python has a library for everything, apparently.

from ipaddress import ip_address

def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))