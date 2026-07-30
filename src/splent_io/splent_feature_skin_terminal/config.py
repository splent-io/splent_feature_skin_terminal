"""
skin_terminal feature configuration.

The skin has no environment variables. What it publishes is a palette, and a
palette belongs to the feature rather than to the deployment: an EGC wiki is
EGC-coloured wherever it runs. The tokens therefore live in __init__ and this
hook stays empty, so the loader has nothing to inject.

To regenerate from source code: splent feature:inject-config splent_feature_skin_terminal
"""


def inject_config(app):
    return
