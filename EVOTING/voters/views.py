from django.shortcuts import render,render_to_response,redirect
from voters.models import Voters
from django.http import HttpResponse,JsonResponse
import requests
from flask import jsonify
# Create your views here.
def index(request):
    voters_id= request.COOKIES.get('id')
    password=request.COOKIES.get('password')
    if (voters_id is None or password is None):
            return redirect('http://127.0.0.1:8000/voters/login')
    else:
            response = requests.get('http://127.0.0.1:5000/count_a')
            a=15
            b=50
            c=10
            d=30
            e=60
            f=45
            return render(request,'voters/index.html',{'yVal':a,'yVal1':b,'yVal2':c,'yVal3':d,'yVal4':e,'yVal5':f})

def vote(request):
    voters_id= request.COOKIES.get('id')
    password=request.COOKIES.get('password')
    if (voters_id is None or password is None):
            return redirect('http://127.0.0.1:8000/voters/login')
    else:

        c=0
        if(request.method=='POST'):
            vot_id = request.COOKIES.get('id')
            consta = Voters.objects.filter(voter_id = voters_id).values('location')
            cand = request.POST['cid']
            cand = 1
            #response.set_cookie('cid',candidate_Id)
            fla = Voters.objects.filter(voter_id=voters_id).values('vote_flag')
            d= {}
            d['voter_id']=vot_id
            d['constituency']=consta
            d['candidate_Id']=cand
            data2={"voter_id": "vot_id",
                    "constituency": "consta",
                    "candidate_Id": "cand",
                    "flag" : "3"}
            #a=json.dumps(data2)
            #r=json.loads(a)
            #data2= JsonConvert.SerializeObject( data2 );

            otp=1
            otpm=1
            while(c<3):
                if(otp==otpm):
                    response2=requests.post(url='http://127.0.0.1:5000/add_transaction',data=d)
                    response=requests.get('http://127.0.0.1:5000/mine_block')
                    response2=render_to_response('voters/index.html')
                    return response2
                else:
                    c=c+1
                    #message

        else:
    #    response = requests.get('http://127.0.0.1:5000/mine_block')
    #    geodata = response.json()
            return render(request,'voters/vote.html')

def Login(request):
    data = 'INVALID LOGIN'
    if(request.method=='POST'):
        usersid= request.POST['first_name']
        psw=request.POST['password']
        try:
            passd=Voters.objects.filter(voter_id=usersid).values_list('password',flat='True')
            a = passd[0]
            past =str(a)
            if(psw==past ):
                response= render_to_response('voters/index.html')
                response.set_cookie('id',usersid)
                response.set_cookie('password',psw)
                return response
            else:
                return render(request,'voters/signup.html')

        except:
            return render(request,'voters/Login.html')
    else:
        return render(request,'voters/Login.html')
def Profile(request):
    voters_id= request.COOKIES.get('id')
    password=request.COOKIES.get('password')
    if (voters_id is None or password is None):
            return redirect('http://127.0.0.1:8000/voters/login')
    else:
            b=Voters.objects.filter(voter_id=voters_id).values_list('first_name','last_name','Age','voter_id','gender','pan_id','phone_number','location')
            a=b[0]
            return render(request,'voters/profile.html',{'fn':a[0],'ln':a[1],'age':a[2],'voter_id':a[3],'gender':a[4],'pan_id':a[5],'phone_number':a[6],'location':a[7]})

def signup(request):
    if(request.method=='POST'):
        Fname = request.POST['fname']
        Lname = request.POST['lname']
        Gender = request.POST['gender']
        m_no = request.POST['m_no']
        Age = request.POST['age']
        Location = request.POST['loc']
        v_id = request.POST['vid']
        pan = request.POST['pid']
        psw = request.POST['psw']
        T = Voters(first_name=Fname,last_name=Lname,voter_id=v_id,Age=Age,pan_id=pan,gender=Gender,password=psw,location=Location,phone_number=m_no,vote_flag=True)
        T.save()
        response=render_to_response('voters/index.html')
        response.set_cookie('id',v_id)
        response.set_cookie('password',psw)
        return response
    else:
        return render(request,'voters/signup.html')
