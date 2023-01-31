import pandas as pd
import numpy as np


class decision_tree():
    def __init__(self, examples, target_attribute, attributes):
        self.root = self.node()
        self.examples = examples
        self.target_attribute = target_attribute
        self.attributes = attributes

    
    class node():
        def __init__(self, label, left, right):
            self.label = label
            self.left = left
            self.right = right




