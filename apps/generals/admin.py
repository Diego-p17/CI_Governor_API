from django.contrib import admin
from .models        import *

# Register your models here.
admin.site.register(TbCity)
admin.site.register(TbCountry)
admin.site.register(TbDeviceType)
admin.site.register(TbHwPlatform)
admin.site.register(TbOs)
admin.site.register(TbSettingType)
admin.site.register(TbTokenType)

