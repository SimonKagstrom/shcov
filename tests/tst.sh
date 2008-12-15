#!/bin/bash

function vobb() {
    echo "vobb $1"
}

mibb() # Other fn syntax
{
    echo "Are we really executing this?"
    echo "Perhaps not?"
}

function hej_hopp { # Yet another
    echo Hejsan
}

function hej_hopp2
{ # Yet yet another
    echo Hejsan
}

vobb hejhopp
vobb tjoho
hej_hopp2
echo "al-mibb"

if [ $# -gt 1 ]; then
    echo hejsan
fi

a=5
while [ $a -gt 0 ]; do
    a=$(($a - 1))
    echo "Count $a"
done

for file in `ls *`; do
    echo $file
done

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
