import requests
import pyperclip
import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(description='Shorten a URL using the Bitly API')
parser.add_argument('url', help='the URL to shorten')

# Parse the arguments
args = parser.parse_args()

# Set up the API endpoint and access token
endpoint = 'https://api-ssl.bitly.com/v4/shorten'
access_token = 'YOUR_ACCESS_TOKEN_HERE'

# Set up the headers and data for the API request
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
data = {
    'long_url': args.url
}

# Send the API request
response = requests.post(endpoint, headers=headers, json=data)

# Get the shortened URL from the response
short_url = response.json()['link']

# Copy the shortened URL to the clipboard
pyperclip.copy(short_url)

# Print the shortened URL to the console
print(f'Short URL: {short_url}')
