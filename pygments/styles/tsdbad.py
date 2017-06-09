# -*- coding: utf-8 -*-
"""
    pygments.styles.tsdbad
    ~~~~~~~~~~~~~~~~~~~~~~

    pygments Two Scoops of Django 'bad' theme

    :copyright: Copyright 2017 by Daniel Roy Greenfeld
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Token, Whitespace


class TSDBadStyle(Style):
    """
    pygments Two Scoops of Django 'bad' theme
    """

    background_color = '#666666'
    highlight_color = '#666666'

    styles = {
        Token:              '#000000',
        Whitespace:         '#666666',

        Comment:            'italic #000000',
        Comment.Preproc:    'italic bold #000000',
        Comment.Special:    'italic bold #000000 bg:#000000',

        Keyword:            'bold #000000',
        Keyword.Pseudo:     'nobold',
        Operator.Word:      'bold #000000',

        String:             '#000000',
        String.Other:       '#000000',

        Number:             '#000000',

        Name.Builtin:       '#000000',
        Name.Variable:      '#000000',
        Name.Constant:      '#000000',
        Name.Class:         'bold #000000',
        Name.Function:      'bold #000000',
        Name.Namespace:     'bold #000000',
        Name.Exception:     'bold #000000',
        Name.Tag:           'bold #000000',
        Name.Attribute:     'bold #000000',
        Name.Decorator:     'bold #000000',

        Generic.Heading:    'bold #ffffff',
        Generic.Subheading: 'underline #ffffff',
        Generic.Deleted:    '#000000',
        Generic.Inserted:   '#000000',
        Generic.Error:      '#000000',
        Generic.Emph:       'italic',
        Generic.Strong:     'bold',
        Generic.Prompt:     '#d0d0d0',
        Generic.Output:     '#d0d0d0',
        Generic.Traceback:  '#000000',

        Error:              'bg:#000000 #d0d0d0'
    }
