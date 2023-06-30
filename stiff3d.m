tic
% Assumes the element is a cube: multiplies the final matrix by the volume instead of multiplying each dimension by its size

% Transverse isotropy, symmetry plane yz
% Constants: Ex, Ey, nuxy, nuyz, Gxy
% Non-independent:
% Ez = Ey
% nuxz = nuxy
% Gzx = Gxy
% Gyz = Ey/(2*(1+nuyz))
syms Ex Ey nuxy nuyz Gxy

S = [1/Ex,-nuxy/Ex,-nuxy/Ex,0,0,0;
    -nuxy/Ex,1/Ey,-nuyz/Ey,0,0,0;
    -nuxy/Ex,-nuyz/Ey,1/Ey,0,0,0;
    0,0,0,2*(1+nuyz)/Ey,0,0;
    0,0,0,0,1/Gxy,0;
    0,0,0,0,0,1/Gxy];
C = inv(S);

% Rotation around z
syms theta
T = [cos(theta)^2, sin(theta)^2, 0, 0, 0, -2*cos(theta)*sin(theta);
    sin(theta)^2, cos(theta)^2, 0, 0, 0, 2*cos(theta)*sin(theta);
    0, 0, 1, 0, 0, 0;
    0, 0, 0, cos(theta), sin(theta), 0;
    0, 0, 0, -sin(theta), cos(theta), 0;
    cos(theta)*sin(theta), -cos(theta)*sin(theta), 0, 0, 0, cos(theta)^2-sin(theta)^2];
Cr = T * C * transpose(T);

syms r s t
a = 1/8 * (1-r) * (1-s) * (1-t);
b = 1/8 * (1+r) * (1-s) * (1-t);
c = 1/8 * (1+r) * (1+s) * (1-t);
d = 1/8 * (1-r) * (1+s) * (1-t);
e = 1/8 * (1-r) * (1-s) * (1+t);
f = 1/8 * (1+r) * (1-s) * (1+t);
g = 1/8 * (1+r) * (1+s) * (1+t);
h = 1/8 * (1-r) * (1+s) * (1+t);

B1 = [diff(a,r), 0, 0; 0, diff(a,s), 0; 0, 0, diff(a,t); 0, diff(a,t), diff(a,s); diff(a,t), 0, diff(a,r); diff(a,s), diff(a,r), 0];
B2 = [diff(b,r), 0, 0; 0, diff(b,s), 0; 0, 0, diff(b,t); 0, diff(b,t), diff(b,s); diff(b,t), 0, diff(b,r); diff(b,s), diff(b,r), 0];
B3 = [diff(c,r), 0, 0; 0, diff(c,s), 0; 0, 0, diff(c,t); 0, diff(c,t), diff(c,s); diff(c,t), 0, diff(c,r); diff(c,s), diff(c,r), 0];
B4 = [diff(d,r), 0, 0; 0, diff(d,s), 0; 0, 0, diff(d,t); 0, diff(d,t), diff(d,s); diff(d,t), 0, diff(d,r); diff(d,s), diff(d,r), 0];
B5 = [diff(e,r), 0, 0; 0, diff(e,s), 0; 0, 0, diff(e,t); 0, diff(e,t), diff(e,s); diff(e,t), 0, diff(e,r); diff(e,s), diff(e,r), 0];
B6 = [diff(f,r), 0, 0; 0, diff(f,s), 0; 0, 0, diff(f,t); 0, diff(f,t), diff(f,s); diff(f,t), 0, diff(f,r); diff(f,s), diff(f,r), 0];
B7 = [diff(g,r), 0, 0; 0, diff(g,s), 0; 0, 0, diff(g,t); 0, diff(g,t), diff(g,s); diff(g,t), 0, diff(g,r); diff(g,s), diff(g,r), 0];
B8 = [diff(h,r), 0, 0; 0, diff(h,s), 0; 0, 0, diff(h,t); 0, diff(h,t), diff(h,s); diff(h,t), 0, diff(h,r); diff(h,s), diff(h,r), 0];

B = [B1, B2, B3, B4, B5, B6, B7, B8];

BCB = transpose(B) * Cr * B;
K = int(int(int(BCB, r, -1, 1), s, -1, 1), t, -1, 1);
dK = diff(K, theta);

f = fopen('dkdt3d.py','w');
fprintf(f,'import numpy as np\n');
fprintf(f,'def dkdt3d(Ex,Ey,nuxy,nuyz,Gxy,T,V):\n');
fprintf(f,'    c = np.cos(T)\n');
fprintf(f,'    c2 = np.cos(2*T)\n');
fprintf(f,'    c4 = np.cos(4*T)\n');
fprintf(f,'    s = np.sin(T)\n');
fprintf(f,'    s2 = np.sin(2*T)\n');
fprintf(f,'    s4 = np.sin(4*T)\n');
fprintf(f,'    dkdt = np.zeros((24,24))\n');
for i = 1:24
    for j = i:24
        line = string(dK(i,j));
        line = strrep(line,'^','**');
        line = strrep(line,'cos(theta)','c');
        line = strrep(line,'cos(2*theta)','c2');
        line = strrep(line,'cos(4*theta)','c4');
        line = strrep(line,'sin(theta)','s');
        line = strrep(line,'sin(2*theta)','s2');
        line = strrep(line,'sin(4*theta)','s4');
        
        % searches if expression was already calculated in previous terms
        found = false;
        for k = 1:i
            if found
                break
            end
            for l = k:24
                if i==k && j==l
                    break
                end
                if dK(i,j) == dK(k,l)
                    line = sprintf('dkdt[%d][%d]', k-1, l-1);
                    found = true;
                    break
                end
                if dK(i,j) == -dK(k,l)
                    line = sprintf('-dkdt[%d][%d]', k-1, l-1);
                    found = true;
                    break
                end
            end
        end
        fprintf(f,'    dkdt[%d][%d] = %s\n', i-1, j-1, line);
    end
end
fprintf(f,'    dkdt += dkdt.T - np.diag(dkdt.diagonal())\n');
fprintf(f,'    dkdt *= V\n');
fprintf(f,'    return dkdt');
fclose(f);
toc