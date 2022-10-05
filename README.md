# Action-Check

利用Github Action每天自动运行Auto-Check项目

设置东八区时间

timedatectl set-timezone Asia/Shanghai

crontab -e打开计划任务文件

45 8 * * 1-5 python /root/tmp/schedule.py
