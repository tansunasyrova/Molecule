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
        return (0, 4), (2, 2), (3, 1)

    @property
    def valences_exceptions(self):
        return ((0, 3, (1, 'H')),
                (0, 2, ((2, 'O'), (2, 'O'))),
                (0, 2, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (1, 1, ((1, 'F'), (1, 'F'), (1, 'F'))),  #MCoF3
                (1, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),
                (2, 2, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  #M2CoF4
                (2, 2, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),
                (2, 2, ((1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'))),  #M2CoBr4
                (2, 2, ((1, 'I'), (1, 'I'), (1, 'I'), (1, 'I'))),
                (2, 2, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  #M2[Co(CNO)4]
                (1, 2, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  #M[Co(CN4)]
                (3, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  #M3CoCl5
                (3, 1, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  #M3[Co(NCS)5]
                (4, 2, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  #M4[Co(NCS)6]
                (0, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'Co'))),  # Октакарбонилдикобальт
                (0, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'H'))),  # Тетракарбонилкобальтовая кислота
                (0, 2, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'C'))),  # Витамин B12
                (1, 2, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'O'))),  # Гидроксокобаламин
                (3, 2, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  #K3[Co(CN)4]
                (3, 2, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # K3[Co(CN)6]
                (6, 2, ((2, 'O'), (2, 'O'), (2, 'O'))),  #Li6[CoO4]
                (3, 2, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  #K3[Co(OH)6]
                (3, 1, ((1, 'O'), (1, 'O'), (1, 'O'))),  #Na3[Co(CO3)3]
                (2, 2, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  #Na2[Co(OH)4]
                (4, 2, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  #Ba2[Co(OH)6]
                (1, 1, ((1, 'O'), (1, 'O'), (1, 'O')))) #M[Co(NO3)3]


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
        return (0, 4), (3, 1),

    @property
    def valences_exceptions(self):
        return ((0, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'H'))),  # Тетракарбонилродиевая кислота
                (0, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'Rh'))),  # Октакарбонил родия
                (0, 1, ((1, 'P'), (1, 'P'), (1, 'P'), (1, 'C'), (1, 'H'))),  # Гидридотрис(трифенилфосфин)карбонилродий
                (0, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (0, 2, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (0, 2, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # Rh(OH)4
                (0, 2, (2, 'O')),  # RhO
                (0, 2, ((2, 'O'), (2, 'O'))), # RhO2
                (0, 2, ((1, 'O'), (1, 'O'))),  # Rh(OH)2
                (0, 2, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (0, 2, ((1, 'S'), (1, 'S'))),
                (0, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'Rh'), (1, 'Rh'), (1, 'Rh'))),  # Додекакарбонил родия
                (0, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'Rh'), (1, 'Rh'), (1, 'Rh'))),  # Додекакарбонил
                (0, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'Rh'), (1, 'Rh'), (1, 'Rh'), (1, 'Rh'))),  # Гексадекакарбонил
                (3, 2, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  #K3[Rh(NO2)6]
                (3, 2, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))), #K3[RhCl6]
                (3, 1, ((1, 'O'), (1, 'O'), (1, 'O'))), #M3[Rh(SO4)3]
                (1, 2, ((1, 'O'), (1, 'O'))), #M[Rh(SO4)2]
                (1, 2, ((1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br')))) #MRhBr4


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
        return (0, 4), (2, 2), (3, 1),

    @property
    def valences_exceptions(self):
        return ((0, 3, (1, 'F'),
                (0, 3, (1, 'Cl'),
                (0, 3, (1, 'Br')),
                (0, 3, (1, 'I')),
                (0, 2, ((2, 'O'), (2, 'O'))),
                (0, 2, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (0, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (0, 2, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),
                (0, 2, ((1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'))),
                (0, 2, ((1, 'I'), (1, 'I'), (1, 'I'), (1, 'I'))),
                (0, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'Ir'))), # Октакарбонил иридия
                (0, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (3, 2, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),
                (3, 2, ((1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'))),
                (3, 2, ((1, 'I'), (1, 'I'), (1, 'I'), (1, 'I'), (1, 'I'), (1, 'I'))),
                (3, 2, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),
                (2, 2, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))))


__all__ = ['GroupIX', 'Co', 'Rh', 'Ir']
