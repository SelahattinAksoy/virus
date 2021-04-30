# Generated by Django 2.2.2 on 2021-04-11 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adenovirus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('virus_taxid', models.CharField(max_length=100)),
                ('virus_ScientificName_CommonName', models.CharField(max_length=100)),
                ('virus_LineageInfo', models.CharField(max_length=200)),
                ('host_taxid', models.CharField(max_length=100)),
                ('host_Scientific_CommonName', models.CharField(max_length=100)),
                ('host_LineageInfo', models.CharField(max_length=200)),
                ('viralProteins_ViralProtein1_Accession_GeneName_ProteinName', models.CharField(max_length=100)),
                ('hostReceptorProteins_Receptor1_Accession_GeneName_ProteinName', models.CharField(max_length=100)),
                ('hostReceptorProteins_Receptor2_Accession_GeneName_ProteinName', models.CharField(max_length=100)),
                ('hostReceptorProteins_Receptor3_Accession_GeneName_ProteinName', models.CharField(max_length=100)),
                ('hostReceptorProteins_Receptor4_Accession_GeneName_ProteinName', models.CharField(max_length=100)),
                ('hostReceptorProteins_Receptor5_Accession_GeneName_ProteinName', models.CharField(max_length=100)),
                ('hostReceptorProteins_Receptor6_Accession_GeneName_ProteinName', models.CharField(max_length=100)),
                ('hostReceptorProteins_Receptor7_Accession_GeneName_ProteinName', models.CharField(max_length=100)),
                ('hostReceptorProteins_Receptor8_Accession_GeneName_ProteinName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Coronavirus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('virus_taxid', models.CharField(max_length=100)),
                ('virus_ScientificName_CommonName', models.CharField(max_length=100)),
                ('virus_LineageInfo', models.CharField(max_length=200)),
                ('host_taxid', models.CharField(max_length=100)),
                ('host_ScientificName_CommonName', models.CharField(max_length=100)),
                ('host_LineageInfo', models.CharField(max_length=200)),
                ('viralProteins_ViralProtein1_Accession_GeneName_ProteinName', models.CharField(max_length=100)),
                ('hostReceptorProteins_Receptor1_Accession_GeneName_ProteinName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Influenza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('virus_taxid', models.CharField(max_length=100)),
                ('virus_ScientificName_CommonName', models.CharField(max_length=100)),
                ('virus_LineageInfo', models.CharField(max_length=200)),
                ('host_taxid', models.CharField(max_length=100)),
                ('host_Scientific_CommonName', models.CharField(max_length=100)),
                ('host_LineageInfo', models.CharField(max_length=200)),
                ('viralProteins_ViralProtein1_Accession_GeneName_ProteinName', models.CharField(max_length=100)),
                ('viralProteins_ViralProtein2_Accession_GeneName_ProteinName', models.CharField(max_length=100)),
                ('viralProteins_ViralProtein3_Accession_GeneName_ProteinName', models.CharField(max_length=100)),
                ('viralProteins_ViralProtein4_Accession_GeneName_ProteinName', models.CharField(max_length=100)),
                ('hostReceptorProteins_Receptor1_Accession_GeneName_ProteinName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Virus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('qt', models.IntegerField()),
            ],
        ),
    ]
