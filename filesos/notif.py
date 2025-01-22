import schedule 
import time 

def send_notification():
    print("This is your scheduled notification!")
# Schedule the notification every 10 seocnds 
schedule.every(10).seconds.do(send_notification)

print("Scheduler started. Press Ctrl+C to Stop.")
while True:
    schedule.run_pending()
    time.sleep(1)