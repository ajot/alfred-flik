from twilio.rest import TwilioRestClient

def make_the_call(text_message,contact):

# Get your Twilio account & token id at http://twilio.com
	account = "your_twilo_account_id"
	token = "your_twilo_token"	
	
	client = TwilioRestClient(account, token)
	
	address_book = {'name1':'phone1','name2':'phone2'}
	#Example: {'John':'+1212123456','Ana':'+417123456'}
	
	for name, number in address_book.iteritems():
		if name == contact:
			to = number
			break
		else:
			to = '+17033625298'
		
	print "Following movies were sent to %s: \r\r" % (name)
	
	#Truncating the text message
	text_message = text_message[0:155]
	message1 = client.sms.messages.create(to=to, from_="+16464616641", body=text_message)
	