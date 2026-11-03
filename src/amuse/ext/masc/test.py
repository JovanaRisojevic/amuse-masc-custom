import logging
import numpy

from amuse.units import (
    units,
    nbody_system,
    generic_unit_converter,
    constants,
)
from amuse.units.trigo import sin, cos
from amuse.datamodel.particles import Particles
from amuse.ic.plummer import new_plummer_sphere
from amuse.ic.kingmodel import new_king_model
from stars import new_masses

masses = new_masses(number_of_stars=100)
print(masses.value_in(units.MSun))
print(masses.maximum)

# a = numpy.array([0, 1, 2, 3])
# b = numpy.array([0, 0, 5, 5])
# mask = a<b
# print(len(a[mask]))