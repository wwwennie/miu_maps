#pseudo-experimental del_Hf (eV)
#host=("BiVO4",-11.676)
#compete=[("Bi2O3",-5.9479),
#         ("VO2",-4.475),
#         ("V2O3",-12.32),
#         ("V2O5",-16.070)]

# DFT+U, this work
host=("BiVO4",-11.676)
compete=[("Bi2O3",-5.785),
         ("VO2",-7.386),
         ("V2O3",-13.273),
         ("V2O5",-16.1427), 
        ("BiV",-11.676)] # last ineq is helper line for identifying boundaries

## Yin 2011
#host=("BiVO4",-13.95)
#compete=[("Bi2O3",-5.94805),
#         ("VO2",-9),
#         ("V2O3",-13.07),
#         ("V2O5",-19.01)]

# constraint variable
# host enthalpy of formation will constrain mu_O
c_var = "O"
# plot mu_Bi v mu_V, with mu_V as dependent variable
dep_var = "V"
ind_var = ("Bi",)

# Choice of Shaded region
# The convention of shading regions is "<" for True
# chosen mu_V as dependent variable; for vanadates, mu_V will naturally arise on LHS
# However, must book keep when this is not the case, as is for bi2o3
# since dependence on mu_V only occurs when constraint is added
tuple_list = [False, True, True, True,False]

# plotting parameters
xlim=(-13,0)
ylim=(-13,0)
xaxes_label=r"$\mu_{Bi}$ (eV)"
yaxes_label=r"$\mu_{V}$ (eV)"
