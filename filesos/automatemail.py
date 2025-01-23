# can put this in Cv 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# 587 __> code for gmail n
# nvof bers oduz kdqd


# Email credentials
sender_email = "anjalisimkhada5@gmail.com"
receiver_email =   " akhanda1477@gmail.com" #"aachalsimkhada193@gmail.com" # "athma2377@gmail.com",
password = "nvof bers oduz kdqd" # Use app Password, NOT your Gmail passwords app testing 

# Create the email 
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email"

# Email Body 
body = "Hello, this is an automatic email that i made from python"
message.attach(MIMEText(body, "plain"))

# Send the email 
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!!!!")
except Exception as e:
    print(f"Error: {e}")
