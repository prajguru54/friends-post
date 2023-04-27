from graphene import ObjectType

from .post.mutations import PostMutations


class Mutation(PostMutations, ObjectType):
    pass
