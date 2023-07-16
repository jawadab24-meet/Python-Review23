def create_youtube_video(title,description):
	new_youtube_video={}
	new_youtube_video["title"]=title:
	new_youtube_video["description"= description]
	new_youtube_video["likes"] = 0
	new_youtube_video["dislike"]= 0
	new_youtube_video["comments"]= {}
	return create_youtube_video
def like(create_youtube_video):
	if like in create_youtube_video:
		new_youtube_video["likes"] +=1
	return new_youtube_video
def dislike(create_youtube_video):
	if dislike in create_youtube_video:
		new_youtube_video["dislike"]+=1
	return new_youtube_video
def add_comment(new_youtube_video,username,comment_text):
	if "comments" in new_youtube_video:
		new_youtube_video["comments"][username]= comment_text
	return new_youtube_video
new_youtube_video1 =create_youtube_video("title","description")
