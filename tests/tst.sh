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

function in_background()
{
    a=0
    while [ $a -lt 5 ]; do
        echo "Background job executing..."
        sleep 1
        a=$(($a + 1))
    done # Hej
    echo "Background job has finished"
}

first_stuff=1

vobb hejhopp
vobb tjoho
hej_hopp2

in_background &

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

# Not yet handled
cat <<EOF
vobb
mibb
EOF

# Handled
for idx in 1 \
    2 \
    3 \
    4 ; do
    echo mibb
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

echo mibb >&2

dn=`dirname $0`
echo "mibb" > /tmp/a

source $dn/second-tst.sh

a=`ls -l /proc`
