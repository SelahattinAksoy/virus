from django.shortcuts import render
from django.http import JsonResponse
import redis
from .models import Virus,Announcement,Adenovirus,Coronavirus,Influenza,Publication
import time
from django.core.cache import cache
from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static
import os.path
from django.conf import settings


def index(request):
   

    path=os.path.join(settings.MEDIA_ROOT, 'text/maintext')
    f = open(path, 'r',encoding='utf8')
    file_content = f.read()
    f.close()

    annonces=Announcement.objects.all().order_by('-id')[:3]
    return render(request,"virus.html",{"annonces":annonces,'maintext':file_content})

def team(request):
    
    return render(request,"team.html")


def predicter(request):
    
    return render(request,"predicter_1.html")

def autocompilite(request):
    
    return render(request,"virustype.html")

def about(request):
    
    path=os.path.join(settings.MEDIA_ROOT, 'text/what_we_do')
    f = open(path, 'r',encoding='utf8')
    file_content_what_we_do = f.read()
    f.close()
    
    path=os.path.join(settings.MEDIA_ROOT, 'text/who_we_are')
    f = open(path, 'r',encoding='utf8')
    file_content_who_we_are = f.read()
    f.close()
    
    return render(request,"about.html",{"file_content_who_we_are":file_content_who_we_are})



def virustableintro(request):
    
    path=os.path.join(settings.MEDIA_ROOT, 'text/virustable_intro')
    f = open(path, 'r',encoding='utf8')
    file_content = f.read()
    f.close()

    
    return render(request,"VIRIS_HOST_TABLE_TEMPLATES/virustableintro.html",{"file_content":file_content})

def virustable(request):
    table_link_list=["viralProteins_ViralProtein1_Accession_GeneName_ProteinName","hostReceptorProteins_Receptor1_Accession_GeneName_ProteinName"] #link yapmak istediğini buraya ekle

    if  request.method == "POST":
        
         if "select_virus_family" in request.POST:
                a = request.POST['virus_family_selected']
                print(a)
                if a.lower()=="coronavirus":
                    print("yess")
                    data=Coronavirus.objects.all().values()
                
                    for i in data:
                        del i["id"]
              
                    
                    tabele_structure={}
                   
                    for field in Coronavirus._meta.fields[1:]:
                        name=field.name
                        output=x = name.split("_", 1)
                        key=output[0]
                        value=output[1]
                        value=value.replace("_"," / \n")
                        
                        if key not in tabele_structure:
                            lis=[value]
                            tabele_structure[key]=lis
                        else:
                            tabele_structure[key].append(value) 
                    print(data)
                    return render(request,"VIRIS_HOST_TABLE_TEMPLATES/virustable.html",{"tabele_structure":tabele_structure,"data":data,"table_link_list":table_link_list})
               
                if a.lower()=="influenza":
                    print("yess")
                    data=Influenza.objects.all().values()
                    tabele_structure={}
                    for i in data:
                        del i["id"]
                        
                    for field in Influenza._meta.fields[1:]:
                        name=field.name
                        output=x = name.split("_", 1)
                        key=output[0]
                        value=output[1]
                        value=value.replace("_"," / \n")
                        if key not in tabele_structure:
                            lis=[value]
                            tabele_structure[key]=lis
                        else:
                            tabele_structure[key].append(value) 
                  
                    return render(request,"VIRIS_HOST_TABLE_TEMPLATES/virustable.html",{"tabele_structure":tabele_structure,"data":data,"table_link_list":table_link_list})
         
         if request.is_ajax():
            
            value=request.POST.get("text")
            #print("******","ST "+value)
            result="s"
            return JsonResponse({"x":result},status=200)
 
      
    elif  'term' in request.GET:
       print("yead")
       qst=Virus.objects.filter(title__startswith=request.GET.get("term"))
       titles=list()
       for i in qst:
         titles.append(i.title) 
      
       return JsonResponse(titles,safe=False) 
   

    data=Adenovirus.objects.all().values()
  

    for i in data:
        del i["id"]
  
    tabele_structure={}
  
    for field in Adenovirus._meta.fields[1:]:
       name=field.name
       output=x = name.split("_", 1)
       key=output[0]
       value=output[1]
       value=value.replace("_","/\n")
       if key not in tabele_structure:
          lis=[value]
          tabele_structure[key]=lis
       else:
           tabele_structure[key].append(value) 
       

    #cache.clear()
    return render(request,"VIRIS_HOST_TABLE_TEMPLATES/virustable.html",{"tabele_structure":tabele_structure,"data":data,"table_link_list":table_link_list})









def viral_infectintro(request):
    
    path=os.path.join(settings.MEDIA_ROOT, 'text/ppi_intro')
    f = open(path, 'r',encoding='utf8')
    file_content = f.read()
    f.close()

    
    return render(request,"VIRAL_INFECT_TEMPLATES/viral_infectintro.html",{"file_content":file_content})


def viral_infectpredicter(request):
    
    if  'term' in request.GET:
         print("yead")
         qst=Virus.objects.filter(title__startswith=request.GET.get("term"))
         titles=list()
         for i in qst:
              titles.append(i.title) 
    
         return JsonResponse(titles,safe=False) 
   
    return render(request,"VIRAL_INFECT_TEMPLATES/viral_infectpredicter.html")






def ppintro(request):
    
    path=os.path.join(settings.MEDIA_ROOT, 'text/ppi_intro')
    f = open(path, 'r',encoding='utf8')
    file_content = f.read()
    f.close()

    
    return render(request,"PPI_TEMPLATES/ppintro.html",{"file_content":file_content})

def ppipredicter(request):
    
    if request.method=="POST":
        
        viral_protein_sequence = request.POST["viral_protein_sequence"]
        viral_protein_sequence_fatsa_file = request.FILES["viral_protein_sequence_fatsa_file"]
        
        receptor_protein_sequence = request.POST["receptor_protein_sequence"]
        receptor_protein_sequence_fatsa_file = request.FILES.get("receptor_protein_sequence_fatsa_file")
        
        fs=FileSystemStorage()
        try:
            fs.save(viral_protein_sequence_fatsa_file.name,viral_protein_sequence_fatsa_file)
            fs.save(receptor_protein_sequence_fatsa_file.name,receptor_protein_sequence_fatsa_file)
        except:
            pass
       
    
    return render(request,"PPI_TEMPLATES/ppipredicter.html")



def publications(request):
    
    
    publications=Publication.objects.all().order_by('-id')
    return render(request,"publications.html",{"publications":publications})


def announcement(request):
    
    if  request.method == "POST":
        announce_id=request.POST["announce_id"]
        annonce = Announcement.objects.get(id=announce_id)
        
    
        return render(request,"announcement.html",{"annonce":annonce})
    annonces=Announcement.objects.all().order_by('-id')
    
    return render(request,"announcement.html",{"annonces":annonces})



