#!/usr/bin/env python

from classifier.base import BaseClassifier
import feature as feature


class VformClassifier(BaseClassifier):
    def __init__(self):
        super(VformClassifier, self).__init__()

        self.feature_funcs = [
            feature.is_first_word,
            feature.is_last_word,
        ]
