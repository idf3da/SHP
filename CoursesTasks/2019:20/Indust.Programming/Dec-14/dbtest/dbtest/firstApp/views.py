from django.shortcuts import render
from firstApp.models import CalcHistory
from firstApp.models import Mistor
from django.http import HttpResponse
# Create your views here.
from datetime import datetime

def deleteCalcHistory(request, id):
  print(request.method)
  if request.method == 'DELETE':
    CalcHistory.objects.filter(pk=id).delete()
    return HttpResponse(status=200, content='Удалил')
  return HttpResponse(status=405, content='only DELETE is supported')

def index(request):
  first = request.GET.get('first', 0)
  second = request.GET.get('second', 0)
  result = int(first) + int(second)
  mistor_id = int(request.GET.get('mistor', 1))

  mistor = Mistor.objects.get(pk=mistor_id)
  history = CalcHistory(date=datetime.now(),
                        first=first,
                        second=second,
                        result=result,
                        author=mistor)
  history.save()
  all = CalcHistory.objects.filter(author=mistor)
  context = {
    'items': all
  }
  return render(request, 'index.html', context)
