from rest_framework import serializers
from .models import Branch, Bank

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['name'] 

class BranchSerializer(serializers.ModelSerializer):
    bank = BankSerializer(source='bank_id') 

    class Meta:
        model = Branch
        fields = ['ifsc', 'branch', 'address', 'city', 'district', 'state', 'bank']
