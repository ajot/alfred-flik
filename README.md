# What is "AlfredFlik"?
 
"AlfredFlik" is an [Alfred](http://www.alfredapp.com/) extension built using Python, that finds similar movies using Rovi's Metadata and Search API and then allow you to text them to a phone number using Twilio's API.

## What is Alfred?
[Alfred](http://alfredapp.com) is an award-winning productivity application for Mac OS X, which aims to save you time in searching your local computer and the web. Whether it's maps, Amazon, eBay, Wikipedia, you can feed your web addiction quicker than ever.

The real power of Alfred lies in it's [powerpack](http://www.alfredapp.com/powerpack/) that allows you to create your very own Terminal shell scripts, AppleScripts, workflows, search filters and file groups to extend Alfred.

## Summary

Say, you're a fan of Arnold and you watched Terminator last week with your friend. You can't get enough of the action and you wanna watch more movies along the same lines. You can now use Alfred-Flik - a handy extension that lets you specify a movie name and the name/phone number of the person you'd like to text the list of movies to. Alfred-Flik then queries Rovi's Metadata and Search API, pulls up a list of similar movies. It also finds the ratings of these movies via Rotten Tomatoes. Finally it sends it as an SMS to the phone number you provide using Twilio. 

## Requirements

1. [Alfred](http://www.alfredapp.com/) + [Alfred Powerpack](http://www.alfredapp.com/powerpack/)
2. [Rovi API Key](http://developer.rovicorp.com)
3. [Twilio API Key](http://twilio.com)
4. Growl
5. Nice and shiny Mac - Of course you have one!


## How to Use

1. Make sure Alfred is running. 

2. Just hit your Alfred keyboard shortcut. In my case I have it configured it as CMD + SPACE. (The default is probably ALT + SPACE)

	![Alfred Launch Bar](https://github.com/ajotwani/Alfred-Flik/raw/master/images/alfred_launch_bar.png)

3. Type the keyword **movie** followed by the **name of the movie** you want to search by and then the **name/phone number** of the person you'd like to text the results to (You can change the keyword by editing the info.plist file)	
	
	Using the phone number
	
	![Alfred Launch Bar](https://github.com/ajotwani/Alfred-Flik/raw/master/images/alfred_launch_bar_fill_1.png)	
	
	Using the address book described in **call_twilio.py** file
	
	![Alfred Launch Bar](https://github.com/ajotwani/Alfred-Flik/raw/master/images/alfred_launch_bar_fill_2.png)	

4. A text message is sent to your friend 

	![Alfred Text Message](https://github.com/ajotwani/Alfred-Flik/raw/master/images/text_message.png)
	
5. Also, you get a Growl notification confirming that the text was sent and the list of the movies that were sent.

	![Alfred Growl Notification](https://github.com/ajotwani/Alfred-Flik/raw/master/images/alfred_growl.png)


## Examples ##
	<pre>movie terminator john</pre>
	<pre>movie "safety not guaranteed" +1417123456</pre>

## Installation

	
1. Grab the latest source
	<pre>git clone git://github.com/ajotwani/Alfred-Flik.git</pre>

2. Copy the directory you just downloaded to -
	<pre>~/Library/Application Support/Alfred/extensions/scripts</pre>

3. Rename this directory to say "AlfredFlik"	

4. Open the file "~/Library/Application Support/Alfred/extensions/scripts/AlfredFlik/rovi_auth.py" and type in your type in your Rovi **API key** & **Shared Secret**. Get your Rovi (Metadata and Search) API Key [here](http://developer.rovicorp.com)

	![Type your Rovi API Key](https://github.com/ajotwani/Alfred-Flik/raw/master/images/rovi_api_key.png)
5. Open the file "call\_twilio\_.py" and type in your Twilio account id and toke id. Get your Twilio account & token id [here](http://twilio.com)

	![Type your Twilio API Key](https://github.com/ajotwani/Alfred-Flik/raw/master/images/twilio_api_key.png)
6. Install all dependencies. Open Terminal and type the following (If you run into permission issues, try with sudo) -

	Twilio's Python module
	
	<pre>easy_install twilio</pre> 
	
	SimpleJSON
	<pre>easy_install simplejson</pre> 

7. You're done. Just give Alfred a whirl now. Refer [How to Use](#how-to-use) above.	


## Development

Be sure to follow the configuration steps above and use this step-by-step guide to tweak to your heart's content.

1. Grab the latest source
	<pre>git clone git://github.com/ajotwani/Alfred-Flik.git</pre>

2. All the Rovi search related action takes place in the file **'rovi\_search\_.py'**

3. All the Rovi auth related action takes place in the file **'rovi_auth.py'**

4. All the Twilio related action takes place in the file **"call_twilio.py"**

5. Tweak away


## About 

* No warranty expressed or implied.  Software is as is.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly created by [Mashery Dev](http://dev.mashery.com)