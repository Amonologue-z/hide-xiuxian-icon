import os
import time
import keyboard
def run_cmd(comm):
    a = os.popen(comm)
    print('1')

class key(object):
    def __init__(self):
        super(key, self).__init__()

    def test_a(self):
        print('a')
    def showicon(self):
        run_cmd(' hidetrayicon 1 show 运气修仙')
    def hideicon(self):
        run_cmd('hidetrayicon 1 hide 运气修仙')


    def testing(self):
        keyboard.add_hotkey('alt+w', self.hideicon)
        keyboard.add_hotkey('alt+e', self.showicon)
        keyboard.wait()


if __name__ == '__main__':
    key = key()
    key.testing()

