from django.shortcuts import render
from numpy import *
# Create your views here.
def index(req):
    return render(req,'index.html',{})
def caldiff(req):
    if req.method == 'POST':
        try : 
            d = req.POST
            eq = d['eq']
            n = int(d['nh'])
            h = 10**(-n)
            x = float(d['x'])
            data = []
            data.append(['Differentiation'])
            data.append(['Equation : f(x) = ',eq])
            data.append(['x = ',x])
            data.append(['h = ',h])
            # print(eval(eq),x,h)
            data.append(['1CDA = ',firstCDA(eq,x,h)])
            data.append(['2CDA = ',secondCDA(eq,x,h)])
            data.append(['3CDA = ',thirdCDA(eq,x,h)])
            data.append(['4CDA = ',fourthCDA(eq,x,h)])
            return render(req,'result.html',{'show':data})
        except:
            data = []
            data.append(['Differentiation'])
            data.append(['Equation : f(x) = ',eq])
            data.append(['x = ',x])
            data.append(['h = ',h])
            data.append(['บางอย่างผิดพลาด ไม่สามารถคำนวณได้'])
            return render(req,'result.html',{'show':data})

    else:
        return render(req,'result.html',{})
def calin(req):
    if req.method == 'POST':
        try : 
            d = req.POST
            eq = d['eq']
            n = int(d['n'])
            a = float(d['a'])
            b = float(d['b'])
            data = []
            data.append(['Integration'])
            data.append(['Equation : f(x) = ',eq])
            data.append(['a = ',a])
            data.append(['b = ',b])
            data.append(['n = ',n])
            if a > b : b,a = a,b 
            data.append(['Trapezoidal rule = ',trapezoid(eq,a,b,n)])
            data.append(["Simpson's rule = ",firstsimpson(eq,a,b,n)])
            return render(req,'result.html',{'show':data})
        except:
            data = []
            data.append(['Integration'])
            data.append(['Equation : f(x) = ',eq])
            data.append(['a = ',a])
            data.append(['b = ',b])
            data.append(['n = ',n])
            data.append(['บางอย่างผิดพลาด ไม่สามารถคำนวณได้'])
            return render(req,'result.html',{'show':data})

    else:
        return render(req,'result.html',{})
def froot1(req):
    if req.method == 'POST':
        try : 
            d = req.POST
            eq = d['eq']
            a = float(d['a'])
            b = float(d['b'])
            pe = float(d['pe'])
            epsilon = 10**(-pe)
            ps = float(d['ps'])
            step = 10**(-ps)
            data = []
            data.append(['Root-finding : ','Incremental Search Method'])
            data.append(['Equation : f(x) = ',eq])
            data.append(['a = ',a])
            data.append(['b = ',b])
            data.append(['epsilon = ',epsilon])
            data.append(['step = ',step])
            if a > b : b,a = a,b 
            data.append(["Incremental Search Method = ",incsearch(eq,a,b,epsilon,step)])
            return render(req,'result.html',{'show':data})
        except:
            data = []
            data.append(['Root-finding : ','Incremental Search Method'])
            data.append(['Equation : f(x) = ',eq])
            data.append(['a = ',a])
            data.append(['b = ',b])
            data.append(['epsilon = ',epsilon])
            data.append(['step = ',step])
            data.append(['บางอย่างผิดพลาด ไม่สามารถคำนวณได้'])
            return render(req,'result.html',{'show':data})

    else:
        return render(req,'result.html',{})
def froot2(req):
    if req.method == 'POST':
        try : 
            d = req.POST
            eq = d['eq']
            x = float(d['x'])
            n = int(d['n'])
            data = []
            data.append(['Root-finding : ','newtonraphson,secant'])
            data.append(['Equation : f(x) = ',eq])
            data.append(['x = ',x])
            data.append(['n = ',n])
            data.append(['newtonraphson = ',newtonraphson(eq,x,n)])
            data.append(["secant = ",secant(eq,x,n)])
            return render(req,'result.html',{'show':data})
        except:
            data = []
            data.append(['Root-finding : ','newtonraphson,secant'])
            data.append(['Equation : f(x) = ',eq])
            data.append(['x = ',x])
            data.append(['n = ',n])
            data.append(['บางอย่างผิดพลาด ไม่สามารถคำนวณได้'])
            return render(req,'result.html',{'show':data})

    else:
        return render(req,'result.html',{})
def tof(sf,x):
    return eval(sf)

def firstCDA(sf,x,h):
    return (tof(sf,x+h) - tof(sf,x-h))/(2*h)
def secondCDA(f,x,h):
    return (tof(f,x+h)-2*tof(f,x)+tof(f,x-h))/(h**2)
def thirdCDA(f,x,h):
    return (tof(f,x+2*h)-2*tof(f,x+h)+2*tof(f,x-h)-tof(f,x-2*h))/(2*h**3)
def fourthCDA(f,x,h):
    return ( tof(f,x+2*h) -4*tof(f,x+h) +6*tof(f,x) -4*tof(f,x-h) + tof(f,x-2*h)  )/(h**4)

def trapezoid(f,a, b, n):
    l = (b-a)/n
    r = (tof(f,a) + tof(f,b))/2
    for i in range(1,n) : r += tof(f,a+i*l)
    return r*l
def incsearch(eq, a, b, epsilon=10**-3, step=10**-3):
    while a<b:
        if abs(firstCDA(eq,a,10**(-5))) < epsilon :
            print(a)
            break
        a+=step
    return a if a<b else None

def firstsimpson(f, a, b, n):
    h = (b-a)/n
    x0 = a # x_i = x_0 + i*h
    #tof(f,x0) + 4*tof(f,x1) + 2*tof(f,x2) + .... + 4*tof(f,x_n-1) + tof(f,x_n)
    s = tof(f,x0)

    # odd - x1, x3, x5, ...
    #s += 4*tof(f,x1) + 4*tof(f,x3) + 4*tof(f,x5) + ...
    for i in range(1,n,2):
        s += 4*tof(f,x0+i*h)

    # even - x2, x4, x6, ...
    #s += 2*tof(f,x2) + 2*tof(f,x4) + 2*tof(f,x6) + ...
    for i in range(2,n-1,2):
        s += 2*tof(f,x0+i*h)

    s += tof(f,b)
    return s*h/3
def newtonraphson(f,  x=-1, n=20):
    for i in range(n):
        deltaX = -tof(f,x)/firstCDA(f,x,10**(-5))
        x += deltaX
    return x
def secant(f, x=-1, n=20, h=0.00001):
    xo = x
    xn = x + h
    for i in range(n):
        q = (tof(f,xo) - tof(f,xn))/(xo-xn)
        xo = xn
        xn += -(tof(f,xn)/q)
    return xn

