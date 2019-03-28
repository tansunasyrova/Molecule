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


class GroupIV:
    pass


class Ti(Element, PeriodIII, GroupIV):
    @property
    def atomic_number(self):
        return 22

    @property
    def atomic_mass(self):
        return 47.867

    @property
    def electronegativity(self):
        return 1.54

    @property
    def common_isotope(self):
        return 48

    @property
    def max_isotope(self):
        return 50

    @property
    def min_isotope(self):
        return 44

    @property
    def common_valences(self):
        return (0, 3), (2, 1), (3, 2), (4, 1),

    @property
    def valences_exceptions(self):
        return ((-1, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (-2, 2, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (-3, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (-2, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))), #K2TiCl6
                (-2, 1, ((1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'))), #K2TiBr6
                (-2, 1, ((1, 'I'), (1, 'I'), (1, 'I'), (1, 'I'), (1, 'I'), (1, 'I'))), #K2TiI6
                (-2, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))), #K2[Ti(SO4)3] и др
                (-2, 1, ((2, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))), #K2[TiO(SO4)2] и др
                (-1, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))), #H[Ti(SO4)2]
                (-2, 1, ((2, 'O'), (2, 'O'), (2, 'O'))), #K2TiO3
                (-4, 1, ((2, 'O'), (2, 'O'), (2, 'O'), (2, 'O'))), #Ba2[TiO4]
                (-2, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))), #H2[Ti(OH)4]
                (-2, 1, ((2, 'O'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))), #H2[TiOF4]
                (-2, 1, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))), #M2[Ti(SCN)6]
                (-2, 1, ((2, 'O'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))), #M2[TiO(SCN)4]
                (-3, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))), #K3[Ti(CN)6]
                (-4, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))), #K4[Ti(CN)6]
                (-4, 1, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C')))) #K4[Ti(CN)4]


class Zr(Element, PeriodIV, GroupIV):
    @property
    def atomic_number(self):
        return 40

    @property
    def atomic_mass(self):
        return 91.224

    @property
    def electronegativity(self):
        return 1.33

    @property
    def common_isotope(self):
        return 90

    @property
    def max_isotope(self):
        return 96

    @property
    def min_isotope(self):
        return 88

    @property
    def common_valences(self):
        return (0, 3), (2, 1), (3, 2), (4, 1),

    @property
    def valences_exceptions(self):
        return ((0, 2, (1, 'Cl')),  #ZrCl
                (0, 2, (1, 'Br')),
                (0, 2, (1, 'I')),
                (3, 2, (1, 'F')),  #ZrF (3+)
                (3, 2, (1, 'O')), # ZrNO3 (3+)
                (2, 1, (1, 'O'), (1, '0')),  # ZrSO4 (2+)
                (-1, 2, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  #Cs[Zr(ClO4)5]
                (3, 2, ((1, 'O'), (1, 'O'), (1, 'O'))),  #ZrOH (3+)
                (-2, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (-2, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),
                (-2, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  #H2[Zr(OH)6]
                (-3, 2, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  #Cs3[Zr(ClO4)7]
                (-5, 2, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C')))) #K5Zr(CN)5)
                #Na5Zr(PO4)3 - есть такое соединение, но я не понимаю, как у циркония может быть 9 связей с О


class Hf(Element, PeriodV, GroupIV):
    @property
    def atomic_number(self):
        return 72

    @property
    def atomic_mass(self):
        return 178.49

    @property
    def electronegativity(self):
        return 1.3

    @property
    def common_isotope(self):
        return 180

    @property
    def max_isotope(self):
        return 182

    @property
    def min_isotope(self):
        return 172

    @property
    def common_valences(self):
        return (0, 3), (2, 1), (3, 2), (4, 1),

    @property
    def valences_exceptions(self):
        return ((0, 2, (1, 'Cl')),
                (0, 2, (1, 'Br')),
                (0, 2, (1, 'I')),
                (3, 2, (1, 'O')),  # HfNO3 (3+)
                (2, 1, (1, 'O'), (1, '0')), #HfSO4 (2+)
                (3, 2, (1, 'F')),  # HfF (3+)
                (3, 2, ((1, 'O'), (1, 'O'), (1, 'O'))),  # HfOH (3+)
                (-2, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # H2[Hf(OH)6]
                (-2, 1, ((1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'))), #Rb2[HfBr6]
                (-2, 1, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))))


__all__ = ['GroupIV', 'Ti', 'Zr', 'Hf']
