import time  # 导入time模块，提供与时间相关的函数
import datetime  # 导入datetime模块，提供日期和时间处理的功能


def wait_time():
    """
    计算当前时间距离当天目标时间（09:03:50）的时间差，以秒为单位返回。
    如果当前时间晚于目标时间，返回None。
    """
    # 获取当前时间，精确到秒
    current_time = datetime.datetime.now()

    # 打印当前的Unix时间戳（自1970年1月1日以来的秒数）
    print(time.time())

    # 定义当天的目标时间为09:03:50
    target_time = datetime.datetime(
        current_time.year, current_time.month, current_time.day, 19, 22, 59)

    # 如果当前时间在目标时间之前，计算时间差
    if current_time < target_time:
        # 计算目标时间与当前时间的时间差
        time_difference = target_time - current_time

        # 将时间差转换为总秒数
        seconds_to_wait = time_difference.total_seconds()

        # 返回距离目标时间的秒数
        return seconds_to_wait
    else:
        return 0


# 打印提示信息，表示程序等待主体程序运行
print("距离主体程序运行还有：")

# 使用while循环，持续检查距离目标时间的秒数，并逐秒倒计时
while wait_time() > 0:
    # 获取当前距离目标时间的秒数
    seconds_to_wait = wait_time()

    # 计算每次调用wait_time前后的误差
    print(f"误差={seconds_to_wait - wait_time()}")

    # 计算剩余的小时数（整除3600，得到总小时数）
    hours = seconds_to_wait // 3600

    # 计算剩余的分钟数（将秒数除以3600取余后，再整除60得到总分钟数）
    minutes = (seconds_to_wait % 3600) // 60

    # 计算剩余的秒数（将秒数除以60取余得到剩余秒数）
    seconds = seconds_to_wait % 60

    # 打印当前距离目标时间的倒计时，格式为小时、分钟、秒
    print(f"{int(hours)}小时 {int(minutes)}分钟 {seconds}秒")

    # 打印剩余的总秒数
    print(f"{seconds_to_wait}秒\n")

    # 如果剩余时间大于等于1秒
    if seconds_to_wait >= 1:
        # 程序休眠1秒，模拟倒计时
        time.sleep(1)

        # 减少等待时间1秒，确保倒计时顺利进行
        # seconds_to_wait -= 1
    else:
        # 如果剩余时间小于1秒，程序休眠剩余的秒数，然后跳出循环
        time.sleep(seconds_to_wait)
        break

# 当循环结束时，表示距离目标时间已经过去，开始运行主体程序
print("主体程序开始运行")
a = 1
