from __future__ import unicode_literals
from TwitterAPI import TwitterAPI


consumer_key = "iyCOKqmIgE48iGn2rxvONulu8",
consumer_secret = "HjHE1jGGYILIwf9FgXhUUvvDfA9DWPxyBnHrS6eKuZcTwRL2AL",
access_token_key = "859515563374067712-cW804i62lNaf8SCnEaOZDJRK3sZ7EnJ",
access_token_secret = "x1VjBNcTyrNzw8zjuq6nVsHfEC6AT8Hhekgs22yxtvRG5",

api = TwitterAPI(consumer_key,
 				 consumer_secret,
 				 access_token_key, 
                 access_token_secret)

r = api.request('search/tweets', {'q':'this'})
for item in r:
        print(item)