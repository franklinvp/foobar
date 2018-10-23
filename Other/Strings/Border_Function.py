"""
A string B is a *border* of a non-empty string P if there are non-empty string U, V 
such that P = BU = VB.

Border(P) = longest border of P.

border(P) = |Border(P)| = the length of Border(P).

border(P, k) = border(P_k), where P_k is the k-th prefix of P and k = 0, 1, ..., |P| - 1.

Lemma: For all (u, a) in A^+ \times A

    Border(ua) = \begin{cases}
                     Border(u)a&          \text{ if }Border(u)a\text{ is a prefix of }u\\
                     Border(Border(u)a)&  \text{ otherwise.}
                 \end{cases}
"""

def Border_Function(P):
    m = len(P)
    i = 0
    border = m*[0]
    for j in range(1, m):
        border[j-1] = i
        while i >= 0 and P[j] != P[i]:
            if i == 0:
                i = -1
            else:
                i = border[i-1]
        i += 1
    border[m-1] = i
    return border



if __name__ == '__main__':
    P = 'abbabaabbabaaaabbabbaa'
    border = Border_Function(P)
    # [0, 0, 0, 1, 2, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 3, 4, 1]
    print(border)
