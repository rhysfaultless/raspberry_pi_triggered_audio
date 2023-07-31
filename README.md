# raspberry_pi_triggered_audio

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
