"""
LengthConstraint Plugin Demo
============================

Written by T.J. Sego, Ph.D.

Biocomplexity Institute

Indiana University

Bloomington, IN, U.S.A.

Description
===========

LengthConstraint Plugin is responsible for imposing a degree of elongated shape in cells.
Elongation is known to affect development and morphology of vascular networks in simulation.
Elongation is imposed by enforcing a constraint on the length of the major axis of a cell's inertia tensor.

This simple demo shows basic functionality of LengthConstraint and how elongation affects a vascular network that
forms via chemotaxis.
Each cell releases a chemoattractant to which all cells chemotax.
Use the sliders to adjust the strength and target length of the length constraint, and strength by which cells chemotax.
"""
from cc3d import CompuCellSetup
from ElongationDemoSteppables import ElongationDemoSteppable

CompuCellSetup.register_steppable(steppable=ElongationDemoSteppable(frequency=1))
CompuCellSetup.run()
