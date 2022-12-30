#WAP to create a list of mixed types elements separate each type of elements in separate list.
l=[3,5,34,5.5,383,'v','vikas','4',78,True]
lint=[]
lchar=[]
lbool=[]
lfloat=[]
for i in l:
    if type(i)==int:
        lint.append(i)
    elif type(i)==float:
        lfloat.append(i)
    elif type(i)==str:
        lchar.append(i)
    elif type(i)==bool:
        lbool.append(i)
print(f"char : {lchar}")
print(f"int : {lint}")
print(f"bool : {lbool}")
print(f"float : {lfloat}")
# output:
# char : ['v', 'vikas', '4']
# int : [3, 5, 34, 383, 78]
# bool : [True]
# float : [5.5]