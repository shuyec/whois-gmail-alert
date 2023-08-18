# **Whois Gmail Alert**

Python script that sends an email to yourself when a domain in the wish list does not exist anymore (expired).

## Requirements
* [whoisdomain](https://pypi.org/project/whoisdomain/)

## WhoIsDomain requirements
* Please install also the command line "whois" of your distribution as this library parses the output of the "whois" cli command of your operating system.

For Windows, download and extract [command line Whois](https://learn.microsoft.com/en-us/sysinternals/downloads/whois) in the project folder.

## Setup
1. Create the text file `domains.txt` and put the wanted domains like in `domains.txt.example`
2. Create a `config.ini` file like `config.ini.example` and insert your gmail email
3. Create an [app password](https://support.google.com/accounts/answer/185833?hl=en) for your Google account and copy it to `config.ini`

## Notes
* The script `with_timer.py` is in an infinite while loop, so it needs to be stopped manually.
* The timer between the checks can be changed in the `config.ini` file. It is 5 minutes (300 seconds) by default.
* The script `without_timer.py` runs it once, so it needs something like Windows 10 Task Scheduler to automatically run it multiple times.