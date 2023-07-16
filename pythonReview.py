def create_youtube_video(title, description):
    youtube_video = {"title": title,"description": description,"likes":0,"dislikes": 0,"comments": {}}
    return youtube_video

def like(youtube_video):
    if "likes" in youtube_video:
        likes = youtube_video.get("likes")
        youtube_video["likes"] += 1
    return youtube_video

def dislike(youtube_video):
    if "dislikes" in youtube_video:
        dislikes = youtube_video.get("dislikes")
        youtube_video["dislikes"] += 1
    return youtube_video

def add_comment(youtube_video, username, comment_text):
    youtube_video['comments'][username] = comment_text
    return youtube_video

video = create_youtube_video("My Video", "This is a great video!")

print(video)
video = like(video)
video = dislike(video)
video = add_comment(video, "MRdonaldDuck", "Great video!")
video = add_comment(video, "Progamer214", "I disagree with some points.")
print(video)

for _ in range(495):
    video = like(video)
print(video)
