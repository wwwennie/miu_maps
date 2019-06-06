# miu_maps

A small python package for generating chemical potential maps involving a host material and competing phases. 

Using sympy: based on inputted phases and enthalpies of formation, it parses chemical formulae, constructs and solves appropriate chemical potential inequalities, and creates a plot

See data_\*.py for example input formats.

Dependencies: [fillplots](https://github.com/tkf/fillplots)

Note: for compatibility in python 3.+, modify in <mplcolors.py>
~~~~
        colors = rcParams['axes.color_cycle']
~~~~

to a color picker routine of your choice.
