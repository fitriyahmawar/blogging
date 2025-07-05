from django.contrib import admin
from artikel.models import Kategori, ArtikelBlog

# Register your models here.

class KategoriAdmin(admin.ModelAdmin):
    list_display = ['nama', 'created_at', 'created_by']
    search_fields = ['nama']
admin.site.register(Kategori, KategoriAdmin)

class ArtikelBlogAdmin(admin.ModelAdmin):
    list_display = ['kategori', 'judul', 'created_at', 'created_by', 'status']
    search_fields = ['kategori__nama', 'judul']
admin.site.register(ArtikelBlog, ArtikelBlogAdmin)