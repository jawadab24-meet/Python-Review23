def create_youtube_video(title,description):
	new_youtube_video={}
	new_youtube_video["title"]=title
	new_youtube_video["description"]= description
	new_youtube_video["likes"] = 0
	new_youtube_video["dislikes"]= 0
	new_youtube_video["comments"]= {}
	return new_youtube_video


def like(new_youtube_video):
	if "likes" in new_youtube_video:
		new_youtube_video["likes"] += 1
	return new_youtube_video

def dislike(new_youtube_video):
	if "dislikes" in new_youtube_video:
		new_youtube_video["dislikes"]+=1
	return new_youtube_video

def add_comment(new_youtube_video,username,comment_text):
	if "comments" in new_youtube_video:
		new_youtube_video["comments"][username]= comment_text
	return new_youtube_video

video = create_youtube_video("Funny cat moments","very funny")
for i in range(495):
	like(video)

video = add_comment(video, "User12", "LOL!")
print(video)
