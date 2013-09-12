# -*- encoding: utf-8 -*-
import os
from experimental.tools.scoremanagertools.proxies.FilesystemAssetProxy \
    import FilesystemAssetProxy


class FileProxy(FilesystemAssetProxy):
    r'''File proxy.
    '''

    ### CLASS VARIABLES ###

    _generic_class_name = 'file'

    _temporary_asset_name = 'temporary_file.txt'

    extension = ''

    ### PRIVATE PROPERTIES ###

    @property
    def _is_executable(self):
        if self.filesystem_path.endswith('.py'):
            return True
        return False

    @property
    def _is_editable(self):
        if self.filesystem_path.endswith(('.tex', '.py')):
            return True
        return False

    @property
    def _is_viewable(self):
        if self.filesystem_path.endswith('.pdf'):
            return True
        return False

    ### PRIVATE METHODS ###

    def _handle_main_menu_result(self, result):
        if result in self.user_input_to_action:
            self.user_input_to_action[result](self)

    def _make_main_menu(self):
        main_menu = self.session.io_manager.make_menu(where=self._where)
        self._main_menu = main_menu
        command_section = main_menu.make_command_section()
        if self._is_editable:
            command_section.append(('edit', 'ed'))
        command_section.append(('rename', 'ren'))
        command_section.append(('remove', 'rm'))
        if self._is_executable:
            command_section.append(('run', 'run'))
        if self._is_viewable:
            command_section.append(('view', 'v'))
        return main_menu

    ### PUBLIC METHODS ###

    def interactively_edit(self):
        r'''Interactively edits file.

        Returns none.
        '''
        os.system('vim + {}'.format(self.filesystem_path))

    def interactively_view(self):
        r'''Interactively views file.

        Returns none.
        '''
        if self.filesystem_path.endswith('.pdf'):
            command = 'open {}'.format(self.filesystem_path)
        else:
            command = 'vim -R {}'.format(self.filesystem_path)
        os.system(command)

    def make_empty_asset(self, is_interactive=False):
        r'''Makes emtpy file.

        Returns none.
        '''
        if not self.exists():
            file_reference = file(self.filesystem_path, 'w')
            file_reference.write('')
            file_reference.close()
        self.session.io_manager.proceed(is_interactive=is_interactive)

    def read_lines(self):
        r'''Reads lines in file.

        Returns list.
        '''
        result = []
        if self.filesystem_path:
            if os.path.exists(self.filesystem_path):
                file_pointer = file(self.filesystem_path)
                result.extend(file_pointer.readlines())
                file_pointer.close()
        return result

    def run(self):
        r'''Runs Python on file.

        Returns none.
        '''
        command = 'python {}'.format(self.filesystem_path)
        os.system(command)

    ### UI MANIFEST ###

    user_input_to_action = FilesystemAssetProxy.user_input_to_action.copy()
    user_input_to_action.update({
        'ed': interactively_edit,
        'run': run,
        'v': interactively_view,
        })
