# running locally

## create and enter python virtual enviroment

`python -m venv env`

`env/Scripts/activate.bat`

`pip install -r requirements.txt`

## start simulator

`python sim_code.py`

## exit virtual env

`deactivate`

# pico pin connections

| label | connection |
|-|-|
| VBUS | |
| VSYS | |
| GND | |
| 3V3_EN | |
| 3v3 | joystick and jewel power in |
| ADC_VREF | |
| GP28_A2 | joystick sw |
| AGND | |
| GP27_A1 | joystick vrx |
| GP26_A0 | joystick vry |
| RUN | |
| GP22 | |
| GND | joystick ground |
| GP21 | |
| GP20 | jewel data input |
| GP19 | |
| GP18 | |
| GND | |
| GP17 | |
| GP16 | |

![pico pinout diagram](https://microcontrollerslab.com/wp-content/uploads/2021/01/Raspberry-Pi-Pico-pinout-diagram.svg)
