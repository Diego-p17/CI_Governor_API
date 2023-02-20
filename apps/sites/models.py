from django.db            import models

# Create your models here.
class TbSite(models.Model):
    
    Id_Site      = models.AutoField(db_column='Id_Site', primary_key=True)
    nameSite     = models.CharField(db_column='nameSite', max_length=255 , null=False)
    addressSite  = models.CharField(db_column='addressSite', max_length=255 , null=False)
    isActive     = models.BooleanField(db_column= 'isActive', default=True)

    # Dependencies tables
    organization = models.ForeignKey( 'organizations.TbOrganization' , db_column='Id_Organization', on_delete=models.CASCADE)
    city         = models.ForeignKey( 'generals.TbCity' , db_column='Id_City', on_delete=models.CASCADE)

    def __str__(self):
        return self.nameSite
    class Meta:
        managed  = True
        db_table = 'Tb_Site'
