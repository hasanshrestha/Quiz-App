import re
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from quizApp.form import AdminLoginForm, QuestionForm, UserForm, UserLoginForm
from quizApp.models import AdminLogin, Question, User
from django.core.mail import send_mail 
from django.conf import settings
# Create your views here.

#user index
def index(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, "userIndex.html", {'username':username})
    else:
        return render(request, "login.html")

#admin index
def adminIndex(request):
    return render(request, "index.html")

def adminLogin(request):
    adminLoginForm = AdminLoginForm()
    userLoginForm = UserLoginForm()
    return render(request, "login.html", {'form':adminLoginForm, 'userform':userLoginForm})

# def adminLoginPost(request):
#     adminLoginForm = AdminLoginForm()

#     username = request.POST.get('username')
#     password = request.POST.get('password')

#     try:
#         user = AdminLogin.objects.get(username = username)
#         if(password == user.password):
#             request.session['username'] = username
#             return render(request, "index.html", {'username':username})
#         else:
#             msg="Invalid Password"
#             return render(request, "login.html", {'form':adminLoginForm, 'msg': msg})
#     except:
#         msg = "Username Invalid!!!!"
#         return render(request, "login.html", {'form':adminLoginForm,'msg': msg})

def PostAdminLogin(request):
    userLoginForm = UserLoginForm()
    adminLoginForm = AdminLoginForm()

    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
     user = AdminLogin.objects.get(username = username)
     if(password == user.password):
         request.session['username'] = username
         return render(request, "index.html", {'username':username})
     else:
        msg="Invalid Password"
        return render(request, "login.html", {'form':adminLoginForm, 'userform':userLoginForm, 'msg': msg})
    except:
         msg = "Username Invalid!!!!"
         return render(request, "login.html", {'form':adminLoginForm,'msg': msg, 'userform':userLoginForm})

#admin questions crud
def createQuestions(request):
    createform = QuestionForm()
    return render(request, "createquestion.html", {'form': createform})

def addQuestions(request):
    createform = QuestionForm()
    try:
        question = request.POST.get('question')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        correctAns = request.POST.get('correctAns')

        ques = Question(question = question, option1 = option1, option2 = option2, option3 = option3, option4 = option4, \
            correctAns = correctAns)
        ques.save()

        msg = "Question Added Succesfully!!"
        return render(request, "createquestion.html", {'form': createform, 'msg' : msg})
    except:
        msg = "Error Occured!!"
        return render(request, "createquestion.html", {'form': createform, 'msg' : msg})

def showQuestions(request):
    ques = Question.objects.all()
    return render(request, "show.html", {'quesList': ques})

def editQuestion(request, qid):
    edit_ques = Question.objects.get(id = qid)
    return render(request, 'edit.html', {"data": edit_ques})

def updateQuestion(request):
    qid = request.POST.get('id')
    try:
        # data fetch by id
        que = Question.objects.get(id=qid)
        que.question = request.POST.get('question')
        que.option1 = request.POST.get('option1')
        que.option2 = request.POST.get('option2')
        que.option3 = request.POST.get('option3')
        que.option4 = request.POST.get('option4')
        que.correctAns = request.POST.get('correctAns')
        que.save()
        msg = "Successfully updated"
        question_all = Question.objects.all()
        return render(request, 'show.html', {'quesList': question_all, 'msg': msg})
    except:
        msg = "Error Cannot Edit"
        edit_ques = Question.objects.get(id = qid)
        return render(request, 'edit.html', {'data': edit_ques, 'msg': msg})

def deleteQuestion(request, qid):
    que = Question.objects.get(id=qid)
    que.delete()
    un = Question.objects.all()
    return render(request, 'show.html', {'quesList':un, 'msg':"Deleted Successfully"})

#users
def register(request):
    reg_form = UserForm()
    return render(request, "register.html", {'form': reg_form})

def userRegister(request):
    reg_form = UserForm()
    try:
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg = "User Registered Successfully!!"
            return render(request, "register.html", {'form': reg_form, 'msg': msg})
        else:
            msg = "Invalid Form!!"
            return render(request, "register.html", {'form': reg_form, 'msg': msg})
    except:
        msg = "Error. Cannot Register User!!!"
        return render(request, "register.html", {'form': reg_form, 'msg': msg})

def userLogin(request):
    username = request.POST.get('username_user')
    password = request.POST.get('password_user')

    userLoginForm = UserLoginForm()
    adminLoginForm = AdminLoginForm()

    try:
        user = User.objects.get(username_user = username)
        if(password == user.password_user):
            request.session['username'] = username
            request.session['id'] = user.id
            request.session['email'] = user.email
            return render(request, "userIndex.html", {'username':username})
        else:
            msg="Invalid Password"
            return render(request, "login.html", {'userform':userLoginForm,'usermsg': msg, 'form':adminLoginForm})
    except:
        msg = "Username Invalid!!!!"
        return render(request, "login.html", {'userform':userLoginForm,'usermsg': msg, 'form':adminLoginForm})

def userProfile(request):
    userLoginForm = UserLoginForm()
    adminLoginForm = AdminLoginForm()

    if request.session.has_key('username'):
        username = request.session['username']
        if request.session['username'] is not None:

            #username = request.session['username']
            userid = request.session['id']
            #try:
            userDetails = User.objects.get(id=userid)
            return render(request, "userProfile.html", {'data':userDetails, 'username':username, 'username':username})
        # except:
        #     return render(request, "userIndex.html")
        else:
            return render(request, "login.html", {'userform':userLoginForm, 'form':adminLoginForm})
    else:
        return render(request, "login.html", {'userform':userLoginForm, 'form':adminLoginForm})

def takeTest(request):
    userLoginForm = UserLoginForm()
    adminLoginForm = AdminLoginForm()
    if request.session.has_key('username'):
        username = request.session['username']
        test = Question.objects.all()
        return render(request, "quiz.html", {'test': test, 'username':username})
    else:
        return render(request, "login.html", {'userform':userLoginForm, 'form':adminLoginForm})
    
#send email
def sendemail(request):
    if request.method == "GET":
        marks = request.GET.get('marks', None)
        receiver =  request.session['email']
        send_mail(
            subject = 'Quiz Result',
            message = 'You got '+ marks +' marks in the recent test you have taken',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [receiver],
            fail_silently = False,
            # fail_silently takes boolean value. If set False it will raise smtplib.STMPException if the error
            # occurs while sending the email
        )
        return JsonResponse({"success": "Success"}, status=200)
    else:
        return JsonResponse({"error": "form.errors"}, status=400)

def logout(request):
    userLoginForm = UserLoginForm()
    adminLoginForm = AdminLoginForm()
    if request.session.has_key('username'):
        del request.session['username']
        return render(request, "login.html", {'userform':userLoginForm, 'form':adminLoginForm})

#admin dashboard
def getUsersCount(request):
    try:
        usersCount = User.objects.all().count()
        return JsonResponse({"data": usersCount}, status=200)
    except:
        return JsonResponse({"error": "Error"}, status=400)

def getQuestionCount(request):
    try:
        quesCount = Question.objects.all().count()
        return JsonResponse({"data": quesCount}, status=200)
    except:
        return JsonResponse({"error": "Error"}, status=400)

#admin logout
def adminlogout(request):
    userLoginForm = UserLoginForm()
    adminLoginForm = AdminLoginForm()
    if request.session.has_key('username'):
        del request.session['username']
        return render(request, "login.html", {'userform':userLoginForm, 'form':adminLoginForm})