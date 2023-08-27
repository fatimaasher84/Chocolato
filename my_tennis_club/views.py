#Create a view
from django.http import HttpResponse,HttpResponseRedirect

#To import templates 
from django.template import loader

#To render templates 
from django.shortcuts import render,redirect,get_object_or_404

#importing forms.py file class usersform
from .forms import usersForm

#from django.urls import reverse_lazy,reverse

import math

#import our model
from blogs.models import blogs
from news.models import news
from choco.models import choco
from gift.models import giftModel
from contact.models import contactEnquiry
from contact.models import newsletterModel

#To use paginator
from django.core.paginator import Paginator

#To send email
from django.core.mail import send_mail,EmailMultiAlternatives#This library is used to send html content in email

#make a function to create a view
def homePage(request):
    #To send html content in messsage of email
    """ subject="Testing mail"
    from_email="sherameerab@gmail.com"
    to_email="fatimaasher84@gmail.com"
    message="<p>Welcome to the <b>new website</b></p>"
    msg=EmailMultiAlternatives(subject,message,from_email,[to_email,asher.shera@gmail.com])
    msg.content_subtype='html'  #To show the content type
    msg.send() #To send email
    
    send_mail(
        "Testing Email",        #Subject
        "Here is the message.", #Message
        "sherameerab@gmail.com",    #From  
        ["fatimaasher84@gmail.com"],    #To
        fail_silently=False,
    )
    """
    #blog is a model name and objects is a class name(To fetch all data objects from model)
    newsData=news.objects.all()
    blogData=blogs.objects.all()
    bgData=blogs.objects.all().order_by('-id')[:3]#order is ascending without - and for descending we add - and to show only 3 records added we use [:3] 
    data={
        'title':'Chocolato',
        'bdata':'Welcome to Chocolato web store',
        'blogdata':blogData,
        'bgData':bgData,
        'newsData':newsData
    }
     #{% if numbers|length > 0 %}
      #  {% for n in numbers %}
       #     {% if n > 20 %}
        #        <div>{{n}}</div>
         #   {% endif %}
        #{% endfor %}
    #{% else %}
     #   No Data Found
    #{% endif %}
    #{% if numbers|length > 0 %}
     #   {% for n in numbers %}
        #    {% if n > 20 %}
         #       <div>{{n}}</div>
          #  {% endif % 
        #{% endfor %}
    #{% else %}
    #    No Data Found 
    #{% endif %}
    #} 
    return render(request,"index.html",data)

def newsDetail(request,slug):
    details=news.objects.get(news_slug=slug) #get is used to get single row from table
    data={
        'details':details
    }
    return render(request,"detail.html",data)

def blogDetails(request,slug):
    details=blogs.objects.get(blog_slug=slug) #get is used to get single row from table
    data={
        'details':details
    }
    return render(request,"blogDetails.html",data)

def chocodetails(request,slug):
    details=choco.objects.get(ch_slug=slug) #get is used to get single row from table
    data={
        'details':details
    }
    return render(request,"chocodetails.html",data)

def giftdetails(request,slug):
    gdetails=giftModel.objects.get(gt_slug=slug) #get is used to get single row from table
    data={
        'gdetails':gdetails
    }
    return render(request,"giftdetails.html",data)

#About us page
def aboutus(request):#request parameter is used when we need a value from some form
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"about.html",{'output':output})
         
#Chocolate page
def chocolates(request):#request parameter is used when we need a value from some form
    chocolateData=choco.objects.all().order_by('-id')
    if request.method=="GET":
        st=request.GET.get('chocolatename')
        if st !=None:
            chocolateData=choco.objects.filter(ch_title__icontains=st) #__icontains means we can search with one letter also
    paginator=Paginator(chocolateData,3)
    page_number=request.GET.get('page')
    chocolateDataFinal=paginator.get_page(page_number)
    totalpage=chocolateDataFinal.paginator.num_pages
    """ if request.method=="GET": 
        chocolatet=request.GET.get('chocolatename')
        if chocolatet!=None:
            chocolateData=blog.objects.filter(blog_title__icontains=chocolatet)
 """    
    data={
        'chocolateData':chocolateDataFinal,
        'lastpage':totalpage,
        'totalPageList':[n+1 for n in range(totalpage)]
    }
    return render(request,"chocolates.html",data)

#Blog Page
def blg(request):#request parameter is used when we need a value from some form
    blogData=blogs.objects.all().order_by('-blog_date')
    paginator=Paginator(blogData,3)
    page_number=request.GET.get('page')
    blogDataFinal=paginator.get_page(page_number)
    totalpage=blogDataFinal.paginator.num_pages
    data={
        'blogData':blogDataFinal,
        'lastpage':totalpage,
        'totalPageList':[n+1 for n in range(totalpage)]
    }
    return render(request,"blg.html",data)


#Gift page
def gift(request):
    giftData=giftModel.objects.all().order_by('-id')
    paginator=Paginator(giftData,3)
    page_number=request.GET.get('page')
    giftDataFinal=paginator.get_page(page_number)
    totalpage=giftDataFinal.paginator.num_pages
    data3={
        'giftData':giftDataFinal,
        'lastpage':totalpage,
        'totalPageList':[n+1 for n in range(totalpage)]
    }
    return render(request,"gift.html",data3)

#trade page
def trade(request):
    data3={
        'title':'Chocolato Gift Items',
        'bdata':'Gift Items'
    }
    return render(request,"trade.html",data3)

#delivery page
def delivery(request):
    data3={
        'title':'Chocolato Gift Items',
        'bdata':'Gift Items'
    }
    return render(request,"delivery.html",data3)

""" def LikeView(request,pk):
    post=get_object_or_404(blogs,id=request.POST.get('post_id'))
    #add one like in blog_likes field in blogs model with the Dummyuser name to show who liked the post
    post.blog_likes.add(request.DummyUser)
    return HttpResponseRedirect(reverse('blogDetails',args=[str(pk)]))
 """
#Shop page
def shop(request):
    data3={
        'title':'Chocolato Gift Items',
        'bdata':'Gift Items'
    }
    return render(request,"shop.html",data3)

#newsletter
def newsletter(request):
    msg=""
    if request.method=='POST':
        email=request.POST.get('newsltr')
        print(email)
        en1=newsletterModel(newsEmail=email)
        try:
            en1.save()
            msg='Your email address has been added on our newsletter list.'
        except Exception as e:
            msg= 'Error:'+str(e)
            
    return render(request,"newsletter.html",{'msg':msg})

 #Contact Us page
def contact(request):
    n=""
    if request.method=='POST':
        namec=request.POST.get('contactName')
        emailc=request.POST.get('contactEmail')
        phonec=request.POST.get('contactPhone')
        messagec=request.POST.get('contactMessage')
        en=contactEnquiry(name=namec,email=emailc,phone=phonec,message=messagec)

        try:
            en.save() #save values get from model
            n='Email has been sent successfully'
        except Exception as e:
            n='Error:Data not inserted - '+ str(e)
    return render(request,"contact.html",{'n':n})
    






def userform(request):
    finalans=0
    fn=usersForm()
    data={'form':fn}
    try:
        if request.method == "POST":
        #first=int(request.GET['first'])
        #last=int(request.GET['last'])
        #Second way to use it
            first=int(request.POST.get('first'))
            last=int(request.POST.get('last'))
            finalans=first+last
            data={
                'form':fn,
                'output':finalans
            }
            url="/about/?output={}".format(finalans)
            return redirect(url)
    except:
        pass
    return render(request,"userform.html",data)

def submitform(request):
    try:
        if request.method == "POST":
            first=int(request.POST.get('first'))
            last=int(request.POST.get('last'))
            finalans=first+last
            return HttpResponse(finalans)
    except:
        pass
    
def calculator(request):
    final=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))#eval works for both int and float
            n2=eval(request.POST.get('num2'))   
            opr=request.POST.get('opr')
            if opr=="+":
                final=n1+n2
            elif opr=="-":
                final=n1-n2
            elif opr=="*":
                final=n1*n2
            elif opr=="/":
                final=n1/n2
    except:
        final="Invalid Operator"
    print(final)
        
    return render(request,"calculator.html",{'final':final})

def saveevenodd(request):
    final=''
    try:
        if request.method=="POST":
            if request.POST.get('num1')=="":
                return render(request,"evenodd.html",{'error':True})            
            n1=eval(request.POST.get('num1'))
            if n1%2==0:
                final="Even Number"
            else:
                final="Odd Number"

    except:
        final="Invalid Input"

    return render(request,"evenodd.html",{'final':final})

def marksheet(request):
    data={}
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            n3=eval(request.POST.get('num3'))
            n4=eval(request.POST.get('num4'))
            n5=eval(request.POST.get('num5'))
            total=n1+n2+n3+n4+n5
            per=math.ceil(total*100/500)
            if per>=60:
                divi="First Division"
            elif per>=50:
                divi="Second Division"
            elif per>=40:
                divi="Third Division"
            else:
                divi="Fail"
            data={
                'total':total,
                'per':per,
                'divi':divi
            }
                    
    except:
        final="Invalid Input"
    return render(request,"marksheet.html",data)