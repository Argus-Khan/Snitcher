from fbchat import Client
from fbchat.models import *
from time import sleep

### Note: You need to make a file named "credentials.txt" which has you email on first line
### and password on the second line in case you want to use facebook message feature. It
### wont be nessary in the future as rather than using a normal facebook account it will 
### instead use a proper facebook bot.

def word_check(bad_words):
	with open("credentials.txt", 'r') as cor:
		credentials = cor.readlines()
	receiver = ''
	email = credentials[0]
	password = credentials[1]
	client = Client(email,password)
	mess = f" Hey! this dude/dudette has typed these words {bad_words}]. What a naughty kid ;) "
	client.send(Message(text= mess), thread_id=receiver, thread_type=ThreadType.USER)
	print (mess)
	sleep(2)
	client.logout()