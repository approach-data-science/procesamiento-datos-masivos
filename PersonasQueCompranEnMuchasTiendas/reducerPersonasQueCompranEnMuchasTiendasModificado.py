#!/usr/bin/python3

import sys

current_cliente = None
total_tiendas = 0

for line in sys.stdin:
    line = line.strip()
    cliente, count = line.split("\t", 1)
    count = int(count)
    
    if current_cliente is None:
        current_cliente = cliente
    
    if cliente != current_cliente:
        if total_tiendas >= 3:
            print(current_cliente)
        current_cliente = cliente
        total_tiendas = 0
    
    total_tiendas += count

if current_cliente is not None and total_tiendas >= 3:
    print(current_cliente)
