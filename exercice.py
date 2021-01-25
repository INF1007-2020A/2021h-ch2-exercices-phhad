#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    return mot
    # Test.


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
        'araignée'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
