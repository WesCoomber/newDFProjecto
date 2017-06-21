#!/bin/bash

if [ $# -gt 0 ]; then
        
    if [ $# -gt 2 ]; then
    	echo "Your command line contains $# arguments Please enter ./cleanHermitNodes.sh [graphFileName] [cleanedOutputFileName]" 
    	exit
    fi
else
    echo "Your command line contains no arguments. Please enter ./cleanHermitNodes.sh [graphFileName] [cleanedOutputFileName]"
    exit
fi

echo $1
echo $2

gvpr -c "N[$.degree==0]{delete(root, $)}" $1 > $2.dot
dot -Tpdf $2.dot -o ./$2.pdf

echo "done!"
