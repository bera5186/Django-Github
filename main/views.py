import json
import requests
from django.shortcuts import HttpResponse, render

# Create your views here.


def index(request):
    return HttpResponse('Hello WOrld')


def test(request):
    return HttpResponse('Hello Test')


def profile(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList = []
        jsonList.append(json.loads(req.content))
        userData = {}
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
            userData['location'] = data['location']
        parsedData.append(userData)
    return render(request, 'main/profile.html', {'data': parsedData})
    
