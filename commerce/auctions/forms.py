from django.forms import ModelForm
from .models import Listing

class  ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['category', 'title', 'description', 'imgurl', 'min_price']