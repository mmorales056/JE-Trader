from django.urls import path
from . import views
app_name = 'usuarios'
urlpatterns = [
    path('', views.index, name="inicio" ),
    path('alumnos', views.alumnos, name="alumnos"),
    path('alumnos_inactivos', views.alumnos_inactivos, name="alumnos_inactivos"),
    path('nuevoalumno', views.nuevo_alumno, name="nuevoalumno"),
    path('guardaralumno',views.guardar_alumno, name="guardaralumno"),
    path('editar_alumno/<int:id>', views.editar_alumno, name='editar_alumno'),
    path('actualizar_alumno', views.actualizar_alumno, name='actualizar_alumno'),
    path('renovar/<int:id>', views.renovar, name='renovar'),
    path('renovar_alumno/<int:id>',views.renovar_alumno, name='renovar_alumno'),
    path('activar_alumno',views.activar_alumno, name='activar_alumno'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),

    #Usuarios
    path('nuevo_reporte', views.nuevo_reporte, name='nuevo_reporte'),
    path('guardar_reporte', views.guardar_reporte, name='guardar_reporte'),
    path('reporte_quincenal', views.reporte_quincenal, name='reporte_quincenal'),

]