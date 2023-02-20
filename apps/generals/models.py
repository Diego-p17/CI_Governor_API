from django.db import models

#  -- General Tables -- #
class TbCity(models.Model):
    Id_City    = models.AutoField(db_column='Id_City', primary_key=True)
    nameCity   = models.CharField(db_column='nameCity' , max_length=255 , null=False)
    country    = models.ForeignKey('TbCountry', db_column='Id_Country' , on_delete=models.CASCADE)

    def __str__(self):
        return self.nameCity
    class Meta:
        managed  = True
        db_table = 'Tb_City'

class TbCountry(models.Model):
    Id_Country  = models.AutoField(db_column='Id_Country', primary_key=True)
    nameCountry = models.CharField(db_column='nameCountry',  max_length=255 , null=False)

    def __str__(self):
        return self.nameCountry
    class Meta:
        managed  = True
        db_table = 'Tb_Country'

class TbDeviceType(models.Model):
    Id_DeviceType  = models.AutoField(db_column='Id_DeviceType', primary_key=True)
    nameDeviceType = models.CharField(db_column='nameDeviceType', max_length=255 , null=False)

    def __str__(self):
        return self.nameDeviceType
    class Meta:
        managed  = True
        db_table = 'Tb_DeviceType'

class TbHwPlatform(models.Model):
    Id_HwPlatform  = models.AutoField(db_column='Id_HwPlatform', primary_key=True)
    nameHwPlatform = models.CharField(db_column='nameHwPlatform', max_length=255 , null=False)

    def __str__(self):
        return self.nameHwPlatform
    class Meta:
        managed  = True
        db_table = 'Tb_HwPlatform'

class TbOs(models.Model):
    Id_Os  = models.AutoField(db_column='Id_Os', primary_key=True)
    nameOs = models.CharField(db_column='nameOs', max_length=255 , null=False)

    def __str__(self):
        return self.nameOs
    class Meta:
        managed  = True
        db_table = 'Tb_Os'

class TbTokenType(models.Model):
    Id_TokenType  = models.AutoField(db_column='Id_TokenType', primary_key=True)
    nameTokenType = models.CharField(db_column='nameTokenType', max_length=255 , null=False)

    def __str__(self):
        return self.nameTokenType
    class Meta:
        managed  = True
        db_table = 'Tb_TokenType'

class TbSettingType(models.Model):
    Id_SettingType  = models.AutoField(db_column='Id_SettingType', primary_key=True)
    nameSettingType = models.CharField(db_column='nameSettingType', max_length=255 , null=False)

    def __str__(self):
        return self.nameSettingType
    class Meta:
        managed  = True
        db_table = 'Tb_SettingType'
class TbLevelKeys(models.Model):
    Id_LevelKeys  = models.AutoField(db_column='Id_TokenType', primary_key=True)
    nameLevelKeys = models.CharField(db_column='nameLevelKeys', max_length=255 , null=False)

    def __str__(self):
        return self.nameLevelKeys
    class Meta:
        managed  = True
        db_table = 'Tb_LevelKeys'