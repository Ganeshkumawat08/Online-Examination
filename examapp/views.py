from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

from .models import usermodel
from .forms import userform
from .models import coursemodel
from .forms import courseform
from .models import subjectmodel
from .forms import subjectform
from .models import papermodel
from .forms import paperform
from .models import resultcoursemodel
from .models import resultsubjectmodel

# Create your views here.

def home(request):
    courses=coursemodel.objects.all()
    subjects=subjectmodel.objects.all()
    return render(request,'index.html',{'courses':courses,'subjects':subjects})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

# User Function
def signup(request):
    if request.method == "POST":
        form = userform(request.POST)
        if form.is_valid():
            form.save()
            user=form.instance
            return redirect(f'/examapp/user/{user.id}')
    else:
       form = userform()
    return render(request, 'signup.html', {'form': form,'signup':'signup'})

def login(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        user=usermodel.objects.filter(userid=userid,password=password)
        if user:
            user=usermodel.objects.get(userid=userid)
            return redirect(f'/examapp/user/{user.id}')
        else:
            return render(request,'login.html',{'userid':userid,'error':'Userid or password is not match'})
    else:      
        return render(request,'login.html')

def user(request,id):
    user=usermodel.objects.get(id=id)
    if user.status:
        courses=coursemodel.objects.all()
        subjects=subjectmodel.objects.all()
        return render(request,'user.html',{'user':user,'courses':courses,'subjects':subjects})
    else:
        courses=coursemodel.objects.all()
        subjects=subjectmodel.objects.all()
        return render(request,'user.html',{'user':user,'courses':courses,'subjects':subjects})

def updateuser(request, id):
    user = get_object_or_404(usermodel, id=id)
    if request.method == "POST":
        form = userform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(f"/examapp/user/{user.id}")
    else:
        form = userform(instance=user)
    return render(request, "signup.html", {"form": form,'update':'updateuser',"user":user})




def adminlogin(request):
    if request.method == "POST":
        name = request.POST.get('admin')
        password = request.POST.get('password')
        if name == 'ganesh' and password=='@':
            return redirect(f'/examapp/admin/101')
        else:
            return render(request,'adminlogin.html',{'admin':name})
    else:      
        return render(request,'adminlogin.html')

def admin(request,id):
    if id==101:
        return render(request,'admin.html')
    else:
        return HttpResponse('Invalid Request')
    
def viewusers(request):
    users=usermodel.objects.all()
    return render(request,'viewuser.html',{'users':users})



# Courses
def courses(request):
    courses=coursemodel.objects.all()
    return render(request, 'course.html', {'courses':courses})
    
def addcourse(request):
    if request.method == "POST":
        form = courseform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/examapp/courses')
    else:
       form = courseform()
    return render(request, 'course.html', {'form': form,'add':'add'})

def editcourse(request, id):
    course = get_object_or_404(coursemodel, id=id) 
    if request.method == "POST":
        form = courseform(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect("/examapp/courses")
    else:
        form = courseform(instance=course)
    
    return render(request, "course.html", {"form": form, "course": course.id,'edit':'edit'})

# Subjects
def subjects(request):
    subjects=subjectmodel.objects.all()
    return render(request, 'subject.html', {'subjects':subjects})

def addsubject(request):
    if request.method == "POST":
        form = subjectform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/examapp/subjects')
    else:
       form = subjectform()
    return render(request, 'subject.html', {'form': form,'add':'add'})

def editsubject(request, id):
    subject = get_object_or_404(subjectmodel, id=id)
    
    if request.method == "POST":
        form = subjectform(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect("/examapp/subjects")
    else:
        form = subjectform(instance=subject)
    return render(request, "subject.html", {"form": form, "subject": subject.id,'edit':'edit'})


#Papers
def paper(request):
    papers=papermodel.objects.all().order_by('subject')
    questions={}
    for paper in papers:
        if paper.subject not in questions:
            questions[paper.subject] = []
        questions[paper.subject].append(paper)
    return render(request, 'paper.html', {'questions':questions})
  
def addpaper(request):
    if request.method == "POST":
        form = paperform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/examapp/paper')
    else:
       form = paperform()
    return render(request, 'paper.html', {'form': form,'add':'add'})

def editpaper(request, id):
    paper = get_object_or_404(papermodel, id=id)
    
    if request.method == "POST":
        form = paperform(request.POST, instance=paper)
        if form.is_valid():
            form.save()
            return redirect("/examapp/paper")
    else:
        form = paperform(instance=paper)
    return render(request, 'paper.html', {'form': form,'edit':'edit','paper':paper.id})
    
def subjectpaper(request, id):
    papers = papermodel.objects.filter(subject_id=id) if id else []
    subject=subjectmodel.objects.get(id=id)
    questions = {subject.name: list(papers)}
    return render(request, 'paper.html', {'questions': questions})

def delete(request,modelname,id):
    models={
        'subjects':subjectmodel,
        'courses':coursemodel,
        'paper':papermodel,
    }
    model=models.get(modelname)
    obj=get_object_or_404(model,id=id)
    obj.delete()
    return redirect(f"/examapp/{modelname}")

def checkuser(request,id):
    user=usermodel.objects.get(id=id)
    if user.status:
        user.status=False
    else:
        user.status=True
    user.save()
    return redirect('/examapp/viewusers')

def examcourse(request,cid,id):
    course = get_object_or_404(coursemodel, id=cid)
    user = get_object_or_404(usermodel, id=id)
    subjects=[]
    for subject in course.subjects.all():
        subjects.append(subject)

    totalque=[]
    for x in range(len(subjects)):
        available_questions = papermodel.objects.filter(subject=subjects[x]).values_list('id', flat=True)
        totalque.append(len(available_questions))
    
    return render(request,'examcourse.html',{'user':user,'course':course,'subjects':subjects,'totalque':totalque})


def examsubject(request,sid,id):
    subject = get_object_or_404(subjectmodel, id=sid)
    stu=usermodel.objects.get(id=id)
    totalque=len(papermodel.objects.filter(subject=subject).values_list('id', flat=True))
    return render(request,'examsubject.html',{'user':stu,'subject':subject,'totalque':totalque})

def question(request,subject,id):
    try:
        subject_obj = subjectmodel.objects.get(name=subject) 
    except subjectmodel.DoesNotExist:
        subject_obj = None  

    available_questions = papermodel.objects.filter(subject=subject_obj).values_list('id', flat=True)

    if not available_questions:
        return HttpResponse('NO Question')
    
    while id not in available_questions:
        id += 1

    question = papermodel.objects.get(id=id, subject=subject_obj)

    return render(request, 'exampaper.html', {'question': question})

def resultcourse(request,id):
    if request.method=="POST":
        user=usermodel.objects.get(id=id)
        course = request.POST.get('course')
        subjects = request.POST.get('subjects')  
        questions = request.POST.get('questions')
        totalmarks = request.POST.get('totalmarks')
        percentage = request.POST.get('percentage')
        result = request.POST.get('result')
        resultcoursemodel.objects.create( user=user, course=course, subjects=subjects,marks=totalmarks,questions=questions,percentage=percentage,result=result)
        return redirect(f'/examapp/user/{user.id}')
    else:
        user=usermodel.objects.get(id=id)
        return render(request,'resultsave.html',{'user':user,'course':'course'})

def resultsubject(request,id):
    if request.method=="POST":
        user=usermodel.objects.get(id=id)
        subject = request.POST.get('subject')  
        marks = request.POST.get('marks')
        questions = request.POST.get('questions')
        percentage = request.POST.get('percentage')
        result = request.POST.get('result')
        resultsubjectmodel.objects.create( user=user,subject=subject, marks=marks,questions=questions,percentage=percentage,result=result)
        return redirect(f'/examapp/user/{user.id}')
    else:
        user=usermodel.objects.get(id=id)
        return render(request,'resultsave.html',{'user':user,'subject':'subject'})

def examresult(request,id):
    user=usermodel.objects.get(id=id)  
    courseresult = resultcoursemodel.objects.filter(user_id=id)
    subjectresult = resultsubjectmodel.objects.filter(user_id=id)
    # raw_subjects = courseresult.subjects
    # courseresult.subject_list = [s for s in raw_subjects.split(',') if not s.strip().isdigit() and s.strip()]
    return render(request,'examresult.html',{'user':user,'courseresult':courseresult,'subjectresult':subjectresult})

def results(request):
    course=resultcoursemodel.objects.all()
    subject=resultsubjectmodel.objects.all()
    return render(request,'results.html',{'courseresult':course,'subjectresult':subject})

