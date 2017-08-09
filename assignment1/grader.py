#!/usr/bin/python3
import importlib
import sys
import unittest.mock

INPUTS = ('Roger', 'Rabbit', 'rogerrabbit@pitt.edu', 'Biology',
          'Freshman')
OUTPUT = (
    '=' * 80,
    '= Name: Rabbit, Roger | Email: rogerrabbit@pitt.edu',
    '= Major: Biology | Class: Freshman',
    '=' * 80
)


def main(args):
    """
    First argument is the path to include for imports
    Second argument is the name of the program to grade.
    """
    sys.path.append(args[1])
    deductions = 0
    errors = []
    # Import module
    try:
        with unittest.mock.patch('builtins.input', side_effect=INPUTS) as i:
            with unittest.mock.patch('builtins.print') as p:
                program = importlib.import_module(args[2])

        # Check input calls
        try:
            assert i.call_count == 5
        except AssertionError:
            deductions += 5 - i.call_count
            errors.append('-%s: Expected 5 calls to input(), Found %s' %
                (5 - i.call_count, i.call_count))

        # Check print output
        output = ''
        for c in p.call_args_list:
            output += _mock_print(*c[0], **c[1])
        output = output.split('\n')

        for i, expected in enumerate(OUTPUT):
            yours = ''
            if output:
                yours = output.pop(0)
            if (yours != expected):
                deductions += 1
                errors.append(
                    '-1: Output Line %s:\n\tExpected "%s"\n\tYours "%s"' % 
                        (i + 1, expected, yours))

    except SyntaxError as e:
        deductions += 10
        errors.append('-10: Program does not run when imported: %s' % e)

    print('Score: %i of 15' % (15 - deductions))
    print('Deductions: %s' % '\n\t'.join(errors))


def _mock_print(*args, sep=' ', end='\n'):
    """Alternate print used for output in the program."""
    return sep.join(args) + end


if __name__ == '__main__':
  main(sys.argv)
