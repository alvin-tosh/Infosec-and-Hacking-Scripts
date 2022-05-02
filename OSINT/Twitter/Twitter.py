import twint
from datetime import datetime
today = datetime.now().strftime("%Y-%m-%d")

search = input('What are you looking for? ')
city = input('Where? ')

c = twint.Config()
c.Search = search
c.Near = city
c.Limit = 100
c.Popular_tweets = True

twint.run.Search(c)