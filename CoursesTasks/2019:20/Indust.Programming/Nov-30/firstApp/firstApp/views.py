from django.shortcuts import render

def kek(request):
  return render(request, 'index.html', {})
