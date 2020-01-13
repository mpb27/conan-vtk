#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    if which pyenv > /dev/null; then
        eval "$(pyenv init -)"
    fi
    pyenv activate conan
fi

python build.py &
PID=$!
while [ -d /proc/$PID ]
do
    echo "Building..."
    sleep 540s # 9 minutes
done
