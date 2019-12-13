# this code run on terminal
# python manage.py shell

# filename = 'C:/Users/tamim/PyProjects/AutomatedRating/Natural Language Processing NLP/cvectorize.sav.sav'
# filename = 'C:/Users/tamim/PyProjects/AutomatedRating/Natural Language Processing NLP/sentiment.sav'

# saikat
# filename = 'C:/Users/User/Documents/Visual Studio Code/project 350/Automated-Rating/Natural Language Processing NLP/cvectorize.sav'
# filename = 'C:/Users/User/Documents/Visual Studio Code/project 350/Automated-Rating/Natural Language Processing NLP/sentiment.sav'

import pickle
from posts.models import Posts
from statistics import mean
import numpy as np

filename = 'C:/Users/tamim/PyProjects/AutomatedRating/Natural Language Processing NLP/cvectorize.sav'
loaded_vect = pickle.load(open(filename, 'rb'))
filename = 'C:/Users/tamim/PyProjects/AutomatedRating/Natural Language Processing NLP/sentiment.sav'
loaded_model = pickle.load(open(filename, 'rb'))

#checking
loaded_model.predict(loaded_vect.transform(['this is super good', 'this is good']))

for post in posts:
     comments = post.comments.all()
     rat_lst = []
     for comment in comments:
             #print(comment)
             ar = loaded_model.predict(loaded_vect.transform([str(comment)]))
             rat = (ar[0] + 1)*2
             rat_lst.append(np.float64(rat).item())
     rat_lst
     post.post_item.rating = mean(rat_lst)
     post.post_item.save()
