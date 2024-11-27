# Raspberry Pi GPIO switch to play audio
## What does it do?
This code will play an audio file (in `wav` format) when it detects a switch closes the connection between `ground` and `GPIO pin 2`. If the switch is held closed until the audio file finishes, it will restart. If the switch is opened during play, and then closed again, the audio file will start from the beginning.

## Setup
![pin diagram for rpi](images/pinout.png "From the rpi official website")

- Connect a 'normally open' switch between `Ground (pin 6)` and `GPIO 2 (pin 3)`.
- Log into your rpi and clone this repo.
- Copy your audio file (in `wav` format), to the same folder as the script `pi-switch.py`
- Rename the audio file to `audio.wav` (or edit the script to use your file name)
- Install the dependencies: `pip install -r requirements.txt`
- Run the script: `./pi-switch.py`

## My switch is normally closed (NC) not normally open (NO)!

If your switch's default state is normally closed, then you can modify this line:

```
        if button.is_pressed:
```

to read:

```
        if not button.is_pressed:
```

This should make it so that you get the audio starts when the switch is pressed.
