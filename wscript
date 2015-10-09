# vayalar

# set folder names
out='results'
TESTDIR='tests'
STANDARDS='tests/reference'

# set meta-information
script='mlym'
APPNAME='nlci-' + script
VERSION='0.100'
TTF_VERSION='0.100'
COPYRIGHT='Copyright (c) 2009-2015, NLCI (http://www.nlci.in/fonts/)'

DESC_SHORT='Malayalam Unicode font with OT support'
DESC_LONG='''
Pan Malayalam font designed to support all the languages using the Malayalam script.
'''
DESC_NAME='NLCI-' + script
DEBPKG='fonts-nlci-' + script

# set test parameters
TESTSTRING=u'\u0d15'

# set fonts to build
#faces = ('Vayalar', 'Kalyani', 'Malabar')
#styles = ('-R', '-B', '-I', '-BI')
#stylesName = ('Regular', 'Bold', 'Italic', 'Bold Italic')

faces = ('Vayalar',)
styles = ('-R',)
stylesName = ('Regular',)

# set build parameters
fontbase = 'source/'
tag = script.upper()

for f in faces:
    for (s, sn) in zip(styles, stylesName):
        font(target = process(tag + f + '-' + sn + '.ttf',
                cmd('psfix ${DEP} ${TGT}'),
                name(tag + ' ' + f, lang='en-US', subfamily=(sn))
                ),
            source = fontbase + f + s + '.sfd',
            sfd_master = fontbase + 'master.sfd',
            opentype = internal(),
            #graphite = gdl(fontbase + f + s + '.gdl',
            #    master = fontbase + 'master.gdl',
            #    make_params = '-p 1 -s 2 -l first',
            #    params = '-d -v2'
            #    ),
            #classes = fontbase + 'vayalar_classes.xml',
            ap = f + s + '.xml',
            version = TTF_VERSION,
            copyright = COPYRIGHT,
            license = ofl('Vayalar', 'Kalyani', 'Malabar', 'NLCI'),
            woff = woff(),
            script = 'mlym',
            fret = fret(params = '-r')
        )
