from django.db            import models

# Create your models here.
class TbPeople(models.Model):
    Id_People    = models.AutoField(db_column='Id_People', primary_key=True)
    Id_Username  = models.CharField(db_column='Id_Username', max_length=255,null=False)
    namePeople   = models.CharField(db_column='namePeople', max_length=255 , null=False)
    emailPeople  = models.CharField(db_column='emailPeople', max_length=255 , null=False)
    phonePeople  = models.BigIntegerField(db_column='phonePeople')
    

    # Dependencies tables
    organization = models.ForeignKey( 'organizations.TbOrganization' , db_column='Id_Organization', on_delete=models.CASCADE)

    def __str__(self):
        return self.namePeople
    class Meta:
        managed  = True
        db_table = 'Tb_People'
