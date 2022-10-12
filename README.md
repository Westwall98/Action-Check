# Action-Check

利用Github Action每天自动运行Auto-Check项目

# Linux系统设置东八区时间

sudo timedatectl set-timezone Asia/Shanghai

# 修改Crontab时区

vim /etc/crontab

添加变量 CRON_TZ=Asia/Shanghai

# 打开计划任务文件

crontab -e

45 8 * * 1-5 python3 /home/ethan/schedule.py > /dev/null 2>&1
