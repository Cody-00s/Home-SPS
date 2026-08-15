# Home-SPS
I'm building my own PLC using a Raspberry Pi Pico.

The idea came from the fact that I only have one power strip in my workshop that I can switch on and off. So I thought I'd 
build myself a PLC that controls, switches, and manages things for me. In version 1.0, the plan is to first set everything 
up and control a total of 10 relays with buttons. Anything beyond that will follow in later versions.

V1: 
Currently, the PLC can control one relay each with buttons 1 through 10. 

Button1 => relay1
Button2 => relay2
Button3 => relay3
Button4 => relay4
Button5 => relay5
Button6 => relay6 
Button7 => relay7
Button8 => relay8
Button9 => relay9
Button10 => relay10

Button 11 performs a function check — as long as it's held down, all relays turn on
Button 12 lets you turn off all relays if an error occurs

Warning: if this project is replicated, you should thoroughly research how alternating current works in your own country. I'm 
using voltage supplies designed for the Austrian grid. Also, not everything here is grounded, which makes the build a "build 
at your own risk" situation. Therefore, I take no responsibility for anyone replicating this on their own. However, if every 
precaution is taken the way I did it, I can assure you that everything works without issues! (e.g., covering certain 
components, grounding, installing circuit breakers, finding out what the best components are for your own AC grid, ...)
