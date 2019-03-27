# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  Copyright 2019 Tagir Akhmetshin <tagirshin@gmail.com>
#  Copyright 2019 Tansu Nasyrova <tansu.nasurova@gmail.com>
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


class GroupIX:
    pass


class Co(Element, PeriodIV, GroupIX):
    @property
    def atomic_number(self):
        return 27

    @property
    def atomic_mass(self):
        return 58.9332

    @property
    def electronegativity(self):
        return 1.88

    @property
    def common_isotope(self):
        return 59

    @property
    def max_isotope(self):
        return 60

    @property
    def min_isotope(self):
        return 56

    @property
    def common_valences(self):
        return (2, 1), (3, 1)

    @property
    def valences_exceptions(self):
        return ((0, 1, (1, 'H')),
                (0, 1, (2, 'O'), (2, 'O')),
                (0, 1, (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F')),
                (0, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'Co'))), # Октакарбонилдикобальт
                (0, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'H'))), # Тетракарбонилкобальтовая кислота
                (1, 1, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'C'))), # Витамин B12
                (1, 1, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'O')))) # Гидроксокобаламин
                # Возникли вопросы насчет арсенидов, фосфидов, нитридов, силицидов кобальта.
                # Их много и непонятно, какие там валентности.


class Rh(Element, PeriodV, GroupIX):
    @property
    def atomic_number(self):
        return 45

    @property
    def atomic_mass(self):
        return 102.9055

    @property
    def electronegativity(self):
        return 2.28

    @property
    def common_isotope(self):
        return 103

    @property
    def max_isotope(self):
        return 103

    @property
    def min_isotope(self):
        return 99

    @property
    def common_valences(self):
        return (1, 2), (1, 3), (1, 4),

    @property
    def valences_exceptions(self):
        return ((0, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'H'))), # Тетракарбонилродиевая кислота
                (0, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'Rh'))), # Октакарбонил родия
                (0, 1, ((1, 'P'), (1, 'P'), (1, 'P'), (1, 'C'), (1, 'H'))), # Гидридотрис(трифенилфосфин)карбонилродий
                (0, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (0, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (0, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'Rh'), (1, 'Rh'), (1, 'Rh'))), # Додекакарбонил родия
                (0, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'Rh'), (1, 'Rh'), (1, 'Rh'))), # Додекакарбонил
                (0, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'Rh'), (1, 'Rh'), (1, 'Rh'), (1, 'Rh')))) # Гексадекакарбонил


class Ir(Element, PeriodVI, GroupIX):
    @property
    def atomic_number(self):
        return 77

    @property
    def atomic_mass(self):
        return 192.217

    @property
    def electronegativity(self):
        return 2.20

    @property
    def common_isotope(self):
        return 193

    @property
    def max_isotope(self):
        return 194

    @property
    def min_isotope(self):
        return 189

    @property
    def common_valences(self):
        return (1, 2), (1, 3), (1, 4), (1, 6),

    @property
    def valences_exceptions(self):
        return ((0, 1, (1, 'Br')),
                (0, 1, (1, 'I')),
                (0, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'Ir'))), # Октакарбонил иридия
                (0, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))))


__all__ = ['GroupIX', 'Co', 'Rh', 'Ir']