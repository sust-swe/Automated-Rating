import django
django.setup()
import pickle
from posts.models import Posts, ItemsList, Comment
from statistics import mean
import numpy as np

filename = 'C:/Users/tamim/PyProjects/AutomatedRating/Natural Language Processing NLP/cvectorize.sav'
loaded_vect = pickle.load(open(filename, 'rb'))
filename = 'C:/Users/tamim/PyProjects/AutomatedRating/Natural Language Processing NLP/sentiment.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# checking
# loaded_model.predict(loaded_vect.transform(['this is super good', 'this is good']))

"""comments = Comment.objects.filter(scores__isnull=True)
for comment in comments:
     ar = loaded_model.predict(loaded_vect.transform([str(comment)]))
     rat = ((ar[0] + 1)*2)-0.1
     rat = np.float64(rat).item()
     comment.scores = rat
     comment.save()
     cmt.post.post_item.rating"""

items = ItemsList.objects.all()
for item in items:
     rat_lst = []
     posts = item.posts_set.all()  # using choice set for reverse lookup
     for post in posts:
         comments = post.comments.all()
         for comment in comments:
             ar = loaded_model.predict(loaded_vect.transform([str(comment)]))
             rat = (ar[0] + 1)*2
             rat_lst.append(np.float64(rat).item())
     if (rat_lst != []):
         item.rating = mean(rat_lst)
         item.save()
print("successfully updated rating")
