# Ex1:
'''
1. Vrai
2. Faux 
3. Vrai 
4. Faux 
5. Vrai 
6. Faux 
7. Vrai 
8. Faux 
'''

# Ex 2 : 
'''
1 Vrai
2 Vrai 
3 Vrai 
4 Faux 
5 Vrai
6 Vrai 
7 Vrai 
8 Vrai 
9 Vrai
10 Faux
11 Vrai
12 Vrai
'''

# Ex 3 : 
'''
1. a = '21', b ='21b'

2. a ='aa', b = 'aab'

3. a = 1, b ='ab'

4. a = 'bb', b = 'bba'
'''

# Ex 4: 
def repete(c, n):
    return c * n 

# Ex 5:
def repete2(c,d,n,m):
    return c*d + d*m

# Ex 6: 

    # 1 
def aff(ch, n):
    for i in range(n):
        print(ch)

    # 2
def aff_num(ch, n):
    for i in range(1, n+1):
        print(f'{i}.{ch}')

# Ex 7: 
def aff(c,n):
    for i in range(1, n+1):
        print(c*i)

# Ex 8: 
    # Using enumerate
def premier_occ(ch, c):
    for i, charater in enumerate(ch):
        if charater == c:
            return i 
    return None

    # Usinng yield 
def generator(ch):
    for i in range(len(ch)):
        yield i, ch[i]

def premier_occ1(ch, c):
    for i, charater in generator(ch):
        if charater == c : 
            return i
    return None

    # Creating my own algorithm

class Generator:
    def __init__(self, ch): # Create the class with 2 attributes 
        self.ch = ch # Store the input string 
        self.index = 0  # Store the cuurent index (from 0)
    
    def get_index_and_character(self):  # Return a tuple containing the 'index' and the 'charater' at that index
        if self.index < len(self.ch):
            res = (self.index, self.ch[self.index])
            self.index += 1
            return res
        else:   
            return None # If it reach the end of the string, return None

def premier_occ2(ch, c):
    gen = Generator(ch)   # Create the 'Generator' object with 'ch'
    while True: 
        curr = gen.get_index_and_character() # Call the 'get_index_and_charater' method to get the tuple (index, char)
        if curr is None: # Return None if there are no more characters, also break the loop
            break
        index, char = curr
        if char == c:   # If current character == target 'c', return index 
            return index
    return None  # If can't find charater at 'c', return None

# Ex 9:
def nb_occurrence(ch, c):
    count = 0 
    for character in ch: 
        if character == c: 
            count += 1
    return count

# Ex 10: 
def sous_chaine(ch1, ch2):
    if ch1 in ch2:
        return True

    if ch2 in ch1: 
        return True

    return False

# Ex 11:

    # programme 1 : 'abab' because loops from 1 to 4 -> for k in range(1,5)
    '''
    k = 1 -> 1 % 2 == 1  => take 'a' into 'ch' => 'ch' become 'a'
    k = 2 -> 2 % 2 == 0  => false => take 'b' into 'ch' => 'ch' become 'ab'
    k = 3 -> 3 % 2 == 1  => take 'a' into 'ch' => 'ch' become 'aba'
    k = 4 -> 4 % 2 == 0  => false => take 'b' into 'ch' => 'ch' become 'abab'
    
    '''
    # programme 2 : 'baba' because loops from 0 to 3 -> for k in range(4)
    

# Ex 12: 
    # 1
def triple_six(ch):
    return '666' in ch

    # 2
def triple_six_exact(ch):
    if ch.startswith('666'):
        if ch.startswith('6666'):
            return False
        return True
    
    if ch.endswith('666'):
        if ch.endswith('6666'):
            return False
        return True
    
    if '666' in ch:
        return True
    
    return False

# Ex 13:
    # 1
def miroir2(ch):
    inv = ''
    for e in ch:
        inv = e + inv
    return inv
    
    # 2
def palindrome(ch):
    return ch == ch[::-1]

    # 3
        # a
def sans_espace(ch):
    return ch.replace(' ', '')
        # b
def palindrome2(ch):
    ch = sans_espace(ch).lower() 
    return ch == ch[::-1]

# Ex 14: 
L = [1, 2.3, 4.1, 4, 2.55, 5, 23]
'''
1/ 2.3
2/ 5
3/ IndexError -> IndexError: list index out of range
4/ 7
5/ TypeError -> TypeError: list indices must be integers or slices, not float
6/ TypeError -> TypeError: list indices must be integers or slices, not tuple
7/ [2.3, 4.1, 4, 2.55]
8/ [1, 4.1]
9/ 5
10/ [1, 4]
11/ 3
12/ [1, 1, 1]
13/ False 
14/ True 
15/ True
16/ False -> because [4.1,4] is not found as single element in L 
'''

# Ex 15: 
'''
1/ [1, -2]
2/ -2 
3/ TypeError: 'int' object is not subscriptable
4/ 3
5/ 2
6/ [1, -2, -1, 3.45]
'''

# Ex 16: 
def affiche2 () :
    for j in [0 , 1 , 2 , 3]:
        print(j)

def affiche2 () :
    for j in [0 , 1 , 2 , 3]:
        print(j)


# Ex 17: 

    # 2 
def mul_2(L):
    return [x * 2 for x in L]

L = list(range(1, 101))
L_multi_2 = mul_2(L) 
    # 3 
def carre(n):
    return [i**2 for i in range(1, n + 1)]

    # 4
double = [2*k for k in range(1,101)]

def carre_compr(n):
    return [i for i in range(1, n+1)]

# Ex 18: 
def odd():
    return [2 * i + 1 for i in range(10)]

def carre():
    return [i ** 2 for i in range(11)]

def carre2():
    return [2 ** i for i in range(11)]

def special():
    L = [3]  # Start with 3
    for i in range(1, 12):
        if i % 2 == 1:
            L.append(L[-1] + 3)  # Plus 3 for odd number
        else:
            L.append(L[-1] + 6)  # Plus 6 for even number
    return L

# Ex 19: 
def indices(ch, c):
    res = []
    for i in range(len(ch)):
        if ch[i] == c: 
            res.append(i)
    return res

# Ex 20: 
def sous_liste(L1, L2):
    if len(L2) > len(L1):
        return False
    for i in range(len(L1) - len(L2) + 1):
        if L1[i:i + len(L2)] == L2:
            return True
    return False

# Ex 21:
def tous_positif(L):
    for n in L: 
        if n < 0: 
            return False
    return True

# Ex 22: 
    # 1
def positifs(L):
    return len([x for x in L if x >= 0])

    # 2
def rangs_negatifs(L):
    return [i for i, x in enumerate(L) if x < 0]

    # 3 
L = [1,2,3,0,0,4,5]
def motif(L):
    for i in range(len(L) - 1):
        sublist = L[i:i+2]
        if sublist == [0, 0]:
            return True
    return False

    # 4 
def dix_vingt(L):
    for x in L:
        if x < 10 or x > 20:
            return False
    return True

# Ex 23: 
def croissante(L):
    n = len(L)
    for k in range(n - 1):  
        if L[k] > L[k + 1]:
            return False  
    return True  

def monotone(L):
    est_croissante = croissante(L)

    est_decroissante = all(L[i] >= L[i + 1] for i in range(len(L) - 1))

    if est_croissante: 
        return "croissante"
    elif est_decroissante:
        return "decroissante"
    else: 
        return False

