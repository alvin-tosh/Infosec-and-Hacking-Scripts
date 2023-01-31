import time
import requests
import tweepy

# Replace these with your own API keys
CONSUMER_KEY = ' '
CONSUMER_SECRET = ' '
ACCESS_TOKEN = ' '
ACCESS_TOKEN_SECRET = ' '

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Set the tail number to track
tail_number = 'ZS-RMN'

# Set the OpenSky API URL
api_url = 'https://opensky-network.org/api/states/all'

# Set the current position to None
current_position = None

while True:
  # Make a request to the OpenSky API
  response = requests.get(api_url)
  
  # Check if the request was successful
  if response.status_code != 200:
    # If the request failed, print an error message
    print("Error making request to OpenSky API")
  else:
    # If the request was successful, get the response data
    response_data = response.json()
    
    # Iterate through the list of states
    for state in response_data['states']:
      if state[1] == tail_number:
        # If the tail number matches, get the latitude, longitude, and altitude
        lat = state[6]
        lon = state[5]
        alt = state[7]

        # Check if the position has changed
        position = (lat, lon, alt)
        if position != current_position:
          # If the position has changed, tweet the new location of the airplane
          message = f'Tail number {tail_number} is currently at latitude {lat}, longitude {lon}, and altitude {alt}'
          api.update_status(status=message)

          # Update the current position
          current_position = position
      
  # Wait for 60 seconds before making another request
  time.sleep(60)
