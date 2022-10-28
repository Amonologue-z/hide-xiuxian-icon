import os
import time
import keyboard
def run_cmd(comm):
    a = os.popen(comm)

class key(object):
    def __init__(self):
        super(key, self).__init__()
    def showicon(self):
        run_cmd(' hidetrayicon 1 show 运气修仙')
        print('已显示')
    def hideicon(self):
        run_cmd('hidetrayicon 1 hide 运气修仙')
        print('已隐藏')


    def testing(self):
        keyboard.add_hotkey('alt+w', self.hideicon)
        keyboard.add_hotkey('alt+e', self.showicon)
        keyboard.wait()


if __name__ == '__main__':
    key = key()
    key.testing()

