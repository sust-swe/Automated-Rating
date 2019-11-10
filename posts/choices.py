from .models import PostCategory

rating_choices = {
    '5': '5.00',
    '6': '6.00',
    '7': '7.00',
    '8': '8.00',
    '9': '9.00',
    '10': '10.00',
}

postcriteria_choices = {
    'mpp': 'Most Popular Post',
    'mcp': 'Most Commented Post',
    'mrp': 'Highest Rating'
}

category_choices = {
}

categories = PostCategory.objects.all()
for category in categories:
    category_choices[category.category_name] = category.category_name
