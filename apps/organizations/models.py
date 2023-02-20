from django.db       import models

# Create your models here.
class TbOrganization(models.Model):
    
    Id_Organization          = models.AutoField(db_column='Id_Organization', primary_key=True)
    nameOrganization         = models.CharField(db_column='nameOrganization', max_length=255 , null=False)
    taxIdOrganization        = models.CharField(db_column='taxIdOrganization', max_length=255 , null=False)
    addressOrganization      = models.CharField(db_column='addressOrganization', max_length=255 , null=False)
    contactEmailOrganization = models.CharField(db_column='contactEmailOrganization', max_length=255 , null=False)
    isActive                 = models.BooleanField(db_column= 'isActive', default=True)

    # Dependencies tables
    city                     = models.ForeignKey( 'generals.TbCity' , db_column='Id_City', on_delete=models.CASCADE)

    def __str__(self):
        return self.nameOrganization
    class Meta:
        managed  = True
        db_table = 'Tb_Organization'