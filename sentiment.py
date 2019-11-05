from textblob import TextBlob
from posts.models import Posts
from statistics import mean

posts = Posts.objects.all()

for post in posts:
    comments = post.comments.all()
    rat_lst = []
    for comment in comments:
        pol = TextBlob(str(comment)).sentiment.polarity
        if pol == 0:
            rat = 5
        else:
            rat = 5 + ((pol*10)/2) - 0.1
        rat_lst.append(rat)
    post.post_item.rating = mean(rat_lst)
    post.post_item.save()
