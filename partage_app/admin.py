from django.contrib import admin
import partage_app.models as model

admin.site.register(model.Location)
admin.site.register(model.Shareable)
admin.site.register(model.Category)
