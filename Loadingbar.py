import sys
import time

def loading_bar(total=50, sleep_time=0.1):
    for i in range(total + 1):
        percent = (i / total) * 100
        bar = "#" * i + "-" * (total - i)
        sys.stdout.write(f"\r[{bar}] {percent:.2f}%")
        sys.stdout.flush()
        time.sleep(sleep_time)
    print("\nLoading complete!")

loading_bar()
