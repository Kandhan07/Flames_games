from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,"home.html")

from django.shortcuts import render

def output(request):
    name_1=request.POST["name1"]
    name_2=request.POST["name2"]

    name1_=name_1.lower()
    name2_=name_2.lower()
    
    name1_=name1_.replace(" ","")
    name2_=name2_.replace(" ","")

    for i in name1_: 
            
            for j in name2_:
                
                if i == j:
                    name1_=name1_.replace(i,"",1)    
                    name2_=name2_.replace(j,"",1)  
                    break
    
    number1= len(name1_+name2_)
    print(number1)

    flames_list={
        "f":"Friends🫂❤♾️",
        "l":"love❤️‍🔥💋",
        "a":"affection 🫣🫦",
        "m":"marraige🤵🏻👰🏻",
        'e':"Enemy🤼😈",
        "s":"Sister🩵👩🏻‍❤️‍👩🏻🧬♾️"
    }

    flames1= list(flames_list.keys())
    index=0

    for k in range(5):
        index=(index + number1-1) % len(flames1) 
        flames1.pop(index)

    all_data={
        "name1_data":name_1,
        "name2_data":name_2,
        "relationship":flames_list[flames1[0]],
    }

    return render(request,"output.html",all_data)

