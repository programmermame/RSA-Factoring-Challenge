#!/bin/bash

factorize() {
    number=$1
    for ((i=2; i<=$number/2; i++)); do
        if [ $((number % i)) -eq 0 ]; then
            echo "$number=$i*$(($number / $i))"
            return
        fi
    done
}

main() {
    while IFS= read -r line; do
        number=$(echo $line | tr -d '\r')
        factorize "$number"
    done < "$1"
}

main "$1"

