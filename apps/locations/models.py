from django.db      import models

# Create your models here.
class TbLocation(models.Model):
    Id_Location     = models.AutoField(db_column='Id_Location', primary_key=True)
    addressLocation = models.CharField(db_column='addressLocation', max_length=255 , null=False)
    isActive        = models.BooleanField(db_column='isActive', default=True)
    
    # Tables Dependencies
    device = models.ForeignKey( 'devices.TbDevice',db_column='Id_Device', on_delete=models.CASCADE)
    site   = models.ForeignKey('sites.TbSite' ,db_column='Id_Site', on_delete=models.CASCADE)
    zone   = models.ForeignKey( 'zones.TbZone' ,db_column='Id_Zone', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.addressLocation

    class Meta:
        managed  = True
        db_table = 'Tb_Location'