# main driver for pychempot
# dependencies: pymatgen, sympy, fillplots
# compatible with Python 3.7+

import numpy as np

# local modules
from compound import *
from miu_ineq import *
from miu_plot import *
from miu_intersect import *

# The purpose of this module is to port over the plotting of chemical potential maps to Python
# Three example cases are given: SrZrO3, BiVO4, BaCeO3; import variables from data_*.py files

# Note: Currently tested for ABC-like compounds
# TODO: prettify plotting

def make_miu(host_formula, compete_formula, c_var, dep_var):
    """
    construct miu maps for arbitrary number of competing phases
    host_formula: tuple of the form (formula(string), del_Hf (float))
    compete_formula: list of the form [(formula(string), del_Hf (float))
    c_var: (string) name of element/compound in constraint as defined by formation enthalpy of host
    dep_var: (string) name of element/compound in constraint to plot against

    formula can be of the form "ABC" or "abc"
    del_Hf = enthalpy of formation

    e.g., BiVO4: c_var = "O" eliminates mu_O; plot mu_Bi v mu_V so dep_var = "V"
    e.g., BaCeO3: c_var = "Ba" eliminates mu_Ba; plot mu_Ce v mu_O so dep_var = "O"

    tested with ABC-type compounds
    """

    # initiate Compound classes
    host = Host_Compound(del_Hf=host_formula[1], formula=host_formula[0])
    compete = []
    compete_formulae =[]
    for formula,del_Hf in compete_formula:
        compete.append(Compete_Compound(del_Hf=del_Hf,formula=formula))
        compete_formulae.append(formula) # save formula names for plotting


    # constraint
    host_eq = Constraint(host)
    host_eq_sym = host_eq.solve_for(c_var)

    # manipulation of equations for plotting
    print("Original inequalities (0 >= -del_Hf + sum_i mu_i)")
    compete_list = [Ineq(c) for c in compete]
    print("Add constraint: ", host_eq_sym)
    compete_list = [c.sub_constraint(c_var, host_eq_sym) for c in compete_list]

    return compete_list,compete_formulae

if __name__ == "__main__":

    ## load examples with data
    from data_bvo import *
    #from data_bco import *
    #from data_sro import *

    compete_list,compete_formulae = make_miu(host,compete,c_var,dep_var)
    compete_list_lambdas_mu = solve_for_lambdas(compete_list,dep_var,ind_var,tuple_list)

    # find intersection
    curve1, curve2 = 1,3
    print("")
    print("Intersection between %s and %s"%(compete_formulae[1],compete_formulae[3]))
    (x,y) = linear_intersect(compete_list_lambdas_mu[curve1][0],compete_list_lambdas_mu[curve2][0])
    print(x,y)

    # plot things
    miu_plot(compete_list_lambdas_mu,xaxis=xlim,yaxis=ylim,
             axes_labels=(xaxes_label,yaxes_label),show_legend=True, labels=compete_formulae)
    plt.show()





