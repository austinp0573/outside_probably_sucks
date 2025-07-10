import time
#function to print while waiting for next update
#show something in terminal
def stack_time(one: int, two: int):
    num = 1
    for i in range(1, (one + 1)):
        print()
        for j in range(1, (two + 1)):
            print(num, end=" ", flush=True)
            num += 1
            time.sleep(1)

if __name__ == "__main__":
    stack_time(50, 20)
