stacks=open('file1.txt', 'r')
inst=open('file2.txt', 'r')

ins = inst.read()
s = stacks.read()

#for i in range(0, len(s)):
    #print(i)

print("s:")
print(s)

#storing in list format
stc = s.split('\n')
print("stack:", stc)

#for getting number of stacks
nums=stc.pop()
print("popped nos:", nums)
numOfStc=int(nums[-2])

arr=[]
d={}

#accessing each element from the array to put into particular stack
print("\nhere:")
for i in range(0, len(stc)):
    element=0   #to know which stack the following element belongs to
    for j in range(1, len(stc[i]), 4):
        element+=1
        if(stc[i][j]!=' '):
            print(element,":", stc[i][j], end=' ')
            if element in d.keys():
                d[element].append(stc[i][j])
                #print("in try block")
            else:
                dic={element: []}
                d.update(dic)
                d[element].append(stc[i][j])
                #print("in exception block")
            
    print("")


print("dictionary: ", d)

print("")

print("popped:", stc)

#making into array/dictionary
#more explaination in next commit




#accessing instructions
ins=ins.split('\n')

print(ins)

instruction = ins[0].split()

print(instruction)
move = instruction[1]
_from = instruction[3]
to = instruction[5]

print(move, _from, to)
