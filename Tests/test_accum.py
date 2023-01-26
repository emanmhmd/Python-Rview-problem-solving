"""
this module contains basic uint tests for the accum module.
it's example of how pytest works
"""
#-------------------------------
# Imports
#-------------------------------
import pytest
from Stuff.accum import Accumulator
#-------------------------------
# Tests
#-------------------------------
def test_accum_init():
    accum = Accumulator
    assert accum.count==0
