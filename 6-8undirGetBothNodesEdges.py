import re, sys
import functools
import graphviz as gv
from graphviz import Source


fileName = 'cleanedExSlice.asm'
#fileName = '200CleanedSlice.txt'
outFileName = 'cleanedExGraph.txt'
#outFileName = '200UndirOutputGraph.txt'
renderFileName = 'test-output/cleanedExGraphWes.gv'
#renderFileName = 'test-output/200UndirDataFlowSliceWes.gv'

k = 1 
y = 1 
memAddressList = []
nodeCount = -1
instrEdges = []
instrNodes = []

#get the instrNodes with their appropraite line numbers
with open(fileName) as oldfile:
    for line in oldfile:
        splitLine = line.split()

        tempEdgeList = []

        #if not a system call in the cleanedExSlice then must be a normal slice Instruction 
        #and only add the first word + its line number as a single node 
        if (splitLine[0] != 'call'):
            instrNodes.append('[' +str (k) + '] '+splitLine[0])
            

            for idx, words in enumerate(splitLine):
                if (idx != 0):
                    if ((splitLine[idx] != 'dword') and (splitLine[idx] != 'ptr') and (splitLine[idx] != 'byte')):
                        if('[0x' in splitLine[idx]):
                            memAddressList.append(splitLine[idx])
                        tempEdgeList.append(splitLine[idx])
        #else must be a system call so include both first two words + its line number
        else:
            instrNodes.append('[' +str (k) + '] '+splitLine[0] + '-' + splitLine[1])
        k = k + 1
        instrEdges.append(tempEdgeList) 


#list of instrNodes in the format ['[1] b7ff5c05-cmp', '[2] b7fe3d14-cmp']
print('Done! Instruction instrNodes List Size is : ') 
print(len(instrNodes))

#print(instrNodes)
#print(instrEdges)

print(memAddressList)


print('Done! Instruction Edges List size is : ')
print(len(instrEdges))
#print(instrEdges)


nodeEdgesDict = {k: v for k, v in zip(instrNodes, instrEdges)}
#example dictionary entry is dict1['0-cmp': 'eax, 0xfffff001']
print('Done! Dict (LineNumber-Instruction: Edges) is : ')
#rint("first node(instr): and its edges(operands): " + 'b7ff5c05-cmp: '+str(nodeEdgesDict['b7ff5c05-cmp']))

flagEnterKeys = 1

while (flagEnterKeys == 1):
    input_var = raw_input('Enter a key (b7ff5c05-cmp for the 1st instruction cmp in the slice): TYPE EXIT TO End.\n')
    
    if (input_var in nodeEdgesDict):
        print("Operands for " + input_var + " are: " + str(nodeEdgesDict[input_var]) + ".\n")
        break
    if ((input_var == "exit") or (input_var == ",exit,")):
        flagEnterKeys = 0;
        break
    else :
        print("ERROR! Please enter in a valid key for the instrNodes, instrEdges dictionary.")  

    
    
##New Graphviz-dot code here 
graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')

datG = graph()
#list of instrNodes in the format ['[1] b7ff5c05-cmp', '[2] b7fe3d14-cmp']
#instrNodes
#list of edges in the format ['eax, 0xfffff001', 'eax, 0x33']
#nstrEdges

#This block of code is hacky way to get rid of duplicates in memAddressList
#print(memAddressList)
memAddressDict = {k: v for k, v in zip(memAddressList, memAddressList)}
#memAddressList = list(memAddressDict.keys())
#print(memAddressList)


def add_nodes(graph):
    for n in instrNodes:
        graph.node(n, label = str(n) + '(' + str(nodeEdgesDict[n]) + ')')
    return graph


statusFlags = [] 
datG.node('R', 'Root')
datG.node('EAX', 'EAX')
datG.node('ECX', 'ECX')
datG.node('EDI', 'EDI')
datG.node('EDX', 'EDX')
datG.node('EBX', 'EBX')
datG.node('ESP', 'ESP')
datG.node('EBP', 'EBP')
datG.node('ESI', 'ESI')
datG.node('EDI', 'EDI')
#datG.node('Out', 'Output')


cmpFlags = []
newestOF = 'R'
newestSF = 'R'
newestZF = 'R'
newestAF = 'R'
newestCF = 'R'
newestPF = 'R'

# default values 'R' means edge from root node in the 32-bit 4word registers
#Accumulator    Counter     Data    Base    Stack Pointer   Stack Base Pointer  Source  Destination
EAX = ['EAX','EAX','EAX','EAX']
ECX = ['ECX','ECX','ECX','ECX']
EDI = ['EDI','EDI','EDI','EDI']
EDX = ['EDX','EDX','EDX','EDX']
EBX = ['EBX','EBX','EBX','EBX']
ESP = ['ESP','ESP','ESP','ESP']
EBP = ['EBP','EBP','EBP','EBP']
ESI = ['ESI','ESI','ESI','ESI']
EDI = ['EDI','EDI','EDI','EDI']



#modify Eax register and its 16 and 8 bit versions
def modifyEAX(firstWord, secondWord, thirdWord, fourthWord):
    EAX[0:4] = [firstWord, secondWord, thirdWord, fourthWord]

def modifyAX(thirdWord, fourthWord):
    EAX[2:4] = [thirdWord, fourthWord]

def modifyAH(thirdWord):
    EAX[2:3] = [thirdWord]

def modifyAL(fourthWord):
    EAX[3:4] = [fourthWord]    




#modify ecx register and its 16 and 8 bit versions

def modifyECX(firstWord, secondWord, thirdWord, fourthWord):
    ECX[0:4] = [firstWord, secondWord, thirdWord, fourthWord]

def modifyCX(thirdWord, fourthWord):
    ECX[2:4] = [thirdWord, fourthWord]

def modifyCH(thirdWord):
    ECX[2:3] = [thirdWord]

def modifyCL(fourthWord):
    ECX[3:4] = [fourthWord]    

#modify edx register and its 16 and 8 bit versions

def modifyEDX(firstWord, secondWord, thirdWord, fourthWord):
    EDX[0:4] = [firstWord, secondWord, thirdWord, fourthWord]

def modifyDX(thirdWord, fourthWord):
    EDX[2:4] = [thirdWord, fourthWord]

def modifyDH(thirdWord):
    EDX[2:3] = [thirdWord]

def modifyDL(fourthWord):
    EDX[3:4] = [fourthWord]

#modify ebx register and its 16 and 8 bit versions
def modifyEBX(firstWord, secondWord, thirdWord, fourthWord):
    EBX[0:4] = [firstWord, secondWord, thirdWord, fourthWord]

def modifyBX(thirdWord, fourthWord):
    EBX[2:4] = [thirdWord, fourthWord]

def modifyBH(thirdWord):
    EBX[2:3] = [thirdWord]

def modifyBL(fourthWord):
    EBX[3:4] = [fourthWord]  

#modify esp register and its 16bit versions
def modifyESP(firstWord, secondWord, thirdWord, fourthWord):
    ESP[0:4] = [firstWord, secondWord, thirdWord, fourthWord]

def modifySP(thirdWord, fourthWord):
    ESP[2:4] = [thirdWord, fourthWord]

#modify ebp register and its 16bit versions
def modifyEBP(firstWord, secondWord, thirdWord, fourthWord):
    EBP[0:4] = [firstWord, secondWord, thirdWord, fourthWord]

def modifyBP(thirdWord, fourthWord):
    EBP[2:4] = [thirdWord, fourthWord]

#modify esi register and its 16bit versions
def modifyESI(firstWord, secondWord, thirdWord, fourthWord):
    ESI[0:4] = [firstWord, secondWord, thirdWord, fourthWord]

def modifySI(thirdWord, fourthWord):
    ESI[2:4] = [thirdWord, fourthWord]



#modify edi register and its 16bit versions
def modifyEDI(firstWord, secondWord, thirdWord, fourthWord):
    EDI[0:4] = [firstWord, secondWord, thirdWord, fourthWord]

def modifyDI(thirdWord, fourthWord):
    EDI[2:4] = [thirdWord, fourthWord]

#orange instructions "dest reg or mem location modified as output edge" and one 1 source

orangeInst = [
'cmovz',
'inc',
'neg',
'rep',
'setbe',
'mov',
'cmpxchg',
'setz',
'cmovb',
'cmovbe',
'cmovnbe',
'cmovnz',
'cmovs',
'dec',
'lea',
'movsx',
'movzx',
]




#gold instructions "dest reg or mem location modified as output edge" and two 2 sources

goldInst = [
'and',
'imul',
'sar',
'xor',
'sub',
'add',
'adc',
'shr',
'shl',
'or',
]

#green instructions "dest reg or mem location modified as output edge" and three 3 sources

greenInst = [
'sbb',
]

# one source specified in slice AND one implicit source and no destination output
blueInst = [
#POP = and StackPOINTER is implicitly a source and STACKPOINTER regESP IS MODIFIED
'pop',
#'push',
]

# no source specified in slice AND one implicit source and one destination output
tealInst = [
#PUSH = and StackPOINTER is implicitly a source and STACKPOINTER regESP IS MODIFIED
'push',
]

# one source specified in slice AND one implicit source and one implicit destination output 
redInst = [
#MUL the explicit soure is specified in slice, and AX or DX:AX or EDX:EAX is the implicit source
'mul',
]

# one source specified in slice AND one implicit source and two implicit destination outputs 
greyInst = [
'div',
]

#no explicit sources/one destination output, and consumes flags to set the destination (which is the single explicit arg in slice)
purpInst = [
 'setnz',
]

#pink instructions "NO dest reg or mem location modified as output edge" and two 2 source

pinkInst = [
'test',
'bt',
'cmp'
]



#print('EDGES: ' + str(instrEdges))

pattern = re.compile("^\s+|\s*,\s*|\s+$")
for idx, c in enumerate(instrEdges):

    for idz, b in enumerate(instrEdges[idx]):
        tempNodeStr = instrNodes[(idx)]
        splitStr = instrEdges[idx]

        #input edges for orangeInstructions, such as 'mov' they only have one 1 source(second arg)         
        if idz == 1:
                if any(x in tempNodeStr for x in orangeInst):
                    #print('debug ' + tempNodeStr)
                     #Eax edges 
                    if splitStr[idz] == "eax":
                        for ido, k in enumerate(EAX):
                            datG.edge(k, tempNodeStr, label= k +'(eax)'+str(ido))
                    elif splitStr[idz] == "ax":
                        for ido, k in enumerate(EAX[2:4]):
                            datG.edge(k, tempNodeStr, label= k +'(ax)'+str(ido))
                    elif splitStr[idz] == "ah":
                        for ido, k in enumerate(EAX[2:3]):
                            datG.edge(k, tempNodeStr, label= k +'(ah)'+str(ido))
                    elif splitStr[idz] == "al":
                        for ido, k in enumerate(EAX[3:4]):
                            datG.edge(k, tempNodeStr, label= k +'(al)'+str(ido))
                    #Ecx edges 
                    elif splitStr[idz] == "ecx":
                        for ido, k in enumerate(ECX):
                            datG.edge(k, tempNodeStr, label= k +'(ecx)'+str(ido))
                    elif splitStr[idz] == "cx":
                        for ido, k in enumerate(ECX[2:4]):
                            datG.edge(k, tempNodeStr, label= k +'(cx)'+str(ido))
                    elif splitStr[idz] == "ch":
                        for ido, k in enumerate(ECX[2:3]):
                            datG.edge(k, tempNodeStr, label= k +'(ch)'+str(ido))
                    elif splitStr[idz] == "cl":
                        for ido, k in enumerate(ECX[3:4]):
                            datG.edge(k, tempNodeStr, label= k +'(cl)'+str(ido))
                    #
                    #Edx edges 
                    elif splitStr[idz] == "edx":
                        for ido, k in enumerate(EDX):
                            datG.edge(k, tempNodeStr, label= k +'(edx)'+str(ido))
                    elif splitStr[idz] == "dx":
                        for ido, k in enumerate(EDX[2:4]):
                            datG.edge(k, tempNodeStr, label= k +'(dx)'+str(ido))
                    elif splitStr[idz] == "dh":
                        for ido, k in enumerate(EDX[2:3]):
                            datG.edge(k, tempNodeStr, label= k +'(dh)'+str(ido))
                    elif splitStr[idz] == "dl":
                        for ido, k in enumerate(EDX[3:4]):
                            datG.edge(k, tempNodeStr, label= k +'(dl)'+str(ido))
                    #
                    #Ebx edges 
                    elif splitStr[idz] == "ebx":
                        for ido, k in enumerate(EBX):
                            datG.edge(k, tempNodeStr, label= k +'(ebx)'+str(ido))
                    elif splitStr[idz] == "bx":
                        for ido, k in enumerate(EBX[2:4]):
                            datG.edge(k, tempNodeStr, label= k +'(bx)'+str(ido))
                    elif splitStr[idz] == "bh":
                        for ido, k in enumerate(EBX[2:3]):
                            datG.edge(k, tempNodeStr, label= k +'(bh)'+str(ido))
                    elif splitStr[idz] == "bl":
                        for ido, k in enumerate(EBX[3:4]):
                            datG.edge(k, tempNodeStr, label= k +'(bl)'+str(ido))
                    #esp edges
                    elif splitStr[idz] == "esp":
                        for ido, k in enumerate(ESP):
                            datG.edge(k, tempNodeStr, label= k +'(esp)'+str(ido))
                    elif splitStr[idz] == "sp":
                        for ido, k in enumerate(ESP[2:4]):
                            datG.edge(k, tempNodeStr, label= k +'(sp)'+str(ido))
                    #
                    #ebp edges
                    elif splitStr[idz] == "ebp":
                        for ido, k in enumerate(EBP):
                            datG.edge(k, tempNodeStr, label= k +'(ebp)'+str(ido))
                    elif splitStr[idz] == "bp":
                        for ido, k in enumerate(EBP[2:4]):
                            datG.edge(k, tempNodeStr, label= k +'(bp)'+str(ido))
                    #
                    #esi edges
                    elif splitStr[idz] == "esi":
                        for ido, k in enumerate(ESI):
                            datG.edge(k, tempNodeStr, label= k +'(esi)'+str(ido))
                    elif splitStr[idz] == "si":
                        for ido, k in enumerate(ESI[2:4]):
                            datG.edge(k, tempNodeStr, label= k +'(si)'+str(ido))
                    #
                    #
                    elif splitStr[idz] == "edi":
                        for ido, k in enumerate(EDI):
                            datG.edge(k, tempNodeStr, label= k +'(edi)'+str(ido))
                    elif splitStr[idz] == "di":
                        for ido, k in enumerate(EDI[2:4]):
                            datG.edge(k, tempNodeStr, label= k +'(di)'+str(ido))
                    #
                    else:
                        if splitStr[idz] in (memAddressDict.keys()):
                            for i in range(4):
                                datG.edge(memAddressDict[splitStr[idz]], tempNodeStr, label=memAddressDict[splitStr[idz]]+'(mem)'+str(i))
                        else:
                            pass
                            #datG.edge('R', tempNodeStr, label= k +'(imm)'+str(1))   
        #THIS IS FOR BLUE INSTRUCTIONS, WHICH ARE INSTRUCTIONS THAT HAVE ONLY ONE EXPLICIT ARGUMENT IN THE SLICE
        #PUSH IS NOT RIGHT>?
        if idz == 0:
               if (any(x in tempNodeStr for x in blueInst) or any(x in tempNodeStr for x in redInst) or any(x in tempNodeStr for x in greyInst)):
                    if splitStr[idz] == "eax":
                        for ido, k in enumerate(EAX):
                            datG.edge(k, tempNodeStr, label= k +'(eax)'+str(ido))
                    elif splitStr[idz] == "ax":
                        for ido, k in enumerate(EAX[2:4]):
                            datG.edge(k, tempNodeStr, label= k +'(ax)'+str(ido))
                    elif splitStr[idz] == "ah":
                        for ido, k in enumerate(EAX[2:3]):
                            datG.edge(k, tempNodeStr, label= k +'(ah)'+str(ido))
                    elif splitStr[idz] == "al":
                        for ido, k in enumerate(EAX[3:4]):
                            datG.edge(k, tempNodeStr, label= k +'(al)'+str(ido))
                    #Ecx edges 
                    elif splitStr[idz] == "ecx":
                        for ido, k in enumerate(ECX):
                            datG.edge(k, tempNodeStr, label= k +'(ecx)'+str(ido))
                    elif splitStr[idz] == "cx":
                        for ido, k in enumerate(ECX[2:4]):
                            datG.edge(k, tempNodeStr, label= k +'(cx)'+str(ido))
                    elif splitStr[idz] == "ch":
                        for ido, k in enumerate(ECX[2:3]):
                            datG.edge(k, tempNodeStr, label= k +'(ch)'+str(ido))
                    elif splitStr[idz] == "cl":
                        for ido, k in enumerate(ECX[3:4]):
                            datG.edge(k, tempNodeStr, label= k +'(cl)'+str(ido))
                    #
                    #Edx edges 
                    elif splitStr[idz] == "edx":
                        for ido, k in enumerate(EDX):
                            datG.edge(k, tempNodeStr, label= k +'(edx)'+str(ido))
                    elif splitStr[idz] == "dx":
                        for ido, k in enumerate(EDX[2:4]):
                            datG.edge(k, tempNodeStr, label= k +'(dx)'+str(ido))
                    elif splitStr[idz] == "dh":
                        for ido, k in enumerate(EDX[2:3]):
                            datG.edge(k, tempNodeStr, label= k +'(dh)'+str(ido))
                    elif splitStr[idz] == "dl":
                        for ido, k in enumerate(EDX[3:4]):
                            datG.edge(k, tempNodeStr, label= k +'(dl)'+str(ido))
                    #
                    #Ebx edges 
                    elif splitStr[idz] == "ebx":
                        for ido, k in enumerate(EBX):
                            datG.edge(k, tempNodeStr, label= k +'(ebx)'+str(ido))
                    elif splitStr[idz] == "bx":
                        for ido, k in enumerate(EBX[2:4]):
                            datG.edge(k, tempNodeStr, label= k +'(bx)'+str(ido))
                    elif splitStr[idz] == "bh":
                        for ido, k in enumerate(EBX[2:3]):
                            datG.edge(k, tempNodeStr, label= k +'(bh)'+str(ido))
                    elif splitStr[idz] == "bl":
                        for ido, k in enumerate(EBX[3:4]):
                            datG.edge(k, tempNodeStr, label= k +'(bl)'+str(ido))
                    #esp edges
                    elif splitStr[idz] == "esp":
                        for ido, k in enumerate(ESP):
                            datG.edge(k, tempNodeStr, label= k +'(esp)'+str(ido))
                    elif splitStr[idz] == "sp":
                        for ido, k in enumerate(ESP[2:4]):
                            datG.edge(k, tempNodeStr, label= k +'(sp)'+str(ido))
                    #
                    #ebp edges
                    elif splitStr[idz] == "ebp":
                        for ido, k in enumerate(EBP):
                            datG.edge(k, tempNodeStr, label= k +'(ebp)'+str(ido))
                    elif splitStr[idz] == "bp":
                        for ido, k in enumerate(EBP[2:4]):
                            datG.edge(k, tempNodeStr, label= k +'(bp)'+str(ido))
                    #
                    #esi edges
                    elif splitStr[idz] == "esi":
                        for ido, k in enumerate(ESI):
                            datG.edge(k, tempNodeStr, label= k +'(esi)'+str(ido))
                    elif splitStr[idz] == "si":
                        for ido, k in enumerate(ESI[2:4]):
                            datG.edge(k, tempNodeStr, label= k +'(si)'+str(ido))
                    #
                    #
                    elif splitStr[idz] == "edi":
                        for ido, k in enumerate(EDI):
                            datG.edge(k, tempNodeStr, label= k +'(edi)'+str(ido))
                    elif splitStr[idz] == "di":
                        for ido, k in enumerate(EDI[2:4]):
                            datG.edge(k, tempNodeStr, label= k +'(di)'+str(ido))
                    #
                    else:
                        if splitStr[idz] in (memAddressDict.keys()):
                            for i in range(4):
                                datG.edge(memAddressDict[splitStr[idz]], tempNodeStr, label=memAddressDict[splitStr[idz]]+'(mem)'+str(i))
                        else:
                            datG.edge('R', tempNodeStr, label= k +'(imm)'+str(1))          


        #input edges , cmp has for each argument passed in (a AND b) as 2 sources
        if ((any(x in tempNodeStr for x in pinkInst)) or (any(x in tempNodeStr for x in goldInst))):
            #Eax edges 
            if splitStr[idz] == "eax":
                for ido, k in enumerate(EAX):
                    datG.edge(k, tempNodeStr, label= k +'(eax)'+str(ido))
            elif splitStr[idz] == "ax":
                for ido, k in enumerate(EAX[2:4]):
                    datG.edge(k, tempNodeStr, label= k +'(ax)'+str(ido))
            elif splitStr[idz] == "ah":
                for ido, k in enumerate(EAX[2:3]):
                    datG.edge(k, tempNodeStr, label= k +'(ah)'+str(ido))
            elif splitStr[idz] == "al":
                for ido, k in enumerate(EAX[3:4]):
                    datG.edge(k, tempNodeStr, label= k +'(al)'+str(ido))
            #Ecx edges 
            elif splitStr[idz] == "ecx":
                for ido, k in enumerate(ECX):
                    datG.edge(k, tempNodeStr, label= k +'(ecx)'+str(ido))
            elif splitStr[idz] == "cx":
                for ido, k in enumerate(ECX[2:4]):
                    datG.edge(k, tempNodeStr, label= k +'(cx)'+str(ido))
            elif splitStr[idz] == "ch":
                for ido, k in enumerate(ECX[2:3]):
                    datG.edge(k, tempNodeStr, label= k +'(ch)'+str(ido))
            elif splitStr[idz] == "cl":
                for ido, k in enumerate(ECX[3:4]):
                    datG.edge(k, tempNodeStr, label= k +'(cl)'+str(ido))
            #
            #Edx edges 
            elif splitStr[idz] == "edx":
                for ido, k in enumerate(EDX):
                    datG.edge(k, tempNodeStr, label= k +'(edx)'+str(ido))
            elif splitStr[idz] == "dx":
                for ido, k in enumerate(EDX[2:4]):
                    datG.edge(k, tempNodeStr, label= k +'(dx)'+str(ido))
            elif splitStr[idz] == "dh":
                for ido, k in enumerate(EDX[2:3]):
                    datG.edge(k, tempNodeStr, label= k +'(dh)'+str(ido))
            elif splitStr[idz] == "dl":
                for ido, k in enumerate(EDX[3:4]):
                    datG.edge(k, tempNodeStr, label= k +'(dl)'+str(ido))
            #
            #Ebx edges 
            elif splitStr[idz] == "ebx":
                for ido, k in enumerate(EBX):
                    datG.edge(k, tempNodeStr, label= k +'(ebx)'+str(ido))
            elif splitStr[idz] == "bx":
                for ido, k in enumerate(EBX[2:4]):
                    datG.edge(k, tempNodeStr, label= k +'(bx)'+str(ido))
            elif splitStr[idz] == "bh":
                for ido, k in enumerate(EBX[2:3]):
                    datG.edge(k, tempNodeStr, label= k +'(bh)'+str(ido))
            elif splitStr[idz] == "bl":
                for ido, k in enumerate(EBX[3:4]):
                    datG.edge(k, tempNodeStr, label= k +'(bl)'+str(ido))
            #esp edges
            elif splitStr[idz] == "esp":
                for ido, k in enumerate(ESP):
                    datG.edge(k, tempNodeStr, label= k +'(esp)'+str(ido))
            elif splitStr[idz] == "sp":
                for ido, k in enumerate(ESP[2:4]):
                    datG.edge(k, tempNodeStr, label= k +'(sp)'+str(ido))
            #
            #ebp edges
            elif splitStr[idz] == "ebp":
                for ido, k in enumerate(EBP):
                    datG.edge(k, tempNodeStr, label= k +'(ebp)'+str(ido))
            elif splitStr[idz] == "bp":
                for ido, k in enumerate(EBP[2:4]):
                    datG.edge(k, tempNodeStr, label= k +'(bp)'+str(ido))
            #
            #esi edges
            elif splitStr[idz] == "esi":
                for ido, k in enumerate(ESI):
                    datG.edge(k, tempNodeStr, label= k +'(esi)'+str(ido))
            elif splitStr[idz] == "si":
                for ido, k in enumerate(ESI[2:4]):
                    datG.edge(k, tempNodeStr, label= k +'(si)'+str(ido))
            #
            #
            elif splitStr[idz] == "edi":
                for ido, k in enumerate(EDI):
                    datG.edge(k, tempNodeStr, label= k +'(edi)'+str(ido))
            elif splitStr[idz] == "di":
                for ido, k in enumerate(EDI[2:4]):
                    datG.edge(k, tempNodeStr, label= k +'(di)'+str(ido))
            #
            else:
                if splitStr[idz] in (memAddressDict.keys()):
                    for i in range(4):
                        datG.edge(memAddressDict[splitStr[idz]], tempNodeStr, label=memAddressDict[splitStr[idz]]+'(mem)'+str(i))
                else:
                    pass
                    #datG.edge('R', tempNodeStr, label=''+'(imm)'+str(2))    

        # orange/gold/green Modify 1 one source
        if idz == 0:
                if ((any(x in tempNodeStr for x in orangeInst)) or (any(x in tempNodeStr for x in goldInst)) or (any(x in tempNodeStr for x in greenInst)) or (any(x in tempNodeStr for x in purpInst))):
                    # if dest reg is eax
                    if splitStr[idz] == "eax":
                        modifyEAX(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    elif splitStr[idz] == "ax":
                        modifyAX(instrNodes[idx],instrNodes[idx])
                    elif splitStr[idz] == "ah":
                        modifyAH(instrNodes[idx])
                    elif splitStr[idz] == "al":
                        modifyAL(instrNodes[idx])
                    #    
                    # elif dest reg is ecx
                    elif splitStr[idz] == "ecx":
                        modifyECX(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    elif splitStr[idz] == "cx":
                        modifyCX(instrNodes[idx],instrNodes[idx])
                    elif splitStr[idz] == "ch":
                        modifyCH(instrNodes[idx])
                    elif splitStr[idz] == "cl":
                        modifyCL(instrNodes[idx])
                    #    
                    # elif dest reg is edx
                    elif splitStr[idz] == "edx":
                        modifyEDX(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    elif splitStr[idz] == "dx":
                        modifyDX(instrNodes[idx],instrNodes[idx])
                    elif splitStr[idz] == "dh":
                        modifyDH(instrNodes[idx])
                    elif splitStr[idz] == "dl":
                        modifyDL(instrNodes[idx])
                    #    
                    # elif dest reg is ebx
                    elif splitStr[idz] == "ebx":
                        modifyEBX(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    elif splitStr[idz] == "bx":
                        modifyBX(instrNodes[idx],instrNodes[idx])
                    elif splitStr[idz] == "bh":
                        modifyBH(instrNodes[idx])
                    elif splitStr[idz] == "bl":
                        modifyBL(instrNodes[idx])
                    #
                    # elif dest reg is esp
                    elif splitStr[idz] == "esp":
                        modifyESP(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    elif splitStr[idz] == "sp":
                        modifySP(instrNodes[idx],instrNodes[idx])
                    # elif dest reg is ebp
                    elif splitStr[idz] == "ebp":
                        modifyEBP(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    elif splitStr[idz] == "ebp":
                        modifyBP(instrNodes[idx],instrNodes[idx])     
                    # elif dest reg is esi
                    elif splitStr[idz] == "esi":
                        modifyESI(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    elif splitStr[idz] == "esi":
                        modifySI(instrNodes[idx],instrNodes[idx])      
                    # elif dest reg is edi
                    elif splitStr[idz] == "edi":
                        modifyEDI(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    elif splitStr[idz] == "di":
                        modifyDI(instrNodes[idx],instrNodes[idx])
                    else:
                        if splitStr[idz] in (memAddressDict.keys()):
                            memAddressDict[splitStr[idz]] = instrNodes[idx]
        if idz == 0:
               if (any(x in tempNodeStr for x in blueInst) or any(x in tempNodeStr for x in redInst) or any(x in tempNodeStr for x in tealInst) or any(x in tempNodeStr for x in greyInst)):
                    if (any(x in tempNodeStr for x in blueInst) or any(x in tempNodeStr for x in tealInst)):
                        modifyESP(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    elif (any(x in tempNodeStr for x in greyInst)):
                        modifyEAX(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                        modifyEDX(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    #if must be redInst
                    elif (any(x in tempNodeStr for x in redInst)):
                        modifyEAX(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    else:
                        if splitStr[idz] in (memAddressDict.keys()):
                            memAddressDict[splitStr[idz]] = instrNodes[idx]

       
        if idz == 1:     
        #iterate through the flags outputted (affected) by the instruction and do both:
        #add an edge from the instruction to generic 'OutputNode'
        #update the flags with newest most recent values
            for idy, c in enumerate(statusFlags):
                #this was the output edge place holder
                #datG.edge(tempNodeStr, 'Out', label=tempNodeStr + ',' + str(c))

                if c == "OF":
                    newestOF = tempNodeStr
                if c == "SF":
                    newestSF = tempNodeStr
                if c == "ZF":
                    newestZF = tempNodeStr
                if c == "AF":
                    newestAF = tempNodeStr
                if c == "CF":
                    newestCF = tempNodeStr
                if c == "PF":
                    newestPF = tempNodeStr
                
            statusFlags = [] 
            FlagRegList = [newestOF, newestSF, newestZF, newestAF, newestCF, newestPF]

        #if affects flags register then if [instr] and set status flags to a list of affected flags
        if idz == 0:
            #if instruction affects flags then put if statement for it under here
            if "and" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'PF']
            if "imul" in tempNodeStr:
                statusFlags = ['CF', 'OF']
            if "neg" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'AF', 'PF']
            #bug shifts should set the OF flag too if it is specifically a 1 bit shift
            if "sar" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'PF']
            if "shr" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'PF']
            if "shl" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'PF']
            if "mul" in tempNodeStr:
                statusFlags = ['CF', 'OF']
            if "and" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'PF']
            if "xor" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'PF']
            if "add" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'AF', 'PF']
            if "adc" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'AF', 'PF']
            if "cmpxchg" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'AF', 'PF']
            if "sbb" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'AF', 'PF']
            if "cmp" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'AF', 'PF']
            if "inc" in tempNodeStr:
                statusFlags = ['OF', 'SF', 'ZF', 'AF', 'PF']
            if "dec" in tempNodeStr:
                statusFlags = ['OF', 'SF', 'ZF', 'AF', 'PF']
            if "sub" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'AF', 'PF']
            if "or" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'PF']            
            if "dec" in tempNodeStr:
                statusFlags = ['AF', 'OF', 'SF', 'ZF', 'PF']
            if "mul" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'AF', 'PF']
            if "div" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'AF', 'PF']
            #
            # if instr takes flag as input then put if statement for it under here
            #FlagRegList = [0newestOF, 1newestSF, 2newestZF, 3newestAF, 4newestCF, 5newestPF]
            if "sbb" in tempNodeStr:
                datG.edge(FlagRegList[4], tempNodeStr, label='(' + 'CF' +')')
                #datG.edge(FlagRegList[4], tempNodeStr, label=FlagRegList[4] + '(' + str(nodeEdgesDict[FlagRegList[4]])+ ', CF' +')')
            if "setz" in tempNodeStr:
                datG.edge(FlagRegList[2], tempNodeStr, label='(' + 'ZF' +')')
                #datG.edge(FlagRegList[2], tempNodeStr, label=FlagRegList[2] + '(' + str(nodeEdgesDict[FlagRegList[2]])+ ', ZF' +')')
            if "setbe" in tempNodeStr:
                datG.edge(FlagRegList[2], tempNodeStr, label='(' + 'ZF' +')')
                #datG.edge(FlagRegList[2], tempNodeStr, label=FlagRegList[2] + '(' + str(nodeEdgesDict[FlagRegList[2]])+ ', ZF' +')')
                datG.edge(FlagRegList[4], tempNodeStr, label='(' + 'CF' +')')
                #datG.edge(FlagRegList[4], tempNodeStr, label=FlagRegList[4] + '(' + str(nodeEdgesDict[FlagRegList[4]])+ ', CF' +')')
            if "cmovz" in tempNodeStr:
                datG.edge(FlagRegList[2], tempNodeStr, label='(' + 'ZF' +')')
                #datG.edge(FlagRegList[2], tempNodeStr, label=FlagRegList[2] + '(' + str(nodeEdgesDict[FlagRegList[2]])+ ', ZF' +')')
            if "cmovb" in tempNodeStr:
                datG.edge(FlagRegList[4], tempNodeStr, label='(' + 'CF' +')')
            if "cmovbe" in tempNodeStr:
                datG.edge(FlagRegList[2], tempNodeStr, label='(' + 'ZF' +')')
                #datG.edge(FlagRegList[2], tempNodeStr, label=FlagRegList[2] + '(' + str(nodeEdgesDict[FlagRegList[2]])+ ', ZF' +')')
                datG.edge(FlagRegList[4], tempNodeStr, label='(' + 'CF' +')')
            #should cmovnbe be an AND? this might be a bug
            if "cmovnbe" in tempNodeStr:
                datG.edge(FlagRegList[2], tempNodeStr, label='(' + 'ZF' +')')
                #datG.edge(FlagRegList[2], tempNodeStr, label=FlagRegList[2] + '(' + str(nodeEdgesDict[FlagRegList[2]])+ ', ZF' +')')
                datG.edge(FlagRegList[4], tempNodeStr, label='(' + 'CF' +')')
            if "cmovnz" in tempNodeStr:
                datG.edge(FlagRegList[2], tempNodeStr, label='(' + 'ZF' +')')
            if "cmovs" in tempNodeStr:
                datG.edge(FlagRegList[1], tempNodeStr, label='(' + 'SF' +')')
            if "setnz" in tempNodeStr:
                datG.edge(FlagRegList[2], tempNodeStr, label='(' + 'ZF' +')')



add_nodes(datG)
#add_edges(datG)

print(datG.source)

with open(outFileName, 'w') as outFile:
    for line in datG.source:
        outFile.write(line)

src = Source(datG)
src.render(renderFileName, view=True)

print('done! check '+ outFileName)