from django.db             import models

# Create your models here.
class TbDevice(models.Model):
    Id_Device           = models.AutoField(db_column='Id_Device', primary_key=True)
    nameDevice          = models.CharField(db_column='nameDevice', max_length=255 , null=False)
    tokenDevice         = models.CharField(db_column='tokenDevice', max_length=255 , null=False)
    creationDateDevice  = models.DateTimeField(db_column='creationDateDevice', auto_now_add=True)
    isActive            = models.BooleanField( db_column='isActive', default=True)

    # Dependencies tables
    hwPlatform   = models.ForeignKey( 'generals.TbHwPlatform' , db_column='Id_HwPlatform', on_delete=models.CASCADE)
    os           = models.ForeignKey( 'generals.TbOs' , db_column='Id_Os', on_delete=models.CASCADE)
    deviceType   = models.ForeignKey( 'generals.TbDeviceType' , db_column='Id_DeviceType', on_delete=models.CASCADE)
    organization = models.ForeignKey( 'organizations.TbOrganization' , db_column='Id_Organization', on_delete=models.CASCADE)

    def __str__(self):
        return self.nameDevice
    class Meta:
        managed  = True
        db_table = 'Tb_Device'