#!/usr/bin/python
from gpiozero import Button
import simpleaudio as sa
import sys
import time

button = Button(2)

wave_obj = sa.WaveObject.from_wave_file("audio.wav")
play_obj = wave_obj.play()
play_obj.stop()

reset_stream = False
while 1:
    try:
        if button.is_pressed:
            if not play_obj.is_playing():
                play_obj = wave_obj.play()
        else:
            if play_obj.is_playing():
                play_obj.stop()
        time.sleep(0.1)
    except KeyboardInterrupt:
        play_obj.stop()
        sys.exit()
