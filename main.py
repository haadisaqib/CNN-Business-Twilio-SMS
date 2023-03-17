import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import time

# Your Twilio account SID and AUTH Token
account_sid = "enter account_sid"
auth_token = "enter auth_token"
client = Client(account_sid, auth_token)

while True:
    # Get the current time
    current_time = time.localtime()

    # Only send the message if it's 6:00 AM
    if current_time.tm_hour == 6 and current_time.tm_min == 00:
        # Send the SMS message
        try:
            # Scrape the latest world news headlines from CNN's website
            page = requests.get("https://www.cnn.com/business")
            soup = BeautifulSoup(page.content, "html.parser")
            headlines = soup.find_all("div", class_="container__headline container_lead-plus-headlines__headline")
            headlines = [headline.text.strip() for headline in headlines]
            print(headlines)

            # Format the message
            message_body = "Latest World News Headlines from CNN:\n\n" + "\n\n".join(headlines[:14]) + "..."

            # Send the message
            message1 = client.messages.create(
                to="enter your number",
                from_="enter twilio number",
                body=message_body
            )

            print("SMS sent successfully!")
        except:
            print("An error occurred while sending the SMS.")

    # Wait for 1 minute before checking the time again
    time.sleep(60)
