# Author: Renzo Mischianti
# Website: www.mischianti.org
#
# Description:
# This script demonstrates how to use the E220 LoRa module with Orange Pi.
# Sending dictionary
#
# Note: This code was written and tested using Orange Pi on an ESP32 board.
#       It works with other boards, but you may need to change the UART pins.

import serial

from lora_e220 import LoRaE220, Configuration
from lora_e220_constants import RssiAmbientNoiseEnable, RssiEnableByte
from lora_e220_operation_constant import ResponseStatusCode

# Initialize the LoRaE220 module
loraSerial = serial.Serial('/dev/ttyS3') #(, baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

lora = LoRaE220('900T22D', loraSerial, aux_pin='PA7', m0_pin='PA8', m1_pin='PA9')
code = lora.begin()
print(f"Initialization: {ResponseStatusCode.get_description(code)}")

# Set the configuration to default values and print the updated configuration to the console
# Not needed if already configured
configuration_to_set = Configuration('900T22D')
# To enable RSSI, you must also enable RSSI on receiver
configuration_to_set.TRANSMISSION_MODE.enableRSSI = RssiEnableByte.RSSI_ENABLED
code, confSetted = lora.set_configuration(configuration_to_set)
print(f"Set configuration: {ResponseStatusCode.get_description(code)}")

# Send a dictionary message (transparent)
data = {'key1': 'value1', 'key2': 'value2'}
code = lora.send_transparent_dict(data)
print(f"Send message: {ResponseStatusCode.get_description(code)}")
