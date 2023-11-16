from django import forms
from .models import Review,Product
from log.models import MyUser


class ProductReviewForm(forms.ModelForm):



    def __init__(self,*args,**kwargs):

        super(ProductReviewForm,self).__init__(*args, **kwargs)    



        for field in self.fields:

            self.fields[field].widget.attrs['class']       = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = field.capitalize()

       
    class Meta:
        model = Review
        fields = ['subject','review']


    user    = forms.ModelChoiceField(queryset=MyUser.objects.all(),required=False)    
    product = forms.ModelChoiceField(queryset=Product.objects.all(),required=False)



