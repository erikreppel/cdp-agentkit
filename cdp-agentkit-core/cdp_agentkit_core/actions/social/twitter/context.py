from contextvars import ContextVar
from contextlib import contextmanager

import tweepy
from pydantic import Field

from cdp_agentkit_core.actions.context import Context
from cdp_agentkit_core.actions.social.twitter.mentions import Mentions


class TwitterContext(Context):
    #  class Config:
    #      arbitrary_types_allowed = True

    client: ContextVar[tweepy.Client] = ContextVar("client", default=None)
    mentions: Mentions = Mentions()


def context() -> TwitterContext:
    return _context.get()


@contextmanager
def current():
    ctx = _context.get()

    if ctx is None:
        raise RuntimeError("Twitter (X) context is unavailable within this scope.")

    try:
        yield ctx
    finally:
        pass


@contextmanager
def new():
    ctx = TwitterContext()
    token = _context.set(ctx)
    try:
        yield ctx
    finally:
        _context.reset(token)


_context = ContextVar('twitter_context', default=None)
_context.set(TwitterContext())
