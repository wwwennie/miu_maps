# Strontium Zirconate
# Based on 10.1103/PhysRevB.89.184109

# del_Hf in eV
host=("SrZrO3",-16.85)
compete=[("ZrO2",-11.193),
         ("SrO",-6.136)]

# constraint variable
# host enthalpy of formation will constrain mu_Ba
c_var = "Sr"
# plot mu_Zr v mu_O, with mu_O as dependent variable
dep_var = "O"
ind_var = ("Zr",)

# Choice of Shaded region
# The convention of shading regions is "<" for True
# chosen mu_O as dependent variable;
tuple_list = [False, True]

# plotting parameters
xlim=(-13,0)
ylim=(-13,0)
xaxes_label=r"$\mu_{Zr}$ (eV)"
yaxes_label=r"$\mu_{O}$ (eV)"