"""
Author: Marta Skowron

Odpowiedź użytkonika Hooked na temat usuwania osi z wykresów
https://stackoverflow.com/questions/9295026/how-to-remove-axis-legends-and-white-padding

Przykłady filtrów konwolucyjnych
https://en.wikipedia.org/wiki/Kernel_(image_processing)
"""

import nrrd
import matplotlib.pyplot as plt
from scipy.ndimage.filters import convolve


def filtry_3D(plik, filtr, tekst): 
    obraz, naglowek = nrrd.read(plik)
    rys, osie = plt.subplots(ncols=5, nrows=3, constrained_layout=True)
    i = 0
    m = obraz.shape[3] // 10 #poimjamy pierwsze 10% obrazów, ponieważ nic nie wnoszą
    for os in osie.flatten():
        if m<obraz.shape[3] and i<obraz.shape[0]:
            os.imshow(obraz[i, :, :, m], cmap=plt.cm.gray)
            os.set_xticks([])
            os.set_yticks([])
            i += obraz.shape[0] // len(osie.flatten())
            m += obraz.shape[3] // len(osie.flatten())
        else:
            break
    plt.savefig("zestawienie.png", bbox_inches='tight')
    plt.show()
    
    przefiltrowany = convolve(obraz[obraz.shape[0] // 2, :, :, 
                                    obraz.shape[3] // 2], filtr)
    
    plt.imshow(przefiltrowany, cmap=plt.cm.gray)
    plt.axis('off')
    plt.savefig('z_filtrem_' + str(tekst) + '.png', bbox_inches='tight')
    plt.show()
    
    plt.imshow(obraz[obraz.shape[0] // 2, :, :, obraz.shape[3] // 2], 
               cmap=plt.cm.gray)
    plt.axis('off')
    plt.savefig("bez_filtra.png", bbox_inches='tight')
    plt.show()


filtry={'wyostrzenie' : [[0,-1,0],[-1,5,-1],[0,-1,0]], 
        'zmodyfikowany_unsharp_masking' : [[1,4,6,4,1],[4,16,24,16,4],
        [6,24,-476,24,6],[4,16,24,16,4],[1,4,6,4,1]]}

filtry_4D('DTI-Brain.nrrd', filtry['wyostrzenie'], 'wostrzenie')
filtry_4D('DTI-Brain.nrrd', filtry['zmodyfikowany_unsharp_masking'], 
          'zmodyfikowany_unsharp_masking')
