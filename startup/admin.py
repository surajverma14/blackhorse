from django.contrib import admin
from .models import Entity , Founder ,Startup_Funding_Details,Upload_video_pitch,Upload_pitch_deck,Upload_financials ,Cofounder,Cofounder3,Cofounder4
# Register your models here.


admin.site.register(Entity)
admin.site.register(Founder)
admin.site.register(Upload_video_pitch)
admin.site.register(Upload_pitch_deck)
admin.site.register(Upload_financials)
admin.site.register(Cofounder)
admin.site.register(Cofounder3)
admin.site.register(Cofounder4)
#admin.site.register(Startup_Funding_Details)
