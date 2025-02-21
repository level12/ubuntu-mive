arg UBUNTU_TAG=24.04

from ubuntu:${UBUNTU_TAG}

# Must be referenced after "from" to be available in this build stage.
arg UBUNTU_TAG


env DEBIAN_FRONTEND=noninteractive \
    TERM=dumb \
    PAGER=cat


run echo 'APT::Get::Assume-Yes "true";' > /etc/apt/apt.conf.d/90level12 \
    && echo 'DPkg::Options "--force-confnew";' >> /etc/apt/apt.conf.d/90level12 \
    && apt-get update \
    && apt-get install -y \
        curl \
        locales \
        software-properties-common \
        sudo \
    && echo 'Defaults    env_keep += "DEBIAN_FRONTEND"' >> /etc/sudoers.d/env_keep \
    && locale-gen en_US.UTF-8 \
    # cleanup
    && rm -rf /var/lib/apt/lists/*


env LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8


run apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        libffi-dev \
        libreadline-dev \
	# git: get the semi-official latest-stable git instead of using the old(er) version from the
	# ubuntu distro
	&& add-apt-repository ppa:git-core/ppa \
    && apt-get install -y git \
    # cleanup
    && rm -rf /var/lib/apt/lists/*


# 22.04 didn't have a non-root user
run if [ "$UBUNTU_TAG" = "22.04" ]; then \
    useradd -m -s /bin/bash ubuntu && \
    echo "ubuntu ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers; \
fi

user ubuntu
env PATH=/home/ubuntu/bin:/home/ubuntu/.local/bin:$PATH

# opt-out of this security feature, not needed in a CI environment
run git config --global --add safe.directory '*'


entrypoint ["/bin/bash"]
cmd []
