# this code run on terminal
# python manage.py shell

# filename = 'C:/Users/tamim/PyProjects/AutomatedRating/Natural Language Processing NLP/cvectorize.sav.sav'
# filename = 'C:/Users/tamim/PyProjects/AutomatedRating/Natural Language Processing NLP/sentiment.sav'

# saikat
# filename = 'C:/Users/User/Documents/Visual Studio Code/project 350/Automated-Rating/Natural Language Processing NLP/cvectorize.sav'
# filename = 'C:/Users/User/Documents/Visual Studio Code/project 350/Automated-Rating/Natural Language Processing NLP/sentiment.sav'

import pickle
from posts.models import Posts, ItemsList, Comment
from statistics import mean
import numpy as np
import time

filename = 'C:/Users/tamim/PyProjects/AutomatedRating/Natural Language Processing NLP/cvectorize.sav'
loaded_vect = pickle.load(open(filename, 'rb'))
filename = 'C:/Users/tamim/PyProjects/AutomatedRating/Natural Language Processing NLP/sentiment.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# checking
# loaded_model.predict(loaded_vect.transform(['this is super good', 'this is good']))

starttime = time.time()
items = ItemsList.objects.all()
while True:
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
     print('success', time.time())
     time.sleep(4.0 - ((time.time() - starttime) % 4.0))
