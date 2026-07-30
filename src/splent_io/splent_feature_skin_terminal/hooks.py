"""Where this skin reaches parts of the product it does not own.

The public shell takes its stylesheet through the asset registry, which is
what a skin is for. The back office does not: splent_feature_admin ships a
Bootstrap shell of its own, and a reader who follows the sign-in link from a
crimson wiki used to land somewhere that looked like a different site.

That is fixed from here, through the layout.head.css slot the shell already
renders, with a stylesheet and nothing else. The admin feature is not
touched, not subclassed, and does not know this exists, which is the point:
a skin restyles a product, and a product is more than its front page.
"""

from flask import current_app, url_for
from markupsafe import Markup

from splent_framework.hooks.template_hooks import register_template_hook


def admin_stylesheet():
    """The skin's back-office stylesheet, and the tokens it is written in.

    The tokens come first and are not optional. The theme declares its
    ``--brand-*`` block in the public shell's template only, so on an admin
    page there are no tokens at all and a stylesheet written against them
    resolves to nothing: the file loads, the page does not change, and the
    only clue is that it looks exactly as it did before.

    Rendered after the shell's own stylesheets, so ordinary class selectors
    win on source order alone and nothing needs !important.
    """
    from splent_io.splent_feature_theme.tokens import get_tokens, tokens_to_css

    tokens = tokens_to_css(get_tokens(current_app))
    href = url_for(
        "skin_terminal.assets", subfolder="css", filename="admin_terminal.css"
    )
    return Markup(
        f'<style id="brand-tokens">{tokens}</style>'
        f'<link rel="stylesheet" href="{href}">'
    )


register_template_hook("layout.head.css", admin_stylesheet, order=200)
