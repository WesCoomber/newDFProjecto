import re, sys
import functools
import graphviz as gv
from graphviz import Source
#bad_words = [ 'jnb','jnbe','jnle','jp', 'jns', 'js', 'jnz', 'jz', 'jno', 'jo', 'jbe', 'jb', 'jle', 'jl', 'jae', 'ja', 'jne loc', 'je', 'jmp', 'jge', 'jg', 'SLICE_EXTRA', '[BUG]', '[ERROR]','SLICE_VERIFICATION', 'syscall', '#PARAMS_LOG']
renderFileName = 'rendered2cleanedExGraphWes.gv'

#removes jumps (Control flow instructions) for right now
bad_words = ['.section', '.globl', '_start:', 'jnb','jnbe','jnle','jp', 'jns', 'js', 'jnz', 'jz', 'jno', 'jo', 'jbe', 'jb', 'jle', 'jl', 'jae', 'ja', 'jne loc', 'je', 'jmp', 'jge', 'jg',]
sliceEnd = False
sliceStarted = False

extraMem = False

graphString = ''

with open('test-output/cleanedExGraphWes.gv') as oldfile, open('2cleanedExGraphWes.gv', 'w') as newfile:
    i=0
    for line in oldfile:
        if (i == 0):
            #line = newfile.readline()
            line = 'strict ' + line
        newfile.write(line)
        graphString = graphString + line
        i = i+1


src = Source(graphString)
src.render(renderFileName, view=True)

print('Done! Parsed graph in: ') + newfile.name



