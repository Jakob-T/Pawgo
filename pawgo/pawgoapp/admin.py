# pawgoapp/admin.py

from django.contrib import admin
from django.db.models import Count
from .models import TopUp

class TopUpAdmin(admin.ModelAdmin):
    change_list_template = "admin/pawgoapp/topup/change_list.html"

    def changelist_view(self, request, extra_context=None):
        # Add custom context data
        extra_context = extra_context or {}
        used_count = TopUp.objects.filter(isused=True).count()
        total_count = TopUp.objects.count()
        extra_context['title'] = f"TopUps ({used_count}/{total_count})"
        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(TopUp, TopUpAdmin)