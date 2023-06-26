import time

def concentration_timer(duration):
    print("专注开始！")
    time.sleep(duration)
    print("专注结束！")

if __name__ == "__main__":
    duration = int(input("请输入专注时长（分钟）："))
    concentration_timer(duration * 60)
