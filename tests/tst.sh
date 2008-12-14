#!/bin/bash

function vobb() {
    echo "vobb $1"
}

mibb() # Other fn syntax
{
    echo "Are we really executing this?"
    echo "Perhaps not?"
}

vobb hejhopp
vobb tjoho
echo "al-mibb"

if [ $# -gt 1 ]; then
    echo hejsan
fi

case $# in
    1)
        echo "1 args"
        ;;
    2)
        echo "2 args"
        ;;# Mibb
    'sorry mister')
        echo "This is very much dead code!"
        ;;
    "SORRY")
        echo "and more of that here"
        ;;
    *)
        echo "else args $#"
        ;;
esac

dn=`dirname $0`
echo "mibb" > /tmp/a

source $dn/second-tst.sh
