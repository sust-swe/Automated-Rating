from .models import PostCategory
from .models import ItemsList

rating_choices = {
    '': 'Blank',
    '3': '3.00',
    '4': '4.00',
    '5': '5.00',
    '6': '6.00',
    '7': '7.00',
    '8': '8.00',
    '9': '9.00',
    '10': '10.00',
}

postcriteria_choices = {
    '': 'Blank',
}

category_choices = {
    '': 'Blank',
}

categories = PostCategory.objects.all()
for category in categories:
    category_choices[category.category_name] = category.category_name

titles = ItemsList.objects.all()
for title in titles:
    postcriteria_choices[title.ItemsList_name] = title.ItemsList_name
