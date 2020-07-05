# wp_comment_spam
Nagios plugin (.py) to check wordpress comment spam



This python script has been tested on Ubuntu Server 20.04 LTS.

You need to install mysql connector module for python 3:
sudo apt-get install python3-mysql.connector

Copy/paste this script to your Nagios plugin folder.

How to use this script:
To run this script, you need to type arguments this way:
- 1st arg: Database username
- 2nd arg: Database password
- 3rd arg: DB host's IP address
- 4th: DB name to use
- 5th: number of comments in last 4 hours as Warning threshold
- 6th: number of comments in last 4 hours as critical threshold
