import serial
import re
import time
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from threading import Timer

all_percentage = None
all_battery = None
  # 读取串口数据
ser = serial.Serial('/dev/cu.usbmodem207236A254527', 115200, timeout=0.1)
  # 向屏幕发送指令
ser.write(b'at+adb\r\n')
# 打开串口



def create_battery_icon(percentage, width=150, height=70, corner_radius=12,battery_level_rect_radius=8,head_corner_radius=5):
    # 创建一个透明背景的图像
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # 绘制电池外框（带有圆角）
    outline_rect = [(10, 12), (width-35, height-12)]
    draw.rounded_rectangle(outline_rect, outline=(80, 80, 80), width=3, radius=corner_radius)

    # 绘制电池头（带有圆角）
    head_width = 6
    head_height = 12
    head_x0 = width - 32
    head_y0 = (height - head_height) // 2
    head_rect = [head_x0, head_y0, head_x0 + head_width, head_y0 + head_height]
    draw.rounded_rectangle(head_rect, fill=(80, 80, 80), radius=head_corner_radius)

    # 绘制电池电量
    fill_width = int((93) * (percentage / 100))
    battery_level_rect = [(9 + battery_level_rect_radius, 11 + battery_level_rect_radius), (battery_level_rect_radius + 7 + fill_width, height - 11 - battery_level_rect_radius)]
    color = "black" if percentage > 20 else "red"
    draw.rounded_rectangle(battery_level_rect, fill=color, radius=battery_level_rect_radius)

    if all_battery > '0':
      lightning_color = (70,175,168)
      lightning_points = [
          (width // 2 - 5, height // 2 - 23),
          (width // 2 - 26, height // 2 + 4),

          (width // 2 - 13, height // 2 + 4),
          (width // 2 - 15, height // 2 + 23),
          (width // 2 + 7, height // 2 - 3),
          (width // 2 - 7, height // 2 - 3)
      ]
      draw.polygon(lightning_points, fill=lightning_color)

    return image

def save_battery_icon(image, path):
    image.save(path)


def task():


  data = ser.readline()
  if data:
  # 将byte数据转换为字符串
    data_str = data.decode('utf-8')
    # 使用正则表达式匹配电量信息
    match = re.search(r'\+BATCG=\d+,(?P<percentage>\d+),', data_str)
    power = re.search(r'\+BATCG=\d+,\d+,\d+,(?P<charge>.\d+),\d+,\d+', data_str)

    if match:
      # 获取电量百分比
      percentage = match.group('percentage')
      battery = power.group('charge')
      # print(f"当前电量：{percentage}%")
      global all_percentage
      global all_battery
      all_percentage = f"{percentage}%"
      all_battery = battery
    # 修改此处的电量参数来生成不同的电池图标
      battery_percentage = int(percentage)
      image = create_battery_icon(battery_percentage)
      save_path = "battery_icon.png"
      save_battery_icon(image, save_path)
      #print(f"Battery icon saved to {save_path}")




def func():
    task()
    # 定义一个定时器
    # 注意timer的语法
    # Timer(interval, function, args=None, kwargs=None)
    t = Timer(1, func)
    t.start()


func()
