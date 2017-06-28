from twitter import *
import re
from time import strftime
from textwrap import fill
from termcolor import colored
from email.utils import parsedate

print("Enter in tracking term")
search_term = raw_input("> ")

config = {}
execfile("config.py", config)

auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"])
stream = TwitterStream(auth = auth, secure = True)

tweet_iter = stream.statuses.filter(track = search_term)

pattern = re.compile("%s" % search_term, re.IGNORECASE)

for tweet in tweet_iter:

	timestamp = parsedate(tweet["created_at"])
	timetext = strftime("%c", timestamp)
	timestamp = parsedate(tweet["created_at"])


	time_colored = colored(timetext, color = "white", attrs = [ "bold" ])
	user_colored = colored(tweet["user"]["screen_name"], "green")
	text_colored = tweet["text"]


	text_colored = pattern.sub(colored(search_term.upper(), "yellow"), text_colored)
	indent = " " * 11
	text_colored = fill(text_colored, 80, initial_indent = indent, subsequent_indent = indent)

	print "(%s) @%s" % (time_colored, user_colored)
	print "%s" % (text_colored)

