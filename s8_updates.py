#!/usr/bin/env python3

import requests
import smtplib
import datetime
import config


resp    = requests.get(config.url)
content = resp.content.decode('utf-8')


def get_update(response, page_content):
    if response.status_code == 200:
        for line in page_content.splitlines():
            if config.date in line:
                update = line[65:-63]
        return update

def compare_updates(new, old=config.versions):
    if new == old:
        print('\n{}: No changes detected.'.format(datetime.datetime.now()))
        pass
    else:
        print('\n{}: Changes detected.'.format(datetime.datetime.now()))
        return True

def send_email(message):
    try:
        server = smtplib.SMTP_SSL(host=config.smtp_srv, port=465)
        server.ehlo()
        server.login(user=config.from_email, password=config.as_passwd)
        server.sendmail(from_addr=config.from_email, to_addrs=config.to_email, msg=message)
        server.close()
        print('\nEmail sent!')
    except KeyboardInterrupt as eki:
        print('\nReceived CTRL+C.\nExiting...')
    except Exception as e:
        print('\nError during send_email()...')
        print(e)

def main():
    latest_update = get_update(resp, content)
    if compare_updates(latest_update) == True:
        send_email(config.mesg)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as eki:
        print('\nReceived CTRL+C.\nExiting...')
    except Exception as e:
        print('Error during main().')
        print(e)
