#!/usr/bin/env python3
"""Critical eTiWi Mini connectivity assertions on exported KiCad netlist.

KiCad ERC does not validate part-specific datasheet circuits. In particular,
a capacitor drawn in the source might be absent from the exported netlist.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

TOKEN = re.compile(r'"(?:\\.|[^"\\])*"|[()]|[^\s()]+')


def parse(text):
    stack, result = [], None
    for tok in TOKEN.findall(text):
        if tok == '(':
            item = []
            if stack: stack[-1].append(item)
            elif result is not None: raise ValueError('multiple S-expression roots')
            else: result = item
            stack.append(item)
        elif tok == ')':
            if not stack: raise ValueError('stray closing parenthesis')
            stack.pop()
        else:
            if not stack: raise ValueError('token outside root expression')
            stack[-1].append(json.loads(tok) if tok.startswith('"') else tok)
    if stack: raise ValueError('unclosed S-expression')
    return result


def children(obj, kind):
    return [x for x in obj if isinstance(x, list) and x and x[0] == kind]


def field(obj, kind):
    found = children(obj, kind)
    if len(found) != 1: raise ValueError(f'expected one {kind}, found {len(found)}')
    return found[0][1]


def connections(root):
    mapping = {}
    netlist = children(root, 'nets')
    if len(netlist) != 1: raise ValueError('missing nets')
    for net in children(netlist[0], 'net'):
        name = field(net, 'name')
        for item in children(net, 'node'):
            key = (field(item, 'ref'), field(item, 'pin'))
            if key in mapping: raise ValueError(f'duplicate pin: {key}')
            mapping[key] = name
    return mapping


def main(filename):
    nets = connections(parse(Path(filename).read_text(encoding='utf-8')))
    wanted = {
        ('U4','1'):'VBUS', ('U4','3'):'VBUS', ('U4','2'):'GND',
        ('U4','5'):'+3V3', ('C201','2'):'VBUS', ('C201','1'):'GND',
        ('C2','2'):'+3V3', ('C2','1'):'GND',
        ('L1','1'):'+1V1', ('U1','50'):'+1V1', ('U1','49'):'+3V3',
        ('U3','1'):'I2C_SDA', ('U3','2'):'GND',
        ('U3','3'):'I2C_SCL', ('U3','4'):'PRESS_INT',
        ('U3','5'):'GND', ('U3','6'):'+3V3', ('U3','7'):'GND',
        ('U2','2'):'I2C_SCL', ('U2','3'):'I2C_SDA',
        ('U2','4'):'GND', ('U2','6'):'GND', ('U2','20'):'+3V3',
        ('J1','A4'):'VBUS', ('J1','A9'):'VBUS',
        ('J1','B4'):'VBUS', ('J1','B9'):'VBUS'
    }
    errors = [f'{ref}.{pin}: expected {name}; got {nets.get((ref,pin), "NOT IN NETLIST")}'
              for (ref,pin),name in wanted.items() if nets.get((ref,pin)) != name]
    pairs = [(('L1','2'),('U1','48')),
             (('J1','A5'),('R53','2')), (('J1','B5'),('R52','1')),
             (('J1','A6'),('J1','B6')), (('J1','A7'),('J1','B7')),
             (('U2','7'),('R101','1'))]
    for a,b in pairs:
        if a not in nets or b not in nets or nets[a]!=nets[b]:
            errors.append(f'{a} must share a net with {b}')
    for i in range(8):
        a,b=('U2',str(8+i)),(f'TP{i+1}','1')
        if a not in nets or b not in nets or nets[a]!=nets[b]:
            errors.append(f'broken touch electrode {i}: {a} and {b}')
    if errors: raise ValueError('NETLIST GATE FAILED:\n' + '\n'.join(errors))
    print(f'NETLIST GATE PASS: {len(wanted)} fixed pins, 6 paired links, 8 touch electrodes')
    print('Electrical pin mapping only; not a mechanical footprint or PCB DRC check.')

if __name__ == '__main__':
    if len(sys.argv) != 2: raise SystemExit('usage: check_netlist.py input.net')
    main(sys.argv[1])
