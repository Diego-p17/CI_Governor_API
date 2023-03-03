from django.db import models

# Create your models here.
class TbPeopleModule(models.Model):
    Id_PeopleModule  = models.AutoField(db_column='Id_PackageConfigKeys', primary_key=True)
    valueModule      = models.TextField(db_column='valueModule', null= False)

    #  Dependencies tables
    people      = models.ForeignKey( 'peoples.TbPeople', db_column='Id_People', on_delete=models.CASCADE)
    aplication  = models.ForeignKey( 'aplications.TbAplication', db_column='Id_Aplication', on_delete=models.CASCADE)

    class Meta:
        managed  = True
        db_table = 'Tb_PeopleModule'