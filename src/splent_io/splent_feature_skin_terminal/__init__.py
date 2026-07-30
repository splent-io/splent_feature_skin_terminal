from splent_framework.blueprints.base_blueprint import create_blueprint

skin_terminal_bp = create_blueprint(__name__)

# Design tokens for the EGC course wiki. Crimson and charcoal are the two
# colours of the subject's logo; the mono display face is what puts the site
# name behind a "~/" prompt and gives code an editor voice.
#
# Light and dark are two palettes, not one palette dimmed. The dark values
# live in the stylesheet's prefers-color-scheme block because the token
# vocabulary is a single set of values and cannot hold both.
EGC_TOKENS = {
    "primary": "#9b1130",
    "primary_contrast": "#ffffff",
    # Charcoal is the quiet half of the identity: body copy, and the eyebrow
    # where a marketing site would put a second colour.
    "accent": "#3a3a3a",
    "bg": "#ffffff",
    "surface": "#f6f7f8",
    "text": "#3a3a3a",
    "heading": "#1c1f24",
    "muted": "#6b7280",
    "border": "#e2e4e8",
    "radius": "6px",
    "container": "1120px",
    "font_body": "'IBM Plex Sans', system-ui, sans-serif",
    "font_heading": "'IBM Plex Sans', system-ui, sans-serif",
    "font_display": "'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, monospace",
    "font_url": "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap",
}


def init_feature(app):
    # A skin sets the theme tokens and registers its stylesheet (order 200, so it
    # cascades last) on top of the theme's brand-agnostic base public.css.
    from splent_framework.assets.asset_registry import register_asset

    app.config["THEME_TOKENS"] = EGC_TOKENS
    register_asset(
        "css",
        "skin_terminal.assets",
        order=200,
        subfolder="css",
        filename="skin_terminal.css",
    )


def inject_context_vars(app):
    return {}
