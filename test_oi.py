import pytest
from oi import mult
from oi import soma
def testesoma():
    resultado=soma(2,3)
    assert resultado == 5
    
def testemult():
    result=mult(2,3)
    assert result == 6