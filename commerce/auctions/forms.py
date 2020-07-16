from django.forms import ModelForm
from .models import Listing, Bid

class  ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['owner','category', 'title', 'description', 'imgurl', 'price']