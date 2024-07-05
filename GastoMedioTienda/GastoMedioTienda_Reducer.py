#!/usr/bin/env python3

import sys

def reducer():
    current_key = None
    current_sum = 0
    current_count = 0

    for line in sys.stdin:
        line = line.strip()
        key, gasto = line.split('\t')
        gasto = float(gasto)

        if current_key == key:
            current_sum += gasto
            current_count += 1
        else:
            if current_key:
                persona, tienda = current_key.split(';')
                print(f"{persona};{tienda};{current_sum / current_count}")
            current_key = key
            current_sum = gasto
            current_count = 1

    if current_key == key:
        persona, tienda = current_key.split(';')
        print(f"{persona};{tienda};{current_sum / current_count}")

if __name__ == "__main__":
    reducer()
