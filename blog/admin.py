from django.contrib import admin
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
	list_display = ["baslik", "yaratilis_tarihi", "yayinlama_tarihi"]
	list_display_link = ["yaratilis_tarihi"]
	list_filter = ["yaratilis_tarihi", "yayinlama_tarihi"]

	class Meta:
		model=Post

admin.site.register(Post, PostModelAdmin)