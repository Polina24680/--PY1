# TODO решить с помощью list comprehension и распечатать его

def dict_(n):
    dict_ = {'bin':bin(n), 'dec':n, 'hex':hex(n), 'oct':oct(n)}
    return dict_

list_=[dict_(0),
       dict_(1),
       dict_(2),
       dict_(3),
       dict_(4),
       dict_(5),
       dict_(6),
       dict_(7),
       dict_(8),
       dict_(9),
       dict_(10),
       dict_(11),
       dict_(12),
       dict_(13),
       dict_(14),
       dict_(15)
       ]


from pprint import pprint
pprint(list_)





