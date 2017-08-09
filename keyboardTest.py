import keyboard

def print_pressed_keys(e):
	line = ', '.join(str(code) for code in keyboard._pressed_events)
	print('\r'+line+''*40, end='')

keyboard.hook(print_pressed_keys)
keyboard.wait()