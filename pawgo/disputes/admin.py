from django.contrib import admin
from .models import Dispute

class DisputeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'walker', 'pub_date', 'description', 'ishandled')
    list_filter = ('ishandled', 'pub_date')
    search_fields = ('id', 'user__username', 'walker__username', 'description')
    list_display_links = ('id', 'user', 'walker', 'pub_date')

admin.site.register(Dispute, DisputeAdmin)