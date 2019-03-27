# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  Copyright 2019 Tagir Akhmetshin <tagirshin@gmail.com>
#  Copyright 2019 Tansu Nasyrova <tansu.nasyrova@gmail.com>
#  This file is part of Molecule.
#
#  Molecule is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, see <https://www.gnu.org/licenses/>.
#
from .element import Element
from .periods import *


class GroupXIII:
    pass


class B(Element, PeriodII, GroupXIII):
    @property
    def atomic_number(self):
        return 5

    @property
    def atomic_mass(self):
        return 10.806

    @property
    def electronegativity(self):
        return 2.04

    @property
    def common_isotope(self):
        return 11

    @property
    def max_isotope(self):
        return 11

    @property
    def min_isotope(self):
        return 10

    @property
    def common_valences(self):
        return (3, 1),
    @property
    def valences_exceptions(self):
        return (-1, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F')))


class Al(Element, PeriodIII, GroupXIII):
    @property
    def atomic_number(self):
        return 13

    @property
    def atomic_mass(self):
        return 26.9816

    @property
    def electronegativity(self):
        return 1.61

    @property
    def common_isotope(self):
        return 27

    @property
    def max_isotope(self):
        return 27

    @property
    def min_isotope(self):
        return 26

    @property
    def common_valences(self):
        return (0, 1), (3, 1),

    @property
    def valences_exceptions(self):
        return ((-1, 1, ((1, 'H'), (1, 'H'), (1, 'H'), (1, 'H'))),
                (-3, 1, ((1, 'H'), (1, 'H'), (1, 'H'), (1, 'H'), (1, 'H'), (1, 'H'), (1, 'H'), (1, 'H'))),
                (-3, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (-1, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (-3, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))))


class Ga(Element, PeriodIV, GroupXIII):
    @property
    def atomic_number(self):
        return 31

    @property
    def atomic_mass(self):
        return 69.723

    @property
    def electronegativity(self):
        return 1.81

    @property
    def common_isotope(self):
        return 69

    @property
    def max_isotope(self):
        return 71

    @property
    def min_isotope(self):
        return 69

    @property
    def common_valences(self):
        return (3, 1),

    @property
    def valences_exceptions(self):
        return ((0, 1, (1, 'Br')),
                (0, 1, (1, 'I')),
                (0, 1, (1, 'O')),
                (0, 1, (1, 'S')),
                (0, 1, (1, 'Se')),
                (0, 1, ((1, 'Cl'), (1, 'Cl'))),
                (0, 1, ((1, 'Br'), (1, 'Br'))),
                (0, 1, ((1, 'I'), (1, 'I'))),
                (0, 1, ((1, 'S'), (1, 'S'))),
                (0, 1, ((1, 'Se'), (1, 'Se'))),
                (0, 1, ((1, 'Te'), (1, 'Te'))))


__all__ = ['GroupXIII', 'B', 'Al', 'Ga']
