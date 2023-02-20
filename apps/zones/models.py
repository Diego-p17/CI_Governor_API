from django.db     import models

# Create your models here.
class TbZone(models.Model):
    Id_Zone  = models.AutoField(db_column='Id_Zone', primary_key=True)
    nameZone = models.CharField(db_column='nameZone', max_length=255 , null=False)

    # Dependencies tables
    site = models.ForeignKey( 'sites.TbSite' , db_column='Id_Site', on_delete=models.CASCADE)

    def __str__(self):
        return self.nameZone
    class Meta:
        managed  = True
        db_table = 'Tb_Zone'
