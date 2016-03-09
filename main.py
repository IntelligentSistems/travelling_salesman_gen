#!/bin/bash

from environment import Environment
import sys

e = Environment(filename=sys.argv[1])
e.adapt()
