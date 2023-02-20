from django.db import models

# Create your models here.
class TbAplication(models.Model):
    Id_Aplication  = models.AutoField(db_column='Id_Aplication', primary_key=True)
    nameAplication = models.CharField(db_column='nameAplication', max_length=255 , null=False)
    isActive       = models.BooleanField(db_column= 'isActive', default=True)

    def __str__(self):
        return self.nameAplication
    class Meta:
        managed  = True
        db_table = 'Tb_Aplication'

class TbModule(models.Model):
    Id_Module  = models.AutoField(db_column='Id_Module', primary_key=True)
    nameModule = models.CharField(db_column='nameModule', max_length=255 , null=False)

    # Tables Dependencies
    aplication = models.ForeignKey( 'TbAplication' , db_column='Id_Aplication', on_delete=models.CASCADE)


    def __str__(self):
        return self.nameModule
    class Meta:
        managed  = True
        db_table = 'Tb_Module'

class TbSection(models.Model):
    Id_Section  = models.AutoField(db_column='Id_Section', primary_key=True)
    nameSection = models.CharField(db_column='nameSection', max_length=255 , null=False)

    # Tables Dependencies
    aplication = models.ForeignKey( 'TbAplication' , db_column='Id_Aplication', on_delete=models.CASCADE)

    def __str__(self):
        return self.nameSection
    class Meta:
        managed  = True
        db_table = 'Tb_Section'

