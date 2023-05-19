from rest_framework import serializers
from apps.posts.models import Post
from datetime import timezone


class PostSerializers(serializers.ModelSerializer):
    creator = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields =[
            'id',
            'title',
            'body',
            'creator',
            'created_at',
            'updated_at',
        ]
        
    def create(self, validated_data):
        user = self.context.get('user')
        print(user.nim)
        obj_post = Post.objects.create(
            title = validated_data.get('title'),
            body = validated_data.get('body'),
            creator=user
        )
        return obj_post
    
    def update(self, instance, validated_data):
        title = validated_data.get('title')
        body = validated_data.get('body')

        post_instance = Post.objects.filter(id=instance.id).first()
        post_instance.title = title
        post_instance.body = body
        post_instance.save()

        return post_instance

class PostDestroySerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields =[
            'id',
            'title',
            'body',
            'creator',
            'created_at',
        ]

    def destroy(self, instance):
        # get_id_Documents = validated_data.get("id")
        Post.objects.filter(id=instance.id).update(is_deleted=True)