import time
import board
import digitalio
import analogio
import neopixel

# board led
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# joystick
stick_x = analogio.AnalogIn(board.A1)
stick_y = analogio.AnalogIn(board.A0)
switch = digitalio.DigitalInOut(board.GP28)
switch.direction = digitalio.Direction.INPUT
click_state = False
click_counter = 0

# neopixel jewel 7
pixel_pin = board.GP20
num_pixels = 7
pixels = neopixel.NeoPixel(
	pixel_pin,
	num_pixels,
	pixel_order=(1, 0, 2, 3) # RGBW
)

n = 0
m = 0
o = 0
max_brightness = 3

while True:
	n += 1
	if n > max_brightness:
		n = 0
		m += 1
	if m > num_pixels - 1:
		m = 0
		o += 1
	if o > 3:
		o = 0
	color = [0, 0, 0, 0]
	color[o] = n
	pixels[m] = tuple(color)
	#print(m, color)
	time.sleep(0.01)

while True:
	# click joystick
	if switch.value == False and click_state == False:
		click_state = True
		click_counter += 1
		led.value = not led.value
		print("click!", click_counter)
	# release click joystick
	elif switch.value == True and click_state == True:
		click_state = False

	x = stick_x.value
	y = stick_y.value
	# prints values between 0 and 65535
	# neutral position is 32757
	#print("x", x, "y", y)
