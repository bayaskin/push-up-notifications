import time
import sys
import plyer


def send_notification():
    plyer.notification.notify(
            title = "Time for a Push-ups",
            message = "Do at least 15 push ups!!!",
            app_name = "Push-up Reminder",
            timeout = 10
            )

if __name__ == '__main__':
    while True:
        send_notification()
        time.sleep(3600)


