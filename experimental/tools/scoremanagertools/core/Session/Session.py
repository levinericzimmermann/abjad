# -*- encoding: utf-8 -*-
import os
from abjad.tools import stringtools
from abjad.tools import abctools
from experimental.tools.scoremanagertools.core.ScoreManagerConfiguration import \
    ScoreManagerConfiguration
from experimental.tools.scoremanagertools.core.Transcript import Transcript


class Session(abctools.AbjadObject):

    ### CLASS ATTRIBUTES ###

    configuration = ScoreManagerConfiguration()

    ### INITIALIZER ###

    def __init__(self, user_input=None):
        self._backtracking_stack = []
        self._breadcrumb_cache_stack = []
        self._breadcrumb_stack = []
        self._command_history = []
        self._session_once_had_user_input = False
        self._transcript = Transcript()
        self.underscore_delimited_current_score_name = None
        self.display_pitch_ranges_with_numbered_pitches = False
        self.dump_transcript = False
        self.enable_where = False
        self.hide_next_redraw = False
        self.initial_user_input = user_input
        self.is_autoadding = False
        self.is_backtracking_locally = False
        self.is_backtracking_to_score = False
        self.is_backtracking_to_score_manager = False
        self.is_navigating_to_next_score = False
        self.is_navigating_to_prev_score = False
        self.last_command_was_composite = False
        self.menu_header_width = 100
        self.nonnumbered_menu_sections_are_hidden = False
        self.transcribe_next_command = True
        self.use_current_user_input_values_as_default = False
        self.user_input = user_input
        self.user_specified_quit = False
        self.show_active_scores()

    ### SPECIAL METHODS ###

    def __repr__(self):
        summary = []
        if self.initial_user_input is not None:
            summary.append('initial_user_input={!r}'.format(self.initial_user_input))
        if self.user_input is not None:
            summary.append('user_input={!r}'.format(self.user_input))
        summary = ', '.join(summary)
        return '{}({})'.format(type(self).__name__, summary)

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def backtracking_stack(self):
        return self._backtracking_stack

    @property
    def breadcrumb_cache_stack(self):
        return self._breadcrumb_cache_stack

    @property
    def breadcrumb_stack(self):
        return self._breadcrumb_stack

    @property
    def command_history(self):
        return self._command_history

    @property
    def command_history_string(self):
        return ' '.join(self.explicit_command_history)

    @property
    def current_materials_directory_path(self):
        if self.is_in_score:
            parts = []
            parts.append(self.configuration.user_scores_directory_path)
            parts.append(self.underscore_delimited_current_score_name)
            parts.extend(self.configuration._score_internal_materials_path_infix_parts)
            return os.path.join(*parts)
        else:
            return self.configuration.system_materials_directory_path

    @property
    def current_materials_package_path(self):
        if self.is_in_score:
            parts = []
            parts.append(self.underscore_delimited_current_score_name)
            parts.extend(self.configuration._score_internal_materials_path_infix_parts)
            return '.'.join(parts)
        else:
            return self.configuration.system_materials_package_path

    @property
    def current_score_package_proxy(self):
        from experimental.tools.scoremanagertools.proxies.ScorePackageProxy import ScorePackageProxy
        if self.is_in_score:
            return ScorePackageProxy(
                score_package_name=self.underscore_delimited_current_score_name, session=self)

    @property
    def current_segments_directory_path(self):
        if self.is_in_score:
            parts = []
            parts.append(self.configuration.user_scores_directory_path)
            parts.append(self.underscore_delimited_current_score_name)
            parts.extend(self.configuration._score_internal_segments_path_infix_parts)
            return os.path.join(*parts)
        else:
            return self.configuration.user_sketches_directory_path

    @property
    def current_segments_package_path(self):
        if self.is_in_score:
            parts = []
            parts.append(self.underscore_delimited_current_score_name)
            parts.extend(self.configuration._score_internal_segments_path_infix_parts)
            return '.'.join(parts)
        else:
            return self.configuration.user_sketches_package_path

    @property
    def current_specifiers_directory_path(self):
        if self.is_in_score:
            return os.path.join(
                self.configuration.user_scores_directory_path, 
                self.underscore_delimited_current_score_name, 
                'music', 'specifiers')
        else:
            return self.configuration.system_specifiers_directory_path

    @property
    def current_specifiers_package_path(self):
        if self.is_in_score:
            parts = []
            parts.append(self.underscore_delimited_current_score_name)
            parts.extend(self.configuration._score_internal_specifiers_path_infix_parts)
            return '.'.join(parts)
        else:
            return self.configuration.system_specifiers_package_path

    @property
    def explicit_command_history(self):
        result = []
        for command in self.command_history:
            if command == '':
                result.append('default')
            else:
                result.append(command)
        return result

    @property
    def is_complete(self):
        return self.user_specified_quit

    @property
    def is_displayable(self):
        return not self.user_input

    @property
    def is_in_score(self):
        return self.underscore_delimited_current_score_name is not None

    @property
    def is_navigating_to_sibling_score(self):
        if self.is_navigating_to_next_score:
            return True
        if self.is_navigating_to_prev_score:
            return True
        return False

    @property
    def last_semantic_command(self):
        for command in reversed(self.command_history):
            if not command.startswith('.'):
                return command

    @property
    def menu_header(self):
        return '\n'.join(self.format_breadcrumb_stack())

    @property
    def scores_to_show(self):
        return self._scores_to_show

    @property
    def session_once_had_user_input(self):
        return self._session_once_had_user_input

    @property
    def testable_command_history_string(self):
        result = []
        for part in self.explicit_command_history:
            if ' ' in part and ',' not in part:
                part = part.replace(' ', '~')
            result.append(part)
        return ' '.join(result)

    @apply
    def transcribe_next_command():
        def fget(self):
            return self._transcribe_next_command
        def fset(self, transcribe_next_command):
            assert isinstance(transcribe_next_command, bool)
            self._transcribe_next_command = transcribe_next_command
        return property(**locals())

    @property
    def transcript(self):
        return self._transcript

    @property
    def user_input_is_consumed(self):
        if self._session_once_had_user_input:
            if self.user_input is None:
                return True
        return False

    ### READ / WRITE PUBLIC PROPERTIES ###

    @apply
    def dump_transcript():
        def fget(self):
            return self._dump_transcript
        def fset(self, dump_transcript):
            assert isinstance(dump_transcript, bool)
            self._dump_transcript = dump_transcript
        return property(**locals())

    @apply
    def hide_next_redraw():
        def fget(self):
            return self._hide_next_redraw
        def fset(self, hide_next_redraw):
            assert isinstance(hide_next_redraw, bool)
            self._hide_next_redraw = hide_next_redraw
        return property(**locals())

    @apply
    def is_autoadding():
        def fget(self):
            return self._is_autoadding
        def fset(self, is_autoadding):
            assert isinstance(is_autoadding, bool)
            self._is_autoadding = is_autoadding
        return property(**locals())

    @apply
    def is_backtracking_locally():
        def fget(self):
            return self._is_backtracking_locally
        def fset(self, is_backtracking_locally):
            assert isinstance(is_backtracking_locally, bool)
            self._is_backtracking_locally = is_backtracking_locally
        return property(**locals())

    @apply
    def is_backtracking_to_score():
        def fget(self):
            return self._is_backtracking_to_score
        def fset(self, is_backtracking_to_score):
            assert isinstance(is_backtracking_to_score, bool)
            self._is_backtracking_to_score = is_backtracking_to_score
        return property(**locals())

    @apply
    def is_backtracking_to_score_manager():
        def fget(self):
            return self._is_backtracking_to_score_manager
        def fset(self, is_backtracking_to_score_manager):
            assert isinstance(is_backtracking_to_score_manager, bool)
            self._is_backtracking_to_score_manager = is_backtracking_to_score_manager
        return property(**locals())

    @apply
    def nonnumbered_menu_sections_are_hidden():
        def fget(self):
            return self._nonnumbered_menu_sections_are_hidden
        def fset(self, nonnumbered_menu_sections_are_hidden):
            assert isinstance(nonnumbered_menu_sections_are_hidden, bool)
            self._nonnumbered_menu_sections_are_hidden = nonnumbered_menu_sections_are_hidden
        return property(**locals())

    @apply
    def underscore_delimited_current_score_name():
        def fget(self):
            return self._underscore_delimited_current_score_name
        def fset(self, underscore_delimited_current_score_name):
            assert isinstance(underscore_delimited_current_score_name, (str, type(None)))
            self._underscore_delimited_current_score_name = underscore_delimited_current_score_name
        return property(**locals())

    @apply
    def use_current_user_input_values_as_default():
        def fget(self):
            return self._use_current_user_input_values_as_default
        def fset(self, use_current_user_input_values_as_default):
            assert isinstance(use_current_user_input_values_as_default, bool)
            self._use_current_user_input_values_as_default = use_current_user_input_values_as_default
        return property(**locals())

    @apply
    def user_input():
        def fget(self):
            return self._user_input
        def fset(self, user_input):
            assert isinstance(user_input, (str, type(None)))
            self._user_input = user_input
            if isinstance(user_input, str):
                self._session_once_had_user_input = True
        return property(**locals())

    @apply
    def user_specified_quit():
        def fget(self):
            return self._user_specified_quit
        def fset(self, user_specified_quit):
            assert isinstance(user_specified_quit, bool)
            self._user_specified_quit = user_specified_quit
        return property(**locals())

    ### PUBLIC METHODS ###

    def backtrack(self, source=None):
        if self.is_complete:
            return True
        elif self.is_backtracking_to_score_manager and source == 'home':
            self.is_backtracking_to_score_manager = False
            return False
        elif self.is_backtracking_to_score_manager and not source == 'home':
            return True
        elif self.is_backtracking_to_score and source in ('score', 'home'):
            self.is_backtracking_to_score = False
            return False
        elif self.is_backtracking_to_score and not source in ('score', 'home'):
            return True
        elif self.is_backtracking_locally and not source == 'home' and \
            self.backtracking_stack:
            return True
        elif self.is_backtracking_locally and not source == 'home' and \
            not self.backtracking_stack:
            self.is_backtracking_locally = False
            return True

    def cache_breadcrumbs(self, cache=False):
        if cache:
            self.breadcrumb_cache_stack.append(self._breadcrumb_stack[:])
            self._breadcrumb_stack[:] = []

    def clean_up(self):
        if self.dump_transcript:
            self.transcript.write_to_disk()

    def format_breadcrumb_stack(self):
        if not self._breadcrumb_stack:
            return ''
        result_lines = [self._breadcrumb_stack[0]]
        hanging_indent_width = len(stringtools.strip_diacritics_from_binary_string(
            self._breadcrumb_stack[0]))
        hanging_indent_width += len(' - ')
        for breadcrumb in self._breadcrumb_stack[1:]:
            candidate_line = result_lines[-1] + ' - ' + breadcrumb
            if len(candidate_line) <= self.menu_header_width:
                result_lines[-1] = candidate_line
            else:
                result_line = hanging_indent_width * ' ' + breadcrumb
                result_lines.append(result_line)
        return result_lines

    def pop_backtrack(self):
        return self.backtracking_stack.pop()

    def pop_breadcrumb(self, rollback=True):
        if rollback:
            return self._breadcrumb_stack.pop()

    def push_backtrack(self):
        if self.backtracking_stack:
            last_number = self.backtracking_stack[-1]
            self.backtracking_stack.append(last_number + 1)
        else:
            self.backtracking_stack.append(0)

    def push_breadcrumb(self, breadcrumb, rollback=True):
        if rollback:
            self._breadcrumb_stack.append(breadcrumb)

    def reinitialize(self):
        type(self).__init__(self)

    def restore_breadcrumbs(self, cache=False):
        if cache:
            self._breadcrumb_stack[:] = self.breadcrumb_cache_stack.pop()

    def show_active_scores(self):
        self._scores_to_show = 'active'

    def show_all_scores(self):
        self._scores_to_show = 'all'

    def show_mothballed_scores(self):
        self._scores_to_show = 'mothballed'

    def swap_user_input_values_default_status(self):
        current = self.use_current_user_input_values_as_default
        self.use_current_user_input_values_as_default = not current
