from django.shortcuts import render


def HomeViews(request):
      return render(request, 'bios/index.html')


def BioViews(request):
      return render(request, 'bios/bio.html')


# Redes indenticar user
def Redes(request):
      return render(request,'bios/redes.html')


# Proyectos subir desde el admin 
def Proyectos(request):
      return render(request,'bios/proyectos.html')


# Historias breves 
def Historias(request):
      return render(request,'bios/historias.html')


# Seccion de Citas son frases pequeñas
def Citas(request):

      return render(request,'bios/citas.html')



# wandyadminxw Es la super def mi project 
# Con ella practicare 
def wandyadminxw(request,password, nameuser):
      pass