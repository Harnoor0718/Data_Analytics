data (dict)
│
├── kind
├── etag
├── nextPageToken
├── pageInfo
└── items (list)
      │
      ├── item 1 (dict)
      │      │
      │      ├── kind
      │      ├── etag
      │      ├── id (Comment Thread ID)
      │      └── snippet
      │             │
      │             ├── channelId
      │             ├── videoId
      │             ├── canReply
      │             ├── totalReplyCount
      │             ├── isPublic
      │             └── topLevelComment
      │                    │
      │                    ├── id (Actual Comment ID)
      │                    └── snippet
      │                           │
      │                           ├── authorDisplayName
      │                           ├── textOriginal
      │                           ├── textDisplay
      │                           ├── likeCount
      │                           ├── publishedAt
      │                           ├── updatedAt
      │                           ├── authorChannelId
      │                           ├── authorProfileImageUrl
      │                           └── ...
      │
      ├── item 2
      ├── item 3
      └── ...