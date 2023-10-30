from django.shortcuts import render, redirect
from .models import PontosTuristicos, CuidadosDicas


# Create your views here.
def home(request):
  pontos = PontosTuristicos.objects.all()
  cuidados = CuidadosDicas.objects.all()
  
  return render(request, "home.html", context={
    "pontos": pontos,
    "cuidados": cuidados
  
  
  })

# FUNCOES E FORMS PARA PONTOS TURISTICOS

def create_pontosturisticos(request):
  if request.method == "POST":
    # Criar um novo ponto turistico usando os valores do meu formulário
    PontosTuristicos.objects.create(
      ponto_turistico = request.POST["ponto_turistico"],
      bairro = request.POST["bairro"],
      cidade = request.POST["cidade"],
      rating = request.POST["rating"]
    )

    return redirect("home")
  return render(request, "forms.html", context={"action": "Adicionar"})

def update_pontosturisticos(request, id):
  pontos = PontosTuristicos.objects.get(id = id)
  if request.method == "POST":
    # Criar um novo ponto turistico usando os valores do meu formulário
    pontos.ponto_turistico = request.POST["ponto_turistico"]
    pontos.bairro = request.POST["bairro"]
    pontos.cidade = request.POST["cidade"]
    pontos.rating = request.POST["rating"]
    pontos.save()

    return redirect("home")
  return render(request, "forms.html", context={"action": "Atualizar","pontos": pontos})

def delete_pontosturisticos(request, id):
  pontos = PontosTuristicos.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      pontos.delete()

    return redirect("home")
  return render(request, "are_you_sure.html", context={"pontos": pontos})





# FUNCOES E FORMS PARA CUIDADOS E DICAS

def create_cuidadosdicas(request):
  if request.method == "POST":
    # Criar um novo ponto turistico usando os valores do meu formulário
    CuidadosDicas.objects.create(
      cuidados = request.POST["cuidados"],
      lugares_para_ter_cuidado = request.POST["lugares_para_ter_cuidado"],
      perigo = request.POST["perigo"])
    return redirect("home")

  #options = CuidadosDicas.cuidados.options

  return render(request, "forms2.html", context={"action": "Adicionar"})

def update_cuidadosdicas(request, id):
  cuidados = CuidadosDicas.objects.get(id = id)
  if request.method == "POST":
    # Criar um novo ponto turistico usando os valores do meu formulário
    cuidados.cuidados = request.POST["cuidados"]
    cuidados.lugares_para_ter_cuidado = request.POST["lugares_para_ter_cuidado"]
    cuidados.perigo = request.POST["perigo"]
    cuidados.save()
    return redirect("home")
    
  #options = CuidadosDicas.cuidados.options

  return render(request, "forms2.html", context={
    "action": "Atualizar",
    "cuidados": cuidados
    
  })




def delete_cuidadosdicas(request, id):
  cuidados = CuidadosDicas.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      cuidados.delete()

    return redirect("home")
  return render(request, "are_you_sure2.html", context={"cuidados": cuidados})

