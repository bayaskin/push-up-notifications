import os
import time


def send_push_up_notification():
    message = "Time to do push-ups! Do at least 15 push ups!"
    os.system(f"notify-send '{message}'")

if __name__ == "__main__":
    send_push_up_notification()

