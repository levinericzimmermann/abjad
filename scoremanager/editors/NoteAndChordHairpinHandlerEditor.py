# -*- encoding: utf-8 -*-
from experimental.tools import handlertools
from scoremanager import getters
from scoremanager.editors.Editor import Editor


class NoteAndChordHairpinHandlerEditor(Editor):
    r'''NoteAndChorHairpinHandler editor.
    '''

    ### PUBLIC PROPERTIES ###

    @property
    def target_manifest(self):
        from editors import TargetManifest
        return TargetManifest(
            handlertools.NoteAndChordHairpinHandler,
            ('hairpin_token', None, 'ht', getters.get_hairpin_token, True),
            ('minimum_duration', None, 'md', getters.get_duration, True),
            )
