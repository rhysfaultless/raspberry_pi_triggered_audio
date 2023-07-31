#python3
#raspberry_pi_triggered_audio.py
#tested with a raspberry pi 3B+ with Raspberry Pi OS 64 bit 
#
#reminder: edit the file /etc/rc.local to run this program on startup


#imports
from gpiozero import Button
from time import sleep
from pygame import mixer

button = Button(2) #raspberry pi pin 2 as a GPIO input
time_to_wait = 10 #number of seconds to wait after audio runs

#audio setup
mixer.init()
mixer.music.load('/home/administrator/raspberry_pi_triggered_audio/software/media/audio_track.mp3')

while True:
	button.wait_for_press()
	mixer.music.play()
	while mixer.music.get_busy() == True:
    		continue
	sleep(time_to_wait)
