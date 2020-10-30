#!/bin/bash

# set -o xtrace       ## To debug scripts
# set -o errexit      ## To exit on error
# set -o errunset     ## To exit if a variable is referenced but not set


function main() {
    SCRIPTPATH="$( cd "$(dirname "")" >/dev/null 2>&1 ; pwd -P )"
    cd "${SCRIPTPATH}"
    echo "Working Dir: " $(pwd)
    source "../venv/bin/activate"
    # Note: Can replace 127.0.0.1 with 0.0.0.0 to make it 'network/internet' accessable...
    # Note 2: Keycloak uses 8080. Change it or keep this as is.
    gunicorn wsgi:app -b 127.0.0.1:6969 # <module>:<app>   IE <file>:<flask app variable>
}
main $@;
