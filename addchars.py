#!/bin/python

from addcharslib import *

def modifySource(sfd, f, s, sn):
    print sfd

    workshop = 1.0
    upm = 1000.0/2048.0
    scale = '-s ' + str(upm/workshop) + ' '

    asn = sn
    asn = asn.replace('BoldItalic', 'Bold')
    asn = asn.replace('Italic', 'Regular')
    cmd = scale + '-i ' + annapurna + asn + '.ttf' + ' --rangefile cs/annapurna/main.txt'
    modifyFile(cmd, sfd)

    gs = s.replace('-', '')
    cmd = scale + '-i ' + gentium + gs + '.ttf' + ' --namefile cs/gentium/main_glyphs.txt --rangefile cs/gentium/pre.txt --rangefile cs/gentium/main.txt'
    modifyFile(cmd, sfd)
    cmd = scale + '-i ' + charis + s + '.ttf' + ' --rangefile cs/charis/composite4gentium.txt --rangefile cs/charis/extra4gentium.txt'
    modifyFile(cmd, sfd)

for f in faces:
    for (s, sn) in zip(styles, stylesName):
        sn = sn.replace(' ', '')
        modifySource(f + '-' + sn + '.sfd', f, s, sn)
