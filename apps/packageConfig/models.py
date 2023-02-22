from django.db       import models

# Create your models here.
class TbPackageConfig(models.Model):
    Id_PackageConfig  = models.AutoField(db_column='Id_PackageConfig', primary_key=True)
    namePackage       = models.CharField(db_column='namePackage',max_length=255, null=False)
    site              = models.IntegerField(db_column='Id_Site', default=0, null=True)
    zone              = models.IntegerField(db_column= 'Id_Zone', default=0, null=True)
    #  Dependencies tables
    organization = models.ForeignKey( 'organizations.TbOrganization', db_column='Id_Organization', on_delete=models.CASCADE)
    deviceType   = models.ForeignKey( 'generals.TbDeviceType', db_column='Id_DeviceType', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.namePackage

    class Meta:
        managed  = True
        db_table = 'Tb_PackageConfig'