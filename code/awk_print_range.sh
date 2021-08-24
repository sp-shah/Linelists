#!/bin/bash
# Script to extract ranges of lines from master_mol_list.moog
# Example:
# ./awk_print_range.sh 4310 4320

# Check two arguments are integers and $1 < $2
re='^[0-9]+$'
if ! [[ $1 =~ $re ]] ; then
    echo "error: $1 not an integer" >&2; exit 1
fi
if ! [[ $2 =~ $re ]] ; then
    echo "error: $2 not an integer" >&2; exit 1
fi
if [ "$1" -ge "$2" ] ; then
    echo "error: $1 >= $2" >&2; exit 1
fi

echo $3
#awk -v wllo=$1 -v wlhi=$2 '$1>=wllo && $1 <=wlhi {print}' master_mol_list.moog
awk -v wllo=$1 -v wlhi=$2 '$1>=wllo && $1 <=wlhi {print}' ~/shahlabtools/shahgithub/linemake/super_master_list.moog
