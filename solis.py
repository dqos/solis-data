import minimalmodbus
import serial
import time
import requests

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout  = 3

try:
        Realtime_ACW = instrument.read_long(3004, functioncode=4, signed=False) #Read AC Watts as Unsigned 32-Bit
        print("AC Watts: " + str(Realtime_ACW) + " W")
        Realtime_DCU = instrument.read_register(3021, number_of_decimals=0, functioncode=4, signed=False) #Read DC volts as Unsigned 16-Bit
        print("DC Volt: " + str(Realtime_DCU/10.0) + " V")
        Realtime_DCI = instrument.read_register(3022, number_of_decimals=0, functioncode=4, signed=False) #Read DC current as Unsigned 16-Bit
        print("DC Current: " + str(Realtime_DCI/10.0) + " A")
        Realtime_ACU = instrument.read_register(3035, number_of_decimals=0, functioncode=4, signed=False) #Read AC volts as Unsigned 16-Bit
        print("AC volt: " + str(Realtime_ACU/10.0) + " V")
        Realtime_ACI = instrument.read_register(3038, number_of_decimals=0, functioncode=4, signed=False) #Read AC current as Unsigned 16-Bit
        print("AC Current: " + str(Realtime_ACI/10.0) + " A")
        Realtime_ACF = instrument.read_register(3042, number_of_decimals=0, functioncode=4, signed=False) #Read AC frequency as Unsigned 16-Bit
        print("AC Frequency: " + str(Realtime_ACF/100.0) + " Hz")
        Inverter_C = instrument.read_register(3041, number_of_decimals=0, functioncode=4, signed=True) #Read inverter temperature as Signed 16-Bit
        print("Inverter temperature: " + str(Inverter_C/10.0) + " C")
        AlltimeEnergy_KWH = instrument.read_long(3008, functioncode=4, signed=False) #Read all time energy (kWh total) as Unsigned 32-Bit
        print("Generated all time: " + str(AlltimeEnergy_KWH) + " kWh")
        Today_KWH = instrument.read_register(3014, number_of_decimals=1, functioncode=4, signed=False) #Read todays energy (kWh total) as 16-Bit
        print("Generated today: " + str(Today_KWH) + " kWh")

        payload = {
                'acw': str(Realtime_ACW),
                'dcv': str(Realtime_DCU/10.0),
                'dci': str(Realtime_DCI/10.0),
                'acv': str(Realtime_ACU/10.0),
                'aci': str(Realtime_ACI/10.0),
                'acf': str(Realtime_ACF/100.0),
                'temp': Inverter_C/10,
                'alltime': str(AlltimeEnergy_KWH),
                'today': str(Today_KWH)
        }
        r = requests.post("https://webserver/solis/post.php", data=payload)
        print(r.text)

except Exception, e:
        print(str(e));