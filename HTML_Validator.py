#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by
    checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    # empty html is valid lol
    if len(html) == 0:
        return True

    tags = _extract_tags(html)
    stack = []

    # catch if no tags
    if len(tags) == 0:
        return False

    for tag in tags:
        if tag[1] != '/':
            stack.append(tag)
        else:
            if len(stack) == 0:
                return False
            # if closing tag
            if stack[-1] == tag.replace('/', '', 1):
                stack.pop()
            else:
                return False
    return len(stack) == 0

    # HINT:
    # use the _extract_tags function below to generate a list of
    # html tags without any extra text;
    # then process these html tags using the balanced parentheses
    # algorithm from the class/book
    # the main difference between your code and the code from class
    # will be that you will have to keep track of not just the 3
    # types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to
    be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in
    the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    in_tag = False
    tag = ""
    output = []

    for c in html:
        if c == '<' and not in_tag:
            in_tag = True
            tag = '<'
        elif c == '>' and in_tag:
            in_tag = False
            # removes stuff in tag after ' ' character
            tag = tag.split(' ')[0]
            tag += '>'
            output.append(tag)
        elif in_tag:
            tag += c
        else:
            pass

    return output
