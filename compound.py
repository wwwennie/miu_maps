from pymatgen import Composition

class Compound(object):
    """
    Compound class

    Attributes (of subclass compete_compound and host_compound):
        del_Hf = enthalpy of formation
        formula (string) = chemical formula for compound, e.g., LiPO4
    """
    def __init__(self,del_Hf=0.00,formula=''):
        self.del_Hf=del_Hf
        self.formula=formula
        self.comp = Composition(formula)

    def get_stoich(self):
        """ Returns dictionary of elements where the keys contains the stoichiometry
            e.g., LiPO4 returns {"Li" : 1, "P": 1, "O": 4}
        """
        return self.comp.get_el_amt_dict()

    def uniq_elements(self):
        """ Returns list of unique elements
            e.g., LiPO4 returns ["Li","P","O"]
        """
        return [*self.comp.get_el_amt_dict().keys()]

    def get_stoich_coeff(self,element):
        """ Returns stoichiometrric coefficient for element
            e.g., LiPO4 for element="O" would return 4
        """
        dict=self.get_stoich()
        return dict[element]

    def name(self):
        return self.formula

class Compete_Compound(Compound):
    """
    Class for competing compounds which place additional limits to the chemical potential
    """
    def __init__(self,del_Hf=0.00,formula=''):
        super(Compete_Compound,self).__init__(del_Hf=del_Hf,formula=formula)
        self.del_Hf=del_Hf
        self.formula=formula
        self.comp = Composition(formula)


class Host_Compound(Compound):
    """
    Class for the host compound
    """

    def __init__(self, del_Hf=0.00, formula=''):
        super(Host_Compound, self).__init__(del_Hf=del_Hf, formula=formula)
        self.del_Hf=del_Hf
        self.formula=formula
        self.comp = Composition(formula)
