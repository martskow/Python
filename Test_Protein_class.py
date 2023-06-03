"""
Autor: Marta Skowron

Ten moduł zawiera funkcję testującą dla funkcji zawartych w klasie Protein w
pliku Zad_3.py.
"""
import pytest


def test__init__():
    from Zad_3 import Protein

    test_ID = Protein('AAA123', 'ACDEFGHIKLMNPQRSTVWY').ID
    assert test_ID == 'AAA123'

    test_sequence = Protein('AAA123', 'ACDEFGHIKLMNPQRSTVWY').sequence
    assert test_sequence == 'ACDEFGHIKLMNPQRSTVWY'

    test_name = Protein('AAA123', 'ACDEFGHIKLMNPQRSTVWY').name
    assert test_name is None

    test_organism = Protein('AAA123', 'ACDEFGHIKLMNPQRSTVWY').organism
    assert test_organism is None

    test_name = Protein('BBB123', 'ACDEFGHIKLMNPQRSTVWY', 'Hgb', 'Human').name
    assert test_name == 'Hgb'

    test_organism = Protein('BBB123', 'ACDEFGHIKLMNPQRSTVWY', 'Hgb', 'Human').organism
    assert test_organism == 'Human'

    with pytest.raises(TypeError):
        from Zad_3 import Protein
        return Protein(111, 'ACDEFGHIKLMNPQRSTVWY', 'Hgb', 'Human')

    with pytest.raises(TypeError):
        from Zad_3 import Protein
        return Protein('AAA123', 111, 'Hgb', 'Human')

    with pytest.raises(TypeError):
        from Zad_3 import Protein
        return Protein('AAA123', 'ACDEFGHIKLMNPQRSTVWY', 111, 'Human')

    with pytest.raises(TypeError):
        from Zad_3 import Protein
        return Protein('AAA123', 'ACDEFGHIKLMNPQRSTVWY', 'Hgb', 111)

    with pytest.raises(ValueError):
        from Zad_3 import Protein
        return Protein('', 'ACDEFGHIKLMNPQRSTVWY', 'Hgb', 'Human')

    with pytest.raises(ValueError):
        from Zad_3 import Protein
        return Protein('AAA123', '', 'Hgb', 'Human')

    with pytest.raises(ValueError):
        from Zad_3 import Protein
        return Protein('AAA123', 'XXX', 'Hgb', 'Human')


@pytest.fixture
def protein1():
    from Zad_3 import Protein
    return Protein('AAA123', 'ACDEFGHIKLMNPQRSTVWY')


@pytest.fixture
def protein2():
    from Zad_3 import Protein
    return Protein('BBB123', 'ACDEFGHIKLMNPQRSTVWY', 'Hgb', 'Human')


@pytest.fixture
def protein3():
    from Zad_3 import Protein
    return Protein('CCC123', 'ACDEFGHIKLMNPQRSTVWY', 'Hgb')


@pytest.fixture
def protein4():
    from Zad_3 import Protein
    return Protein('DDD123', 'ACDEFGHIKLMNPQRSTVWY', organism='Human')


def test__str__(protein1, protein2, protein3, protein4):
    test_protein1 = protein1.__str__()
    assert test_protein1 == '>sp|AAA123|' + '\n' + 'ACDEFGHIKLMNPQRSTVWY'

    test_protein2 = protein2.__str__()
    assert test_protein2 == '>sp|BBB123|Hgb OS=Human' + '\n' + 'ACDEFGHIKLMNPQRSTVWY'

    test_protein3 = protein3.__str__()
    assert test_protein3 == '>sp|CCC123|Hgb' + '\n' + 'ACDEFGHIKLMNPQRSTVWY'

    test_protein4 = protein4.__str__()
    assert test_protein4 == '>sp|DDD123| OS=Human' + '\n' + 'ACDEFGHIKLMNPQRSTVWY'


@pytest.fixture
def protein5():
    from Zad_3 import Protein
    return Protein('DDD123', 'A')


def test_lenght(protein1, protein5):
    test_protein1 = protein1.lenght()
    assert test_protein1 == 20

    test_protein5 = protein5.lenght()
    assert test_protein5 == 1


def test_cut(protein1, protein2):
    test_protein1 = protein1.cut(5, 10).__str__()
    assert test_protein1 == '>sp|AAA123/5-10|' + '\n' + 'FGHIKL'

    test_protein1 = protein1.cut(5, 5).__str__()
    assert test_protein1 == '>sp|AAA123/5-5|' + '\n' + 'F'

    test_protein2 = protein2.cut(5, 10).__str__()
    assert test_protein2 == '>sp|BBB123/5-10|Hgb OS=Human' + '\n' + 'FGHIKL'

    test_protein2 = protein2.cut(5, 5).__str__()
    assert test_protein2 == '>sp|BBB123/5-5|Hgb OS=Human' + '\n' + 'F'

    with pytest.raises(ValueError):
        return protein2.cut(10, 5)

    with pytest.raises(ValueError):
        return protein2.cut(10, 101)

    with pytest.raises(ValueError):
        return protein2.cut(-10, 10)

    with pytest.raises(TypeError):
        return protein2.cut('1', 5)

    with pytest.raises(TypeError):
        return protein2.cut(5, '10')

    with pytest.raises(TypeError):
        return protein2.cut('5', '10')


def test_modify(protein1, protein2):
    test_protein1 = protein1.modify(1, 'C').__str__()
    assert test_protein1 == '>sp|AAA123 A1C|' + '\n' + 'CCDEFGHIKLMNPQRSTVWY'

    test_protein1 = protein1.modify(10, 'C').__str__()
    assert test_protein1 == '>sp|AAA123 L10C|' + '\n' + 'ACDEFGHIKCMNPQRSTVWY'

    test_protein1 = protein1.modify(20, 'C').__str__()
    assert test_protein1 == '>sp|AAA123 Y20C|' + '\n' + 'ACDEFGHIKLMNPQRSTVWC'

    test_protein1 = protein1.modify(1, 'A').__str__()
    assert test_protein1 == '>sp|AAA123|' + '\n' + 'ACDEFGHIKLMNPQRSTVWY'

    test_protein2 = protein2.modify(10, 'A').__str__()
    assert test_protein2 == '>sp|BBB123 L10A|' + '\n' + 'ACDEFGHIKAMNPQRSTVWY'

    with pytest.raises(IndexError):
        return protein1.modify(21, 'A')

    with pytest.raises(IndexError):
        return protein1.modify(0, 'A')

    with pytest.raises(ValueError):
        return protein1.modify(2, 'B')

    with pytest.raises(ValueError):
        return protein1.modify(2, '')

    with pytest.raises(ValueError):
        return protein1.modify(2, 'AAA')

    with pytest.raises(TypeError):
        return protein1.modify('2', 'A')

    with pytest.raises(TypeError):
        return protein1.modify(10, 10)


#pytest.main(["--cov=Zad_3", "--cov-report=term-missing"])
