from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from contact.models import Contact
from contact.forms import ContactForm, UploadFileForm
from contact.xml import handle_uploaded_xml
import inspect


# Create your views here.

def index(request):
    return render(request, "contact/index.html")

def find(request, surname, name):
    contacts = Contact.objects.all().filter(lastname=surname, firstname=name)
    context = {'contacts':contacts}
    return render(request, 'contact/contacts.html', context)

def data_errmsg(f):
    err_msg = f"""
        These fileds are compulsory :
        First name, Surname, Email.
        {f.errors}"""
    for code,text in zip(['lastname','firstname','email'],['Surname','First name','Email']):
        err_msg = err_msg.replace(code, text)
    return err_msg

def check_saved(lastname, firstname, email):
    contacts = Contact.objects.all().filter(lastname=lastname, firstname=firstname, email=email)
    return {'contacts':contacts}

def add(request):
    f = ContactForm(request.POST)
    if f.is_valid():
        try:
            c = Contact()
            c.lastname = f.cleaned_data['lastname']
            c.firstname = f.cleaned_data['firstname']
            c.email = f.cleaned_data['email']
            c.address = f.cleaned_data['address']
            c.phone = f.cleaned_data['phone']
            c.save()
        except Exception as e:
            print(f"{'#'*50} {__name__} {inspect.stack()[0][3]}\nException : {e}")
            return render(request, 'contact/errmsg.html', {'message':'Server Internal Error.'})
        else:
            context = check_saved(c.lastname, c.firstname, c.email)
            return render(request, 'contact/contacts.html', context)
    else:
        err_msg = data_errmsg(f)
        return HttpResponse(err_msg)

def xmlapi(request):
    def xml_errmsg(f):
        return f"""
            There is no file. Re-upload the file.
            {f.errors}"""

    if request.method == 'POST':
        if hasattr(request, 'FILES'):
            f = UploadFileForm(request.POST, request.FILES)
            if f.is_valid():
                data = handle_uploaded_xml(request.FILES['file'])
                c = Contact()
                c.lastname = data['lastname']
                c.firstname = data['firstname']
                c.email = data['email']
                c.address = data['address']
                c.phone = data['phone']
                c.save()
                context = check_saved(c.lastname, c.firstname, c.email)
                return render(request, 'contact/contacts.html', context)
            else:
                err_msg = xml_errmsg(f)
                return HttpResponse(err_msg)
        else:
            err_msg = xml_errmsg(f)
            return HttpResponse(err_msg)
    else:
        print(f"{'#'*50} {__name__} {inspect.stack()[0][3]}\nException : {e}")
        return render(request, 'contact/errmsg.html', {'message':'Server Internal Error.'})
