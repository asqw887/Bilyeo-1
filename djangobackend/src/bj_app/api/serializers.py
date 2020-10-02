from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	StringRelatedField
)
from bj_app.models import BJ_BOARD, BJ_ITEM, BJ_COMMENT

class ItemListSerializer(ModelSerializer):
	
	author = StringRelatedField()
	
	class Meta:
		model = BJ_ITEM
		fields = ('bj_id','bj_title', 'bj_content', 'bj_views', 'author', 'published')


class ItemDetailSerializer(ModelSerializer):

	author = StringRelatedField()

	class Meta:

		model = BJ_ITEM
		lookup_field = 'pk'
		fields = ('bj_title', 'bj_content', 'author', 'bj_views', 'published')


class ItemCreateSerializer(ModelSerializer):
	
	author = StringRelatedField()
	
	class Meta:
		model = BJ_ITEM
		fields = ('bj_title', 'bj_content', 'author', 'published')




# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BJ_COMMENT
#         fields = ('bj_comment_id', 'bj_comment_datetime', 'bj_comment_content')

# class CreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BJ_ITEM
#         fields = ('user_id','bj_title', 'bj_content', 'bj_reportingTime', 'bj_views')