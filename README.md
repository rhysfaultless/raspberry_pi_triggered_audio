# raspberry_pi_triggered_audio

## hardware components

1.  [Raspberry Pi 3 B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/) and micro SD card
2.  [SICK WTT2SL-2P1192](https://www.sick.com/us/en/photoelectric-sensors/photoelectric-sensors/powerprox/wtt2sl-2p1192/p/p532248?ff_data=JmZmX2lkPXA1MzIyNDgmZmZfbWFzdGVySWQ9cDUzMjI0OCZmZl90aXRsZT1XVFQyU0wtMlAxMTkyJmZmX3F1ZXJ5PVdUVDJTTC0yUDExOTImZmZfcG9zPTEmZmZfb3JpZ1Bvcz0xJmZmX3BhZ2U9MSZmZl9wYWdlU2l6ZT0yNCZmZl9vcmlnUGFnZVNpemU9MjQmZmZfc2ltaT05Mi4w)
3.  Resistor 1000 Ω 
4.  Resistor 100 Ω
5.  24 V power supply
6.  5 V power supply with micro-usb termination, for powering the Raspberry Pi
7.  3.5 mm audio jack, audio amplifier, and speaker
8.  Terminal blocks, connectors, solder, or other method for making the connections detailed in the wiring diagram

## software setup

1.  Use [Raspberry Pi Imager](https://www.raspberrypi.com/software/) to seup a micro SD card.
    I used the 64 bit Desktop version of Raspberry Pi OS, but the Lite / Server variant should also work.
2.  Insert the micro SD card into the Raspberry Pi 3B+
3.  Connect a monitor, keyboard and mouse.
4.  Turn the Raspberry Pi on.
5.  During the setup, set the username as `administrator`.
6.  Optional, to simplify maintenance / development:
    - Allow SSH
    - Change the hostname to something unique
    - Setup Wi-Fi
7.  In a terminal, navigate to the folder `/home/administrator`, and then clone this repository:
    ```
    https://github.com/rhysfaultless/raspberry_pi_triggered_audio.git
    ```
8.  In a terminal, enter:
    ```
    sudo nano /etc/rc.local
    ```

    Add this line near the end of the file, before the exit statement:

    ```
    sudo -H -u administrator /usr/bin/python /home/administrator/raspberry_pi_triggered_audio/raspberry_pi_triggered_audio.py &
    ```

    This will run the program `raspberry_pi_triggered_audio.py` when the Raspberry Pi boots.
    You can refer to the file `example_rclocal.txt` for how `/etc/rc.local` should be configured.
