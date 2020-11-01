from django.shortcuts import render,redirect
from .models import Note
from .forms import CreateNoteForm
# Create your views here.

def writepad(request):
    form = CreateNoteForm()

    if request.method == "POST":
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    allnotes = Note.objects.all()

    context = {'form':form,'Notes':allnotes}
    return render(request,'writepad.html',context)


def readNote(request,id):
    read_Note = Note.objects.get(id=id)
    print(read_Note.Title)
    # context = {'read_Note':read_Note}
    return render(request,'read_note.html',{'read_Note':read_Note})


def editNote(request,id):
    note = Note.objects.get(id=id)
    form = CreateNoteForm(instance=note)
    if request.method== 'POST':
        form = CreateNoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'edit_note.html',{'form':form})

def deleteNote(request,id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('/')


def searchNote(request):
    query = request.GET['search']
    print(query)
    notes_search = Note.objects.all()
    if len(query)>80:
        parms = Note.objects.none()
    else:
        note_title = Note.objects.filter(Title__icontains=query)
        note_content = Note.objects.filter(Content__icontains=query)
        notes_search = note_title.union(note_content)
        parms = {'note_searched':notes_search,'query':query}

    return render(request,'search_note.html',parms)