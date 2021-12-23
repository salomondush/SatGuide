from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import School, Student

from . import util

import random
import markdown2

# library - util
# getting a specific file, run util.get_entry(title)
# saving a specific file, run util.save_entry(title, contents)
# getting all files, run util.list_entries()


def index(request):
    """loads the home page (index.html)
    """
    

    return render(request, "scholarGuide/index.html")



def blogs(request):
    """Returns all blogs we've written so far using the query "util.list_entries()" to get all entries
    we have made.
    post: passes over that information to "scholarGuide/blogs.html"
    """
    
    



def title(request, title):
    """ getting a specific file with title from our entries
    """
    entry = util.get_entry(title)
    if entry is None:
        return render(request, "scholarGuide/error.html", {"error": "Page Not Found!"}) 
    else:
        return render(request, "scholarGuide/title.html", {"entry": markdown2.markdown(entry), "title": title})


def profile(request, school_id):
    """loads information about a specific school from the database to profile.html
    pre: schoold_id -- integer
    post: load satguide/profile.html
    """

    if request.method == "GET":

        school = School.objects.get(pk=school_id)

        # TODO: we don't have a personal statements and school essays in database

        # example:
            # students = school.students.all()
            # total = 0
            # for student in students:
                # total += student.sat
            
            # school.sat_average = (total / len(students))
            # school.save()
    

        return render(request, "scholarGuide/profile.html", {
            "num_students": school.students.all().count(),
            "average_sat": school.sat_average,
            "average_national_exams": school.average_percentage_ne,
            "average_grades": school.average_percentage_class
        })


def schools(request):
    """This function retrieves a list of all school objects in the School table
    request: 'GET' request
    post: Passes over that information to "scholarGuide/schools.html"
    """






def search(request):
    title = request.POST["title"]
    entries = util.list_entries()
    
    #now let's look for matches
    match = []
    if title in entries:
        return HttpResponseRedirect(reverse("title", args=(title,)))
    else:
        for entry in entries:
            if title in entry:
                match.append(entry)

    #now we should render this to the index page
    return render(request, "scholarGuide/index.html", {"entries": match, "search": True})

def newentry(request):
    if request.method == "GET":
        return render(request, "scholarGuide/newentry.html")
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")
        #check if not exists already
        entries = util.list_entries()
        if title in entries:
            return render(request, "scholarGuide/error.html", {"error": "Entry Already Exists!"})
        else:
            #save the new entry
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("title", args=(title,)))

def edit(request, entry_title):
    if request.method == "GET":
        entry = util.get_entry(entry_title)
        return render(request, "scholarGuide/edit.html", {"content": entry, "title": entry_title})
    else:
        content = request.POST.get("content")
        #save the users entry
        util.save_entry(entry_title, content)
        #redirect to the entries page
        return HttpResponseRedirect(reverse("title", args=(entry_title,)))
    
    
def random_entry(request):
    entries = util.list_entries()
    entry = random.choice(entries)
    return HttpResponseRedirect(reverse("title", args=(entry,)))