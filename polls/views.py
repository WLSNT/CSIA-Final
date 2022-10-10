from lib2to3.pgen2.token import DEDENT
from .models import Folder, Tag, Source
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


# classes to handle authentication (log in and sign up)
#page for user login
class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('sorter:index')

#page for user sign up
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_message = "Your profile was created successfully"
    success_url = reverse_lazy('sorter:index')

#profile start
#view profile only
def Profile_View(request):
    user = request.user
    return render(request, 'sorter/profile_view.html', {'user': user})

#editing profile
def edit_profile(request):
    user = request.user
    try: 
        if request.method == "POST": #if the request is a post, get data that the user inputted and save it to the database
            data= request.POST
            user.username = data.get("username")
            user.first_name = data.get("firstname")
            user.last_name = data.get("lastname")
            user.profile.gender = data.get("gender")
            user.email = data.get("email")
            user.profile.bio = data.get("bio")
            #saving the data to the database
            user.save()
            user.profile.save()
    except:
        pass
    return render(request, 'sorter/profile_edit.html', {
        'user': user, 
        })

#profile end

#Home page class, with a priority queue based off whether a folder is marked as important
class IndexView(generic.ListView):    
    template_name = 'sorter/index.html'
    context_object_name = 'latest_folder_list'
    def get_queryset(self): #priority queue
        flist = Folder.objects.order_by('-pub_date')[:]
        print(flist)
        for x in flist:
            print (x.pub_date)

        prio = []
        non_prio = []
        for x in flist:
            non_prio.append(x)
        for folder in flist:
            if folder.is_important == True:
                prio.append(folder)
                non_prio.remove(folder)
        return prio + non_prio


#importance change for home page
def ImportanceChangeView(request, pk):
    changed_folder = Folder.objects.get(pk=pk)
    changed_folder.set_importance()
    return redirect('/sorter')

#importance change for tags page
def ImportanceChangeForFolderView (request, pk, pk1):
    changed_folder = Folder.objects.get(pk=pk)
    changed_folder.set_importance()
    pk1=pk1
    return redirect(f'/sorter/{pk1}/tag_contents')

#editing folder page
def EditFolderView(request, pk):
    new = Folder.objects.get(pk=pk)
    existing_tags = new.tags.all()
    try:
        if request.method == "POST":
            data = request.POST
            new.set_folder_text(data.get("foldername"))
            #setting tags, breaking a list of tags into strings, then checking if the tag exists there are no duplicates
            tag_list = data.get("tags")
            tag_list = tag_list.split()            
            def check_exist(t): #t is the inputted tag
                for i in Tag.objects.all():
                    if t == i.tag_text:
                        return i
                return False
            for tag in tag_list: #for every tag in the list, check if it already exists
                check = check_exist(tag)
                if check != False: #if it already exists connect the existing tag with the folder
                    new.tags.add(check)
                    new.save()
                else: #if it does not exist create a new tag and connect it wtht the folder
                    created_tag = Tag.objects.create() 
                    created_tag.set_tag_text(tag)
                    new.tags.add(created_tag)
                    new.save()
            return redirect('/sorter')
    except:
        pass

    return render(request, 'sorter/edit_folder.html', {
        "folder": new,
        "tag_list": " ".join([t.tag_text for t in existing_tags]) #joining the tags at the end back into an array
    })

#page showing a list of tags
def TagListView(request):
    #if there are no folders connecting to a tag, the tag will be removed
    for tag in Tag.objects.all():
        if not tag.folder_set.all():
            tag.delete()
    return render(request, 'sorter/tags_list.html', {
        "tags": Tag.objects.all()
    })

#page showing the folders connected to the tags
def TagContentsView(request, pk):
    flist = Tag.objects.get(pk=pk).folder_set.all()
    prio = []
    non_prio = []
    for x in flist:
        non_prio.append(x)
    for folder in flist:
        if folder.is_important == True:
            prio.append(folder)
            non_prio.remove(folder)
    final = prio + non_prio

    return render(request, 'sorter/tags_contents.html', {
        "tag_folder_list": final,
        "tag" : Tag.objects.get(pk=pk)
    })

#page for the creation of a folder
def CreateFolderView(request, folderid = None):
    new = Folder()
    submitted = False
    creator = request.user
    try:
        if request.method == "POST":
            data = request.POST
            if data.get("foldername") == "":
                return render(request, 'sorter/create_folder.html', {
                "folder": new,
                "error_message": "Please Enter A Folder Name"
                })
            submitted = True
            new.set_folder_text(data.get("foldername"))
            tag_list = data.get("tags")
            tag_list = tag_list.split()
            new.set_creator(creator)
            #same tag addition and checking function as in the edit folder view
            #setting tags, breaking a list of tags into strings, then checking if the tag exists there are no duplicates
            def check_exist(t):
                for i in Tag.objects.all(): #i is each tag
                    if t == i.tag_text: #t is the tag inputted into the function
                        return i
                return False

            for tag in tag_list: #for every tag in the list, check if it already exists
                check = check_exist(tag)
                if check != False: #if it already exists connect the existing tag with the folder
                    new.tags.add(check)
                    new.save()
                else: #if it does not exist create a new tag and connect it wtht the folder
                    created_tag = Tag.objects.create()
                    created_tag.tag_text = tag
                    created_tag.save()
                    new.tags.add(created_tag)
                    new.save()
    except: 
        pass
    if submitted == False:
        return render(request, 'sorter/create_folder.html', {
            "folder": new,
            "submitted":submitted
        })
    else:
            return redirect('/sorter')

#page to create a new source
def NewSourceView(request, pk):
    used_folder = Folder.objects.get(pk=pk)
    new = Source.objects.create()
    submitted = False
    print(new)
    try:
        if request.method == "POST":
            data = request.POST
            submitted = True
            print("works kinda well but not really")            
            new.folders_contained_in.add(used_folder)
            new.set_source_text(data.get("source_text"))
            new.set_source(data.get("source_url"))
            new.set_description(data.get("description"))
            new.set_date_added(data.get("date_added"))
            new.set_date_published(data.get("date_published"))
            new.set_author(data.get("author"))
            print("works2")
            return redirect('/{pk}/view/')

    except: 
        pass
    if submitted == False:
        return render(request, 'sorter/create_source.html', {
            "folder": used_folder,
            "source": new,
        })
    else:
        return redirect(f'/sorter/{used_folder.id}/view')

#page to show the contents of a specified folder with id pk
def FolderContentsView(request, pk):
    new = Folder.objects.get(pk=pk) 
    print(new.source_set.all)
    if request.method == "POST":
        try:     
            selected_source = new.source_set.get(pk=request.POST['source'])
        except (KeyError, Source.DoesNotExist):
            # Redisplay the question voting form.
                return render(request, 'sorter/folder_contents.html', {
                'folder': new,
                'error_message': "You didn't select a source.",
                        })
        else:
            selected_source.delete()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a                # user hits the Back button.
    return render(request, 'sorter/folder_contents.html', {
        'folder': new,
        })

#page to show the contents of a specified source in a specified folder
def SourceView(request, pk, pk1):
    new = Source.objects.get(pk=pk) 

    try:
        if request.method == "POST":
            data = request.POST
            new.set_source_text(data.get("source_text"))
            new.set_description(data.get("description"))
            new.set_author(data.get("author"))
            new.set_source(data.get("source_url"))
            new.set_date_published(data.get("date_published"))

            return redirect(f'/{pk1}/view/')

    except: 
        pass
    return render(request, 'sorter/edit_source.html', {
            "source": new,
        })


#page to delete specified folder
def DeleteFolderView(request, pk): 
    new = Folder.objects.get(pk=pk)
    try:
        if request.method == "POST":
            new.delete()
            return redirect('/')
    except: 
        pass
    return render(request, 'sorter/delete_folder.html', {
        "folder": new,
        })

#page to change the users password
def PasswordChangeView(request):
    user = request.user
    try:
        if request.method == "POST":
            data = request.POST
            print(data.get("new_password"))
            user.set_password(data.get("new_password"))
            user.save()
            print(data.get("new_password"))
    except:
        pass
    return render(request, 'sorter/password_change.html', {
        "user": user,
    })