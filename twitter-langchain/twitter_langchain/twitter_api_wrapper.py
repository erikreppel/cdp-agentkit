"""Util that calls Twitter API."""

import contextvars
import inspect
from collections.abc import Callable
from typing import Any

#  from contextvars_registry import ContextVarsRegistry
from cdp_agentkit_core.actions.social.twitter import TwitterContext
from langchain_core.utils import get_from_dict_or_env
from pydantic import BaseModel, Field, model_validator

import cdp_agentkit_core.actions.social.twitter.context as context
from cdp_agentkit_core.actions.social.twitter.mentions_monitor_start import get_thread

#  class TwitterContext(ContextVarsRegistry):
#      client: tweepy.Client | None = None

class TwitterApiWrapper(BaseModel):
    """Wrapper for Twitter API."""

    #  twitterContext: TwitterContext | None = None
    #  client:tweepy.Client = Field(..., description="twitter client")

    @model_validator(mode="before")
    @classmethod
    def validate_environment(cls, values: dict) -> Any:
        """Validate that Twitter access token, token secret, and tweepy exists in the environment."""
        api_key = get_from_dict_or_env(values, "twitter_api_key", "TWITTER_API_KEY")
        api_secret = get_from_dict_or_env(values, "twitter_api_secret", "TWITTER_API_SECRET")
        access_token = get_from_dict_or_env(values, "twitter_access_token", "TWITTER_ACCESS_TOKEN")
        access_token_secret = get_from_dict_or_env(values, "twitter_access_token_secret", "TWITTER_ACCESS_TOKEN_SECRET")
        bearer_token = get_from_dict_or_env(values, "twitter_bearer_token", "TWITTER_BEARER_TOKEN")

        try:
            import tweepy
        except Exception:
            raise ImportError(
                "Tweepy Twitter SDK is not installed. " "Please install it with `pip install tweepy`"
            ) from None

        #  api_auth = tweepy.OAuth1UserHandler(
        #      api_key,
        #      api_secret,
        #      access_token,
        #      access_token_secret,
        #      )

        #  api = tweepy.API(api_auth)

        client = tweepy.Client(
            bearer_token=bearer_token,
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
        )

        #  ctx = context.get_context()
        #  ctx.set_client(client)

        #  context.set_context(ctx)

        context.set_client(client)

        #  with context.context() as ctx:
        #      ctx.set_client(client)

        #  twitterContext = TwitterContext()
        #  context.set_api(api)
        #  twitterContext.set_client(client)

        #  context.client.set(client)

        #  values["twitterContext"] = twitterContext
        #  values["api"] = api
        values["client"] = client
        values["api_key"] = api_key
        values["api_secret"] = api_secret
        values["access_token"] = access_token
        values["access_token_secret"] = access_token_secret

        return values

    def run_action(self, func: Callable[..., str], **kwargs) -> str:
        """Run a Twitter Action."""
        #  import tweepy

        #  func_signature = inspect.signature(func)
        #  first_kwarg = next(iter(func_signature.parameters.values()), None)

        response = ""

        #  with context.context() as ctx:
        #      print("client")
        #      print(ctx.get_client())

            #  ctx.set_client(self.client)

        #  ctx = contextvars.copy_context()
        #  for var, value in ctx.items():
        #      var.set(value)

        print("client")
        print(context.get_client())
        print(context.unwrap())
        print(get_thread())

        if context.unwrap() is not None:
            print("yay?")
            print(context.unwrap().mentions.get())
        func(**kwargs)

        return response

        #  if first_kwarg and first_kwarg.annotation is tweepy.Client:
        #      return func(self.client, **kwargs)
        #  else:
        #      return func(**kwargs)
