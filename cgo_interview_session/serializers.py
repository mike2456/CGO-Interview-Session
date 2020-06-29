from rest_framework import serializers


class CGO_Interview_Session_Serializer(serializers.Serializer):
    opposite_bank = serializers.IntegerField()
    falling_leaves_list = serializers.ListField(child=serializers.IntegerField())