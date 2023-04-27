from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from post_service.models import Post as PostModel


class Post(SQLAlchemyObjectType):
    class Meta:
        model = PostModel
        interfaces = (relay.Node,)
