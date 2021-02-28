from django.shortcuts import render
from .models import Qustions

# Create your views here.

def mcqs_list(request):
    context = {'qustion_topic_list':Qustions.objects.values('qestion_topic','qestion_id').distinct()}
    return render(request,"MCQsSampleApp/index.html",context)

def question_list(request,qestion_id):
    args = {}
    args['mytext'] = qestion_id
    return render(request,"MCQsSampleApp/startquzz.html",args)

def question_details(request):
    qestion_id=request.POST['qestion_id']
    qestion_no=request.POST['qestion_no']
    qestion_no = int(qestion_no)
    if qestion_no>2:
        return render(request,"MCQsSampleApp/showresult.html")
    else:
        qestion_next = qestion_no+1
        qestion_no = str(qestion_no)
        context = {'qustion_list':Qustions.objects.filter(qestion_id=qestion_id,qestion_no=qestion_no),
                    'mytext': qestion_next}
        return render(request,"MCQsSampleApp/showquestions.html",context)