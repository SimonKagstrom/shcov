#!/bin/bash

function vobb() {
    echo "vobb $1"
}

function mibb() {
    echo "Are we really executing this?"
    echo "Perhaps not?"
}

vobb hejhopp
vobb tjoho
echo "al-mibb"

if [ $# -gt 1 ]; then
    echo hejsan
fi

echo "mibb" > /tmp/a

source second-tst.sh

