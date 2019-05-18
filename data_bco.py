# Barium Cerate
# Based on 10.1103/PhysRevB.92.214114

# del_Hf in eV
host=("BaCeO3",-17.23)
compete=[("BaO",-5.10),
         ("BaO2",-5.77),
         ("CeO2",-11.61),
         ("Ce2O3",-19.75)]

# constraint variable
# host enthalpy of formation will constrain mu_Ba
c_var = "Ba"
# plot mu_Ce v mu_O, with mu_O as dependent variable
dep_var = "O"
ind_var = ("Ce",)

# Choice of Shaded region
# The convention of shading regions is "<" for True
# chosen mu_O as dependent variable; for cerates, mu_Ce will naturally arise on LHS
# However, must book keep when this is not the case, as is for BaO and BaO2
# since mu_Ce only occurs when constraint is added
tuple_list = [False, False, True, True]

# plotting parameters
xlim=(-13,0)
ylim=(-13,0)
xaxes_label=r"$\mu_{Ce}$ (eV)"
yaxes_label=r"$\mu_{O}$ (eV)"