# from rest_framework import status
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView

from pi_web_rest.serializers import PIValueSerializer, PIRecordedValuesSerializer
import pi_web_rest.pi_functions as pf
from rest_framework import mixins
from rest_framework import generics

# @api_view(['GET'])
# def current_values(request, str_taglist, format=None):
#     """
#     获取tag点的当前值
#     """
#     if request.method == 'GET':
#         tags = str_taglist.split(',')
#         pi_values = pf.get_current_values(tags)
#         serializer = PIFloatValueSerializer(pi_values, many=True)
#         return Response(serializer.data)


class CurrentValues(APIView):
    def get(self, request, str_taglist, format=None):
        tags = str_taglist.split(',')
        pi_values = pf.get_current_values(tags)
        serializer = PIValueSerializer(pi_values, many=True)
        return Response(serializer.data)

class RecordedValues(APIView):
    def get(self, request, str_taglist, begin, end, format=None):
        tags = str_taglist.split(',')
        recorded_values = pf.get_recorded_values(tags, begin, end)
        serializer = PIRecordedValuesSerializer(recorded_values,  many=True)
        return Response(serializer.data)