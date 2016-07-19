# tplink-hs100

I wanted to figure out how to turn on or off my TP-Link HS100 Smart Plug. There doesnt seem to be any public API so I ran tcpdump on my tomato router while watching the commands sent from my phone to the device.

You'll probably need to change the `IPADDR` constant in the scripts but I dont think the port needs to change.


### How I got the data
This might be useful to others, but if nothing else its my own notes of how to replicate my data:

1. SSH into the tomato router
1. Install the package manager ipkg from these directions: http://tomatousb.org/tut:optware-installation
1. Install tcpdump `ipkg install tcpdump`
1. Start capturing: `/opt/sbin/tcpdump -w /mnt/sdb1/lighton-to-off-v2.tcpdump host 192.168.1.150`
1. Copy file from /mnt/sdb1/*.tcpdump to my machine
1. Use wireshark to open *.tcpdump files.
1. Optional: use this filter on wireshark: `tcp.flags.push == 1` to grab just the tcp packets. This might not be good if you want to inpsect the UDP broadcast packets.