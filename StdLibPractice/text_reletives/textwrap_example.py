# textwrap examples

import textwrap

sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired. It offers
    programmatic functionality similar to the paragraph wrapping
    or filling deatures found in many text editors.
    '''

# print(textwrap.fill(sample_text, width=50))

dedented_text = textwrap.dedent(sample_text).strip()
# for width in [45, 60]:
#     print('{} Columns:\n'.format(width))
#     print(textwrap.fill(dedented_text, width=width))
#     print()
# print("Dedented:", dedented_text)

wrapped = textwrap.fill(dedented_text, width=50)
wrapped += '\n\nSecond paragraph after a blank line.'
final = textwrap.indent(wrapped, '> ')

print('Quoted block:\n', final)

# hanging indents
print(textwrap.fill(dedented_text,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=50))

#truncating long text
shortened = textwrap.shorten(wrapped, width=100, placeholder='......')
shortened_wrapped = textwrap.fill(shortened, 50, )
print("Shortened: \n", shortened_wrapped)
