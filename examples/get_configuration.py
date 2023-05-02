# Author: Renzo Mischianti
# Website: www.mischianti.org
#
# Description:
# This script initializes the E220 LoRa module with Raspberry Pi,
# retrieves the current configuration, and prints it to the console.
# The code demonstrates how to use the LoRaE32 library to interact with the module and read its configuration.
#
# Note: This code was written and tested using Raspberry Pi on an ESP32 board.
#       It works with other boards, but you may need to change the UART pins.


import serial

from lora_e220 import LoRaE220, print_configuration
from lora_e220_operation_constant import ResponseStatusCode

loraSerial = serial.Serial('/dev/serial0') #, baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

lora = LoRaE220('400T22D', loraSerial, aux_pin=18, m0_pin=23, m1_pin=24)

code = lora.begin()
print("Initialization: {}", ResponseStatusCode.get_description(code))

code, configuration = lora.get_configuration()

print("Retrieve configuration: {}", ResponseStatusCode.get_description(code))

print_configuration(configuration)

#
# Initialization: {} Success
# Retrieve configuration: {} Success
# ----------------------------------------
# HEAD :  0xc1   0x0   0x8
#
# AddH :  0x0
# AddL :  0x0
#
# Chan :  23  ->  433
#
# SpeedParityBit :  0b0  ->  8N1 (Default)
# SpeedUARTDatte :  0b11  ->  9600bps (default)
# SpeedAirDataRate :  0b10  ->  2.4kbps (default)
#
# OptionSubPacketSett:  0b0  ->  200bytes (default)
# OptionTranPower :  0b0  ->  22dBm (Default)
# OptionRSSIAmbientNo:  0b0  ->  Disabled (default)
#
# TransModeWORPeriod :  0b11  ->  2000ms (default)
# TransModeEnableLBT :  0b0  ->  Disabled (default)
# TransModeEnableRSSI:  0b0  ->  Disabled (default)
# TransModeFixedTrans:  0b0  ->  Transparent transmission (default)
# ----------------------------------------
