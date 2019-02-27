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


class Components:
    @property
    def components(self):
        if not self._atoms:
            return []
        atoms = set(self._atoms)
        components = []
        while atoms:
            start = atoms.pop()
            component = list(self.__component(start))
            components.append(component)
            atoms.difference_update(component)
        return components

    @property
    def number_of_components(self):
        return len(self.components)

    def __component(self, start):
        seen = {start}
        queue = [start]
        while queue:
            start = queue.pop(0)
            yield start
            for i in self._bonds[start].keys() - seen:
                queue.append(i)
                seen.add(i)
