from django.db       import models

# Create your models here.
class TbPackageConfig(models.Model):
    Id_PackageConfig  = models.AutoField(db_column='Id_PackageConfig', primary_key=True)
    namePackage       = models.CharField(db_column='namePackage',max_length=255, null=False)
    #  Dependencies tables
    organization = models.ForeignKey( 'organizations.TbOrganization', db_column='Id_Organization', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.namePackage

    class Meta:
        managed  = True
        db_table = 'Tb_PackageConfig'