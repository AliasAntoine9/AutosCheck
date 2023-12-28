import os

from dynaconf import Dynaconf


VERSION = "1.0.0"
PREFIX = "/api/v1"
ENV = os.environ.get("DYNACONF_ENV", "local")

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    environment=True,
    default_env="base",
    includes=["configs/**/*"],
    env=ENV,
)
