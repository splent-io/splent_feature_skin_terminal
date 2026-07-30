"""
Unit tests for splent_feature_skin_terminal.

Unit tests verify individual classes and functions in isolation.
External dependencies (DB, HTTP, other services) MUST be mocked.
These tests should be fast and have zero side effects.

A skin has no services. What it has is a dictionary, and the failure worth
catching is a key that is not part of the token vocabulary: a misspelt
token is ignored in silence and a missing one falls back to the neutral
default, so the product renders in a colour nobody chose.
"""

from splent_io.splent_feature_skin_terminal import EGC_TOKENS
from splent_io.splent_feature_theme.tokens import DEFAULT_TOKENS


def test_the_palette_covers_the_token_vocabulary_exactly():
    assert set(EGC_TOKENS) == set(DEFAULT_TOKENS)
