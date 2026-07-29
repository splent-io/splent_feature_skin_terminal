"""
Functional tests for splent_feature_skin_egc.

Functional tests use Flask's test client to exercise full HTTP
request/response cycles (GET, POST, redirects, rendered HTML).

A skin is a config feature: it registers no routes, it publishes design
tokens and one stylesheet that the theme cascades after its own. The
scaffolded test asked for a page the skin never serves. These assert what
the skin actually contributes.
"""

from splent_framework.assets.asset_registry import get_assets
from splent_io.splent_feature_skin_egc import EGC_TOKENS


def test_tokens_are_published_to_the_theme(test_client):
    assert test_client.application.config["THEME_TOKENS"] == EGC_TOKENS


def test_stylesheet_is_registered_last(test_client):
    # get_assets resolves each URL with url_for, so it needs a request
    # context; without one every asset is skipped and the list comes back
    # empty.
    with test_client.application.test_request_context():
        urls = get_assets("css")
    assert any("skin_egc.css" in url for url in urls)
    # Registered at order 200 so it cascades after the theme base and any
    # feature stylesheet, which is what makes the skin win.
    assert "skin_egc.css" in urls[-1]
