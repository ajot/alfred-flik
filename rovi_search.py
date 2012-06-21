import urllib2
import rovi_auth
import call_twilio
import json
import simplejson

def get_relatedMovies(search,contact):
	
	contact = contact
	sig = rovi_auth.sign()
	try:
		#Accessing Rovi's Metadata and Search API
		url ='http://api.rovicorp.com/data/v1/movie/related?movie=%s&country=US&language=en&format=json&apikey=zz746f6m7guwqg2fehsecdah&sig=%s&limit=3' % (search,sig)
		rovi_json = urllib2.urlopen(url).read()
		
		# convert to a native python object
		(true,false,null) = (True,False,None)
		
		#Parsing the json payload
		rovi_data = eval(rovi_json)
		
		#Retrieving movie from the payload
		movie = rovi_data ['related']['isRelatedTo']
		related_movies =''
		movie_review =''
		reviews_message=''
		
		for i, m in enumerate(movie):

				movie_title_original = m ['title']				
				movie_title = (movie_title_original.replace(" ", "+")).replace(':','')
				
				release_year = m ['releaseYear']
		
				#Getting movie_id from Rotten Tomatoes for each movie returned by Rovi's related API. This code must run multiple times in a loop.
				rotten_get_movie_id_url ='http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=bhtrz42e3ndmmnu4q62ppm2s&q=%s' % (movie_title)
				rotten_json = urllib2.urlopen(rotten_get_movie_id_url).read()		 		
				
				(true,false,null) = (True,False,None)
				rotten_data = eval(rotten_json)				
			
				try:					
					movie_id = rotten_data ['movies'][i]['id']

					#Getting movie reviews from Rotten Tomatoes for each movie_id returned by Rotten Tomatoes' movies API. This code must run multiple times in a loop.
					rotten_get_movie_review_url ='http://api.rottentomatoes.com/api/public/v1.0/movies/%s/reviews.json?apikey=bhtrz42e3ndmmnu4q62ppm2s' % (movie_id)
					
					reviews_json = urllib2.urlopen(rotten_get_movie_review_url).read()
					reviews_data = simplejson.loads(reviews_json)					
					movie_review = reviews_data ['reviews'][i]['links']['review']
				
				except IndexError:
					# print 'Review Not available'
					print ' '
					
				except simplejson.decoder.JSONDecodeError:	
					# print 'Review Not available'
					print ' '
				
				related_movies = related_movies + str(i+1) + '. ' + movie_title_original + ' \r'

	except urllib2.URLError, e:
		print e	
	except KeyError, e:
		print e	
		
	call_twilio.make_the_call(related_movies,contact)
	print "Message Sent \r"
	print related_movies
