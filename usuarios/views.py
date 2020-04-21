from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from datetime import datetime, date,timedelta
from django.db.models import Count,Sum
from dateutil.relativedelta import relativedelta

from usuarios.models import Alumnos, Dia, Noche

# Create your views here.
def index(request):
    try:
        return render(request,'usuarios/inicio.html')
    except Exception as e:
        return HttpResponse(e)

def alumnos(request):
    try:
        fecha= date.today()
        dias= timedelta(days=0)
        f= str(fecha+dias)
        print('hola: ', f)
        fechas = Alumnos.objects.filter(fecha_fin__lt=f).update(estado=False)
        print('record: ', fechas)
        a= Alumnos.objects.all()
        for i in a:
            if i.fecha_fin <= f:
                print(i.fecha_fin)
                
        cantidad= a.count()
        
        print(cantidad)
        return render(request,'usuarios/alumnos.html',{'a':a,'c':cantidad})
    except Exception as e:
        return HttpResponse(e)

def nuevo_alumno(request):
    try:
        return render(request,'usuarios/nuevo_alumno.html')
    except Exception as e:
        return HttpResponse(e)

def guardar_alumno(request):
    try:
        fecha_inicio = request.POST['fechaInicio']
        fecha = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        #dias = timedelta(month=request.POST['meses'])
        month = relativedelta(months= int(request.POST['meses']))
        fechaFin= str((fecha + month).date())
        alumno = Alumnos(
            nombre= request.POST['nombre'],
            apellido= request.POST['apellido'],
            celular = request.POST['celular'],
            fecha_inicio = fecha_inicio,
            fecha_fin = fechaFin,
            estado=True
        )
        alumno.save()
                
        return HttpResponseRedirect(reverse('usuarios:alumnos',args=()))
    except Exception as e:
        print(e)
        return HttpResponse(e)
    
def editar_alumno(request,id):
    try:
        a= Alumnos.objects.get(pk=id)        
        
        return render(request,'usuarios/editar_alumno.html',{'a':a})
    except Exception as e:
        return HttpResponse(e)
    
def actualizar_alumno(request):
    try:
        a= Alumnos.objects.get(pk=request.POST['id'])
        a.nombre= request.POST['nombre']
        a.apellido = request.POST['apellido']
        a.celular = request.POST['celular']
        a.fecha_inicio = request.POST['fechaInicio']
        a.fecha_fin = request.POST['fechaFin']
        a.save()
        
        return HttpResponseRedirect(reverse('usuarios:alumnos',args=()))
    except Exception as e:
        return HttpResponse(e)

def renovar(request,id):
    try:
        a = Alumnos.objects.get(pk=id)
        if request.POST['estado']=='si':
            num = int(request.POST['meses'])
            fecha_inicio = a.fecha_fin
            fecha = datetime.strptime(fecha_inicio, '%Y-%m-%d')
            month = relativedelta(months= int(request.POST['meses']))
            fechaFin= str((fecha + month).date())
            a.fecha_inicio = fecha_inicio
            a.fecha_fin = fechaFin
            a.estado = True
            a.save()            
        return HttpResponse('ok')
    except Exception as e:
        return HttpResponse(e)

def alumnos_inactivos(request):
    try:
        a= Alumnos.objects.all().filter(estado=False).values('id','nombre','apellido','celular','fecha_inicio','fecha_fin')

        print(a)
        return render(request,'usuarios/alumnos_inactivos.html',{'a':a})

    except Exception as e:
        return HttpResponse(e)

def renovar_alumno(request,id):
    try:
        alumno = Alumnos.objects.get(pk=id)
        return render(request,'usuarios/renovar_alumno.html',{'a':alumno})
    except Exception as e:
        return HttpResponse(e)

def activar_alumno(request):
    try:
        a= Alumnos.objects.get(pk=request.POST['id'])

        fecha_inicio = request.POST['fecha_inicio']
        fecha = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        month = relativedelta(months= int(request.POST['meses']))
        fechaFin= str((fecha + month).date())
        a.fecha_inicio=fecha_inicio
        a.fecha_fin = fechaFin
        a.estado= True
        a.save()
        return HttpResponseRedirect(reverse('usuarios:alumnos_inactivos',args=()))
    except Exception as e:
        return HttpResponse(e)

def eliminar(request,id):
    try:
        a= Alumnos.objects.get(pk=id)
        a.estado= False
        a.save()
        return HttpResponse('ok')
    except Exception as e:
        return HttpResponse(e)


def nuevo_reporte(request):
    try:
        dia = Dia.objects.all()
        noche= Noche.objects.all()
        return render(request,'usuarios/ingresar_reporte.html',{'dia':dia,'noche':noche})
    except Exception as e:
        return HttpResponse(e)


def guardar_reporte(request):
    try:
        if request.POST['sesion'] == 'dia':
            if request.POST['ope'] == 'ganada':
                profit = float(request.POST['profit'])
                inversion = float(request.POST['inversion'])
                total = (inversion * profit)/100
                
                dia = Dia(
                    fecha = request.POST['fecha'],
                    estado = True,
                    inversion= inversion,
                    profit = profit,
                    divisa = request.POST['divisa'],
                    total = total
                )
                dia.save()
            else:
                profit = float(request.POST['profit'])
                inversion = float(request.POST['inversion'])
                total = (inversion * 100)/100
                dia = Dia(
                    fecha = request.POST['fecha'],
                    estado = False,
                    inversion= inversion,
                    profit = profit,
                    divisa = request.POST['divisa'],
                    total = total
                )
                dia.save()

        else:
            if request.POST['ope'] == 'ganada':
                profit = float(request.POST['profit'])
                inversion = float(request.POST['inversion'])
                total = (inversion * profit)/100
                
                noche = Noche(
                    fecha = request.POST['fecha'],
                    estado = True,
                    inversion= inversion,
                    profit = profit,
                    divisa = request.POST['divisa'],
                    total = total
                )
                noche.save()
            else:
                profit = float(request.POST['profit'])
                inversion = float(request.POST['inversion'])
                total = (inversion * 100)/100                
                noche = Noche(
                    fecha = request.POST['fecha'],
                    estado = False,
                    inversion= inversion,
                    profit = profit,
                    divisa = request.POST['divisa'],
                    total = total
                )
                noche.save()

        return HttpResponseRedirect(reverse('usuarios:nuevo_reporte',args=()))
    except Exception as e:
        return HttpResponse(e)

def reporte_quincenal(request):
    try:
        total_ganadas_dia= Dia.objects.all().filter(estado=True).aggregate(Sum('total'))        
        total_ganadas_noche= Noche.objects.all().filter(estado=True).aggregate(Sum('total'))

        total_perdidas_dia= Dia.objects.all().filter(estado=False).aggregate(Sum('total'))        
        total_perdidas_noche= Noche.objects.all().filter(estado=False).aggregate(Sum('total'))        
        
        total_ganadas = ((float(total_ganadas_dia['total__sum']) + float(total_ganadas_noche['total__sum']))  )
        total_perdidas = ((float(total_perdidas_dia['total__sum'] )+ float(total_perdidas_noche['total__sum']) ))
        print(total_ganadas - total_perdidas)



        total_ganadas_dia = Dia.objects.all().filter(estado=True).count()
        total_ganadas_noche= Noche.objects.all().filter(estado=True).count()
        print(total_ganadas_dia + total_ganadas_noche)

        total_perdidas_dia= Dia.objects.all().filter(estado=False).count()      
        total_perdidas_noche= Noche.objects.all().filter(estado=False).count()
        print(total_perdidas_dia + total_perdidas_noche)

        return HttpResponse('ok')
    except Exception as e:
        return HttpResponse(e)