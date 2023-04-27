from graphene import ObjectType

from .create_post import CreatePost


class PostMutations(ObjectType):
    create_post = CreatePost.Field()
