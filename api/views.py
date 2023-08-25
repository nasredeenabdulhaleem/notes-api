from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, mixins
from rest_framework.request import Request

from rest_framework import generics
from api.models import Note
from .serializers import NoteSerializer
from .permissions import IsAuthor

# from rest_framework.permissions

# Create your views here.


class NoteApiView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    # query notes model base on user
    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)


notes_view = NoteApiView.as_view()


class NoteDetailView(generics.RetrieveAPIView):
    queryset = Note  # .objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    # query notes model base on user
    # def get_queryset(self):
    #     return Note.objects.filter(owner=self.request.user)

    def filter_queryset(self, queryset):
        return queryset.objects.filter(owner=self.request.user)


notes_detail_view = NoteDetailView.as_view()


class NoteCreateView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    queryset = Note  # .objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    # query notes model base on user
    def filter_queryset(self, queryset):
        return queryset.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user.id
        serializer.save(owner_id=user)
        return super().perform_create(serializer)

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


notes_create_view = NoteCreateView.as_view()


class NoteUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    # query notes model base on user
    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)


notes_update_view = NoteUpdateView.as_view()


class NoteDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    # query notes model base on user
    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)


notes_delete_view = NoteDeleteView.as_view()


class SearchListView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get("q")
        results = Note.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results
