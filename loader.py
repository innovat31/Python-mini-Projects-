# this is a basic loader.

import sys
import time

def loading_animation():
    loading_symbols = ['|', '/', '-', '\\']  # These are the four symbols we will cycle through
    for _ in range(20):  # We will display the loader for 20 cycles (or as desired)
        for symbol in loading_symbols:
            sys.stdout.write(f'\rLoading... {symbol}')  # The `\r` makes it overwrite the previous line
            sys.stdout.flush()  # Make sure it writes to the screen immediately
            time.sleep(0.2)  # Adjust the speed of the animation by modifying the time delay

    sys.stdout.write('\rLoading... Done!      \n')  # Display "Done!" after the animation

# Call the function
loading_animation()
