from graphene import ObjectType

from .post.queries.post import PostQuery


class Query(PostQuery, ObjectType):
    pass
