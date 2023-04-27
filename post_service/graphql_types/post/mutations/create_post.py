from typing import Any, Dict, List

import graphene
from graphene import relay

posts: List[Dict[str, Any]] = []


class CreatePost(relay.ClientIDMutation):
    class Input:
        title = graphene.Argument(
            graphene.String(required=True),
        )
        content = graphene.Argument(graphene.String(required=True))

    ok = graphene.Boolean()
    post = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        title = input.get("title")
        content = input.get("content")
        post = {"id": 1, "title": title, "content": content}
        post.append(post)
        return CreatePost(ok=True, post=post)
