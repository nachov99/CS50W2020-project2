from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import ListingForm
def index(request):
    context = {
        'user': request.user,
        "listings": Listing.objects.all(),
        'category': Category.objects.all(),
    }
    return render(request, "auctions/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

''' CREATE AUCTION '''
@login_required
def createProduct(request):

    form = ListingForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "auctions/product_form.html", context)

''' SEE PRODUCT '''
@login_required
def productDetail(request, listing_id):
    product = Listing.objects.get(pk=listing_id)
    
    context = {'product':product}
    return render(request, "auctions/product_detail.html", context)

''' ADD TO WATCHLIST '''
@login_required
def addWatchlist(request, listing_id):

    product, created = Listing.objects.get_or_create(Listing, pk=listing_id)
    watchlist, created = Watchlist.objects.get_or_create(user=request.user)
    
    watchlist.product.add(listing_id)
    return HttpResponseRedirect(reverse("index"))

''' SEE WATCHLIST '''
@login_required
def watchlist(request):
    context = {
        'user': request.user,
        'watchlists': Watchlist.objects.all(),
    }
    return render(request, "auctions/watchlist.html", context)

''' DELETE FROM WATCHLIST '''
@login_required
def deleteWatchlist(request, listing_id):
    product, created = Listing.objects.get_or_create(Listing, pk=listing_id)
    watchlist, created = Watchlist.objects.get_or_create(user=request.user)
    
    watchlist.product.delete(listing_id)
    return HttpResponseRedirect(reverse("watchlist"))

''' CATEGORIES '''
@login_required
def categories(request):
    context = {
        'categories': Category.objects.all(),
    }
    return render(request, "auctions/categories.html", context)

@login_required
def categoryDetail(request, category_id):
    listings = Listing.objects.filter(category=category_id)

    context = {'Listings':listings}
    return render(request, "auctions/category_detail.html", context)