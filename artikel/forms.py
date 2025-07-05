from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from artikel.models import Kategori, ArtikelBlog

class KategoriForms(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ('nama',)
        widgets = {
            "nama" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required':True
                }
            ),
        }


        # widgets = {
        #     "ruang" : forms.Select(
        #         attrs={
        #             'class': 'form-control select2-ruangan',
        #             'type':'text',
        #             'data-style' : 'btn btn-danger btn-block',
        #             'title' : 'pilih kategori',
        #             'data-size' : '7',
        #         }
        #     ),
        #     "nama" : forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'cols':'30',
        #             'rows':'10',
        #             'required':True
        #         }
        #     ),
        #     "jumlah" : forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'cols':'30',
        #             'rows':'10',
        #             'required':True
        #         }
        #     ),
        #     "baik" : forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'cols':'30',
        #             'rows':'10',
        #             'required':True
        #         }
        #     ),
        #     "perbaikan" : forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'cols':'30',
        #             'rows':'10',
        #             'required':True
        #         }
        #     ),
        #     "musnah" : forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'cols':'30',
        #             'rows':'10',
        #             'required':True
        #         }
        #     ),
        # }

class ArtikelForms(forms.ModelForm):
    class Meta:
        model = ArtikelBlog
        fields = ('kategori', 'judul', 'konten', 'gambar', 'status')
        widgets = {
            "kategori" : forms.Select(
                attrs={
                    'class': 'form-control',
                    'required':True,
                }
            ),
            "judul" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required':True
                }
            ),
            "konten" : CKEditor5Widget(
                attrs=
                  {"class": "django_ckeditor_5"
                }, 
            )
          
            # "gambar" : forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'required':True
            #     }
            # ),
            # "status" : forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'required':True
            #     }
            # ),
        }