from django.shortcuts import render, redirect
from artikel.models import Kategori, ArtikelBlog

def index(request):
    template_name = "landingpage/index.html"
    kategori = Kategori.objects.all()
    artikel = ArtikelBlog.objects.all()
    top_berita = ArtikelBlog.objects.all()[:3]

    print(request.user)

    for a in artikel:
        print(a)
    
    context = {
        "title":"selamat datang",
        "kategori":kategori,
        "artikel":artikel,
        "top_berita": top_berita,
    }
    return render(request, template_name, context)

def detail(request, id):
    template_name = "landingpage/detail.html"
    try:
        artikel = ArtikelBlog.objects.get(id=id)
    except ArtikelBlog.DoesNotExist:
        return redirect(not_found)
    
    artikel_lainnya = ArtikelBlog.objects.all().exclude(id=id)

    
    context = {
        "title":"selamat datang",
        "artikel":artikel,
        "artikel_lainnya":artikel_lainnya,
    }
    return render(request, template_name, context)

def kategori_filter(request, nama_kategori):
    template_name = "landingpage/index.html"
    kategori = Kategori.objects.all()
    try:
        kategori_terpilih = Kategori.objects.get(nama=nama_kategori)
        artikel = ArtikelBlog.objects.filter(kategori=kategori_terpilih)
    except Kategori.DoesNotExist:
        artikel = []

    context = {
        "title": f"Kategori: {nama_kategori}",
        "kategori": kategori,
        "artikel": artikel,
    }
    return render(request, template_name, context)


def not_found(request):
    template_name = "not_found.html"
    return render(request, template_name)

def kontak(request):
    template_name = "kontak.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)

def galeri(request):
    template_name = "galeri.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)



def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/auth-login')
    
    template_name = "dashboard/index.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)

def artikel_list(request):
    template_name = "dashboard/artikel_list.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)

