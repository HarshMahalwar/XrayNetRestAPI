from django.urls import path
from core.schema import schema
from graphene_file_upload.django import FileUploadGraphQLView

urlpatterns = [
    path('graphql', FileUploadGraphQLView.as_view(graphiql=True, schema=schema)),
]