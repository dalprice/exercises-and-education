__author__ = 'Dal'

from sys import argv

script, filename = argv


print 'We\'re going to erase {}'.format(filename)
print 'If you don\'t want that, hit CTRL-C.'
print 'If you do want that, hit RETURN.'

raw_input('?')

print 'Opening the file...'
target = open(filename, 'r+')

print 'Reading the file.'
target.read()

print 'Truncating the file. Goodbye!'
target.truncate()

print 'Now I\'m going to ask you for three lines.'
line_1 = raw_input('Line 1: ')
line_2 = raw_input('Line 2: ')
line_3 = raw_input('Line 3: ')

print 'I\'m going to write these to the file.'

target.write(line_1 + '\n' + line_2 + '\n' + line_3 + '\n')

print 'And finally, we close it.'
target.close()
