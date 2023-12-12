from rest_framework import mixins, viewsets


class CreateListMixin(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    pass
