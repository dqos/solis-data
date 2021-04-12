# Solis Data
Gather data from a Solis inverter and push to web server. 

### Requirements
- Any Raspberry Pi with USB working;
- Raspbian 10 or higher;
- USB to RS485 Converter;
- Python 2.7.16-1 or higher;
- Solis inverter with COM port.

### Installation
```
sudo apt-get install python python-pip 
sudo python -m pip install pyserial
sudo pip install minimalmodbus
```
Then place solis.py anywhere you want, create a cron like: `*/5 * * * * python /root/solis.py`

### Hardware
Note that the COM input of Solis is proprietary, so I used some hacking to connect it, see the photos below.

### Photos
![complete.jpg](https://raw.githubusercontent.com/dqos/solis-data/main/photos/complete.jpg)

![connector.jpg](https://raw.githubusercontent.com/dqos/solis-data/main/photos/connector.jpg)

![specs.jpg](https://raw.githubusercontent.com/dqos/solis-data/main/photos/specs.jpg)

### License
MIT License

### Credits
Code is based on the work of others on these websites:
https://gathering.tweakers.net/forum/list_messages/1900048
https://alphyraz.tweakblogs.net/blog/17760/solis-omvormer-uitlezen-met-een-raspberry-pi