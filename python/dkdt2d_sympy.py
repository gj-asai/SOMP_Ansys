import numpy as np
def dkdt2d(Ex,Ey,nuxy,nuyz,Gxy,T,V):
    c = np.cos(T)
    s = np.sin(T)
    delta = 1.0*Ex - 1.0*Ey*nuxy**2
    dkdt = np.zeros((8,8))
    dkdt[0][0] = -0.666666666666667*Ex**2*s**3*c/delta - 1.5*Ex**2*s**2*c**2/delta - 0.666666666666667*Ex**2*s*c**3/delta + 0.5*Ex**2*c**4/delta - 0.5*Ex*Ey*nuxy*s**4/delta + 3.0*Ex*Ey*nuxy*s**2*c**2/delta - 0.5*Ex*Ey*nuxy*c**4/delta + 0.5*Ex*Ey*s**4/delta + 0.666666666666667*Ex*Ey*s**3*c/delta - 1.5*Ex*Ey*s**2*c**2/delta + 0.666666666666667*Ex*Ey*s*c**3/delta - 1.0*Ex*Gxy*s**4/delta + 6.0*Ex*Gxy*s**2*c**2/delta - 1.0*Ex*Gxy*c**4/delta + 1.0*Ey*Gxy*nuxy**2*s**4/delta - 6.0*Ey*Gxy*nuxy**2*s**2*c**2/delta + 1.0*Ey*Gxy*nuxy**2*c**4/delta
    dkdt[0][1] = -0.333333333333333*Ex**2*s**4/delta - 1.0*Ex**2*s**3*c/delta + 1.0*Ex**2*s*c**3/delta + 0.333333333333333*Ex**2*c**4/delta + 2.0*Ex*Ey*nuxy*s**3*c/delta - 2.0*Ex*Ey*nuxy*s*c**3/delta + 0.333333333333333*Ex*Ey*s**4/delta - 1.0*Ex*Ey*s**3*c/delta + 1.0*Ex*Ey*s*c**3/delta - 0.333333333333333*Ex*Ey*c**4/delta + 4.0*Ex*Gxy*s**3*c/delta - 4.0*Ex*Gxy*s*c**3/delta - 4.0*Ey*Gxy*nuxy**2*s**3*c/delta + 4.0*Ey*Gxy*nuxy**2*s*c**3/delta
    dkdt[0][2] = -0.333333333333333*Ex**2*s**3*c/delta + 1.66666666666667*Ex**2*s*c**3/delta + 2.0*Ex*Ey*nuxy*s**3*c/delta - 2.0*Ex*Ey*nuxy*s*c**3/delta - 1.66666666666667*Ex*Ey*s**3*c/delta + 0.333333333333333*Ex*Ey*s*c**3/delta + 4.0*Ex*Gxy*s**3*c/delta - 4.0*Ex*Gxy*s*c**3/delta - 4.0*Ey*Gxy*nuxy**2*s**3*c/delta + 4.0*Ey*Gxy*nuxy**2*s*c**3/delta
    dkdt[0][3] = -0.166666666666667*Ex**2*s**4/delta + 1.5*Ex**2*s**2*c**2/delta - 0.333333333333333*Ex**2*c**4/delta + 0.5*Ex*Ey*nuxy*s**4/delta - 3.0*Ex*Ey*nuxy*s**2*c**2/delta + 0.5*Ex*Ey*nuxy*c**4/delta - 0.333333333333333*Ex*Ey*s**4/delta + 1.5*Ex*Ey*s**2*c**2/delta - 0.166666666666667*Ex*Ey*c**4/delta + 1.0*Ex*Gxy*s**4/delta - 6.0*Ex*Gxy*s**2*c**2/delta + 1.0*Ex*Gxy*c**4/delta - 1.0*Ey*Gxy*nuxy**2*s**4/delta + 6.0*Ey*Gxy*nuxy**2*s**2*c**2/delta - 1.0*Ey*Gxy*nuxy**2*c**4/delta
    dkdt[0][4] = 0.333333333333333*Ex**2*s**3*c/delta + 1.5*Ex**2*s**2*c**2/delta + 0.333333333333333*Ex**2*s*c**3/delta - 0.5*Ex**2*c**4/delta + 0.5*Ex*Ey*nuxy*s**4/delta - 3.0*Ex*Ey*nuxy*s**2*c**2/delta + 0.5*Ex*Ey*nuxy*c**4/delta - 0.5*Ex*Ey*s**4/delta - 0.333333333333333*Ex*Ey*s**3*c/delta + 1.5*Ex*Ey*s**2*c**2/delta - 0.333333333333333*Ex*Ey*s*c**3/delta + 1.0*Ex*Gxy*s**4/delta - 6.0*Ex*Gxy*s**2*c**2/delta + 1.0*Ex*Gxy*c**4/delta - 1.0*Ey*Gxy*nuxy**2*s**4/delta + 6.0*Ey*Gxy*nuxy**2*s**2*c**2/delta - 1.0*Ey*Gxy*nuxy**2*c**4/delta
    dkdt[0][5] = 0.166666666666667*Ex**2*s**4/delta + 1.0*Ex**2*s**3*c/delta - 1.0*Ex**2*s*c**3/delta - 0.166666666666667*Ex**2*c**4/delta - 2.0*Ex*Ey*nuxy*s**3*c/delta + 2.0*Ex*Ey*nuxy*s*c**3/delta - 0.166666666666667*Ex*Ey*s**4/delta + 1.0*Ex*Ey*s**3*c/delta - 1.0*Ex*Ey*s*c**3/delta + 0.166666666666667*Ex*Ey*c**4/delta - 4.0*Ex*Gxy*s**3*c/delta + 4.0*Ex*Gxy*s*c**3/delta + 4.0*Ey*Gxy*nuxy**2*s**3*c/delta - 4.0*Ey*Gxy*nuxy**2*s*c**3/delta
    dkdt[0][6] = 0.666666666666667*Ex**2*s**3*c/delta - 1.33333333333333*Ex**2*s*c**3/delta - 2.0*Ex*Ey*nuxy*s**3*c/delta + 2.0*Ex*Ey*nuxy*s*c**3/delta + 1.33333333333333*Ex*Ey*s**3*c/delta - 0.666666666666667*Ex*Ey*s*c**3/delta - 4.0*Ex*Gxy*s**3*c/delta + 4.0*Ex*Gxy*s*c**3/delta + 4.0*Ey*Gxy*nuxy**2*s**3*c/delta - 4.0*Ey*Gxy*nuxy**2*s*c**3/delta
    dkdt[0][7] = 0.333333333333333*Ex**2*s**4/delta - 1.5*Ex**2*s**2*c**2/delta + 0.166666666666667*Ex**2*c**4/delta - 0.5*Ex*Ey*nuxy*s**4/delta + 3.0*Ex*Ey*nuxy*s**2*c**2/delta - 0.5*Ex*Ey*nuxy*c**4/delta + 0.166666666666667*Ex*Ey*s**4/delta - 1.5*Ex*Ey*s**2*c**2/delta + 0.333333333333333*Ex*Ey*c**4/delta - 1.0*Ex*Gxy*s**4/delta + 6.0*Ex*Gxy*s**2*c**2/delta - 1.0*Ex*Gxy*c**4/delta + 1.0*Ey*Gxy*nuxy**2*s**4/delta - 6.0*Ey*Gxy*nuxy**2*s**2*c**2/delta + 1.0*Ey*Gxy*nuxy**2*c**4/delta
    dkdt[1][1] = -0.5*Ex**2*s**4/delta + 0.666666666666667*Ex**2*s**3*c/delta + 1.5*Ex**2*s**2*c**2/delta + 0.666666666666667*Ex**2*s*c**3/delta + 0.5*Ex*Ey*nuxy*s**4/delta - 3.0*Ex*Ey*nuxy*s**2*c**2/delta + 0.5*Ex*Ey*nuxy*c**4/delta - 0.666666666666667*Ex*Ey*s**3*c/delta + 1.5*Ex*Ey*s**2*c**2/delta - 0.666666666666667*Ex*Ey*s*c**3/delta - 0.5*Ex*Ey*c**4/delta + 1.0*Ex*Gxy*s**4/delta - 6.0*Ex*Gxy*s**2*c**2/delta + 1.0*Ex*Gxy*c**4/delta - 1.0*Ey*Gxy*nuxy**2*s**4/delta + 6.0*Ey*Gxy*nuxy**2*s**2*c**2/delta - 1.0*Ey*Gxy*nuxy**2*c**4/delta
    dkdt[1][2] = dkdt[0][3]
    dkdt[1][3] = 1.33333333333333*Ex**2*s**3*c/delta - 0.666666666666667*Ex**2*s*c**3/delta - 2.0*Ex*Ey*nuxy*s**3*c/delta + 2.0*Ex*Ey*nuxy*s*c**3/delta + 0.666666666666667*Ex*Ey*s**3*c/delta - 1.33333333333333*Ex*Ey*s*c**3/delta - 4.0*Ex*Gxy*s**3*c/delta + 4.0*Ex*Gxy*s*c**3/delta + 4.0*Ey*Gxy*nuxy**2*s**3*c/delta - 4.0*Ey*Gxy*nuxy**2*s*c**3/delta
    dkdt[1][4] = dkdt[0][5]
    dkdt[1][5] = 0.5*Ex**2*s**4/delta - 0.333333333333333*Ex**2*s**3*c/delta - 1.5*Ex**2*s**2*c**2/delta - 0.333333333333333*Ex**2*s*c**3/delta - 0.5*Ex*Ey*nuxy*s**4/delta + 3.0*Ex*Ey*nuxy*s**2*c**2/delta - 0.5*Ex*Ey*nuxy*c**4/delta + 0.333333333333333*Ex*Ey*s**3*c/delta - 1.5*Ex*Ey*s**2*c**2/delta + 0.333333333333333*Ex*Ey*s*c**3/delta + 0.5*Ex*Ey*c**4/delta - 1.0*Ex*Gxy*s**4/delta + 6.0*Ex*Gxy*s**2*c**2/delta - 1.0*Ex*Gxy*c**4/delta + 1.0*Ey*Gxy*nuxy**2*s**4/delta - 6.0*Ey*Gxy*nuxy**2*s**2*c**2/delta + 1.0*Ey*Gxy*nuxy**2*c**4/delta
    dkdt[1][6] = dkdt[0][7]
    dkdt[1][7] = -1.66666666666667*Ex**2*s**3*c/delta + 0.333333333333333*Ex**2*s*c**3/delta + 2.0*Ex*Ey*nuxy*s**3*c/delta - 2.0*Ex*Ey*nuxy*s*c**3/delta - 0.333333333333333*Ex*Ey*s**3*c/delta + 1.66666666666667*Ex*Ey*s*c**3/delta + 4.0*Ex*Gxy*s**3*c/delta - 4.0*Ex*Gxy*s*c**3/delta - 4.0*Ey*Gxy*nuxy**2*s**3*c/delta + 4.0*Ey*Gxy*nuxy**2*s*c**3/delta
    dkdt[2][2] = -0.666666666666667*Ex**2*s**3*c/delta + 1.5*Ex**2*s**2*c**2/delta - 0.666666666666667*Ex**2*s*c**3/delta - 0.5*Ex**2*c**4/delta + 0.5*Ex*Ey*nuxy*s**4/delta - 3.0*Ex*Ey*nuxy*s**2*c**2/delta + 0.5*Ex*Ey*nuxy*c**4/delta - 0.5*Ex*Ey*s**4/delta + 0.666666666666667*Ex*Ey*s**3*c/delta + 1.5*Ex*Ey*s**2*c**2/delta + 0.666666666666667*Ex*Ey*s*c**3/delta + 1.0*Ex*Gxy*s**4/delta - 6.0*Ex*Gxy*s**2*c**2/delta + 1.0*Ex*Gxy*c**4/delta - 1.0*Ey*Gxy*nuxy**2*s**4/delta + 6.0*Ey*Gxy*nuxy**2*s**2*c**2/delta - 1.0*Ey*Gxy*nuxy**2*c**4/delta
    dkdt[2][3] = -0.333333333333333*Ex**2*s**4/delta + 1.0*Ex**2*s**3*c/delta - 1.0*Ex**2*s*c**3/delta + 0.333333333333333*Ex**2*c**4/delta - 2.0*Ex*Ey*nuxy*s**3*c/delta + 2.0*Ex*Ey*nuxy*s*c**3/delta + 0.333333333333333*Ex*Ey*s**4/delta + 1.0*Ex*Ey*s**3*c/delta - 1.0*Ex*Ey*s*c**3/delta - 0.333333333333333*Ex*Ey*c**4/delta - 4.0*Ex*Gxy*s**3*c/delta + 4.0*Ex*Gxy*s*c**3/delta + 4.0*Ey*Gxy*nuxy**2*s**3*c/delta - 4.0*Ey*Gxy*nuxy**2*s*c**3/delta
    dkdt[2][4] = dkdt[0][6]
    dkdt[2][5] = dkdt[0][7]
    dkdt[2][6] = 0.333333333333333*Ex**2*s**3*c/delta - 1.5*Ex**2*s**2*c**2/delta + 0.333333333333333*Ex**2*s*c**3/delta + 0.5*Ex**2*c**4/delta - 0.5*Ex*Ey*nuxy*s**4/delta + 3.0*Ex*Ey*nuxy*s**2*c**2/delta - 0.5*Ex*Ey*nuxy*c**4/delta + 0.5*Ex*Ey*s**4/delta - 0.333333333333333*Ex*Ey*s**3*c/delta - 1.5*Ex*Ey*s**2*c**2/delta - 0.333333333333333*Ex*Ey*s*c**3/delta - 1.0*Ex*Gxy*s**4/delta + 6.0*Ex*Gxy*s**2*c**2/delta - 1.0*Ex*Gxy*c**4/delta + 1.0*Ey*Gxy*nuxy**2*s**4/delta - 6.0*Ey*Gxy*nuxy**2*s**2*c**2/delta + 1.0*Ey*Gxy*nuxy**2*c**4/delta
    dkdt[2][7] = 0.166666666666667*Ex**2*s**4/delta - 1.0*Ex**2*s**3*c/delta + 1.0*Ex**2*s*c**3/delta - 0.166666666666667*Ex**2*c**4/delta + 2.0*Ex*Ey*nuxy*s**3*c/delta - 2.0*Ex*Ey*nuxy*s*c**3/delta - 0.166666666666667*Ex*Ey*s**4/delta - 1.0*Ex*Ey*s**3*c/delta + 1.0*Ex*Ey*s*c**3/delta + 0.166666666666667*Ex*Ey*c**4/delta + 4.0*Ex*Gxy*s**3*c/delta - 4.0*Ex*Gxy*s*c**3/delta - 4.0*Ey*Gxy*nuxy**2*s**3*c/delta + 4.0*Ey*Gxy*nuxy**2*s*c**3/delta
    dkdt[3][3] = 0.5*Ex**2*s**4/delta + 0.666666666666667*Ex**2*s**3*c/delta - 1.5*Ex**2*s**2*c**2/delta + 0.666666666666667*Ex**2*s*c**3/delta - 0.5*Ex*Ey*nuxy*s**4/delta + 3.0*Ex*Ey*nuxy*s**2*c**2/delta - 0.5*Ex*Ey*nuxy*c**4/delta - 0.666666666666667*Ex*Ey*s**3*c/delta - 1.5*Ex*Ey*s**2*c**2/delta - 0.666666666666667*Ex*Ey*s*c**3/delta + 0.5*Ex*Ey*c**4/delta - 1.0*Ex*Gxy*s**4/delta + 6.0*Ex*Gxy*s**2*c**2/delta - 1.0*Ex*Gxy*c**4/delta + 1.0*Ey*Gxy*nuxy**2*s**4/delta - 6.0*Ey*Gxy*nuxy**2*s**2*c**2/delta + 1.0*Ey*Gxy*nuxy**2*c**4/delta
    dkdt[3][4] = dkdt[0][7]
    dkdt[3][5] = dkdt[1][7]
    dkdt[3][6] = dkdt[2][7]
    dkdt[3][7] = -0.5*Ex**2*s**4/delta - 0.333333333333333*Ex**2*s**3*c/delta + 1.5*Ex**2*s**2*c**2/delta - 0.333333333333333*Ex**2*s*c**3/delta + 0.5*Ex*Ey*nuxy*s**4/delta - 3.0*Ex*Ey*nuxy*s**2*c**2/delta + 0.5*Ex*Ey*nuxy*c**4/delta + 0.333333333333333*Ex*Ey*s**3*c/delta + 1.5*Ex*Ey*s**2*c**2/delta + 0.333333333333333*Ex*Ey*s*c**3/delta - 0.5*Ex*Ey*c**4/delta + 1.0*Ex*Gxy*s**4/delta - 6.0*Ex*Gxy*s**2*c**2/delta + 1.0*Ex*Gxy*c**4/delta - 1.0*Ey*Gxy*nuxy**2*s**4/delta + 6.0*Ey*Gxy*nuxy**2*s**2*c**2/delta - 1.0*Ey*Gxy*nuxy**2*c**4/delta
    dkdt[4][4] = dkdt[0][0]
    dkdt[4][5] = dkdt[0][1]
    dkdt[4][6] = dkdt[0][2]
    dkdt[4][7] = dkdt[0][3]
    dkdt[5][5] = dkdt[1][1]
    dkdt[5][6] = dkdt[0][3]
    dkdt[5][7] = dkdt[1][3]
    dkdt[6][6] = dkdt[2][2]
    dkdt[6][7] = dkdt[2][3]
    dkdt[7][7] = dkdt[3][3]
    dkdt += dkdt.T - np.diag(dkdt.diagonal())
    dkdt *= V
    return dkdt