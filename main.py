import whois, smtplib, time
from configparser import ConfigParser
from email.message import EmailMessage

def main():
    infinite = True
    config = ConfigParser()
    config.read("config.ini")
    timer = int(config["settings"]["timer"])
    gmail_user = config["account"]["gmail_user"]
    gmail_app_password = config["account"]["app_password"]
    
    if gmail_user != "your_gmail_user@example.com" and gmail_app_password != "your_google_app_password":
        while infinite:
            print("Checking domains...")
            msg = EmailMessage() 
            msg['From'] = gmail_user
            msg["To"] = gmail_user
            msg["Subject"] = "EXPIRED DOMAINS"

            with open("domains.txt", 'r') as file:
                domains = [stripped for line in file if (stripped := line.strip())]

            msg_content = ( "https://domains.google/ \n"
                            "Expired domains:\n\n"
                            )
            expired_domains = []
            for domain in domains:
                try:
                    whois.whois(domain)
                except:
                    expired_domains.append(domain)
                    msg_content = msg_content + f"- {domain}\n"
            if expired_domains:
                msg.set_content(msg_content)
                try:
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.ehlo()
                    server.login(gmail_user, gmail_app_password)
                    server.send_message(msg)
                    server.close()
                    print(expired_domains)
                    print('Email sent!')
                except Exception as exception:
                    print(f"Error: {exception}!\n\n")
            print(f"Done. {len(expired_domains)} domains expired.\n")
            time.sleep(timer)

    else:
        print("Insert gmail_user and app_password in config.ini")


if __name__ == "__main__":
    main()