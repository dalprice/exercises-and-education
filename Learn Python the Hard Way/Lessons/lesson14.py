__author__ = 'Dal'

from sys import argv

script, other_var, user_name = argv
prompt = '> '

print 'Hi {}, I\'m the {} script.'.format(user_name, script)
print 'I\'d like to ask you a few questions.'
print 'Do you like me {}?'.format(user_name)
likes = raw_input(prompt)

print 'Where do you live {}'.format(user_name)
lives = raw_input(prompt)

print 'What kind of computer do you have?'
computer = raw_input(prompt)

print """
Alright, so you said {} about liking me.
You live in {}. Not sure where that is.
And you have a {} computer. Nice. {}
""".format(likes, lives, computer, other_var)

