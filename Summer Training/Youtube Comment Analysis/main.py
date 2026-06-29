import sys
import requests
import mysql.connector
from datetime import datetime

from config import API_KEY
from database import connect_db

# Fix Unicode issue on Windows
sys.stdout.reconfigure(encoding="utf-8")

VIDEO_ID = "eHTXQW58WhA"

URL = "https://www.googleapis.com/youtube/v3/commentThreads"

conn = connect_db()
cursor = conn.cursor()

query = """
INSERT INTO comments
(comment_id, video_id, author, comment, likes, published_at)
VALUES (%s, %s, %s, %s, %s, %s)
"""

total_inserted = 0
page_number = 1
next_page_token = None

print("Fetching comments...\n")

while True:

    params = {
        "part": "snippet",
        "videoId": VIDEO_ID,
        "maxResults": 100,
        "textFormat": "plainText",
        "key": API_KEY
    }

    if next_page_token:
        params["pageToken"] = next_page_token

    response = requests.get(URL, params=params)

    if response.status_code != 200:
        print("API Error:", response.status_code)
        print(response.json())
        break

    data = response.json()

    print(f"Page {page_number} : {len(data['items'])} comments")

    for item in data["items"]:

        comment_data = item["snippet"]["topLevelComment"]["snippet"]

        comment_id = item["snippet"]["topLevelComment"]["id"]
        author = comment_data["authorDisplayName"]
        comment = comment_data["textOriginal"]
        likes = comment_data["likeCount"]

        published = datetime.strptime(
            comment_data["publishedAt"],
            "%Y-%m-%dT%H:%M:%SZ"
        )

        values = (
            comment_id,
            VIDEO_ID,
            author,
            comment,
            likes,
            published
        )

        try:
            cursor.execute(query, values)
            total_inserted += 1

        except mysql.connector.IntegrityError:
            # Duplicate comment
            pass

    # Save current page
    conn.commit()

    # Next page
    next_page_token = data.get("nextPageToken")

    if not next_page_token:
        break

    page_number += 1

# Close database
cursor.close()
conn.close()
reply_count = item["snippet"]["totalReplyCount"]
print("\n---------------------------------------")
print(f"Total New Comments Inserted : {total_inserted}")
print("Database connection closed.")
print("---------------------------------------")