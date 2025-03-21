# TNTgo-Boom

一款为 **TNTgo 在 macOS 上使用** 而编写的软件。  

⚠ **注意：本程序仅在 Intel 芯片的 Mac 设备上测试正常，Apple Silicon 设备请自行测试。**  

## ✨ 功能介绍
TNTgo-Boom 提供以下两个主要功能：
1. **安装驱动**：在 macOS 上驱动TNTgo的大部分外设，包括：
   - **显示**、**触摸**、**触控板**、**键盘**、**摄像头**
2. **状态栏电量显示**：在 macOS 状态栏显示 TNTgo 的 **电量** 及 **充电状态**

---

## 🚀 使用方法
- **静默启动**：  
  - 运行后，**仅在顶部状态栏显示电量图标**，点击图标可查看电量及充电状态。  
  - 可将其添加到 **登录项**，实现 **开机自启**。  
- **安装驱动**：  
  目前由于程序内无法输入密码运行sudo命令，所以请下载release中的kextload.zip来配合安装驱动
  
  **开始前需要先关闭SIP，请自行百度如何关闭SIP**
     1. 将文件解压后的kextload文件夹放在用户文稿（Documents）文件夹中  （请严格安装要求放置，不要修改路径和文件名）
     2. 打开文件夹，右键用文稿编辑app编辑kext-load文件，按照文件内提示修改为你自己的电脑密码
     3. 双击运行一次文件夹内的kext-load，看看是否会显示进程已完成。（如果要输入密码就是第二步修改错了） 
     4. 第一次可能需要前往 **系统设置 → 隐私与安全性**，允许 **加载内核扩展**。 安装要求重启后即可
        
- **开机自启动**：
  
   **强烈建议为TNTgo Boom添加开机自启，否则每次重启后都需要手动运行kext-load来安装驱动**
  - 在**系统设置 → 登录项**中添加TNTgo Boom.app
  - 添加启动项后，每次开机都会自动加载驱动，如果有时候TNTgo的外设不能用，请插拔接口重新连接一下TNTgo，让驱动生效

---

## 🛠 TNTgo 在 macOS 的使用建议
1. **连接线选择**：建议使用 **原装短线**，部分第三方线可能无法正常连接 Mac。  
2. **音量调节**：若无法调节音量，推荐使用 **[SoundSource](https://rogueamoeba.com/soundsource/)**。  
3. **屏幕分辨率**：推荐使用 **[BetterDisplay](https://github.com/waydabber/BetterDisplay)**，支持：
   - **调整分辨率**
   - **开启 HiDPI（防止画面模糊）**  
4. **亮度调节**：亮度也可以使用BetterDisplay调节，但是这种软件调节相当于添加灰色蒙版。硬件调节只能使用键盘，目前我还没有解决方法。  

---

## 🔧 功能实现方式
TNTgo-Boom 采用 **Python** 编写，功能实现方法如下：
- **电量读取**：通过 **串口通信** 读取电池电量及充电状态。  
- **驱动支持**：
  - 参考 **黑苹果 VoodooI2C 驱动** 方案（VoodooI2C 可驱动 Surface 设备的触摸板 & 键盘）。  
  - 在 macOS（白苹果）上，**VoodooI2C 可作为内核扩展使用**，从而驱动 **TNTgo 外设**。  

---
目前部分功能可能仍有优化空间，但整体已基本可用。如果有问题可以反馈，但非致命性问题大概率不会再更新

不过如果想优化这个项目的话，也欢迎Pull Request

---

