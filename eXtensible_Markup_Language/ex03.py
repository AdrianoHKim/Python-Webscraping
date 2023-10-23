import urllib.request
import json

url = input("Enter location: ")

try:
    data = urllib.request.urlopen(url).read()
    print("Retrieving", url)
except:
    print("Invalid URL or unable to retrieve data.")
    quit()

try:
    json_data = json.loads(data)
except:
    print("Invalid JSON data.")
    quit()

# Extract the list of comments
comments = json_data.get("comments", [])

count_sum = 0

# Loop through the comments and sum the counts
for comment in comments:
    count = comment.get("count", 0)
    count_sum += count

print("Count:", len(comments))
print("Sum:", count_sum)
