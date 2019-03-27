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
from collections import defaultdict
from itertools import product, combinations
from typing import Dict, List, Set, Hashable, Iterator


def clique(graph: Dict[Hashable, Set[Hashable]]) -> Iterator[List[Hashable]]:
    """ adopted from networkx algorithms.clique.find_cliques"""
    subgraph = {x for x, y in graph.items() if y}  # skip isolated nodes
    if not subgraph:
        return  # empty or fully disconnected
    elif len(subgraph) == 2:  # dimer
        yield list(subgraph)
        return

    stack = []
    clique_atoms = [None]
    candidates = subgraph.copy()
    roots = candidates - graph[max(subgraph, key=lambda x: len(graph[x]))]

    while True:
        if roots:
            root = roots.pop()
            candidates.remove(root)
            clique_atoms[-1] = root
            neighbors = graph[root]
            neighbors_subgraph = subgraph & neighbors
            if not neighbors_subgraph:
                yield clique_atoms.copy()
            else:
                neighbors_candidates = candidates & neighbors
                if neighbors_candidates:
                    if roots:
                        stack.append((subgraph, candidates, roots))
                    clique_atoms.append(None)
                    subgraph = neighbors_subgraph
                    candidates = neighbors_candidates
                    roots = candidates - graph[max(subgraph, key=lambda x: len(candidates & graph[x]))]
        elif not stack:
            return
        else:
            clique_atoms.pop()
            subgraph, candidates, roots = stack.pop()


class MCS:
    def mcs_mapping(self, other) -> Dict[int, int]:
        p = {}
        a1 = defaultdict(set)
        for (s, v1), (o, v2) in product(self._atoms.items(), other._atoms.items()):
            if v1 == v2:
                p[(s, o)] = set()
                a1[s].add(o)
        for (s1, v1), (s2, v2) in combinations(a1.items(), 2):
            for o1, o2 in product(v1, v2):
                if o1 != o2:
                    k1 = (s1, o1)
                    k2 = (s2, o2)
                    p[k1].add(k2)
                    p[k2].add(k1)
        mapping = {}
        for c in clique(p):
            if len(c) > len(mapping) and all(self._bonds[s1].get(s2) == other._bonds[o1].get(o2)
                                             for (s1, o1), (s2, o2) in combinations(c, 2)):
                mapping = dict(c)
        return mapping
