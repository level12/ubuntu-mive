#!/bin/sh
#MISE description="Confirm mise and uv are latest versions"

check_update() {
    local tool=$1
    local installed_version
    local latest_version
    local repo

    case "$tool" in
        mise)
            installed_version=$(mise version --json | jq -r '.latest')
            repo="jdx/mise"
            ;;
        uv)
            installed_version=$(uv --version | awk '{print $2}')  # Extracts the version from `uv --version uv X.Y.Z`
            repo="astral-sh/uv"
            ;;
        *)
            echo "Unsupported tool: $tool"
            return 1
            ;;
    esac

    latest_version=$(curl -s https://api.github.com/repos/$repo/releases/latest | jq -r '.tag_name' | sed 's/^v//')

    if [ "$installed_version" = "$latest_version" ]; then
        echo "$tool is up to date: $installed_version"
        return 0
    else
        echo "$tool update available! Installed: $installed_version, Latest: $latest_version"
        return 1
    fi
}

# Check both mise and uv
check_update mise
mise_status=$?

check_update uv
uv_status=$?

# Exit 1 if either tool needs an update
if [ $mise_status -ne 0 ] || [ $uv_status -ne 0 ]; then
    exit 1
else
    exit 0
fi
