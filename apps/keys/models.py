from django.db             import models

# Create your models here.
class TbKey(models.Model):
    Id_Key    = models.AutoField(db_column='Id_Key', primary_key=True)
    nameKey   = models.CharField(db_column='nameKey', max_length=255 ,null=False)
    valueKey  = models.TextField(db_column='valueKey' ,null=False)

    #  Dependencies tables
    organization = models.ForeignKey( 'organizations.TbOrganization', db_column='Id_Organization', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nameKey

    class Meta:
        managed  = True
        db_table = 'Tb_Key'