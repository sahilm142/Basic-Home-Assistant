# Basic-Home-Assistant
----------------------------------------------------------------------------------- A Basic Home Assistant --------------------------------------------------------------------------------------------------------------------------------------
To get started-


1)Download the grove_rgb_lcd library at https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight/archive/master.zip.

2)Connect SDA to pin3, scl to pin5, vcc to pin2 and gnd to pin6 of raspberry pi

3)Download the bluetooth library using the following steps

sudo apt-get install bluetooth blueman bluez
sudo apt-get install python-bluetooth
sudo apt-get install python-rpi.gpio

4)Pair your androidphone with raspberry pi with bluetooth using the following steps

sudo bluetoothctl
[bluetooth]# power on
[bluetooth]# agent on
[bluetooth]# discoverable on
[bluetooth]# pairable on
[bluetooth]# scan on
pair <address of your phone>

5)-Install pyown library using this step

pip install pyowm

6)-Install gTTS library using following step

pip install gTTS

7)-Install wikipedia library using following step

 pip install wikipedia

8)- Install feedparser (Parse Atom and RSS feed)

can be install by using distutils or setup tools by running
$python setup.py install

 
9)-Install Blue Term App in the phone

10)-Insert the speaker/headphones pin in the 3.5 mm Audio and Composite Output jack for audio output

11)-Run the program, connect the phone through the app.

12)-Open Voice Keyboard on your phone and speak your commands

13)-What you can do-

  a)-Ask weather condition

  b)-News

  c)-Wiki-Search  

  d)-Play a song

All the outputs will be displayed on the lcd and have respective audio outputs.
