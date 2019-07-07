from typing import List
import numpy as np
from pymesh import Element


Vector = List[float]


class Node:
    """A base class of a node in a mesh"""
    def __init__(self):
        self.coordinates = None
        self.elements = set()

    def __index__(self, coord: Vector):
        self.coordinates = np.array(coord)
        self.elements = set()

    def add_element(self, element: Element):
        self.elements.add(element)

    def remove_element(self, element: Element):
        self.elements.remove(element)
