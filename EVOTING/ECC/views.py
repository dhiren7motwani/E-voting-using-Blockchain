from django.shortcuts import render,redirect,render_to_response
from .models import ECC
# Create your views here.
def index(request):
    e_id= request.COOKIES.get('eid')
    epass=request.COOKIES.get('epass')
    if (e_id is None or epass is None):
            return redirect('http://127.0.0.1:8000/ECC/login')
    else:
            return render(request,'ECC/index.html')


def profile(request):
    ecc_id= request.COOKIES.get('eid')
    epassword=request.COOKIES.get('epass')
    if (ecc_id is None or epassword is None):
            return redirect('http://127.0.0.1:8000/ECC/login')
    else:
            b=ECC.objects.filter(employee_id=ecc_id).values_list('first_name','last_name','gender','pan_id','employee_id','phone_number')
            a=b[0]
            return render(request,'ECC/profile.html',{'fn':a[0],'ln':a[1],'gender':a[2],'pan_id':a[3],'employee_id':a[4],'phone_number':a[5]})

def login(request):
    data = 'INVALID LOGIN'
    if(request.method=='POST'):
        e_id= request.POST['e_id']
        psw=request.POST['e_pass']
        epass=ECC.objects.filter(employee_id=e_id).values_list('password',flat='True')
        a = epass[0]
        past =str(a)
        if(psw==past ):
            response= render_to_response('ECC/index.html')
            response.set_cookie('eid',e_id)
            response.set_cookie('epass',psw)
            response.set_cookie('epass',psw)

        return response
    else:
            return render(request,'ECC/login.html')
