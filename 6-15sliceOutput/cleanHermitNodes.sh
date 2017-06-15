#!/bin/bash

if [ $# -gt 0 ]; then
    echo "Your command line contains $# arguments Please enter ./helloworld.sh [graphFileName] [cleanedOutputFileName]"
else
    echo "Your command line contains no arguments. Please enter ./helloworld.sh [graphFileName] [cleanedOutputFileName]"
fi

echo $0
echo $1
echo $2

gvpr -c "N[$.degree==0]{delete(root, $)}" $1 > $2.dot
dot -Tpdf $2.dot -o ./$2.pdf
