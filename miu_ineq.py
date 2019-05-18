from sympy import Symbol, sympify, solve, Eq, symbols
from sympy.utilities.lambdify import lambdify

# local modules
from compound import *

def solve_for_lambda(sym_eq, dep_var, vars):
    """
    Rearrange expression symbolically for dep_var

    sym_eq (sympy object): expression to rearrange
    dep_var (string): element/compound name; dependent variable axis of plot; LHS
    var: tuple of strings corresponding to element/compound name; RHS variables
    returns lambda equivalent numeric function for interface with numpy

    note: order that vars is in is the order to substitute in lambda function
    """
    vars = tuple([v.lower() for v in vars])
    exp_py = solve(Eq(sym_eq, 0.0), dep_var.lower())

    print(dep_var.lower(),"<",exp_py[0])
    return lambdify(vars,exp_py[0])  # only one solution

def solve_for_lambdas(list_sym_eq,dep_var,vars,tuple_list):
    """
    Wrapper for solve_for_lambda for handling lots of equations

    list_sym_eq: list of sympy equations
    dep_var (string): element/compound name; dependent variable axis of plot; LHS
    var: tuple of strings corresponding to element/compound name; RHS variables
    """
    list_eq = []
    i=0
    for symeq in list_sym_eq:
        print(symeq)
    print()

    print("Solve for %s as function of %s"%(dep_var,vars))
    print("Choice of True corresponds to <")
    for symeq in list_sym_eq:

        l = solve_for_lambda(symeq,dep_var,vars)
        list_eq.append(tuple((l,tuple_list[i])))
        i=i+1
        # also tuple-fy to make compatible with fillplots
        # assume region plotting following "<"

    return list_eq

class Linear_Exp(object):
    """ Base class for chemical potential expressions
        handles only linear expressions

        Subclasses: Ineq, Constraint
    """
    def __init__(self,compound:Compound):
        self.stoich = compound.get_stoich()
        self.formula = compound.name()
        self.del_Hf= compound.del_Hf
        self.eqtype = None

        ### build string expression
        # Expressions of the form:
        # $ 0 >= -\Delta H_f + \sum_i (w_i * \mu_i)$ where w_i is the stoichiometric coefficient

        # this choice aligned with plotting with fillplots module
        # at this point, no equality is set
        # Variable names are element/compound names

        string = "-%f "%self.del_Hf
        symbols=''
        for specie in self.stoich:
            stoich_coeff = self.stoich[specie]
            string = string + "+ (%d * %s) "%(stoich_coeff,specie)
            symbols=symbols+"%s "

        # due to conflict with sympy (e.g., O symbol), lower case all symbols
        self.exp_string = string.lower()
        self.exp_sym = sympify(self.exp_string, evaluate=False)  # symbolic expression
        self.sym_string = symbols

    def solve_for(self,dep_var):
        """
        Rearrange expression symbolically for dep_var
        dep_var (string): element/compound name; dependent variable axis of plot
        returns sympy object
        """
        exp_py = solve(Eq(self.exp_sym,0.0),dep_var.lower())
        return exp_py[0] # only one solution

    def __repr__(self):
        return ("{} : {}".format(self.formula, self.exp_string))


    def __str__(self):
        return ("{} : {}".format(self.formula, self.exp_string))

class Ineq(Linear_Exp):
    """
    Chemical potential expression involving inequalities
    i.e., competing phases
    """
    def __init__(self,compound:Compound):
        Linear_Exp.__init__(self,compound)
        self.eqtype = "inequality"
        print("{}: {}".format(self.formula, self.exp_sym))

    def sub_constraint(self,var,constraint):
        """
        subsitutes constraint to chemical potential inequality

        var: (string) variable to substitute
        constraint: sympy object corresponding to constraint
        up to user to make sure to keep track of dependent and independent variables

        returns simplified sympy object  in which var is substituted for constraint
        """
        return self.exp_sym.subs(var.lower(),constraint)


class Constraint(Linear_Exp):
    """
    Chemical potential expression involving equalities
    i.e., host phase enthalpy of formation constraint on chemical potentials
    """
    def __init__(self,compound:Compound):
        Linear_Exp.__init__(self,compound)
        self.eqtype = "constraint"
