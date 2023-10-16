import urllib.request

url = "https://www.example.com"
response = urllib.request.urlopen(url)

# Read the response content
html = response.read()

# Close the response
response.close()

# Print the HTML content
print(html)