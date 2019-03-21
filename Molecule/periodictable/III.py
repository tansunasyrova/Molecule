# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  Copyright 2019 Tagir Akhmetshin <tagirshin@gmail.com>
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


class GroupIII:
    pass


class Sc(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 21

    @property
    def atomic_mass(self):
        return 44.956

    @property
    def electronegativity(self):
        return 1.36

    @property
    def common_isotope(self):
        return 45

    @property
    def max_isotope(self):
        return 48

    @property
    def min_isotope(self):
        return 45

    @property
    def common_valences(self):
        return (0, 2), (3, 1)

    @property
    def valences_exceptions(self):
        return (-3, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),


class Y(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 39

    @property
    def atomic_mass(self):
        return 88.906

    @property
    def electronegativity(self):
        return 1.22

    @property
    def common_isotope(self):
        return 89

    @property
    def max_isotope(self):
        return 87

    @property
    def min_isotope(self):
        return 91

    @property
    def common_valences(self):
        return (0, 2), (3, 1)

    @property
    def valences_exceptions(self):
        return ()


__all__ = ['GroupIII', 'Sc', 'Y']
