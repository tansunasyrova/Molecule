# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
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


class MCS:
    def clique(self):
        clique = []
        clique_atoms = set()
        roots = sorted(self._bonds, key=lambda x: len(self._bonds[x]), reverse=True)
        for i in roots:
            neighbours = self._bonds[i].keys() - clique_atoms
            if not neighbours:
                continue
            neighbours_root = neighbours.copy()
            neighbours_root.add(i)
            for j in neighbours:
                n_n = set(self._bonds[j])
                n_n.add(j)
                if not n_n.issuperset(neighbours_root):
                    break
            else:
                clique.append(list(neighbours_root))
                clique_atoms.update(neighbours_root)
        return clique
