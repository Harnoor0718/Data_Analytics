import sys
import requests
from config import API_KEY

# Fix Unicode issue on Windows (for emojis)
sys.stdout.reconfigure(encoding="utf-8")

# YouTube Video ID
VIDEO_ID = "eHTXQW58WhA"

# YouTube API Endpoint
url = "https://www.googleapis.com/youtube/v3/commentThreads"

# Parameters
params = {
    "part": "snippet",
    "videoId": VIDEO_ID,
    "maxResults": 10,
    "textFormat": "plainText",
    "key": API_KEY
}

# Send GET Request
response = requests.get(url, params=params)

# Check if request is successful
if response.status_code == 200:

    data = response.json()

    print(f"Successfully fetched {len(data['items'])} comments.\n")

    # Loop through each comment
    for item in data["items"]:

        # Comment details
        comment_data = item["snippet"]["topLevelComment"]["snippet"]

        # Extract required information
        comment_id = item["snippet"]["topLevelComment"]["id"]
        author = comment_data["authorDisplayName"]
        comment = comment_data["textOriginal"]
        likes = comment_data["likeCount"]
        published = comment_data["publishedAt"]

        # Display
        print("=" * 70)
        print(f"Author      : {author}")
        print(f"Comment ID  : {comment_id}")
        print(f"Likes       : {likes}")
        print(f"Published   : {published}")
        print("\nComment:")
        print(comment)
        print("=" * 70)
        print()

else:
    print("Error:", response.status_code)
    print(response.json())