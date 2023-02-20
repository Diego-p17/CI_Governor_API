from django.db             import models


# Create your models here.
class TbPermission(models.Model):
    Id_Permission  = models.AutoField(db_column='Id_Permission', primary_key=True)
    dataPermission = models.TextField(db_column='dataPermission', null=False)

    #  Dependencies tables
    aplication   = models.ForeignKey( 'aplications.TbAplication' , db_column='Id_Aplication', on_delete=models.CASCADE)
    organization = models.ForeignKey( 'organizations.TbOrganization', db_column='Id_Organization', on_delete=models.CASCADE)
    people       = models.ForeignKey( 'peoples.TbPeople' , db_column='id_People', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.dataPermission

    class Meta:
        managed  = True
        db_table = 'Tb_Permission'