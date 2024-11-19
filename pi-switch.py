import pygame
import RPi.GPIO as GPIO
import sys

pygame.mixer.music.load('audio.mp3')

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

switch_open_event = pygame.USEREVENT + 1
switch_closed_event = pygame.USEREVENT + 2


def switch_open_callback(channel):
    pygame.event.post(switch_open_event)


def switch_closed_callback(channel):
    pygame.event.post(switch_closed_event)


# Setup event on pin 10 falling edge
GPIO.add_event_detect(10, GPIO.FALLING, callback=switch_open_callback)

# Setup event on pin 10 rising edge
GPIO.add_event_detect(10, GPIO.RISING, callback=switch_closed_callback)

pygame.init()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GPIO.cleanup()  # Clean up
            sys.exit()
        elif event.type == switch_open_event:
            print("Starting audio")
            pygame.mixer.music.play()
        elif event.type == switch_closed_event:
            print("Stopping audio")
            pygame.mixer.music.stop()
