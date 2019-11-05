from rest_framework import serializers

from core.models import Tag, Ingredient, Post, Image


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_Fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for an ingredient object"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)


class PostImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to Post"""
    imageRef = serializers.ImageField(max_length=None, allow_empty_file=True, allow_null=True, required=False)
    class Meta:
        model = Image
        fields = ('id', 'imageRef',)
        read_only_fields = ('id',)


class PostSerializer(serializers.ModelSerializer):
    """Serialize a Post"""
    # images = PostImageSerializer(many=True)
    # images = PostImageSerializer(many=True)
    # ingredients = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Ingredient.objects.all()
    # )
    # tags = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Tag.objects.all()
    # )

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'time_minutes', 'price',
            'link',
        )
        read_only_fields = ('id',)

    # def create(self, validated_data):
    #     print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    #     print(validated_data)
    #     images_data = validated_data.pop('images')
    #     post = Post.objects.create(**validated_data)
    #     print(len(images_data))
    #     for image in images_data:
    #         # image['post'] = post
    #         Image.objects.create(post=post, **image)
    #     return post


class PostDetailSerializer(PostSerializer):
    # ingredients = IngredientSerializer(many=True, read_only=True)
    # tags = TagSerializer(many=True, read_only=True)
    print("vwvwvwvvwvwvvwvwvwvwwv")
    images = PostImageSerializer(many=True)