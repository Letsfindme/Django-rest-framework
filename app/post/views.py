from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

from core.models import Tag, Ingredient, Post, Image

from post import serializers


class TagViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    """Manage tags in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Create a new ingredient"""
        serializer.save(user=self.request.user)


class IngredientViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin):
    """Manage ingredients in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')


class BasePostAttrViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    """Base viewset for user owned Post attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        """Return objects for current user"""
        assigned_only = bool(self.request.query_params.get('assigned_only'))
        queryset = self.queryset
        if assigned_only:
            queryset = queryset.filter(post__isnull=False)

        return queryset.filter(
            user=self.request.user
        ).order_by('-name').distinct()


class PostViewSet(viewsets.ModelViewSet):
    """Manage Posts in the database"""
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser, MultiPartParser, FormParser,)

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]
    
    def get_queryset(self):
        """Retrieve the posts for the authenticated user"""
        tags = self.request.query_params.get('tags')
        ingredients = self.request.query_params.get('ingredients')
        queryset = self.queryset
        if tags:
            tag_ids = self._params_to_ints(tags)
            queryset = queryset.filter(tags__id__in=tag_ids)
        if ingredients:
            ingredient_ids = self._params_to_ints(ingredients)
            queryset = queryset.filter(ingredients__id__in=ingredient_ids)
    
        return queryset.filter(user=self.request.user)

    # def get_serializer_class(self):
    #     """Return appropriate serializer class"""
    #     return serializers.PostSerializer
        # if self.action == 'retrieve':
        #     return serializers.PostDetailSerializer
        # elif self.action == 'upload_image':
        #     return serializers.PostImageSerializer

        # return self.serializer_class

 
    def post(self, request, *args, **kwargs):
        # property_id = request.data['property_id']
        files_list = request.FILES
        data = request.data
        print(len(files_list))
        print(len(data))
        # serializer = self.get_serializer(
        #     post,
        #     data=request.data
        # )
        # serializer.save(user=self.request.user)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        # converts querydict to original dict
        # images = dict((request.data).lists())['image']
        # flag = 1
        # arr = []
        # for img_name in images:
        #     modified_data = modify_input_for_multiple_files(property_id,
        #                                                     img_name)
        #     file_serializer = ImageSerializer(data=modified_data)
        #     if file_serializer.is_valid():
        #         file_serializer.save()
        #         arr.append(file_serializer.data)
        #     else:
        #         flag = 0

        # if flag == 1:
        #     return Response(arr, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(arr, status=status.HTTP_400_BAD_REQUEST)


    def perform_create(self, serializer):
        """Create a new ingredient"""
        serializer.save(user=self.request.user)

    # @action(methods=['POST'], detail=True, url_path='upload-image')
    # def upload_image(self, request, pk=None):
    #     """Upload an image to a post"""
    #     post = self.get_object()
    #     serializer = self.get_serializer(
    #         post,
    #         data=request.data
    #     )

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(
    #             serializer.data,
    #             status=status.HTTP_200_OK
    #         )

    #     return Response(
    #         serializer.errors,
    #         status=status.HTTP_400_BAD_REQUEST
    #     )