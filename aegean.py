#!/usr/bin/env python3
import sys
import re

AIR = "airborne"
SEA = "by-sea"

def norm_mode(s: str) -> str:
    s = s.strip().lower()
    s = s.rstrip('s') 
    if s in ("airborne", "airborne"):
        return AIR
    if s in ("by-sea", "by-sea"):
        return SEA
    raise ValueError(f"Unknown transport mode: {s}")

def parse_input(lines):
    it = iter(lines)
    H = int(next(it).strip())
    C = int(next(it).strip())
    customers = []
    pair_re = re.compile(r'\s*(\d+)\s+([A-Za-z-]+)\s*')
    for _ in range(C):
        line = next(it).strip()
        if not line:
            customers.append(([], None))
            continue
        parts = [p.strip() for p in line.split(",")]
        sea_choices = set()
        air_choice = None
        for p in parts:
            m = pair_re.fullmatch(p)
            if not m:
                raise ValueError(f"Bad pair: {p}")
            h = int(m.group(1))
            t = norm_mode(m.group(2))
            if h < 0 or h >= H:
                raise ValueError(f"Hop index out of range: {h}")
            if t == SEA:
                sea_choices.add(h)
            else:
                if air_choice is not None:

                    raise ValueError("Customer has more than one airborne request")
                air_choice = h
        customers.append((sorted(sea_choices), air_choice))
    return H, C, customers

def solve(H, customers):

    assignment = [SEA] * H

    changed = True
    while changed:
        changed = False
        for sea_list, air in customers:

            satisfied = False

            for h in sea_list:
                if assignment[h] == SEA:
                    satisfied = True
                    break

            if not satisfied and air is not None and assignment[air] == AIR:
                satisfied = True

            if satisfied:
                continue

            if air is not None:
                if assignment[air] != AIR:
                    assignment[air] = AIR
                    changed = True
            else:
                
                return None
    return assignment

def format_output(assignment):
    parts = []
    for h, mode in enumerate(assignment):
        parts.append(f"{h} {mode}")
    return ", ".join(parts)

def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        print("NO ITINERARY")
        return
    try:
        H, C, customers = parse_input(data)
        assignment = solve(H, customers)
        if assignment is None:
            print("NO ITINERARY")
        else:
            print(format_output(assignment))
    except Exception as e:
        print("NO ITINERARY")

if __name__ == "__main__":
    main()
