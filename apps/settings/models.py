from django.db       import models

# Create your models here.
class TbSetting(models.Model):
    Id_Setting  = models.AutoField(db_column='Id_Setting', primary_key=True)
    dataSetting = models.TextField(db_column='dataSetting', null=False)

    #  Dependencies tables
    device      = models.ForeignKey( 'devices.TbDevice' , db_column='Id_Device', on_delete=models.CASCADE)
    settingType = models.ForeignKey( 'generals.TbSettingType', db_column='Id_SettingType', on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.dataSetting

    class Meta:
        managed  = True
        db_table = 'Tb_Setting'
