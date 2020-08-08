from django.shortcuts import render, redirect

from . import util
from encyclopedia.forms import AddPageForm

def search_entries(search_term):
    all_entries = util.list_entries()    
    
    matching_entries = []
    for entry in all_entries:
        if search_term in entry:
            matching_entries.append(entry)

    return matching_entries
    
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
            
            util.save_entry(vtitle, vbody)
            return render(request, "encyclopedia/addpage.html", {
                "ptitle" : vtitle,
                "pbody" : vbody,
                "tapform" : AddPageForm()
               })
            #vtitle.append(task)
            
            
    return render(request, "encyclopedia/addpage.html", {
        "tapform" : AddPageForm()
    })
    
def entrypage(request, utitle = None):
    
    if request.method == "POST":
        utitle = request.POST.get('q')
        wiki_entry = util.get_entry(utitle)
        if wiki_entry is None:
            possible_entries = search_entries(utitle)
            return render(request, 'encyclopedia/index.html', {
                "entries" : possible_entries
            })
            
             # if wiki_entry is None:
            # possible_entries = search_entries(utitle)
            # return redirect(reverse('/', args=(entries,possible_entries))
            
    wiki_entry = util.get_entry(utitle)
    
    if wiki_entry is not None:
        vbody = wiki_entry
    else:
        return render(request, 'encyclopedia/error.html', { "dtitle" : utitle})
        
    return render(request, "encyclopedia/displaypage.html", {
        "dtitle" : utitle,
        "dbody"  : vbody
    })