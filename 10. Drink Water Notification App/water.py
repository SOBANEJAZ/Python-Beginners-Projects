import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water",
            message = "Drinking water helps better to work and refreshes us",
            app_icon = "D:/My Github repositories/Python-Projects-Collection/10. Drink Water Notification App/water.ico",
            timeout = 10
        )      
        time.sleep(60*60)
