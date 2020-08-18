#!/usr/bin/python3
# this is a smith configuration file

# vayalar

# command line options
opts = preprocess_args(
    {'opt' : '-l'}, # build fonts from legacy for inclusion into final fonts
    {'opt' : '-p'}, # do not run psfix on the final fonts
    {'opt' : '-s'}  # only build a single font
    )

import os2

# override the default folders
DOCDIR = ['documentation', 'web']

# set meta-information
script='mlym'
APPNAME='nlci-' + script

DESC_SHORT='Malayalam Unicode font with OT support'
DESC_NAME='NLCI-' + script
getufoinfo('source/Vayalar-Regular.ufo')
# BUILDLABEL = 'beta1'

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

# set fonts to build
faces = ('Vayalar', 'Malabar') # Kalyani
facesLegacy = ('vaya', 'mala') # kaly
styles = ('-R', '-B', '-I', '-BI')
stylesName = ('Regular', 'Bold', 'Italic', 'Bold Italic')
stylesLegacy = ('', 'bd', 'i', 'bi')

if '-s' in opts:
    faces = (faces[0],)
    facesLegacy = (facesLegacy[0],)
    styles = (styles[0],)
    stylesName = (stylesName[0],)
    stylesLegacy = (stylesLegacy[0],)

# set build parameters
fontbase = 'source/'
archive = fontbase + 'archive/unhinted/'
generated = 'generated/'
tag = script.upper()

panose = [2, 0, 0, 3]
codePageRange = [0, 29]
unicodeRange = [0, 1, 2, 3, 4, 5, 6, 7, 15, 23, 29, 31, 32, 33, 35, 38, 39, 40, 45, 60, 62, 67, 69, 91]
hackos2 = os2.hackos2(panose, codePageRange, unicodeRange)

if '-l' in opts:
    for f, fLegacy in zip(faces, facesLegacy):
        for (s, sn, sLegacy) in zip(styles, stylesName, stylesLegacy):
            font(target = process('ufo/' + f + '-' + sn.replace(' ', '') + '.ttf',
                    cmd(hackos2 + ' ${DEP} ${TGT}'),
                    name(f, lang='en-US', subfamily=(sn))
                    ),
                source = legacy(f + s + '.ttf',
                                source = archive + fLegacy + sLegacy + '.ttf',
                                xml = fontbase + 'vayalar_unicode.xml',
                                params = '',
                                noap = '')
                )

psfix = 'cp' if '-p' in opts else 'psfix'

if '-l' in opts:
    faces = list()
for f in faces:
    p = package(
        appname = APPNAME + '-' + f.lower(),
        version = VERSION,
        docdir = DOCDIR # 'documentation'
    )
    for sn in stylesName:
        snf = '-' + sn.replace(' ', '')
        fontfilename = tag + f + snf
        font(target = process(fontfilename + '.ttf',
                cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', [fontbase + f + snf + '.ufo']),
                name(tag + ' ' + f, lang='en-US', subfamily=(sn))
                ),
            source = fontbase + f + snf + '.ufo',
            opentype = fea(generated + f + snf + '.fea',
                master = fontbase + 'master.feax',
                make_params = ''
                ),
            #graphite = gdl(generated + f + snf + '.gdl',
            #    master = fontbase + 'master.gdl',
            #    make_params = '-p 1 -s 2',
            #    params = '-e ' + f + snf + '_gdlerr.txt'
            #    ),
            #classes = fontbase + 'vayalar_classes.xml',
            #ap = generated + f + snf + '.xml',
            version = VERSION,
            #woff = woff('woff/' + fontfilename + '.woff', params = '-v ' + VERSION + ' -m ../' + fontbase + f + '-WOFF-metadata.xml'),
            script = 'mlm2', # 'mlym'
            package = p,
            pdf = fret(params = '-oi')
        )
