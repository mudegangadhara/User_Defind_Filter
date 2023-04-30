from django.shortcuts import render

# Create your views here.
def user_filter(request):
    d={'data':'When AN ErroR OR EXCEPtion As We CALL it PYthon NORMALLY STOP and GenaREter An ERRor MeSSage'}
    return render(request, 'user_filter.html',d)