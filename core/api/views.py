from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import SiteSerializer


class SiteListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SiteSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.order_by('-id').all()


class SiteCreateView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SiteSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class SiteVoteView(UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SiteSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = self.model.objects.get(pk=pk)
        instance.vote_count += 1
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
