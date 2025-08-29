# aegean-tour-solver

# Problem

This program prepares an island tour itinerary with H hops and ensures:

Each hop is either airborne or by-sea

Every customer’s request is satisfied (at least one preferred hop matches)

The number of airborne hops is minimized

If no valid itinerary exists, the program outputs NO ITINERARY

# Setup & Requirements

Python 3.8+ (no external libraries required)

Clone this repository:

git clone https://github.com/Srinathars/aegean-tour-solver.git

cd aegean-tour-solver

# Running the Program

You can run the program by providing input through stdin:

python3 aegean.py


Then type/paste the input, for example:

6
4
0 by-sea, 2 by-sea, 3 by-sea
0 by-sea, 5 airborne
0 airborne, 5 by-sea
2 airbornes


On Linux/macOS press Ctrl+D (Windows: Ctrl+Z, then Enter) to signal end of input.

Example Output
0 by-sea, 1 by-sea, 2 airborne, 3 by-sea, 4 by-sea, 5 by-sea
