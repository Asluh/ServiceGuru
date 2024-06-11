from rest_framework import serializers

from api.models import Customer,Work


class WorkSerializers(serializers.ModelSerializer):
    
    customer=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        
        model=Work

        fields="__all__"

        read_only_fields=['id','customer','status','created_date','updated_date','is_active']

class CustomerSerializers(serializers.ModelSerializer):
    
    technician=serializers.StringRelatedField(read_only=True)
    
    work_count=serializers.CharField(read_only=True)
    
    work_total=serializers.CharField(read_only=True)
    # works=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Customer

        fields="__all__"

        read_only_fields=['id','technician','status','created_date','updated_date','is_active']