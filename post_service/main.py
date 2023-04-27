import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from post_service.graphql_types.root_mutation import Mutation as AllMutations
from post_service.graphql_types.root_query import Query as AllQueries

app = FastAPI()

schema = graphene.Schema(query=AllQueries, mutation=AllMutations)
app.add_route("/", GraphQLApp(schema=schema))
