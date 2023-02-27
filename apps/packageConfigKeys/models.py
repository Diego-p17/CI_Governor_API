from django.db import models

# Create your models here.
class TbPackageConfigKeys(models.Model):
    Id_PackageConfigKeys  = models.AutoField(db_column='Id_PackageConfigKeys', primary_key=True)
    organization          = models.IntegerField(db_column='Id_Configuration', null= False)
    site                  = models.IntegerField(db_column='Id_Site', default=0)
    zone                  = models.IntegerField(db_column= 'Id_Zone', default=0)
    #  Dependencies tables
    deviceType    = models.ForeignKey( 'generals.TbDeviceType', db_column='Id_DeviceType', on_delete=models.CASCADE)
    packageConfig = models.ForeignKey( 'packageConfig.TbPackageConfig', db_column='Id_PackageConfig', on_delete=models.CASCADE)
    keys          = models.ForeignKey( 'keys.TbKey', db_column='Id_Key', on_delete=models.CASCADE)

    class Meta:
        managed  = True
        db_table = 'Tb_PackageConfigKeys'
