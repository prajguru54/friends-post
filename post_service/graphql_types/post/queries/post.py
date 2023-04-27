import graphene

from db_conf import session
from post_service.models import Post as PostModel

from ..node.post import Post


class PostQuery(graphene.ObjectType):
    post = graphene.relay.Node.Field(Post)
    all_posts = graphene.List(Post)

    def resolve_all_posts(self):
        return session.query(PostModel).all()
