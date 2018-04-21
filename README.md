Approach Followed:
--------------------

1. First we create a twitter API by creating a twitter account and logging into http://apps.twitter.com. Here we generate an access token to our API.


2. We install the twitter libraries as:

  $ python setup.py build     
  $ python setup.py install


3. The access tokens generated as above we use in our program IIITDtwitter.py file.

4. We run IIITDtwitter.py for getting 10000 tweets into mysql database.

5. Now to get the news from a news API we create an account over https://newsapi.org/ to get the API key and use it in       file to get      the news.
