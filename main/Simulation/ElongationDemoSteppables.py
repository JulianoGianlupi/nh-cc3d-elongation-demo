"""
Adapated from
    Merks, Roeland MH, et al.
    "Cell elongation is key to in silico replication of in vitro vasculogenesis and subsequent remodeling."
    Developmental biology 289.1 (2006): 44-54.

    Merks, Roeland MH, et al.
    "Contact-inhibited chemotaxis in de novo and sprouting blood-vessel growth."
    PLoS Comput Biol 4.9 (2008): e1000163.

Written by T.J. Sego, Ph.D.
Biocomplexity Institute
Indiana University
Bloomington, IN
Use the sliders to adjust chemotaxis and elongation during angiogensis
"""

from cc3d.core.PySteppables import *


class ElongationDemoSteppable(SteppableBasePy):

    def __init__(self, frequency=1):
        SteppableBasePy.__init__(self, frequency)

    def start(self):
        self.build_wall(self.WALL)

    def add_steering_panel(self):
        self.add_steering_param(name="target_length", val=0.0, min_val=0.0, max_val=40.0, decimal_precision=0,
                                widget_name="slider")
        self.add_steering_param(name="lambda_length", val=0.0, min_val=0.0, max_val=1.0, decimal_precision=2,
                                widget_name="slider")
        self.add_steering_param(name="lambda_chemo", val=0.0, min_val=0.0, max_val=1E3, decimal_precision=0,
                                widget_name="slider")

    def process_steering_panel_data(self):
        self.get_xml_element("length").TargetLength = self.get_steering_param("target_length")
        self.get_xml_element("length").LambdaLength = self.get_steering_param("lambda_length")
        self.get_xml_element("chemo").Lambda = self.get_steering_param("lambda_chemo")
