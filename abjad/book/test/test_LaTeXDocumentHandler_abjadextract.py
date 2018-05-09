import abjad
import abjad.book
from uqbar.strings import normalize


def test_abjadextract_1():
    input_file_contents = [
        '',
        '\\begin{comment}',
        '<abjadextract abjad.book:example_function \>',
        '\\end{comment}',
        '',
        ]
    document_handler = abjad.book.LaTeXDocumentHandler()
    input_blocks = document_handler.collect_input_blocks(input_file_contents)
    code_block = tuple(input_blocks.values())[0]
    assert code_block.executed_lines == (
        'from abjad.book import example_function',
        )
    assert code_block.input_file_contents == (
        'def example_function(argument):',
        "    r'''This is a multiline docstring.",
        '',
        '    This is the third line of the docstring.',
        "    '''",
        '    # This is a comment.',
        "    print('Entering example function.')",
        '    try:',
        '        argument = argument + 1',
        '    except TypeError:',
        "        print('Wrong type!')",
        '    print(argument)',
        "    print('Leaving example function.')",
        )


def test_abjadextract_2():
    input_file_contents = [
        '\\begin{comment}',
        '<abjadextract abjad.book:example_function \>',
        '\\end{comment}',
        '',
        '\\begin{comment}',
        '<abjad>[allow_exceptions=true]',
        "example_function('foo')",
        '</abjad>',
        '\\end{comment}',
        '',
        '\\begin{comment}',
        '<abjad>[allow_exceptions=true]',
        "example_function(23)",
        '</abjad>',
        '\\end{comment}',
        ]
    document_handler = abjad.book.LaTeXDocumentHandler(
        input_file_contents=input_file_contents,
        )
    rebuilt_source = document_handler(return_source=True)
    assert rebuilt_source == normalize(
        """
        \\begin{comment}
        <abjadextract abjad.book:example_function \\>
        \\end{comment}

        %%% ABJADBOOK START %%%
        \\begin{lstlisting}
        def example_function(argument):
            r'''This is a multiline docstring.

            This is the third line of the docstring.
            '''
            # This is a comment.
            print('Entering example function.')
            try:
                argument = argument + 1
            except TypeError:
                print('Wrong type!')
            print(argument)
            print('Leaving example function.')
        \\end{lstlisting}
        %%% ABJADBOOK END %%%

        \\begin{comment}
        <abjad>[allow_exceptions=true]
        example_function('foo')
        </abjad>
        \\end{comment}

        %%% ABJADBOOK START %%%
        \\begin{lstlisting}
        >>> example_function('foo')
        Entering example function.
        Wrong type!
        foo
        Leaving example function.
        \\end{lstlisting}
        %%% ABJADBOOK END %%%

        \\begin{comment}
        <abjad>[allow_exceptions=true]
        example_function(23)
        </abjad>
        \\end{comment}

        %%% ABJADBOOK START %%%
        \\begin{lstlisting}
        >>> example_function(23)
        Entering example function.
        24
        Leaving example function.
        \\end{lstlisting}
        %%% ABJADBOOK END %%%
        """,
        )


def test_abjadextract_3():
    input_file_contents = [
        '\\begin{comment}',
        '<abjadextract abjad.book:example_function \>[hide=true]',
        '\\end{comment}',
        '',
        '\\begin{comment}',
        '<abjad>[allow_exceptions=true]',
        "example_function('foo')",
        '</abjad>',
        '\\end{comment}',
        '',
        '\\begin{comment}',
        '<abjad>[allow_exceptions=true]',
        "example_function(23)",
        '</abjad>',
        '\\end{comment}',
        ]
    document_handler = abjad.book.LaTeXDocumentHandler(
        input_file_contents=input_file_contents,
        )
    rebuilt_source = document_handler(return_source=True)
    assert rebuilt_source == normalize(
        """
        \\begin{comment}
        <abjadextract abjad.book:example_function \\>[hide=true]
        \\end{comment}

        \\begin{comment}
        <abjad>[allow_exceptions=true]
        example_function('foo')
        </abjad>
        \\end{comment}

        %%% ABJADBOOK START %%%
        \\begin{lstlisting}
        >>> example_function('foo')
        Entering example function.
        Wrong type!
        foo
        Leaving example function.
        \\end{lstlisting}
        %%% ABJADBOOK END %%%

        \\begin{comment}
        <abjad>[allow_exceptions=true]
        example_function(23)
        </abjad>
        \\end{comment}

        %%% ABJADBOOK START %%%
        \\begin{lstlisting}
        >>> example_function(23)
        Entering example function.
        24
        Leaving example function.
        \\end{lstlisting}
        %%% ABJADBOOK END %%%
        """,
        )