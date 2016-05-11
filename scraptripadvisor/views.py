from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from bs4 import BeautifulSoup
from lxml import html
import urllib2
import requests
import re

# Import model here if necessary

def index(request):
     template = loader.get_template('scraptripadvisor/index.html')
     soup = BeautifulSoup(open("scraptripadvisor/Singapore-tripadvisor.html").read())
     tList = []
     spans = soup.findAll('span', attrs={'class':u'reviewCount'})
     for span in spans:
       a = span.find('a')
       m = re.search(r'\d+',str(a.string))
       resto = re.search('(?<=Reviews-)(.*?)(?=-Singapore)',a.get('href')).group(0)
       tList.append((str(resto),str(m.group(0))))
       tList.sort(key=lambda review: review[1], reverse=True)
#     print(soup.prettify())
#     return HttpResponse("Hello, let's scrap")
#     return render(request, 'scraptripadvisor/index.html')
     context = {'list':tList}
     return HttpResponse(template.render(context, request))
# Create your views here.
