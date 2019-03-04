# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
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


class GroupXVII:
    pass


class I(Element, PeriodIV, GroupXVII):

    @property
    def atomic_number(self):
        return 53

    @property
    def atomic_mass(self):
        return 126.9044

    @property
    def electronegativity(self):
        return 2.66

    @property
    def common_isotope(self):
        return 127

    @property
    def max_isotope(self):
        return 131

    @property
    def min_isotope(self):
        return 124

    @property
    def common_valences(self):
        return (0, 1), (1, 1), (3, 1), (5, 3), (7, 3)

    @property
    def valences_exeptions(self):
        return ()


class At(Element, PeriodV, GroupXVII):

    @property
    def atomic_number(self):
        return 85

    @property
    def atomic_mass(self):
        return  209.9871

    @property
    def electronegativity(self):
        return 2.5

    @property
    def common_isotope(self):
        return 127

    @property
    def max_isotope(self):
        return 127

    @property
    def min_isotope(self):
        return 127

    @property
    def common_valences(self):
        return (0, 1), (1, 1), (3, 1), (5, 3), (7, 3)

    @property
    def valences_exeptions(self):
        return ()