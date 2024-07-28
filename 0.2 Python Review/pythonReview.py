# youtube_videos = {}
def create_youtube_video():
    title = input("Title of the video: ")
    description = input("Description: ") 
    youtube_videos = {
        "title": title,
        "description": description,
        "likes": 0,
        "dislikes": 0,
        "comments": []
    }
    return youtube_videos

def like(youtube_videos):
    youtube_videos["likes"] += 1
    return youtube_videos

def dislike(youtube_videos):
    youtube_videos["dislikes"] += 1
    return youtube_videos
    
def add_comment(youtube_videos):
    user_name = input("Name: ")
    comment = input("Comment: ")
    youtube_videos["comments"].append({"username": user_name, "comment": comment})
    return youtube_videos

# Main script
youtube_videos = create_youtube_video()

while True:
    print("\nWhat do you want to do?")
    print("1. Create a new YouTube video")
    print("2. Like the video")
    print("3. Dislike the video")
    print("4. Add a comment")
    print("5. Show video details")
    print("6. Exit")
    
    action = int(input("Choose an action (1-6): "))
    
    if action == 1:
        youtube_videos = create_youtube_video()
    elif action == 2:
        youtube_videos = like(youtube_videos)
    elif action == 3:
        youtube_videos = dislike(youtube_videos)
    elif action == 4:
        youtube_videos = add_comment(youtube_videos)
    elif action == 5:
        print(youtube_videos)
    elif action == 6:
        break
    else:
        print("Invalid action. Please choose a number between 1 and 6.")