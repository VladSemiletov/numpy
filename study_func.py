from sympy import *


def study_function(y, singp=0, asimp=True):
    if asimp:
        if singp != 0:
            for i in range(0, len(singp)):
                lim = limit(y, x, singp[i])
                if abs(lim) == oo:
                    print('')
        lp = limit(y, x, +oo)
        lm = limit(y, x, -oo)
        if (abs(lp) != oo) & (abs(lm) != oo):
            print('')
        elif (abs(lp) != oo) & (abs(lm) == oo):
            print('')
        elif (abs(lp) == oo) & (abs(lm) != oo):
            print('')
        kp = limit(y/x, x, oo, '+')
        km = limit(y/x, x, oo, '-')
        if (kp != 0) & (km != 0):
            if (kp != oo) & (km != oo):
                b = limit(y - kp * x, x, oo)
                if b != oo:
                    print('')
            elif (kp != oo) & (km == oo):
                b = limit(y - kp * x, x, oo, '+')
                if b != oo:
                    print('')
        y_ = diff(y, x)
        print("у': ", y_.simplify())
        y2_ = diff(y, х, 2)
        print('у": ', y2_.simplify())
        y3_ = diff(y, х, 3)
        roots_diff = solve(y_, x)
        k = len(roots_diff)
        if k > 0:
            for i in range(0, k):
                ri = roots_diff[i]
                y2_0 = y2_.subs(x, ri)
                if y2_0 > 0:
                    print('x = %s - точка минимума, y_min = %s' % (ri, y.subs(x, ri)))
                elif y2_0 < 0:
                    print('x = %s - точка максимума, y_max = %s' % (ri, y.subs(x, ri)))
                else:
                    y3_0 = y3_.subs(x, ri)
                    if y3_0 != 0:
                        print('x = %s - точка перегиба, у(х) = %s' % (ri, y.subs(x, ri)))
                    else:
                        print('B критической точке %s требуется дополнительное исследование' % ri)
        roots_2diff = solve(y2_)
        k = len(roots_2diff)
        if k > 0:
            for i in range(0, k):
                ri = roots_2diff[i]
                y3_0 = y3_.subs(x, ri)
                y_0 = y_.subs(x, ri)
                if (y3_0 != 0) & (y_0 != 0):
                    print('x = %s - точка перегиба, y(x) = %s' % (ri, y.subs(x, ri)))
