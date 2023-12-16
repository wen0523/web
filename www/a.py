import subprocess,time

# 启动第一个脚本
process1 = subprocess.Popen(['python', 'app.py'],cwd='D:\Web_Python\wesome-python3-webapp\www')

# 启动第二个脚本
process2 = subprocess.Popen(['python', 'create_app.py'],cwd='D:\Web_Python\wesome-python3-webapp\www')

# 等待两个脚本执行完成
process1.wait()
process2.wait()
