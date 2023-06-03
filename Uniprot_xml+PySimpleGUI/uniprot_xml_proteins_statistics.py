"""
Autor: Marta Skowron
"""

import xmltodict
import pandas as pd
import PySimpleGUI as sg
from tkinter import messagebox
import statistics


def uniprot_xml_read(xml_file):
    """
    Function transforms the xml file with information about the protein
    downloaded from the website https://www.uniprot.org/ into list and
    distinguishes information about the access codes, protein names, organisms,
    sequences and lenght of those sequences.
    Arg:
        xml_file(file): file in XLM format from https://www.uniprot.org/; file
        must contain at least data on two proteins
    Return:
        data(list): list contains five lists - accessions, names,
        organisms, sequences and lenght of those sequences
    """
    with open(xml_file, 'rt') as file:
        file = xmltodict.parse(file.read())
    names = []
    accessions = []
    organisms = []
    sequences = []

    for i in range(0, len(file['uniprot']['entry'])):
        try:
            name = protein_name(file, i)
            access = protein_accesion(file, i)
            organism = protein_organism(file, i)
            sequence = file['uniprot']['entry'][i]['sequence']['#text']

            names.append(name)
            accessions.append(access)
            organisms.append(organism)
            sequences.append(sequence)

        except KeyError:
            print('The ' + str(i) + 'th sequence was ommited')
            pass

        except IndexError:
            print('The ' + str(i) + 'th sequence was ommited')
            pass

    data = [accessions, names, organisms, sequences,
            sequence_statictics(sequences)['lenghts']]

    return data


def protein_name(file, i):
    """
    Function for the xml file (file must be open already!) with information
    about the protein downloaded from the website https://www.uniprot.org/ and
    number of position protein in this file returns the name of this protein.
    Arg:
        file(file): file in XLM format from https://www.uniprot.org/; file
        must contain at least data on two proteins; file must be open
        i(int): i must be in the range 0 to the number of proteins the file
        informs about
    Return:
        name(string): name of protein from file from i position
    """
    try:
        name = file['uniprot']['entry'][i]['protein']['recommendedName']['fullName']['#text']
    except TypeError:
        name = file['uniprot']['entry'][i]['protein']['recommendedName']['fullName']
    except KeyError:
        try:
            name = file['uniprot']['entry'][i]['protein']['submittedName']['fullName']['#text']
        except TypeError:
            name = file['uniprot']['entry'][i]['protein']['submittedName']['fullName']
    except IndexError:
        raise IndexError

    return name


def protein_accesion(file, i):
    """
    Function for the xml file (file must be open already!) with information
    about the protein downloaded from the website https://www.uniprot.org/ and
    number of position protein in this file returns the access of this protein.
    Arg:
        file(file): file in XLM format from https://www.uniprot.org/; file
        must contain at least data on two proteins; file must be open
        i(int): i must be in the range 0 to the number of proteins the file
        informs about
    Return:
        name(string): access of protein from file from i position
    """
    try:
        if len(file['uniprot']['entry'][i]['accession'][0]) == 1:
            access = file['uniprot']['entry'][i]['accession']
        else:
            access = file['uniprot']['entry'][i]['accession'][0]
    except IndexError:
        raise IndexError

    return access


def protein_organism(file, i):
    """
    Function for the xml file (file must be open already!) with information
    about the protein downloaded from the website https://www.uniprot.org/ and
    number of position protein in this file returns the name of the organism of
    this protein.
    Arg:
        file(file): file in XLM format from https://www.uniprot.org/; file
        must contain at least data on two proteins; file must be open
        i(int): i must be in the range 0 to the number of proteins the file
        informs about
    Return:
        name(string): organism name of protein from file from i position
    """
    try:
        organism = file['uniprot']['entry'][i]['organism']['name'][0]['#text']
    except KeyError:
        organism = file['uniprot']['entry'][i]['organism']['name']['#text']
    except IndexError:
        raise IndexError

    return organism


def protein_sequence(file, i):
    """
    Function for the xml file (file must be open already!) with information
    about the protein downloaded from the website https://www.uniprot.org/ and
    number of position protein in this file returns the sequence of this protein.
    Arg:
        file(file): file in XLM format from https://www.uniprot.org/; file
        must contain at least data on two proteins; file must be open
        i(int): i must be in the range 0 to the number of proteins the file
        informs about
    Return:
        name(string): sequence of protein from file from i position
    """
    try:
        sequence = file['uniprot']['entry'][i]['sequence']['#text']
    except IndexError:
        raise IndexError

    return sequence


def sequence_statictics(sequences):
    """
    Function for the list of protein sequences returns the dictionary which
    contains lists of lenght for every sequence, the shortest
    (minimum) lenght of the protein present in the list, the greatest (maximum)
    lenght of the protein present in the list, mean and median of those lenghts.
    Arg:
        sequences(list): list conteins sequences of proteins
    Return:
        statistic(dictionary): dictionary contains lists of lenghts for every
        sequence, the shortest (minimum) lenght of the protein present in the
        list, the greatest (maximum) lenght of the protein present in the list,
        mean and median of those lenghts.
    """
    lenghts = []

    try:
        for i in range(0, len(sequences)):
            lenghts.append(len(sequences[i]))

        statistic = {'lenghts': lenghts, 'min': min(lenghts),
                     'max': max(lenghts), 'mean': sum(lenghts) / len(lenghts),
                     'median': statistics.median(lenghts)}
    except ValueError:
        statistic = {'lenghts': [], 'min': '', 'max': '', 'mean': '',
                     'median': ''}

    return statistic


def dataframe_create(data):
    """
    Function transforms list with four elements to dataFrame type table.
    Arg:
        data(list): list with four elements; elements also must be lists
                    (if the elements are of type int, float or string, the
                     table has only one row)
    Return:
        df(DataFrame table): table with four columns named 'access', 'name',
                    'organism' and 'sequence'
    """
    data_df = {
        "access": data[0],
        "name": data[1],
        "organism": data[2],
        "seqence": data[3],
        "sequence lenght": data[4]
    }
    df = pd.DataFrame(data_df)

    return df


def create_window():
    values = []
    headings = ["access", "name", "organism", "seqence", "sequence lenght"]

    layout = [[sg.Text('XML data file:', font=('Arial', 10, 'bold'))],
              [sg.InputText(key='file_name'),
               sg.Text('Statistics for the column "sequence lenght": '),
               sg.Text('minimum'), sg.Text('...', key='min', text_color='red'),
               sg.Text('maximum'), sg.Text('...', key='max', text_color='red'),
               sg.Text('median'), sg.Text('...', key='median', text_color='red'),
               sg.Text('mean', ), sg.Text('...', key='mean', text_color='red')],
              [sg.FileBrowse('Select...', target='file_name'),
               sg.Button('Open')],
              [sg.Table(headings=headings,
                        values=values,
                        key='TABELA',
                        expand_x=True,
                        expand_y=True)],
              [sg.Button('Clear'),
               sg.Button('Close')]]

    window = sg.Window('Uniprot protein', layout, size=(1100, 500))

    while True:
        event, value = window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            break

        if event == 'Open':
            try:
                file = value['file_name']
                values = dataframe_create(uniprot_xml_read(file)).values.tolist()
                window['TABELA'].update(values=values)
                window['min'].update(str(sequence_statictics
                                         (uniprot_xml_read(file)[3])['min']))
                window['max'].update(str(sequence_statictics
                                         (uniprot_xml_read(file)[3])['max']))
                window['mean'].update(str(sequence_statictics
                                          (uniprot_xml_read(file)[3])['mean']))
                window['median'].update(str(sequence_statictics
                                            (uniprot_xml_read(file)[3])['median']))
            except FileNotFoundError:
                messagebox.showinfo(title='Data entry error',
                                    message='File not attached.')

        if event == 'Clear':
            values = []
            window['TABELA'].update(values=values)
            window['min'].update('...')
            window['max'].update('...')
            window['mean'].update('...')
            window['median'].update('...')

    window.close()


create_window()


def test_protein_name():
    """
    Test function for the function protein_name
    Due to the throwing of exceptions by functions the edge cases aren't tested
    """
    with open('ferrytyna.xml', 'rt') as file:
        test_file = xmltodict.parse(file.read())

    test = protein_name(test_file, 0)
    assert test == 'Ferritin-like protein', 'Incorrect result'
    print('Correct test for protein_name')

    test = protein_name(test_file, 10)
    assert test == 'Ferritin-1, chloroplastic', 'Incorrect result'
    print('Correct test for protein_name')


test_protein_name()


def test_protein_access():
    """
    Test function for the function protein_access
    Due to the throwing of exceptions by functions the edge cases aren't tested
    """
    with open('ferrytyna.xml', 'rt') as file:
        test_file = xmltodict.parse(file.read())

    test = protein_accesion(test_file, 0)
    assert test == 'A0A0F5HNH9', 'Incorrect result'
    print('Correct test for protein_access')

    test = protein_accesion(test_file, 10)
    assert test == 'Q39101', 'Incorrect result'
    print('Correct test for protein_access')


test_protein_access()


def test_protein_organism():
    """
    Test function for the function protein_organism
    Due to the throwing of exceptions by functions the edge cases aren't tested
    """
    with open('ferrytyna.xml', 'rt') as file:
        test_file = xmltodict.parse(file.read())

    test = protein_organism(test_file, 0)
    assert test == 'Quasibacillus thermotolerans', 'Incorrect result'
    print('Correct test for protein_organism')

    test = protein_organism(test_file, 10)
    assert test == 'Arabidopsis thaliana', 'Incorrect result'
    print('Correct test for protein_organism')


test_protein_organism()


def test_protein_sequence():
    """
    Test function for the function protein_sequence
    Due to the throwing of exceptions by functions the edge cases aren't tested
    """
    with open('ferrytyna.xml', 'rt') as file:
        test_file = xmltodict.parse(file.read())

    test = protein_sequence(test_file, 0)
    assert test == 'MKEELDAFHQIFTTTKEAIERFMAMLTPVIENAEDDHERLYYHHIYEEEEQRLS' + \
           'RLDVLIPLIEKFQDETDEGLFSPSNNAFNRLLQELNLEKFGLHNFIEHVDLALFSFTDEERQ' + \
           'TLLKELRKDAYEGYQYVKEKLAEINARFDHDYADPHAHHDEHRDHLADMPSAGSSHEEVQPV' + \
           'AHKKKGFTVGSLIQ', 'Incorrect result'
    print('Correct test for protein_sequence')

    test = protein_sequence(test_file, 10)
    assert test == 'MASNALSSFTAANPALSPKPLLPHGSASPSVSLGFSRKVGGGRAVVVAAATVDT' + \
           'NNMPMTGVVFQPFEEVKKADLAIPITSHASLARQRFADASEAVINEQINVEYNVSYVYHSMY' + \
           'AYFDRDNVAMKGLAKFFKESSEEERGHAEKFMEYQNQRGGRVKLHPIVSPISEFEHAEKGDA' + \
           'LYAMELALSLEKLTNEKLLNVHKVASENNDPQLADFVESEFLGEQIEAIKKISDYITQLRMI' + \
           'GKGHGVWHFDQMLLN', 'Incorrect result'
    print('Correct test for protein_sequence')


test_protein_sequence()


def test_sequence_statictics():
    """
    Test function for the function sequence_statictics
    """
    test = sequence_statictics(['MKEELDAFHQIFTTTKEAIERFMAMLTPVIENAEDDHERLY' + \
                                'YHHIYEEEEQRLSRLDVLIPLIEKFQDETDEGLFSPSNNAF' + \
                                'NRLLQELNLEKFGLHNFIEHVDLALFSFTDEERQTLLKELR' + \
                                'KDAYEGYQYVKEKLAEINARFDHDYADPHAHHDEHRDHLAD' + \
                                'MPSAGSSHEEVQPVAHKKKGFTVGSLIQ'])
    assert test == {'lenghts': [192], 'min': 192, 'max': 192,
                    'mean': 192.0, 'median': 192}, 'Incorrect result'
    print('Correct test for sequence_statictics')

    test = sequence_statictics(['MKEELDAFHQIFTTTKEAIERFMAMLTPVIENAEDDHERLY' + \
                                'YHHIYEEEEQRLSRLDVLIPLIEKFQDETDEGLFSPSNNAF' + \
                                'NRLLQELNLEKFGLHNFIEHVDLALFSFTDEERQTLLKELR' + \
                                'KDAYEGYQYVKEKLAEINARFDHDYADPHAHHDEHRDHLAD' + \
                                'MPSAGSSHEEVQPVAHKKKGFTVGSLIQ', 'MASNALSSF' + \
                                'TAANPALSPKPLLPHGSASPSVSLGFSRKVGGGRAVVVAAA' + \
                                'TVDTNNMPMTGVVFQPFEEVKKADLAIPITSHASLARQRFA' + \
                                'DASEAVINEQINVEYNVSYVYHSMYAYFDRDNVAMKGLAKF' + \
                                'FKESSEEERGHAEKFMEYQNQRGGRVKLHPIVSPISEFEHA' + \
                                'EKGDALYAMELALSLEKLTNEKLLNVHKVASENNDPQLADF' + \
                                'VESEFLGEQIEAIKKISDYITQLRMIGKGHGVWHFDQMLLN'])
    assert test == {'lenghts': [192, 255], 'min': 192, 'max': 255,
                    'mean': 223.5, 'median': 223.5}, 'Incorrect result'
    print('Correct test for sequence_statictics')

    test = sequence_statictics([])
    assert test == {'lenghts': [], 'min': '', 'max': '', 'mean': '',
                    'median': ''}, 'Incorrect result'
    print('Correct test for sequence_statictics')


test_sequence_statictics()
