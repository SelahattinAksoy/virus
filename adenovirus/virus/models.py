from django.db import models

# Create your models here.



class  Virus(models.Model):
    title=models.CharField(max_length=100)
    qt=models.IntegerField()


class Announcement(models.Model):
      title=models.CharField(max_length=100)
      body=models.TextField()
      date=models.DateField()
      
class Publication(models.Model):
      title=models.CharField(max_length=250)
      link=models.CharField(max_length=100)

      
      
class  Adenovirus(models.Model):
    virus_taxid=models.CharField(max_length=100)
    virus_ScientificName_CommonName=models.CharField(max_length=100)
    virus_LineageInfo=models.CharField(max_length=200)
    
    host_taxid=models.CharField(max_length=100)
    host_Scientific_CommonName=models.CharField(max_length=100)
    host_LineageInfo=models.CharField(max_length=200)
    
    viralProteins_ViralProtein1_Accession_GeneName_ProteinName=models.CharField(max_length=100)
    
    hostReceptorProteins_Receptor1_Accession_GeneName_ProteinName=models.CharField(max_length=100)
    hostReceptorProteins_Receptor2_Accession_GeneName_ProteinName=models.CharField(max_length=100)
    hostReceptorProteins_Receptor3_Accession_GeneName_ProteinName=models.CharField(max_length=100)      
    hostReceptorProteins_Receptor4_Accession_GeneName_ProteinName=models.CharField(max_length=100)
    hostReceptorProteins_Receptor5_Accession_GeneName_ProteinName=models.CharField(max_length=100)
    hostReceptorProteins_Receptor6_Accession_GeneName_ProteinName=models.CharField(max_length=100) 
    hostReceptorProteins_Receptor7_Accession_GeneName_ProteinName=models.CharField(max_length=100)
    hostReceptorProteins_Receptor8_Accession_GeneName_ProteinName=models.CharField(max_length=100)
    
  
class  Coronavirus(models.Model):
    virus_taxid=models.CharField(max_length=100)      
    virus_ScientificName_CommonName=models.CharField(max_length=100)
    virus_LineageInfo=models.CharField(max_length=200)
    
    host_taxid=models.CharField(max_length=100)
    host_ScientificName_CommonName=models.CharField(max_length=100)
    host_LineageInfo=models.CharField(max_length=200)
    
    viralProteins_ViralProtein1_Accession_GeneName_ProteinName=models.CharField(max_length=100)
    
    hostReceptorProteins_Receptor1_Accession_GeneName_ProteinName=models.CharField(max_length=100)


class  Influenza(models.Model):
    virus_taxid=models.CharField(max_length=100)  
    virus_ScientificName_CommonName=models.CharField(max_length=100)
    virus_LineageInfo=models.CharField(max_length=200)
    
    host_taxid=models.CharField(max_length=100)
    host_Scientific_CommonName=models.CharField(max_length=100)
    host_LineageInfo=models.CharField(max_length=200)
    
    viralProteins_ViralProtein1_Accession_GeneName_ProteinName=models.CharField(max_length=100)
    viralProteins_ViralProtein2_Accession_GeneName_ProteinName=models.CharField(max_length=100)
    viralProteins_ViralProtein3_Accession_GeneName_ProteinName=models.CharField(max_length=100)
    viralProteins_ViralProtein4_Accession_GeneName_ProteinName=models.CharField(max_length=100)
    
    hostReceptorProteins_Receptor1_Accession_GeneName_ProteinName=models.CharField(max_length=100)
    
