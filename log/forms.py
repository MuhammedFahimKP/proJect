from django import forms
from .models import Addresses,MyUser



class AddressCreationForm(forms.ModelForm):


    class Meta:
        model  = Addresses
        fields = ['city','state','landmark','place','pin_code','phone_no','alter_phone_no']


    


    def __init__(self,*args, **kwargs):
        super(AddressCreationForm,self).__init__(*args,**kwargs)

        placeholders = {
            'city':'City',
            'state':'State',
            'place' : 'Place',
            'landmark':'Landmark',
            'pin_code':'Pincode',
            'phone_no':'Phone No',
            'alter_phone_no':'Alternate Phone No'
        }


        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder']=placeholders.get(field,'None')

    user = forms.ModelChoiceField(queryset=MyUser.objects.all(),required=False) 

