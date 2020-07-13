from django.forms import ModelForm
from .models import Listing, Bid

class  ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['category', 'title', 'description', 'imgurl', 'min_price']

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['item_id','bid']