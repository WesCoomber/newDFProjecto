import re, os, sys, subprocess
#import functools
#import graphviz as gv
#from graphviz import Source
import networkx as nx
#from networkx.drawing.nx_agraph import graphviz_layout
from networkx.drawing.nx_pydot import write_dot
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pydot


fileName = 'cleanedExSlice.asm'
#fileName = '200CleanedSlice.txt'
outFileName = 'cleanedExGraph.dot'
#outFileName = '200UndirOutputGraph.txt'
renderFileName = 'cleanedExGraph.pdf'

#toggle this variable to enable interactive matlab graph
yesInteractive = False

k = 1 
y = 1 
memAddressNames = []
nodeCount = -1
instrEdges = []
instrNodes = []
instrNodesUniq = []
FlagRegDict = {}

FlagRegList = []
FlagRegListNames = ['OF', 'SF', 'ZF', 'AF', 'CF', 'PF']
#graph = functools.partial(gv.Graph, format='svg')
#digraph = functools.partial(gv.Digraph, format='svg', strict=False)

JumpInstList = []


nGraph = nx.DiGraph()

endNodeStats = {
    'shape': 'parallelogram',
    'style': 'filled',
    'fillcolor': 'greenyellow',
    'penwidth': '4',
}

endEdgeStats = {
    'shape': 'parallelogram',
    'style': 'bold',
    'color': 'green',
    'penwidth': '5',
}

jumpNodeStats = {
    'shape': 'octagon',
    'style': 'filled',
    'fillcolor': 'crimson',
    'penwidth': '4',
}

jumpEdgeStats = {
    'shape': 'octagon',
    'style': 'bold',
    'color': 'red',
    'penwidth': '5',
}



def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

def add_nodes(graph):
    for n in instrNodes:
        graph.add_node(n, label = str(n) + '(' + str(nodeEdgesDict[n]) + ')')
    return graph

def graph_draw(graph):
    nx.draw(graph,
         node_size = [16 * graph.degree(n) for n in graph],
         node_color = [graph.depth[n] for n in graph],
         with_labels = True)


def addEndNode(name):
    nGraph.add_node(name, label = str(name), shape=endNodeStats['shape'],style=endNodeStats['style'], fillcolor = endNodeStats['fillcolor'], penwidth = endNodeStats['penwidth'])
    return

def addEndEdge(src, dst, name):
    nGraph.add_edge(src, dst, label = str(name), shape=endEdgeStats['shape'],style=endEdgeStats['style'], color = endEdgeStats['color'], penwidth = endEdgeStats['penwidth'])
    return    

def add_endReg(name):
    dupChkDict = {k: v for k, v in zip(name, name)}
    #print(dupChkDict)
    #print(dupChkDict.keys())
    for idx, noder in enumerate(dupChkDict.keys()):
        addEndNode(regListNames[i])
        addEndEdge(noder, regListNames[i], 'EndofSliceValue')
    return

def addJumpNode(name):
    nGraph.add_node(name, label = str(name), shape=jumpNodeStats['shape'],style=jumpNodeStats['style'], fillcolor = jumpNodeStats['fillcolor'], penwidth = jumpNodeStats['penwidth'])
    return

def addJumpEdge(src, dst, name):
    nGraph.add_edge(src, dst, label = str(name), shape=jumpEdgeStats['shape'],style=jumpEdgeStats['style'], color = jumpEdgeStats['color'], penwidth = jumpEdgeStats['penwidth'])
    return    



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

#jumpDict= {}
#get the instrNodes with their appropraite line numbers
with open(fileName) as oldfile:
    for line in oldfile:
        splitLine = line.split()

        tempEdgeList = []
        if not line.isspace():
            #this 'j' block prints all the unique jumps in the slice.
            #if ('j' in splitLine[0]):
            #    jumpDict[splitLine[0]] = splitLine[0]
            #   print(jumpDict.keys())

            #if not a system call in the cleanedExSlice then must be a normal slice Instruction 
            #and only add the first word + its line number as a single node 
            if (splitLine[0] != 'call'):
                instrNodes.append('[' +str (k) + '] '+splitLine[0])
                instrNodesUniq.append(splitLine[0])
                

                for idx, words in enumerate(splitLine):
                    if (idx != 0):
                        if ((splitLine[idx] != 'dword') and (splitLine[idx] != 'ptr') and (splitLine[idx] != 'byte')):
                            if('[0x' in splitLine[idx]):
                                memAddressNames.append(splitLine[idx])
                            tempEdgeList.append(splitLine[idx])
            #else must be a system call so include both first two words + its line number
            else:
                instrNodes.append('[' +str (k) + '] '+splitLine[0] + '-' + splitLine[1])
                instrNodesUniq.append(splitLine[1])
                tempEdgeList.append("eax")
            instrEdges.append(tempEdgeList) 
        k = k + 1
        

#list of instrNodes in the format ['[1] b7ff5c05-cmp', '[2] b7fe3d14-cmp']
print('Done! Instruction instrNodes List Size is : ') 
print(len(instrNodes))

#print(instrNodes)
#print(instrEdges)

#print(memAddressNames)

uniqueInstrDict = {k: v for k, v in zip(instrNodesUniq, instrNodesUniq)}
#print(uniqueInstrDict.keys())

print('Done! Instruction Edges List size is : ')
print(len(instrEdges))
#print(instrEdges)


nodeEdgesDict = {k: v for k, v in zip(instrNodes, instrEdges)}
#example dictionary entry is dict1['0-cmp': 'eax, 0xfffff001']
print('Done! Dict (Nodes: Edges) is : ')
#rint("first node(instr): and its edges(operands): " + 'b7ff5c05-cmp: '+str(nodeEdgesDict['b7ff5c05-cmp']))
print(len(nodeEdgesDict))
#print((nodeEdgesDict))

flagEnterKeys = 0

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


#list of instrNodes in the format ['[1] b7ff5c05-cmp', '[2] b7fe3d14-cmp']
#instrNodes
#list of edges in the format ['eax, 0xfffff001', 'eax, 0x33']
#nstrEdges

#This block of code is hacky way to get rid of duplicates in memAddressNames
#print(memAddressNames)
memAddressDict = {k: v for k, v in zip(memAddressNames, memAddressNames)}
memAddressNames = list(memAddressDict.keys())
#print(memAddressNames)

#print(memAddressDict)



statusFlags = [] 
nGraph.add_node('ROOT')
nGraph.add_node('EAX')
nGraph.add_node('ECX')
nGraph.add_node('EDI')
nGraph.add_node('EDX')
nGraph.add_node('EBX')
nGraph.add_node('ESP')
nGraph.add_node('EBP')
nGraph.add_node('ESI')
nGraph.add_node('EDI')
#nGraph.add_node('Out', 'Output')


cmpFlags = []
newestOF = 'ROOT'
newestSF = 'ROOT'
newestZF = 'ROOT'
newestAF = 'ROOT'
newestCF = 'ROOT'
newestPF = 'ROOT'

# default values 'ROOT' means edge from root node in the 32-bit 4word registers
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

#list of registers(and a list of their values inside) so we can easily include them in the EndofSliceNodes.
regList = [
EAX,
ECX,
EDI,
EDX,
EBX,
ESP,
EBP,
ESI,
EDI,
]

#list of regNames so we can easily include them in the EndofSliceNodes.
regListNames = [
'EAX',
'ECX',
'EDI',
'EDX',
'EBX',
'ESP',
'EBP',
'ESI',
'EDI',
]

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
'movsx',
'movzx',
'lea',
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
 'call', #call is for syscalls that dont actually consume flags, but this is a hack to get them working as modifying the EAX register with the syscall return value
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

        #input edges for orangeInstructions, such as 'mov' they only have one 1 source(second arg). dest, src        
        if idz == 1:
                if any(x in tempNodeStr for x in orangeInst):

                    isMultipleRegs = False

                    #6-8 some extra "movzx eax byte ptr [edi+ecx*1]" handling, 
                    if ((splitStr[idz])[:2]) == '[e':
                        #put into a dict to remove duplicates from the list of source registers
                        dupChkDict = {}
                        #print(tempNodeStr)

                        
                        #add the extra mem source of taint
                        if len(splitStr) >= 3:
                            for i in range(4):
                                nGraph.add_edge(memAddressDict[splitStr[2]], tempNodeStr, label=memAddressDict[splitStr[2]]+'(mem)'+str(i))
                        

                        splitStr[idz] = splitStr[idz].replace('[', '')
                       
                        tempStrList = (splitStr[idz]).split('+')
                        workingList = tempStrList[1].split('*')
                        tempStrList[1] = workingList[0]
                        #print ('tempStrList: ' + splitStr[idz] + ' ' +str(tempStrList))
                        splitStr[idz] = tempStrList
                        #print (splitStr[idz])
                        dupChkDict = {k: v for k, v in zip(tempStrList, tempStrList)}
                        if len(dupChkDict.keys()) <= 1:
                            #print ('1' + str(dupChkDict.keys()))
                            isMultipleRegs = False
                        else:
                            #print ('2' + str(dupChkDict.keys()))
                            isMultipleRegs = True

                    if (isMultipleRegs == True):
                             #Eax edges 
                        if 'eax' in splitStr[idz]:
                            for ido, k in enumerate(EAX):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(eax)'+str(ido))
                        if 'ax' in splitStr[idz]:
                            for ido, k in enumerate(EAX[2:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(ax)'+str(ido))
                        if 'ah' in splitStr[idz]:
                            for ido, k in enumerate(EAX[2:3]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(ah)'+str(ido))
                        if 'al' in splitStr[idz]:
                            for ido, k in enumerate(EAX[3:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(al)'+str(ido))
                        #Ecx edges 
                        if 'ecx' in splitStr[idz]:
                            for ido, k in enumerate(ECX):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(ecx)'+str(ido))
                        if 'cx' in splitStr[idz]:
                            for ido, k in enumerate(ECX[2:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(cx)'+str(ido))
                        if 'ch' in splitStr[idz]:
                            for ido, k in enumerate(ECX[2:3]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(ch)'+str(ido))
                        if 'cl' in splitStr[idz]:
                            for ido, k in enumerate(ECX[3:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(cl)'+str(ido))
                        #
                        #Edx edges 
                        if 'edx' in splitStr[idz]:
                            for ido, k in enumerate(EDX):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(edx)'+str(ido))
                        if 'dx' in splitStr[idz]:
                            for ido, k in enumerate(EDX[2:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(dx)'+str(ido))
                        if 'dh' in splitStr[idz]:
                            for ido, k in enumerate(EDX[2:3]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(dh)'+str(ido))
                        if 'dl' in splitStr[idz]:
                            for ido, k in enumerate(EDX[3:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(dl)'+str(ido))
                        #
                        #Ebx edges 
                        if 'ebx' in splitStr[idz]:
                            for ido, k in enumerate(EBX):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(ebx)'+str(ido))
                        if 'bx' in splitStr[idz]:
                            for ido, k in enumerate(EBX[2:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(bx)'+str(ido))
                        if 'bh' in splitStr[idz]:
                            for ido, k in enumerate(EBX[2:3]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(bh)'+str(ido))
                        if 'bl' in splitStr[idz]:
                            for ido, k in enumerate(EBX[3:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(bl)'+str(ido))
                        #esp edges
                        if 'esp' in splitStr[idz]:
                            for ido, k in enumerate(ESP):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(esp)'+str(ido))
                        if 'sp' in splitStr[idz]:
                            for ido, k in enumerate(ESP[2:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(sp)'+str(ido))
                        #
                        #ebp edges
                        if 'ebp' in splitStr[idz]:
                            for ido, k in enumerate(EBP):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(ebp)'+str(ido))
                        if 'bp' in splitStr[idz]:
                            for ido, k in enumerate(EBP[2:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(bp)'+str(ido))
                        #
                        #esi edges
                        if 'esi' in splitStr[idz]:
                            for ido, k in enumerate(ESI):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(esi)'+str(ido))
                        if 'si' in splitStr[idz]:
                            for ido, k in enumerate(ESI[2:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(si)'+str(ido))
                        #
                        #
                        if 'edi' in splitStr[idz]:
                            for ido, k in enumerate(EDI):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(edi)'+str(ido))
                        if 'di' in splitStr[idz]:
                            for ido, k in enumerate(EDI[2:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(di)'+str(ido))
                        #

                    else:
                         #Eax edges 
                        if 'eax' in splitStr[idz]:
                            for ido, k in enumerate(EAX):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(eax)'+str(ido))
                        elif 'ax' in splitStr[idz]:
                            for ido, k in enumerate(EAX[2:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(ax)'+str(ido))
                        elif 'ah' in splitStr[idz]:
                            for ido, k in enumerate(EAX[2:3]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(ah)'+str(ido))
                        elif 'al' in splitStr[idz]:
                            for ido, k in enumerate(EAX[3:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(al)'+str(ido))
                        #Ecx edges 
                        elif 'ecx' in splitStr[idz]:
                            for ido, k in enumerate(ECX):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(ecx)'+str(ido))
                        elif 'cx' in splitStr[idz]:
                            for ido, k in enumerate(ECX[2:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(cx)'+str(ido))
                        elif 'ch' in splitStr[idz]:
                            for ido, k in enumerate(ECX[2:3]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(ch)'+str(ido))
                        elif 'cl' in splitStr[idz]:
                            for ido, k in enumerate(ECX[3:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(cl)'+str(ido))
                        #
                        #Edx edges 
                        elif 'edx' in splitStr[idz]:
                            for ido, k in enumerate(EDX):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(edx)'+str(ido))
                        elif 'dx' in splitStr[idz]:
                            for ido, k in enumerate(EDX[2:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(dx)'+str(ido))
                        elif 'dh' in splitStr[idz]:
                            for ido, k in enumerate(EDX[2:3]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(dh)'+str(ido))
                        elif 'dl' in splitStr[idz]:
                            for ido, k in enumerate(EDX[3:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(dl)'+str(ido))
                        #
                        #Ebx edges 
                        elif 'ebx' in splitStr[idz]:
                            for ido, k in enumerate(EBX):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(ebx)'+str(ido))
                        elif 'bx' in splitStr[idz]:
                            for ido, k in enumerate(EBX[2:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(bx)'+str(ido))
                        elif 'bh' in splitStr[idz]:
                            for ido, k in enumerate(EBX[2:3]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(bh)'+str(ido))
                        elif 'bl' in splitStr[idz]:
                            for ido, k in enumerate(EBX[3:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(bl)'+str(ido))
                        #esp edges
                        elif 'esp' in splitStr[idz]:
                            for ido, k in enumerate(ESP):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(esp)'+str(ido))
                        elif 'sp' in splitStr[idz]:
                            for ido, k in enumerate(ESP[2:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(sp)'+str(ido))
                        #
                        #ebp edges
                        elif 'ebp' in splitStr[idz]:
                            for ido, k in enumerate(EBP):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(ebp)'+str(ido))
                        elif 'bp' in splitStr[idz]:
                            for ido, k in enumerate(EBP[2:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(bp)'+str(ido))
                        #
                        #esi edges
                        elif 'esi' in splitStr[idz]:
                            for ido, k in enumerate(ESI):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(esi)'+str(ido))
                        elif 'si' in splitStr[idz]:
                            for ido, k in enumerate(ESI[2:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(si)'+str(ido))
                        #
                        #
                        elif 'edi' in splitStr[idz]:
                            for ido, k in enumerate(EDI):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(edi)'+str(ido))
                        elif 'di' in splitStr[idz]:
                            for ido, k in enumerate(EDI[2:4]):
                                nGraph.add_edge(k, tempNodeStr, label= k +'(di)'+str(ido))
                        #
                        else:
                            if splitStr[idz] in (memAddressDict.keys()):
                                for i in range(4):
                                    nGraph.add_edge(memAddressDict[splitStr[idz]], tempNodeStr, label=memAddressDict[splitStr[idz]]+'(mem)'+str(i))
                            else:
                                pass
                                #nGraph.add_edge('ROOT', tempNodeStr, label= k +'(imm)'+str(1))   
        #THIS IS FOR BLUE INSTRUCTIONS, WHICH ARE INSTRUCTIONS THAT HAVE ONLY ONE EXPLICIT ARGUMENT IN THE SLICE
        #PUSH IS NOT RIGHT>?
        if idz == 0:
               if (any(x in tempNodeStr for x in blueInst) or any(x in tempNodeStr for x in redInst) or any(x in tempNodeStr for x in greyInst)):
                    if 'eax' in splitStr[idz]:
                        for ido, k in enumerate(EAX):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(eax)'+str(ido))
                    elif 'ax' in splitStr[idz]:
                        for ido, k in enumerate(EAX[2:4]):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(ax)'+str(ido))
                    elif 'ah' in splitStr[idz]:
                        for ido, k in enumerate(EAX[2:3]):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(ah)'+str(ido))
                    elif 'al' in splitStr[idz]:
                        for ido, k in enumerate(EAX[3:4]):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(al)'+str(ido))
                    #Ecx edges 
                    elif 'ecx' in splitStr[idz]:
                        for ido, k in enumerate(ECX):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(ecx)'+str(ido))
                    elif 'cx' in splitStr[idz]:
                        for ido, k in enumerate(ECX[2:4]):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(cx)'+str(ido))
                    elif 'ch' in splitStr[idz]:
                        for ido, k in enumerate(ECX[2:3]):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(ch)'+str(ido))
                    elif 'cl' in splitStr[idz]:
                        for ido, k in enumerate(ECX[3:4]):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(cl)'+str(ido))
                    #
                    #Edx edges 
                    elif 'edx' in splitStr[idz]:
                        for ido, k in enumerate(EDX):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(edx)'+str(ido))
                    elif 'dx' in splitStr[idz]:
                        for ido, k in enumerate(EDX[2:4]):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(dx)'+str(ido))
                    elif 'dh' in splitStr[idz]:
                        for ido, k in enumerate(EDX[2:3]):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(dh)'+str(ido))
                    elif 'dl' in splitStr[idz]:
                        for ido, k in enumerate(EDX[3:4]):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(dl)'+str(ido))
                    #
                    #Ebx edges 
                    elif 'ebx' in splitStr[idz]:
                        for ido, k in enumerate(EBX):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(ebx)'+str(ido))
                    elif 'bx' in splitStr[idz]:
                        for ido, k in enumerate(EBX[2:4]):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(bx)'+str(ido))
                    elif 'bh' in splitStr[idz]:
                        for ido, k in enumerate(EBX[2:3]):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(bh)'+str(ido))
                    elif 'bl' in splitStr[idz]:
                        for ido, k in enumerate(EBX[3:4]):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(bl)'+str(ido))
                    #esp edges
                    elif 'esp' in splitStr[idz]:
                        for ido, k in enumerate(ESP):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(esp)'+str(ido))
                    elif 'sp' in splitStr[idz]:
                        for ido, k in enumerate(ESP[2:4]):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(sp)'+str(ido))
                    #
                    #ebp edges
                    elif 'ebp' in splitStr[idz]:
                        for ido, k in enumerate(EBP):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(ebp)'+str(ido))
                    elif 'bp' in splitStr[idz]:
                        for ido, k in enumerate(EBP[2:4]):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(bp)'+str(ido))
                    #
                    #esi edges
                    elif 'esi' in splitStr[idz]:
                        for ido, k in enumerate(ESI):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(esi)'+str(ido))
                    elif 'si' in splitStr[idz]:
                        for ido, k in enumerate(ESI[2:4]):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(si)'+str(ido))
                    #
                    #
                    elif 'edi' in splitStr[idz]:
                        for ido, k in enumerate(EDI):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(edi)'+str(ido))
                    elif 'di' in splitStr[idz]:
                        for ido, k in enumerate(EDI[2:4]):
                            nGraph.add_edge(k, tempNodeStr, label= k +'(di)'+str(ido))
                    #
                    else:
                        if splitStr[idz] in (memAddressDict.keys()):
                            for i in range(4):
                                nGraph.add_edge(memAddressDict[splitStr[idz]], tempNodeStr, label=memAddressDict[splitStr[idz]]+'(mem)'+str(i))
                        else:
                            nGraph.add_edge('ROOT', tempNodeStr, label= k +'(imm)'+str(1))          


        #input edges , cmp has for each argument passed in (a AND b) as 2 sources
        if ((any(x in tempNodeStr for x in pinkInst)) or (any(x in tempNodeStr for x in goldInst))):


            #Eax edges 
            if 'eax' in splitStr[idz]:
                for ido, k in enumerate(EAX):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(eax)'+str(ido))
            elif 'ax' in splitStr[idz]:
                for ido, k in enumerate(EAX[2:4]):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(ax)'+str(ido))
            elif 'ah' in splitStr[idz]:
                for ido, k in enumerate(EAX[2:3]):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(ah)'+str(ido))
            elif 'al' in splitStr[idz]:
                for ido, k in enumerate(EAX[3:4]):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(al)'+str(ido))
            #Ecx edges 
            elif 'ecx' in splitStr[idz]:
                for ido, k in enumerate(ECX):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(ecx)'+str(ido))
            elif 'cx' in splitStr[idz]:
                for ido, k in enumerate(ECX[2:4]):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(cx)'+str(ido))
            elif 'ch' in splitStr[idz]:
                for ido, k in enumerate(ECX[2:3]):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(ch)'+str(ido))
            elif 'cl' in splitStr[idz]:
                for ido, k in enumerate(ECX[3:4]):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(cl)'+str(ido))
            #
            #Edx edges 
            elif 'edx' in splitStr[idz]:
                for ido, k in enumerate(EDX):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(edx)'+str(ido))
            elif 'dx' in splitStr[idz]:
                for ido, k in enumerate(EDX[2:4]):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(dx)'+str(ido))
            elif 'dh' in splitStr[idz]:
                for ido, k in enumerate(EDX[2:3]):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(dh)'+str(ido))
            elif 'dl' in splitStr[idz]:
                for ido, k in enumerate(EDX[3:4]):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(dl)'+str(ido))
            #
            #Ebx edges 
            elif 'ebx' in splitStr[idz]:
                for ido, k in enumerate(EBX):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(ebx)'+str(ido))
            elif 'bx' in splitStr[idz]:
                for ido, k in enumerate(EBX[2:4]):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(bx)'+str(ido))
            elif 'bh' in splitStr[idz]:
                for ido, k in enumerate(EBX[2:3]):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(bh)'+str(ido))
            elif 'bl' in splitStr[idz]:
                for ido, k in enumerate(EBX[3:4]):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(bl)'+str(ido))
            #esp edges
            elif 'esp' in splitStr[idz]:
                for ido, k in enumerate(ESP):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(esp)'+str(ido))
            elif 'sp' in splitStr[idz]:
                for ido, k in enumerate(ESP[2:4]):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(sp)'+str(ido))
            #
            #ebp edges
            elif 'ebp' in splitStr[idz]:
                for ido, k in enumerate(EBP):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(ebp)'+str(ido))
            elif 'bp' in splitStr[idz]:
                for ido, k in enumerate(EBP[2:4]):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(bp)'+str(ido))
            #
            #esi edges
            elif 'esi' in splitStr[idz]:
                for ido, k in enumerate(ESI):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(esi)'+str(ido))
            elif 'si' in splitStr[idz]:
                for ido, k in enumerate(ESI[2:4]):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(si)'+str(ido))
            #
            #
            elif 'edi' in splitStr[idz]:
                for ido, k in enumerate(EDI):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(edi)'+str(ido))
            elif 'di' in splitStr[idz]:
                for ido, k in enumerate(EDI[2:4]):
                    nGraph.add_edge(k, tempNodeStr, label= k +'(di)'+str(ido))
            #
            else:
                if splitStr[idz] in (memAddressDict.keys()):
                    for i in range(4):
                        nGraph.add_edge(memAddressDict[splitStr[idz]], tempNodeStr, label=memAddressDict[splitStr[idz]]+'(mem)'+str(i))
                else:
                    pass
                    #nGraph.add_edge('ROOT', tempNodeStr, label=''+'(imm)'+str(2))    

        # orange/gold/green Modify 1 one source
        if idz == 0:
                if ((any(x in tempNodeStr for x in orangeInst)) or (any(x in tempNodeStr for x in goldInst)) or (any(x in tempNodeStr for x in greenInst)) or (any(x in tempNodeStr for x in purpInst))):
                    #print(splitStr)
                    if (any(x in tempNodeStr for x in purpInst)):
                        #print tempNodeStr
                        #print splitStr
                        #print splitStr[idz]
                        #print instrNodes[idx]
                        #print "\n"
                        pass

                    # if dest reg is eax
                    if 'eax' in splitStr[idz]:
                        #print ("eax in purpInst Detected! \n")
                        modifyEAX(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                        #print (EAX)
                    elif 'ax' in splitStr[idz]:
                        modifyAX(instrNodes[idx],instrNodes[idx])
                    elif 'ah' in splitStr[idz]:
                        modifyAH(instrNodes[idx])
                    elif 'al' in splitStr[idz]:
                        modifyAL(instrNodes[idx])
                    #    
                    # elif dest reg is ecx
                    elif 'ecx' in splitStr[idz]:
                        modifyECX(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    elif 'cx' in splitStr[idz]:
                        modifyCX(instrNodes[idx],instrNodes[idx])
                    elif 'ch' in splitStr[idz]:
                        modifyCH(instrNodes[idx])
                    elif 'cl' in splitStr[idz]:
                        modifyCL(instrNodes[idx])
                    #    
                    # elif dest reg is edx
                    elif 'edx' in splitStr[idz]:
                        modifyEDX(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    elif 'dx' in splitStr[idz]:
                        modifyDX(instrNodes[idx],instrNodes[idx])
                    elif 'dh' in splitStr[idz]:
                        modifyDH(instrNodes[idx])
                    elif 'dl' in splitStr[idz]:
                        modifyDL(instrNodes[idx])
                    #    
                    # elif dest reg is ebx
                    elif 'ebx' in splitStr[idz]:
                        modifyEBX(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    elif 'bx' in splitStr[idz]:
                        modifyBX(instrNodes[idx],instrNodes[idx])
                    elif 'bh' in splitStr[idz]:
                        modifyBH(instrNodes[idx])
                    elif 'bl' in splitStr[idz]:
                        modifyBL(instrNodes[idx])
                    #
                    # elif dest reg is esp
                    elif 'esp' in splitStr[idz]:
                        modifyESP(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    elif 'sp' in splitStr[idz]:
                        modifySP(instrNodes[idx],instrNodes[idx])
                    # elif dest reg is ebp
                    elif 'ebp' in splitStr[idz]:
                        modifyEBP(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    elif 'ebp' in splitStr[idz]:
                        modifyBP(instrNodes[idx],instrNodes[idx])     
                    # elif dest reg is esi
                    elif 'esi' in splitStr[idz]:
                        modifyESI(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    elif 'esi' in splitStr[idz]:
                        modifySI(instrNodes[idx],instrNodes[idx])      
                    # elif dest reg is edi
                    elif 'edi' in splitStr[idz]:
                        modifyEDI(instrNodes[idx],instrNodes[idx],instrNodes[idx],instrNodes[idx])
                    elif 'di' in splitStr[idz]:
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
                #nGraph.add_edge(tempNodeStr, 'Out', label=tempNodeStr + ',' + str(c))

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

            allFlagRegs = ['CF', 'OF', 'SF', 'ZF', 'AF', 'PF']    
            statusFlags = [] 
            FlagRegList = [newestOF, newestSF, newestZF, newestAF, newestCF, newestPF]

            FlagRegDict = {k: v for k, v in zip(allFlagRegs, FlagRegList)}


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
            if "test" in tempNodeStr:
                statusFlags = ['SF', 'ZF',  'PF']
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
            #does the flags that are undefined by an instruction means the taint is cleared?
            #mul states "The OF and CF flags are set to 0 if the upper half of the result is 0; otherwise, they are set to 1. The SF, ZF, AF, and PF flags are undefined" 
            #http://x86.renejeschke.de/html/file_module_x86_id_210.html
            if "mul" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'AF', 'PF']
            if "div" in tempNodeStr:
                statusFlags = ['CF', 'OF', 'SF', 'ZF', 'AF', 'PF']
            #
            # if instr takes flag as input then put if statement for it under here
            #FlagRegList = [0newestOF, 1newestSF, 2newestZF, 3newestAF, 4newestCF, 5newestPF]
            if "sbb" in tempNodeStr:
                nGraph.add_edge(FlagRegDict['CF'], tempNodeStr, label='(' + 'CF' +')')
                #nGraph.add_edge(FlagRegDict['CF'], tempNodeStr, label=FlagRegDict['CF'] + '(' + str(nodeEdgesDict[FlagRegDict['CF']])+ ', CF' +')')
            if "setz" in tempNodeStr:
                nGraph.add_edge(FlagRegDict['ZF'], tempNodeStr, label='(' + 'ZF' +')')
                #nGraph.add_edge(FlagRegDict['ZF'], tempNodeStr, label=FlagRegDict['ZF'] + '(' + str(nodeEdgesDict[FlagRegDict['ZF']])+ ', ZF' +')')
            if "setbe" in tempNodeStr:
                nGraph.add_edge(FlagRegDict['ZF'], tempNodeStr, label='(' + 'ZF' +')')
                #nGraph.add_edge(FlagRegDict['ZF'], tempNodeStr, label=FlagRegDict['ZF'] + '(' + str(nodeEdgesDict[FlagRegDict['ZF']])+ ', ZF' +')')
                nGraph.add_edge(FlagRegDict['CF'], tempNodeStr, label='(' + 'CF' +')')
                #nGraph.add_edge(FlagRegDict['CF'], tempNodeStr, label=FlagRegDict['CF'] + '(' + str(nodeEdgesDict[FlagRegDict['CF']])+ ', CF' +')')
            if "cmovz" in tempNodeStr:
                nGraph.add_edge(FlagRegDict['ZF'], tempNodeStr, label='(' + 'ZF' +')')
                #nGraph.add_edge(FlagRegDict['ZF'], tempNodeStr, label=FlagRegDict['ZF'] + '(' + str(nodeEdgesDict[FlagRegDict['ZF']])+ ', ZF' +')')
            if "cmovb" in tempNodeStr:
                nGraph.add_edge(FlagRegDict['CF'], tempNodeStr, label='(' + 'CF' +')')
            if "cmovbe" in tempNodeStr:
                nGraph.add_edge(FlagRegDict['ZF'], tempNodeStr, label='(' + 'ZF' +')')
                #nGraph.add_edge(FlagRegDict['ZF'], tempNodeStr, label=FlagRegDict['ZF'] + '(' + str(nodeEdgesDict[FlagRegDict['ZF']])+ ', ZF' +')')
                nGraph.add_edge(FlagRegDict['CF'], tempNodeStr, label='(' + 'CF' +')')
            #should cmovnbe be an AND? this might be a bug
            if "cmovnbe" in tempNodeStr:
                nGraph.add_edge(FlagRegDict['ZF'], tempNodeStr, label='(' + 'ZF' +')')
                #nGraph.add_edge(FlagRegDict['ZF'], tempNodeStr, label=FlagRegDict['ZF'] + '(' + str(nodeEdgesDict[FlagRegDict['ZF']])+ ', ZF' +')')
                nGraph.add_edge(FlagRegDict['CF'], tempNodeStr, label='(' + 'CF' +')')
            if "cmovnz" in tempNodeStr:
                nGraph.add_edge(FlagRegDict['ZF'], tempNodeStr, label='(' + 'ZF' +')')
            if "cmovs" in tempNodeStr:
                nGraph.add_edge(FlagRegDict['SF'], tempNodeStr, label='(' + 'SF' +')')
            if "setnz" in tempNodeStr:
                nGraph.add_edge(FlagRegDict['ZF'], tempNodeStr, label='(' + 'ZF' +')')
            #JUMPS consuming flags under here as end of slice values
            #
            #FlagRegList = [0newestOF, 1newestSF, 2newestZF, 3newestAF, 4newestCF, 5newestPF]
            if "jnz" in tempNodeStr:
                #nGraph.add_edge(FlagRegDict['ZF'], tempNodeStr, label='(' + 'ZF' +')')
                addJumpEdge(FlagRegDict['ZF'], tempNodeStr, '(ZF)EndofSliceValue')
                addJumpNode(tempNodeStr)
                JumpInstList.append(tempNodeStr)
            if "js" in tempNodeStr:
                #nGraph.add_edge(FlagRegDict['SF'], tempNodeStr, label='(' + 'SF' +')')
                addJumpEdge(FlagRegDict['SF'], tempNodeStr, '(SF)EndofSliceValue')
                addJumpNode(tempNodeStr)
                JumpInstList.append(tempNodeStr)
            if "jz" in tempNodeStr:
                #nGraph.add_edge(FlagRegDict['ZF'], tempNodeStr, label='(' + 'ZF' +')')
                addJumpEdge(FlagRegDict['ZF'], tempNodeStr, '(ZF)EndofSliceValue') 
                addJumpNode(tempNodeStr)
                JumpInstList.append(tempNodeStr)



add_nodes(nGraph)

#go through all the registers and hook them up as end nodes which is the state of the system at the end of slice.
for i in range(len(regList)):
    add_endReg(regList[i])

#go through all modified memory and hook each one as an end node which is the state of the system at the end of slice.
for i in range(len(memAddressNames)):
    #some of the mem addresses in the memAddressNames are not modified by the slice, they are only input sources of memory 
    # this if statement makes sure we only add endpoint nodes/edges for modified memory addresses
    if '[0x' not in ((memAddressDict[memAddressNames[i]])): 
        #add_endNode(memAddressDict[memAddressNames[i]])
        addEndNode(memAddressNames[i])
        addEndEdge(memAddressDict[(memAddressNames[i])], memAddressNames[i], 'EndofSliceValue')
        #nGraph.add_node(memAddressNames[i], label = str(memAddressNames[i]), shape='box', color = 'darkgreen', penwidth = edgePenWidth)
        #nGraph.add_edge(memAddressDict[(memAddressNames[i])], memAddressNames[i], label='(' + 'EndofSliceValue' +')', color='Green', penwidth = edgePenWidth)
        #print(memAddressDict[memAddressNames[i]])

#go through all the flags in the x86 FLAG register and hook each 
#one as an end node to the instruction that last modified it before the slice ended.
for i in range(len(FlagRegList)):
    addEndNode(FlagRegListNames[i])
    addEndEdge(FlagRegList[i], FlagRegListNames[i], 'EndofSliceValue')


if(yesInteractive == True):
    pos = nx.drawing.nx_pydot.pydot_layout(nGraph)
    nx.draw(nGraph,pos,with_labels=True)
    plt.show()

nx.drawing.nx_pydot.write_dot(nGraph, outFileName)
#can remove this below incase you only care about the output .dot file
dotGraph = nx.drawing.nx_pydot.to_pydot(nGraph, strict=True)
dotGraph.write_pdf(renderFileName)

open_file(renderFileName)

def getAncestors(listOfNodes):
    listOfAncestorSets = []
    ancestorDict ={}
    for nodeName in listOfNodes:
        ancestorDict[nodeName] = nx.ancestors(nGraph, nodeName)
        #listOfAncestorSets.append(nx.ancestors(nGraph, nodeName))
    return ancestorDict


#get ancestors of all the end nodes 
endRegAncestors = getAncestors(regListNames)
#print(endRegAncestors)
print(len(endRegAncestors))
print(endRegAncestors.keys())

endMemAncestors = getAncestors(memAddressNames)
#print(endMemAncestors)
print(len(endMemAncestors))
print(endMemAncestors.keys())

endFlagAncestors = getAncestors(FlagRegListNames)
#print(endFlagAncestors)
print(len(endFlagAncestors))
print(endFlagAncestors.keys())
#print(endFlagAncestors['OF'])

endJumpAncestors = getAncestors(JumpInstList)
#print(endMemAncestors)
print(len(endJumpAncestors))
print(endJumpAncestors.keys())
print(endJumpAncestors['[409] jnz'])

#6-16 late afternoon work
#next stop is to clean all nodes that arent an ancestor of a end point?




print('done! check '+ outFileName)