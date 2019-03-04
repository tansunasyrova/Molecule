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


class GroupXVI:
    pass


class Te(Element, PeriodIV, GroupXVI):

    @property
    def atomic_number(self):
        return 52

    @property
    def atomic_mass(self):
        return 127.6033

    @property
    def electronegativity(self):
        return 2.1

    @property
    def common_isotope(self):
        return 130

    @property
    def max_isotope(self):
        return 132

    @property
    def min_isotope(self):
        return 118

    @property
    def common_valences(self):
        return (0, 1), (2, 1), (4, 3), (6, 3)

    @property
    def valences_exeptions(self):
        return ()