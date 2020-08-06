from django.shortcuts import render

from . import util
from encyclopedia.forms import AddPageForm


def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def newpage(request):    
    
    if request.method == "POST":
        vapform = AddPageForm(request.POST)
        
        if vapform.is_valid():
            vtitle = vapform.cleaned_data["title"]
            vbody = vapform.cleaned_data["body"]
            
            return render(request, "encyclopedia/addpage.html", {
                "ptitle" : vtitle,
                "pbody" : vbody,
                "tapform" : AddPageForm()
               })
            #vtitle.append(task)
            
            
    return render(request, "encyclopedia/addpage.html", {
        "tapform" : AddPageForm()
    })

def searchpage(request):

    if request.method == "POST":
        searchterm = request.POST.get('q')
        util.get_entry(searchterm)
    
    return render(request, "encyclopedia/addpage.html", {
        "tapform" : AddPageForm()
    })