from rest_framework import serializers 
from .models import Car
import datetime

class CarSerializer(serializers.ModelSerializer):
    buy_time = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = '__all__'

    def get_buy_time(self, obj):
        if isinstance(obj.buy_time, (datetime.date, datetime.datetime)):
            return obj.buy_time.isoformat()
        return None 