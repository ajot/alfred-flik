import time
import hashlib

# Get your Rovi API Key from http://developer.rovicorp.com
APIKEY = 'your_rovi_api_key'
SECRET = 'your_rovi_shared_secret'

def apikey():
   return APIKEY

def secret():
   return SECRET

def sign():
   my_time = int(time.time())
   sig = hashlib.md5()
   sig.update(APIKEY)
   sig.update(SECRET)
   sig.update(str(my_time))

   return sig.hexdigest()

if __name__ == '__main__':
   print sign()