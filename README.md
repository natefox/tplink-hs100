# tplink-hs100

I wanted to figure out how to turn on or off my TP-Link HS100 Smart Plug. There doesnt seem to be any public API so I ran tcpdump on my tomato router while watching the commands sent from my phone to the device.

I have no idea if this will work with any others - I only have one of these devices. If this works (or doesnt work) for you, please create an issue and just let me know!

You'll probably need to change the `IPADDR` constant in the scripts but I dont think the port needs to change.
