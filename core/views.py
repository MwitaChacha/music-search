from django.shortcuts import render
import requests
from decouple import config
# Create your views here.


def index(request):
    context = None
    if 'term' in request.GET:
        term = request.GET.get('term')
        
        
        # Shazam API URL
        url = "https://shazam.p.rapidapi.com/search"
        
        # Search keyword from the search form in the index page
        
        
        querystring = {"term":term,"locale":"global","offset":"0","limit":"1"}
        
        headers = {
            'x-rapidapi-host': "shazam.p.rapidapi.com",
            'x-rapidapi-key': config('x-rapidapi-key'),
            }
        
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        tracks=response['tracks']
        hits=tracks['hits']
        track=hits[0]['track']
        share=track['share']
            
            
            
        context = {'track':track,'hits':hits,'share':share}
            
            
    return render(request,'index.html',context)

