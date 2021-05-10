import time
wake_time= input("Enter the time to wake up (HH-MM-SS) :")
while True:
    now = time.strftime("%H-%M-%S")
    if now == wake_time:
        print("\nIt's time to wake up!!!!")
        break
    time.sleep(1)

