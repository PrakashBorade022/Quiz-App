from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from .models import Questions
from .forms import QuestionsModelForm
from django.core.paginator import Paginator

def home(request):
    return render(request,'home.html')
    
    
    # print("hello this is printing")
    # var = [1,2,3,4]
    # dict_one = {'bar':var}
    # return render(request,'home.html',dict_one)

def questions(req):
    questions_list =  Questions.objects.all().order_by('qno')
    paginator = Paginator(questions_list,1)
    
    try:
        page = int(req.GET.get('page','1'))
       
    except:
        page =1
    try:
        questions = paginator.page(page)
    except(EmptyPage,InvalidPage):
        questions=paginator.page(paginator.num_pages)

    # print(questions)


    # // this shows an add question form
    # addQue = QuestionsModelForm()


    return render(req,'questions.html',{'questions':questions})
def getValues(req):
    return render (req,'getValues.html')














    # ------------------- second -------------------
    # score =0
    # if req.method =="POST":
        
        
        
    #     try:

    #         q1 = str(req.POST['q1'])
    #         q2= req.POST['q2']
    #         if q1 == 'true':
    #             score +=1
    #         if q2 == 'true':
    #             score +=1
              
    #         return render(req,'getValues.html',{'score':score,'q1':q1,'q2':q2})
    #     except MultiValueDictKeyError:
    #         error ="please select all quiesions"
    #         return render(req,'getValues.html',{'error':error,'score':score})
            
       
    # return render(req,'getValues.html',{'score':score})
    
# ----------------------------------   first   -------------------------------
    # if req.method=='POST':
    
        # try:
        #     country = req.POST['country']
        # except MultiValueDictKeyError:
        #     country = "No country selected"    


         
        # return render(req,{'country':country})
    # return render(req,'getValues.html',{'country':country})
        
        # name = req.POST['name']
        # country = req.POST['country']
        # args = {'country':country}
        
        # if req.POST['country']== None:
        #     print("noting seleetd")
        # print(country)
        
       

    