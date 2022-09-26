# **Whois Gmail Alert**

Python script that sends an email to yourself when a domain in the wish list does not exist anymore (expired).

## Requirements
* [python-whois](https://pypi.org/project/python-whois/)

## Setup
1. Create the text file `domains.txt` and put the wanted domains like in `domains.txt.example`
2. Create a `config.ini` file like `config.ini.example` and insert your gmail email
3. Create an [app password](https://support.google.com/accounts/answer/185833?hl=en) for your Google account and copy it to `config.ini`

## Notes
* The script is in an infinite while loop, so it needs to be stopped manually.
* The timer between the checks can be changed in the `config.ini` file. It is 5 minutes (300 seconds) by default.