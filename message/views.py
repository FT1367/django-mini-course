from django.views.generic import TemplateView

#def messageview(request):
#    return render(request, 'home.html')

class MessageView(TemplateView):
    template_name = 'home.html'

