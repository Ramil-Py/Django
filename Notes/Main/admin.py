from django.contrib import admin
from .models import Notes

class NoteAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(owner=request.user)
        return qs

admin.site.register(Notes, NoteAdmin)