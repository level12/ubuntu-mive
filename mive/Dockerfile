
arg UBUNTU_TAG=24.04
arg PYTHON_VER=3.12

from ghcr.io/level12/ubuntu-base:24.04

# Has to be referenced in this build stage to be viewable
arg PYTHON_VER

# WARN: these images are not automatically refreshed with `docker compose --pull` and need to be
# pulled manually before building this image.  `mise build.sh` will do this for you.
#
# NOTE: it's faster to copy the layers than to install manually and we benefit from Docker's layer
# caching to not do any work if upstream hasn't changed.
copy --from=jdxcode/mise:latest /usr/local/bin/mise /usr/local/bin/
copy --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# `mise sync python --uv` errors when when this directory isn't present.
# Refs: https://github.com/jdx/mise/discussions/4474
run mkdir -p /home/ubuntu/.local/share/uv/python/

# Mise tools install
run mise install python@${PYTHON_VER} \
    && mise sync python --uv
