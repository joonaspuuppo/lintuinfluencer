from twython import Twython
from subprocess import call
import time
from time import strftime, gmtime
import random
import tweet
from tweet import Tweet

# Initialize GPIO 
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(04, GPIO.IN)   # GPIO4 is pin 7

# Twitter Token
APP_KEY = ''
APP_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

SLEEP_DURATION = 30

# local time when the sun sets 20 = 8 PM
SUNSET = 20
SUNRISE = 6

messages = []
messages.append("The early bird gets the fresh seeds. #birds #birdwatching")

# wait for proximity sensor 
while True:

	# Check current local time
	utc_hour = int(strftime("%H", gmtime()))
    	hour = utc_hour - 6
    	if (hour < 0):
        	hour = hour + 24

	# # if motion and if the sun hasn't set
	# if (GPIO.input(04) and hour < SUNSET and hour > SUNRISE):
	# 	try:
	# 		# Take a picture
	# 		call("/opt/vc/bin/raspistill -e jpg --vflip -w 320 -h 320 -q 100 -o /tmp/snapshot.jpg", shell=True)

	# 		# Sign in to Twitter
	# 		twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

	# 		# Post a status update with a picture
	# 		photo = open('/tmp/snapshot.jpg', 'rb')
			
	# 		r = random.randint(0, len(messages)-1)
	# 		message = messages[r]
	# 		twitter.update_status_with_media(status=message, media=photo)

	# 	except:
	# 		print("Unexpected error:")
		
		# Sleep so that multiple pictures aren't taken of the same bird
		time.sleep(SLEEP_DURATION)
	
	else:
		time.sleep(0.25)