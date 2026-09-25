# The Matlab files

just run the uitf_digital_twin.m script from Matlab and you can interact with it by interacting with port 8000 on the computer where Matlab runs. One way to do that is via "netcat". You can start it by "nc -C localhost 8000" if you are on the same computer. The option "-C" ensures that CR/LF end-of-line characters are used. 
