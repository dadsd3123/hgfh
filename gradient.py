import random
import string

# 生成随机字符串
def generate_random_string(length=12):
    characters = string.ascii_letters + string.digits  # 包含大小写字母和数字
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# 获取用户输入的IP地址和生成数量
IPV4 = input("请输入服务器的外网IP：")
PROXY_COUNT = input("请输入需要生成的数量：")

# 生成所需数量的Docker命令
for i in range(int(PROXY_COUNT)):
    RANDOM_PASSWORD = generate_random_string()
    
    # 修改过的Docker命令，移除了代理设置
    DOCKER_COMMAND = (
        f'docker run -d -p {4440+i}:4444 -p {7900+i}:7900 --shm-size="2g" '
        f'-e SE_VNC_PASSWORD={RANDOM_PASSWORD} '
        f'selenium/standalone-chrome:latest'
    )
    
    # 生成VNC登录链接
    LOGIN_VNC = f'http://{IPV4}:{7900+i}?autoconnect=1&resize=scale&password={RANDOM_PASSWORD}'
    
    # 输出生成的命令和链接
    print(f'#{i+1}')
    print(DOCKER_COMMAND)
    print(LOGIN_VNC)
    print('\n')
