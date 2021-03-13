from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.views import View
from .models import ssurlURL
from .forms import SubmitUrlForm
from analytics.models import ClickEvent
# Create your views here.

class HomeView(View):
    def get(self,request, *args,**kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "SSURL.ew",
            "form": the_form
        }
        return render(request, "shortner/home.html",context)

    def post(self,request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "SSURL.ew",
            "form": form
        }
        template = "shortner/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            print(new_url)
            if not "http" in new_url:
                new_url = "http://" + new_url
            print(new_url)
            obj, created = ssurlURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortner/success.html"
            else:
                template = "shortner/already-exists.html"
        
        
        return render(request, template,context)


class URLRedirectView(View):
    def get(self, request, shorturl=None, *args, **kwargs):
        qs = ssurlURL.objects.filter(shorturl__iexact=shorturl)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj=qs.first()
        # print(qs)
        # obj = get_object_or_404(ssurlURL, shorturl=shorturl)
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
        
        

    # def post(self,request,*args,**kwargs):
    #     return HttpResponse()


"""


def ss_redirect_view(request, shorturl=None, *args, **kwargs):  #function based view
    obj = get_object_or_404(ssurlURL, shorturl=shorturl)
    # return HttpResponse(f"hello {obj.url}")
    return HttpResponseRedirect(obj.url)



def ss_redirect_view(request, shorturl=None, *args, **kwargs):  #function based view
    # print(request.user)
    # print(request.user.is_authenticated)
    # print(request.method)
    # print(shorturl)
    # print(kwargs)
    # obj = ssurlURL.objects.get(shorturl=shorturl)

    obj = get_object_or_404(ssurlURL, shorturl=shorturl)
    bj_url = obj.url
    # try:
    #     obj = ssurlURL.objects.get(shorturl=shorturl)
    # except:
    #     obj = ssurlURL.objects.all().first()
    # obj_url = None
    # qs = ssurlURL.objects.filter(shorturl__iexact=shorturl.upper())
    # if qs.exists() and qs.count() == 1:
    #     obj=qs.first()
    #     obj_url = obj.url
    return HttpResponse(f"hello {obj_url}")
"""