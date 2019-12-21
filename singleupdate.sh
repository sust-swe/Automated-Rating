import django
django.setup()
import pickle
from posts.models import Posts, ItemsList, Comment
from statistics import mean
import numpy as np
from decimal import Decimal

filename = 'C:/Users/tamim/PyProjects/AutomatedRating/Natural Language Processing NLP/cvectorize.sav'
loaded_vect = pickle.load(open(filename, 'rb'))
filename = 'C:/Users/tamim/PyProjects/AutomatedRating/Natural Language Processing NLP/sentiment.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# checking
# loaded_model.predict(loaded_vect.transform(['this is super good', 'this is good']))

comments = Comment.objects.filter(scores__isnull=True)
for comment in comments:
     ar = loaded_model.predict(loaded_vect.transform([str(comment)]))
     rat = ((ar[0] + 1)*2)-0.1
     rat = np.float64(rat).item()
     comment.scores = rat
     comment.save()
     item = comment.post.post_item
     if(item.numcomment):
         item.numcomment = item.numcomment + 1
     else:
         item.numcomment = 1
     tot_com = (float(item.numcomment - 1))
     prev_rat = (float(item.rating))
     new_rat = ((tot_com*prev_rat)+rat)/(tot_com + 1)
     item.rating = new_rat
     item.save()
print('successfully updated rating')
