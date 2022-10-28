# Action-Check

利用Github Action每天自动运行Auto-Check项目

# 下载安装deb包

https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo dpkg -i google-chrome-stable_current_amd64.deb

# 下载安装rpm包

https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm

yum localinstall google-chrome-stable_current_x86_64.rpm

# 查找对应版本号的Chromedriver

https://chromedriver.storage.googleapis.com/index.html

# Linux系统设置东八区时间

sudo timedatectl set-timezone Asia/Shanghai

# 修改Crontab时区

vim /etc/crontab

添加变量 CRON_TZ=Asia/Shanghai

# 打开计划任务文件

crontab -e

45 8 * * 1-5 python3 /home/ethan/schedule.py
