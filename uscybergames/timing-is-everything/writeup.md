# [FOR] Timing is Everything
When viewing the pcap file in wireshark, the timing is noticably exact.
If we measure the miliseconds between each request, we can convert them to ascii values to get the flag
To do this, I exported the packets to json then used a python script
File > Export Packet Dissections > Export as JSON
