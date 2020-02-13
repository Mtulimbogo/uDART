import django_tables2 as tables
from .models import gate_detail , train_detail

class GateTable(tables.Table):
    class Meta:
        model = gate_detail
        
class TrainTable (tables.Table):
    class Meta: 
        model = train_detail
        template_name = "django_tables2/bootstrap.html"
        fields = ("train_name","station_of_origin","tag_id","train_type",)