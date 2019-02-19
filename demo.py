s='the quick brown fox jumps over the lazy dog'



s='Python'
#Indexing
'''

  0|1|2|3|4|5
  p|y|t|h|o|n
 -6|-5|-4|-3|-2|-1

     :Low  :High
 +ve  0     5
 -ve -6    -1

#Hashing
seq[index]

print(s[0])=>p
print(s[-3])=>h

#slicing
    low  : high
seq[start:stop]
          (len-1)
1)seq[start:stop]=> seq[start]......seq[stop-1]
2)seq[start:]=>seq[start]...........seq[-1]
3)seq[:stop]=>seq[0]................seq[stop-1]
4)seq[:]=>seq[0]....................seq[-1]

#striding(stepping)

seq[start:stop:(+/-)stride]
a) when stride is +ve
        Low    High
    seq[start:stop:(+)stride]

    1)seq[start:stop:+stride]
        print(s[0:6:2])=>'Python'=>'Pto'
        print(s[-1:-6:2])=>''
b) when stride is -ve
        High  low    
    seq[start:stop:(-)stride]=[]
              len+1

    1)seq[High:low:(-)stride]=>[seq[High],seq[high-stride], seq[[high-stride]-stride],........., seq[low+1]]
    2)seq[High::(-)stride]=>[seq[High],seq[high-stride], seq[[high-stride]-stride],........., seq[0]]
        seq[-1::-1]=>reversed seq
    3)seq[:Low:(-)stride]=>[seq[-1],seq[-1-stride], seq[[-1-stride]-stride],........., seq[Low+1]]
    4)seq[::(-)stride]=>[seq[-1],seq[-1-stride], seq[[-1-stride]-stride],........., seq[0]]
        seq[::-1]=>reversed seq
        
#Ordered seq:eg:str, list, tuple
#Un-Ordered seq:eg: sets, dict
#Mutable seq:eg:List, set, dict
#Immutable seq:eg=>str, tuple, frozenset, numbers
#Iterable seq: eg: str, lists, tuples, dicts, sets
#Hashable seq:(Indexing|ordered)eg: str, list, tuples
#Membership of element(in, not)
#Concatenation(+)
        D.T(seq1)+D.T(seq2)
        D.T(LHS)==D.T(RHS)
#Replication(*)
        D.T(seq1)* D.T(seq2)
        D.T(LHS)==D.T(RHS)(int)
'''


    







































