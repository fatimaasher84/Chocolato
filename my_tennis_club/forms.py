from django import forms

#forms is the package and Form is a class of forms

class usersForm(forms.Form):
    #make a character field 
    first=forms.CharField(label="First Name",max_length=25,widget=forms.TextInput(attrs={'class':"form-control"}))#required is false means not necessary
    last=forms.CharField(label="Last Name",max_length=25,widget=forms.TextInput(attrs={'class':"form-control"}))
    description=forms.CharField(label="Description",max_length=250,required=False,widget=forms.Textarea(attrs={'class':"form-control"}))#widget will change type of field,attrs is the attribute field which specifies class
    email=forms.EmailField(label="Email:",max_length=25)
