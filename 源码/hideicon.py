import os
import time
import keyboard
import datetime

total_hide = 0
total_show = 0
info_time = 0
now = datetime.datetime.now()
date_now = now.strftime("%Y-%m-%d")
def run_cmd(comm):
    a = os.popen(comm)

run_cmd('md log')
print('欢迎使用由biu~开发的托盘隐藏程序~具体使用方法请看使用说明')

def create_file(file_name,msg):
    with open(file_name, "a") as biu:
        biu.write(msg)
        biu.close()

class key(object):

    def __init__(self):
        super(key, self).__init__()
            
    def help(self):
        global help_msg
    def showicon(self):
        global total_hide
        global total_show
        global info_time
        global date_now
        run_cmd(' hidetrayicon 1 show 运气修仙')
        total_show += 1
        info_time += 1
        now_time = time.asctime() 
        log_msg = f'{info_time}INFO {now_time}   已显示    已经累计为您显示托盘图标{total_show}次 \n'
        log_name= f'./log/log{date_now}.txt'
        create_file(log_name,log_msg)
        print(f'第{total_show}次显示 成功')
    def hideicon(self):
        global total_hide
        global total_show
        global info_time
        global date_now
        run_cmd('hidetrayicon 1 hide 运气修仙')
        total_hide += 1
        now_time = time.asctime()
        info_time += 1
        log_msg = f'{info_time}INFO {now_time}   已隐藏    已经累计为您隐藏托盘图标{total_hide}次 \n'
        log_name= f'./log/log{date_now}.txt'
        create_file(log_name,log_msg)
        print(f'第{total_hide}次隐藏 成功')
    def hiding(self):
        keyboard.add_hotkey('alt+w', self.hideicon)
        keyboard.add_hotkey('alt+e', self.showicon)
        keyboard.wait()


if __name__ == '__main__':
    key = key()
    key.hiding()

