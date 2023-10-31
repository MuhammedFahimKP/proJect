from django import forms

from shop.models import Product


class ProductCreationForm(forms.ModelForm):

        class Meta:
         model = Product
         fields = [
             'name', 'slug', 'Brand', 'price', 'stocks', 'img', 'Category','is_available','discrption',
        ]
        
        def __init__(self, *args, **kwargs):
            super(ProductCreationForm,self).__init__(*args, **kwargs)
            self.fields['price'].widget.attrs['min'] = 0
            self.fields['stocks'].widget.attrs['min'] = 0
            for field  in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'
                self.fields[field].widget.attrs['placeholder']=field.capitalize()

            self.fields['is_available'].widget.attrs['type'] = 'checkbox'            
            self.fields['is_available'].widget.attrs['class'] = 'form-check-input'
            self.fields['slug'].widget.attrs['id']='slug'
            self.fields['name'].widget.attrs['id']='prd_name'
            self.fields['img'].widget.attrs['onchange']="showPreview(event);"
            


        def clean(self):
            cleaned_data = super(ProductCreationForm, self).clean()
            price = cleaned_data.get('price')
            stocks = cleaned_data.get('stocks')

            if price < 0:
                self.add_error('price', 'Price must be a non-negative number.')

            if stocks < 0:
                self.add_error('stocks', 'Stocks must be a non-negative number.')

            return cleaned_data     