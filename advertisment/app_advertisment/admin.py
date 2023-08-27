from django.contrib import admin
from .models import Advertisment

class AdvertismentAdmin( admin.ModelAdmin ):
    list_display = [ 'id', 'title', 'description', 'price', 'created_date', 'auction', 'updated_date', 'user', 'show_image' ]
    list_filter = [ 'auction', 'created_at' ]
    actions = [ 'make_auction_as_false', 'make_auction_as_true' ]
    search_fields = [ 'title' ]

    @admin.action( description = 'Убрать возможность торга.' )
    def make_auction_as_false( self, request, queryset ):
        queryset.update( auction = False )

    @admin.action( description = 'Добавить возможность торга.' )
    def make_auction_as_true( self, request, queryset ):
        queryset.update( auction = True )

admin.site.register( Advertisment, AdvertismentAdmin )
