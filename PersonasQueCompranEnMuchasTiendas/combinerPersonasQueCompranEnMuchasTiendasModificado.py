#!/usr/bin/python3

import sys

current_cliente = None
tiendas = set()

for line in sys.stdin:
    line = line.strip()
    cliente, tienda = line.split("\t", 1)
    
    if current_cliente is None:
        current_cliente = cliente
    
    if cliente != current_cliente:
        print(f"{current_cliente}\t{len(tiendas)}")
        current_cliente = cliente
        tiendas = set()
    
    tiendas.add(tienda)

if current_cliente is not None:
    print(f"{current_cliente}\t{len(tiendas)}")
