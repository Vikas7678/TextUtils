from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def Analyze_text(request):
    return render(request, 'HomeAna2.html')

def textutils(request):
    purpose = 'Done'
    # Remove Punctuations
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    
    # get the user text
    usertext = request.POST.get('text', 'default')
    if removepunc == 'on':
        analyzed_text = ""
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~='''
        for char in usertext:
            if char not in punc:
                analyzed_text += char
        usertext = analyzed_text
    
    # Upper case
    if uppercase == 'on':
        analyzed_text = ""
        analyzed_text = usertext.upper()
        usertext = analyzed_text
        
    # Cap First
    if capfirst == 'on':
        analyzed_text = ""
        analyzed_text = usertext.title()
        usertext = analyzed_text
        
    # New Line Remover
    if newlineremover == 'on':
        analyzed_text = ""
        analyzed_text = "".join(usertext.split('\r\n'))
        usertext = analyzed_text
    
    # Space Remover
    if spaceremover == 'on':
        analyzed_text = ""
        analyzed_text = "".join(usertext.split(' '))
        usertext = analyzed_text

    # Char count
    if charcount == 'on':
        analyzed_text = ""
        analyzed_text = str(len(usertext))
        usertext = analyzed_text
    
    if charcount == 'off' and spaceremover == 'off' and removepunc == 'off' and newlineremover == 'off' and uppercase == 'off' and capfirst == 'off':
        return HttpResponse('Please choose specific field and try again!!!')

    output_dict = {'purpose':purpose, 'output_text':usertext}
    return render(request, 'Analyze2.html', output_dict)
    