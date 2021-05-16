import smtplib
from email.message import EmailMessage
import amazon_price as amazon

#send email when price drops below $150, must have the title of the product, the current price and a link to buy the product
def send_email():
    buy_price = 1300

    receiver = "sbongiseni2@yahoo.com"
    sender = ['sbongiseni2@hotmail.com']
    password = ""

    # if amazon.gets_price() < buy_price:
    #     message = f"{amazon.gets_title()} is now {amazon.gets_price()}"
    #
    #     with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
    #         connection.starttls()
    #         result = connection.login(sender, password)
    #         connection.sendmail(
    #             result=result,
    #             from_addr=sender,
    #             to_addrs=receivers,
    #             msg=f"Subject:Amazon Price Alert!\n\n{message}\n{amazon.gets_link()}"
    #         )
    msg = EmailMessage()
    msg["Subject"] = "Testing"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Testing Email")

    server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
    server.login(sender, password)
    server.send_message(msg)
