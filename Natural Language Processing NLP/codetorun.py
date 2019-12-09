# this code run on terminal
# python manage.py shell

# filename = 'C:/Users/tamim/PyProjects/AutomatedRating/Natural Language Processing NLP/finalized_model.sav'
# filename = 'C:/Users/tamim/PyProjects/AutomatedRating/Natural Language Processing NLP/sentiment.sav'

import pickle

filename = 'C:/Users/tamim/PyProjects/AutomatedRating/Natural Language Processing NLP/cvectorize.sav'
loaded_vect = pickle.load(open(filename, 'rb'))
filename = 'C:/Users/tamim/PyProjects/AutomatedRating/Natural Language Processing NLP/sentiment.sav'
loaded_model = pickle.load(open(filename, 'rb'))

#checking
loaded_model.predict(loaded_vect.transform(['this is super good', 'this is good']))
