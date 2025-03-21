import threading
import rumps
import time
from datetime import datetime
from threading import Timer
import subprocess


all_percentage = None
all_battery = None



def script1_function():
    print(subprocess.call('kext/kext-load', shell=True))
    global all_percentage
    global all_battery
    class AwesomeStatusBarApp(rumps.App):
        def __init__(self):
            super(AwesomeStatusBarApp, self).__init__("Awesome App", icon='battery_icon.png', title=f"{all_percentage}")


            self.update_timer = rumps.Timer(self.update_battery_icon, 1)  # 每隔 1 秒更新一次
            self.update_timer.start()
            self.icon_index = 0
            self.icons = ['battery_icon.png']  # 假设有多个图标文件

            self.update_timer = rumps.Timer(self.update_battery_title, 1)  # 每隔 1 秒更新一次
            self.update_timer.start()
            self.title_index = 0
            self.titles = f"{all_percentage}"  # 假设有多个图标文件


        def update_battery_icon(self, sender):
            self.icon = self.icons[self.icon_index]
        def update_battery_title(self, sender):
            self.title = f"{all_percentage}"



        @rumps.clicked("加载驱动")
        def sayhi(self, _):
            print(subprocess.call('kext/kext-load', shell=True))
            if subprocess.call:
                rumps.alert("驱动加载成功!")
        
        @rumps.clicked("重启TNTgo Boom")
        def sayhi(self, _):
            print(subprocess.call('kext/reast', shell=True))




    if __name__ == '__main__':
        AwesomeStatusBarApp().run()
    battery_percentage = script2_function()



def task():
    import serialread
    global all_percentage
    global all_battery
    percentage = serialread.all_percentage
    battery = serialread.all_battery
    all_percentage = percentage
    all_battery = battery

def func():
    task()
    # 定义一个定时器
    # 注意timer的语法
    # Timer(interval, function, args=None, kwargs=None)
    t = Timer(3, func)
    t.start()

def script2_function():
    func()

if __name__ == "__main__":
    # 创建并启动后台线程
    t2 = threading.Thread(target=script2_function)
    t2.start()

    # 在主线程中运行UI相关的代码
    script1_function()

    # 等待后台线程结束（可选）
    t2.join()
