import os

from dynaconf import Dynaconf
from fastapi.templating import Jinja2Templates


ENV = os.environ.get("DYNACONF_ENV", "local")

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    environment=True,
    default_env="base",
    includes=["configs/**/*"],
    env=ENV,
)


templates = Jinja2Templates(directory="templates")
