from django.db        import models


# Create your models here.
class TbToken(models.Model):
    id_Token   = models.AutoField(db_column='Id_Token', primary_key=True)
    valueToken = models.CharField(db_column='valueToken', max_length=255 , null=True)
    isActive   = models.BooleanField( db_column='isActive', default=True)
    Id_Owner   = models.IntegerField(db_column='Id_Owner' , null=False)
    
    # Dependencies tables
    tokenType  = models.ForeignKey( 'generals.TbTokenType' , db_column='Id_TokenType' , on_delete=models.CASCADE)
    people     = models.ForeignKey( 'peoples.TbPeople' , db_column='Id_People' , on_delete=models.CASCADE)


    def __str__(self):
        return self.valueToken
    class Meta:
        managed  = True
        db_table = 'Tb_Token'