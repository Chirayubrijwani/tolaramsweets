from django.shortcuts import render
from home.models import Item,Products

def home(request):
	best_sellers=Products.objects.filter(best_seller=1)
	print(best_sellers)
	return render(request, 'home/index.html',{"bests":best_sellers})

def variety(request,id=1):
	all_products=Products.objects.filter(item_id=int(id))
	return render(request, 'home/variety.html',{"products":all_products})

def menu(request):
	all_ctg=Item.objects.all()
	return render(request, 'home/menu.html',{"categories":all_ctg})

def blog(request):
	return render(request, 'home/blog.html')


def contact(request):
	return render(request, 'home/contact.html')


def events(request):
	return render(request, 'home/events.html')

