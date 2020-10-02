from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView
)
from django.shortcuts import get_list_or_404
from rest_framework.permissions import(
	IsAuthenticatedOrReadOnly
)
from .serializers import (
	ItemListSerializer,
	ItemDetailSerializer,
	ItemCreateSerializer
)
from bj_app.models import BJ_ITEM
from .permissions import IsOwnerOrReadOnly


class ItemCreateView(CreateAPIView):
	serializer_class = ItemCreateSerializer

	def perform_create(self,serializer):
		serializer.save(author=self.request.user)


class ItemDeleteView(DestroyAPIView):
	lookup_field = 'pk'
	queryset = BJ_ITEM.objects.all()
	serializer_class = ItemListSerializer


class ItemListView(ListAPIView):
	queryset = BJ_ITEM.objects.all()
	serializer_class = ItemListSerializer


class ItemDetailView(RetrieveAPIView):
	lookup_field = 'pk'
	queryset = BJ_ITEM.objects.all()
	serializer_class = ItemDetailSerializer


class ItemUpdateView(RetrieveUpdateAPIView):
	lookup_field = 'pk'
	queryset = BJ_ITEM.objects.all()
	serializer_class = ItemCreateSerializer
	permission_classes = (IsOwnerOrReadOnly,)


class AuthorItemView(APIView):
	@staticmethod
	def get(request, userid):
		items = get_list_or_404(BJ_ITEM, author__username=userid)
		item_data = ItemListSerializer(items, many=True)
		return Response(item_data.data)















# from django.utils import timezone
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
# from rest_framework import permissions 
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.permissions import IsAdminUser
# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     ListCreateAPIView,
#     DestroyAPIView,
#     UpdateAPIView
# )
# from bj_app.models import BJ_BOARD, BJ_ITEM, BJ_COMMENT
# from .serializers import ItemSerializer


# class ItemListView(ListAPIView):
#     queryset = BJ_ITEM.objects.all()
#     serializer_class = ItemSerializer
#     permission_classes = (permissions.AllowAny, )


# class ItemDetailView(RetrieveAPIView):
#     queryset = BJ_ITEM.objects.all()
#     serializer_class = ItemSerializer
#     permission_classes = (permissions.AllowAny, )


# class ItemCreateView(ListCreateAPIView):
#     permission_classes = (permissions.AllowAny,)

#     @api_view(['GET', 'POST'])

#     def startCall(request):
#         if request.method == 'POST':
#             serializer = ItemSerializer(data=request.data)
#             data={}
#         if serializer.is_valid():
#             datas = serializer.save()
#             data['bj_title']=datas.bj_title
#             data['bj_content']=datas.bj_content
#             data['bj_reportingTime']=datas.bj_reportingTime
#             data['bj_views']=datas.bj_views
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response(data)

#     # def create(bj_title, bj_content):
#     #     item = BJ_ITEM()
#     #     item.bj_title = bj_title
#     #     item.bj_content = bj_content
#     #     item.bj_reportingTime = timezone.datetime.now()
#     #     item.bj_views = 0
#     #     item.save()
#     #     return 

    

#     #  def list(self, request):
#     #     queryset = self.get_queryset()
#     #     serializer = ItemSerializer(queryset, many=True)
#     #     return Response(serializer.data)


# class ItemUpdateView(UpdateAPIView):
#     queryset = BJ_ITEM.objects.all()
#     serializer_class = ItemSerializer
#     permission_classes = (permissions.IsAuthenticated, )


# class ItemDeleteView(DestroyAPIView):
#     queryset = BJ_ITEM.objects.all()
#     serializer_class = ItemSerializer
#     permission_classes = (permissions.IsAuthenticated, )