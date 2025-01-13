import sys
sys.path.pop(0)
from setuptools import setup

setup(
    name="ebyte-lora-e220-opi",
    package_dir={'': 'src'},
    py_modules=["lora_e220", "lora_e220_constants", "lora_e220_operation_constant"],
    version="0.0.2",
    description="LoRa EBYTE E220 device library complete and tested with Arduino, esp8266, esp32, STM32 and Raspberry Pi Pico. LLCC68, Orange Pi PC Plus",
    long_description="Ebyte E220 LoRa (Long Range) library device very cheap and very long range (from 5Km to 10Km). Arduino LoRa EBYTE E220 device library complete and tested with Arduino, esp8266, esp32, STM32 and Raspberry Pi Pico. LLCC68,Orange Pi PC Plus",
    keywords="LoRa, UART, EByte, esp32, esp8266, stm32, SAMD, Arduino, Raspberry Pi Pico, Raspberry Pi, ,Orange Pi PC Plus",
    url="https://github.com/kervendurdy/EByte_LoRa_E220_python_orangepi_library",
    author="Kervendurdy Allaberdiyev",
    author_email="kervendurdy@gmail.com",
    maintainer="Kervendurdy Allaberdiyev",
    maintainer_email="kervendury@gmail.com",
    license="MIT",
    install_requires=[],
    project_urls={
        'Documentation': 'https://github.com/kervendurdy/EByte_LoRa_E220_python_orangepi_library/blob/master/README.md',

    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: Implementation :: Orange Pi",
        "License :: OSI Approved :: MIT License",
    ],
)