import itertools
def forwards(ParentA, ParentB):
'''
ParentA and ParentB are matrixes that contain patterns of genes.
Would look like ParentA = {'Aa','BB'} and ParentB = {'aa','Bb'}.
The result would look like Result = {'AaBB','AaBb','aaBB','aaBb'}
'''
    return itertools.product(ParentA,ParentB)

def reverse():
'''
Given child, for instance 'aaBB' give the possible parent combinations that
would produce that combination.
Parent combinations would include:
aaBB + aaBB
aaBb + aaBB

'''
    return 0

if __name__ == "__main__":

    return forwards()
