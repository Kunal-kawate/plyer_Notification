
import time 
from plyer import notification 
 
if __name__=="__main__":
        while True:
            notification.notify(
                title = "KunyaThing", # write here your notification title
                message="Ha mai wahi hu jo fokat ka gyan pel raha hai." , # write here notification message
                app_icon="C:/Users/Kunal/Desktop/instagram.ico", #here is the notification icon , use here only ico files 
                # displaying time
                timeout=5
                )
            # waiting time
            time.sleep(20)
