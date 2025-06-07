from django.shortcuts import render
from . import forms
# Create your views here.
def userregistration(request):
    form=forms.ExampleForm()
    if request.method=='POST':
        form=forms.ExampleForm(request.POST)
        if form.is_valid():
            print("Username:",form.cleaned_data['username'])
            print("password:",form.cleaned_data['password'])
            
    return render(request,'userregistration.html',{'form':form})
# Create your views here.
