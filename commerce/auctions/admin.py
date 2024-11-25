from django.contrib import admin

# Register your models here.
from .models import User, AuctionListing, Bid, Comment,Watchlists

admin.site.register(User)
admin.site.register(AuctionListing)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Watchlists)