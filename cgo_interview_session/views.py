from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import CGO_Interview_Session_Serializer


class CGO_Interview_Session(APIView):

    def post(self, request, format=None):
        serializer = CGO_Interview_Session_Serializer(data=request.data)

        if serializer.is_valid():
            opposite_bank = serializer.data['opposite_bank']
            falling_leaves_list = serializer.data['falling_leaves_list']
            return Response(self.solution(opposite_bank, falling_leaves_list))
  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def solution(self, X, A):
        path_incomplete = -1
        destination_path = X
        to_find_path = [-1] * (X)
        falling_leaves = range(0,len(A))    
        
        for index in falling_leaves:
            leaf_position = A[index]

            if to_find_path[leaf_position-1] != -1:
                continue

            else:
                to_find_path[leaf_position-1] = index
                destination_path -= 1

                if destination_path == 0:
                    return index

        return path_incomplete