from django.http import HttpResponse
from django.shortcuts import render

def motivation(request):
    return render(request,"motivation.html")

def result(request):

    lst = []
    score_m = 0
    lst.append(request.GET['q1'])
    lst.append(request.GET['q2'])
    lst.append(request.GET['q3'])
    lst.append(request.GET['q4'])
    lst.append(request.GET['q5'])
    lst.append(request.GET['q6'])
    lst.append(request.GET['q7'])
    lst.append(request.GET['q8'])
    lst.append(request.GET['q9'])
    lst.append(request.GET['q10'])
    lst.append(request.GET['q11'])
    lst.append(request.GET['q12'])
    lst.append(request.GET['q13'])
    lst.append(request.GET['q14'])
    lst.append(request.GET['q15'])
    lst.append(request.GET['q16'])
    lst.append(request.GET['q17'])
    lst.append(request.GET['q18'])
    lst.append(request.GET['q19'])
    lst.append(request.GET['q20'])
    lst.append(request.GET['q21'])
    lst.append(request.GET['q22'])
    lst.append(request.GET['q23'])
    lst.append(request.GET['q24'])
    lst.append(request.GET['q25'])
    lst.append(request.GET['q26'])
    lst.append(request.GET['q27'])
    lst.append(request.GET['q28'])
    lst.append(request.GET['q29'])
    lst.append(request.GET['q30'])
    lst.append(request.GET['q31'])
    lst.append(request.GET['q32'])
    lst.append(request.GET['q33'])
    lst.append(request.GET['q34'])
    lst.append(request.GET['q35'])
    lst.append(request.GET['q36'])
    lst.append(request.GET['q37'])
    lst.append(request.GET['q38'])
    lst.append(request.GET['q39'])
    lst.append(request.GET['q40'])
    lst.append(request.GET['q41'])
    lst.append(request.GET['q42'])
    lst.append(request.GET['q43'])
    lst.append(request.GET['q44'])
    
    for i in range(40):
        score_m = score_m + int(lst[i])

    if(score_m<=61):
        ans = 'Poor'
    elif(score_m<=122):
        ans = 'Satisfactory'
    elif(score_m<=183):
        ans = 'Good'
    elif(score_m<=244):
        ans = 'Very Good'
    else:
        ans = 'Excellent'

    return render(request,"result.html",{'ans':ans})