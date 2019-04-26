import machine
from network import WLAN
import time
## LED
import pycom
##

##bme280
from machine import I2C
import bme280
from bme280 import *
##

def setupLed():
    pycom.heartbeat(False)
    #pycom.rgbled(0x7f0000)
    pycom.rgbled(0x7f7f00) # led amarelo


def ListaWifi():
    wlan = WLAN(mode=WLAN.STA)
    nets = wlan.scan()
    for net in nets:
        print (net)

def conectaWifi():
    wlan = WLAN(mode=WLAN.STA)

    nets = wlan.scan()

    for net in nets:
        if net.ssid == 'NOME_DA_REDE':
            print('Rede encontrada')
            wlan.connect(ssid='NOME_DA_REDE', auth=(WLAN.WPA2, "SENHA"), timeout=5000)
            while not wlan.isconnected():
                pycom.rgbled(0x7f7f00)
                machine.idle()
            print('Conectado')
            pycom.rgbled(0x007f00) # led verde
            print (wlan.ifconfig())
            break

def testeBME280():
    i2c = I2C(0,I2C.MASTER)
    i2c.scan()
    sensor = bme280.BME280(i2c=i2c)

    while True:
        print('temperatura:',sensor.temperature,'ºC')
        print('humidade:',sensor.humidity,'%')
        print('pressão:',sensor.pressure/100,'hPa')
        time.sleep(5)
