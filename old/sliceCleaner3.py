import re, sys
#bad_words = [ 'jnb','jnbe','jnle','jp', 'jns', 'js', 'jnz', 'jz', 'jno', 'jo', 'jbe', 'jb', 'jle', 'jl', 'jae', 'ja', 'jne loc', 'je', 'jmp', 'jge', 'jg', 'SLICE_EXTRA', '[BUG]', '[ERROR]','SLICE_VERIFICATION', 'syscall', '#PARAMS_LOG']

#removes jumps (Control flow instructions) for right now
bad_words = ['.section', '.globl', '_start:', 'jnb','jnbe','jnle','jp', 'jns', 'js', 'jnz', 'jz', 'jno', 'jo', 'jbe', 'jb', 'jle', 'jl', 'jae', 'ja', 'jne loc', 'je', 'jmp', 'jge', 'jg',]
sliceEnd = False
sliceStarted = False

extraMem = False

with open('exslice.asm') as oldfile, open('cleanedExSlice.asm', 'w') as newfile:

    for line in oldfile:
	    if ((not any(bad_word in line for bad_word in bad_words)) and ( not line.startswith('get_mem_value'))):
	    	if (line.startswith('/*slice begins*/')):
	    		sliceStarted = True
	    	if (not line.startswith('/* slice finishes')):
	    		if '[e' in line and '#src_regmemreg' in line:
	    			linePieces = line.split(' #src_regmemreg')
	    			linePieces = linePieces[1].split(',')
	    			linePieces = linePieces[1].split(':')
	    			ultMemAddr = linePieces[0]
	    			extraMem = True

	    		prepline = re.sub("/\*(.|\n)*?\*/", '', line)
	    		prepline = re.sub(",", '', prepline)
	    		prepline = re.sub(' +',' ', prepline)

	    		if extraMem == True:
		    		prepline = re.sub('\n','', prepline)
	    			prepline = prepline + "[0x" + ultMemAddr + ']\n'
	    			extraMem = False
	    			prepline = re.sub("\s\s+",' ', prepline)
	    			#print(prepline)
	    	else: 
	    		sliceEnd = True
	    		break
	    	if not prepline.isspace():
	    		if (sliceStarted == True):
	        		newfile.write(prepline)


print('Done! Parsed slice in: ') + newfile.name

