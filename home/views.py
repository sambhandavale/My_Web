from django.shortcuts import render

users = [
    {'No': 1, 'Name': 'Sam Bhandavale', 'Roll': 17},
    {'No': 2, 'Name': 'Max Dilon', 'Roll': 34}
]


def home(request):
    data = {
        'user': users
    }
    return render(request, 'home/home.html', data)


def user(request, pk):
    user = None
    for i in users:
        if i['No'] == int(pk):
            user = i
    data = {'user': user}
    return render(request, 'home/users.html', data)
