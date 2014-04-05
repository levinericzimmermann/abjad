# -*- encoding: utf-8 -*-
from abjad import *


def apply_dynamics(score):
    r'''Applies dynamics to score.
    '''

    voice = score['Bell Voice']
    dynamic = indicatortools.Dynamic('ppp')
    attach(dynamic, voice[0][1])
    dynamic = indicatortools.Dynamic('pp')
    attach(dynamic, voice[8][1])
    dynamic = indicatortools.Dynamic('p')
    attach(dynamic, voice[18][1])
    dynamic = indicatortools.Dynamic('mp')
    attach(dynamic, voice[26][1])
    dynamic = indicatortools.Dynamic('mf')
    attach(dynamic, voice[34][1])
    dynamic = indicatortools.Dynamic('f')
    attach(dynamic, voice[42][1])
    dynamic = indicatortools.Dynamic('ff')
    attach(dynamic, voice[52][1])
    dynamic = indicatortools.Dynamic('fff')
    attach(dynamic, voice[60][1])
    dynamic = indicatortools.Dynamic('ff')
    attach(dynamic, voice[68][1])
    dynamic = indicatortools.Dynamic('f')
    attach(dynamic, voice[76][1])
    dynamic = indicatortools.Dynamic('mf')
    attach(dynamic, voice[84][1])
    dynamic = indicatortools.Dynamic('pp')
    attach(dynamic, voice[-1][0])

    voice = score['First Violin Voice']
    dynamic = indicatortools.Dynamic('ppp')
    attach(dynamic, voice[6][1])
    dynamic = indicatortools.Dynamic('pp')
    attach(dynamic, voice[15][0])
    dynamic = indicatortools.Dynamic('p')
    attach(dynamic, voice[22][3])
    dynamic = indicatortools.Dynamic('mp')
    attach(dynamic, voice[31][0])
    dynamic = indicatortools.Dynamic('mf')
    attach(dynamic, voice[38][3])
    dynamic = indicatortools.Dynamic('f')
    attach(dynamic, voice[47][0])
    dynamic = indicatortools.Dynamic('ff')
    attach(dynamic, voice[55][2])
    dynamic = indicatortools.Dynamic('fff')
    attach(dynamic, voice[62][2])

    voice = score['Second Violin Voice']
    dynamic = indicatortools.Dynamic('pp')
    attach(dynamic, voice[7][0])
    dynamic = indicatortools.Dynamic('p')
    attach(dynamic, voice[12][0])
    dynamic = indicatortools.Dynamic('p')
    attach(dynamic, voice[16][0])
    dynamic = indicatortools.Dynamic('mp')
    attach(dynamic, voice[25][1])
    dynamic = indicatortools.Dynamic('mf')
    attach(dynamic, voice[34][1])
    dynamic = indicatortools.Dynamic('f')
    attach(dynamic, voice[44][1])
    dynamic = indicatortools.Dynamic('ff')
    attach(dynamic, voice[54][0])
    dynamic = indicatortools.Dynamic('fff')
    attach(dynamic, voice[62][1])

    voice = score['Viola Voice']
    dynamic = indicatortools.Dynamic('p')
    attach(dynamic, voice[8][0])
    dynamic = indicatortools.Dynamic('mp')
    attach(dynamic, voice[19][1])
    dynamic = indicatortools.Dynamic('mf')
    attach(dynamic, voice[30][0])
    dynamic = indicatortools.Dynamic('f')
    attach(dynamic, voice[36][0])
    dynamic = indicatortools.Dynamic('f')
    attach(dynamic, voice[42][0])
    dynamic = indicatortools.Dynamic('ff')
    attach(dynamic, voice[52][0])
    dynamic = indicatortools.Dynamic('fff')
    attach(dynamic, voice[62][0])

    voice = score['Cello Voice']
    dynamic = indicatortools.Dynamic('p')
    attach(dynamic, voice[10][0])
    dynamic = indicatortools.Dynamic('mp')
    attach(dynamic, voice[21][0])
    dynamic = indicatortools.Dynamic('mf')
    attach(dynamic, voice[31][0])
    dynamic = indicatortools.Dynamic('f')
    attach(dynamic, voice[43][0])
    dynamic = indicatortools.Dynamic('ff')
    attach(dynamic, voice[52][1])
    dynamic = indicatortools.Dynamic('fff')
    attach(dynamic, voice[62][0])

    voice = score['Bass Voice']
    dynamic = indicatortools.Dynamic('mp')
    attach(dynamic, voice[14][0])
    dynamic = indicatortools.Dynamic('mf')
    attach(dynamic, voice[27][0])
    dynamic = indicatortools.Dynamic('f')
    attach(dynamic, voice[39][0])
    dynamic = indicatortools.Dynamic('ff')
    attach(dynamic, voice[51][0])
    dynamic = indicatortools.Dynamic('fff')
    attach(dynamic, voice[62][0])