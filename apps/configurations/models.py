from django.db       import models

# Create your models here.
class TbConfiguration(models.Model):
    Id_Configuration  = models.AutoField(db_column='Id_Configuration', primary_key=True)
    dataConfiguration = models.TextField(db_column='dataConfiguration', null=False)

    #  Dependencies tables
    key      = models.ForeignKey( 'keys.TbKey' , db_column='Id_Key', on_delete=models.CASCADE)
    levelKey = models.ForeignKey( 'generals.TbLevelKeys', db_column='Id_LevelKey', on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.dataConfiguration

    class Meta:
        managed  = True
        db_table = 'Tb_Configuration'