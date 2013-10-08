"""This file defines data structures that map latex<->markdown"""
from bidict import bidict

equals={"\\equiv":"==",
        "\\geq":">=",
        "\\leq":"<=",
        "\\ll":"<<",
        "\\gg":">>",
        "\\neq":"!=",
        "\\approx":"~",
        "=":"=",
        "\\gt":">",
        "\\le":"<",
        }
fracs ={"frac":"/",
        "dfrac":")/(",
        }
modify={"super":"^",
        "subsc":"_",
        }

triggers = bidict(equals)
triggers.update(fracs)

macros = bidict({ '+-': '\\pm ', '-+': '\\mp '})


trig_funcs = ['sin', 'cos', 'tan', 'sinc', 'cosc', 'tanc']

for func in trig_funcs:
    macros[func] = '\\'+func

greek_letters = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta',
    'theta', 'iota', 'kappa', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho',
    'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']

escapes={
        '&'      : '\\& '   ,
        '~'      : '\\textasciitilde',
        } 
bslash ={'\\':'\\textbackslash'}
