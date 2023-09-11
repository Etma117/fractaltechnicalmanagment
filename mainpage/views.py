from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base.html')

#class main(LoginRequiredMixin, ListView):
 #   model = Accesorio
  #  template_name = 'Accesorio.html'
   # context_object_name = 'Accesorio'
    #success_url = 'Accesorio'

    #login_url = 'login'  # URL de inicio de sesión
    #redirect_field_name = 'next'  # Nombre del campo de redireccionamiento