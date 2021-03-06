# Autogenerated with SMOP 
from smop.core import *
# 

    
@function
def save3Dtocsv(baseoutfilename=None,folder=None,N=None,Nx=None,Ny=None,Nz=None,dt=None,tmax=None,t=None,i=None,flags=None,lattice=None,vel=None,m=None,Fel=None,Fdamp=None,Fext=None,Ekinpdof=None,Ekinp=None,Ekin=None,Epotp=None,Epot=None,Dfuncp=None,Dfunc=None,covariantbase=None,contravariantbase=None,metriccoefficients=None,g=None,sqrtg=None,reciprocalmetriccoefficients=None,firstChristoffelsymbol=None,secondChristoffelsymbol=None,Riemanntensor=None,Riccitensor=None,R=None,rho=None,u=None,p=None,S=None,gammadot=None,sigma=None,mu=None,tau=None,cs=None,Q=None,feq=None,f=None,defgrad=None,rightCauGretens=None,EulLagstrain=None,Cauchystress=None,*args,**kwargs):
    varargin = save3Dtocsv.varargin
    nargin = save3Dtocsv.nargin

    ##
#        Project: Fluid - structure interaction on deformable surfaces
#         Author: Luca Di Stasio
#    Institution: ETH Zrich
#                 Institute for Building Materials
# Research group: Computational Physics for Engineering Materials
#        Version: 0.1
#  Creation date: July 2nd, 2014
#    Last update: July 31st, 2014
    
    #    Description: 
#          Input: 
#         Output:
    
    #                 Ordering of flags:
#                 flags(1)  --> save fixed lattice (computational domain)
#                 flags(2)  --> save moving mesh (physical domain)
#                 flags(3)  --> save velocities (LSM)
#                 flags(4)  --> save masses (LSM)
#                 flags(5)  --> save elastic forces (LSM)
#                 flags(6)  --> save damping forces (LSM)
#                 flags(7)  --> save external forces (LSM)
#                 flags(8)  --> save total forces (LSM)
#                 flags(9)  --> save particle kinetic energy per dof (LSM)
#                 flags(10) --> save particle kinetic energy (LSM)
#                 flags(11) --> save total kinetic energy (LSM)
#                 flags(12) --> save particle potential energy (LSM)
#                 flags(13) --> save total potential energy (LSM)
#                 flags(14) --> save particle dissipation function (LSM)
#                 flags(15) --> save total dissipation function (LSM)
#                 flags(16) --> save covariant base vectors
#                 flags(17) --> save contravariant base vectors
#                 flags(18) --> save metric tensor
#                 flags(19) --> save metric tensor determinant
#                 flags(20) --> save g
#                 flags(21) --> save reciprocal metric coefficients
#                 flags(22) --> save first Christoffel symbols
#                 flags(23) --> save second Christoffel symbols
#                 flags(24) --> save Riemann tensor
#                 flags(25) --> save Ricci tensor
#                 flags(26) --> save Ricci curvature
#                 flags(27) --> save density (LBM)
#                 flags(28) --> save velocity in cartesian components (LBM)
#                 flags(29) --> save pressure (LBM)
#                 flags(30) --> save strain rate tensor (LBM)
#                 flags(31) --> save strain rate (LBM)
#                 flags(32) --> save stress tensor (LBM)
#                 flags(33) --> save viscosity (LBM)
#                 flags(34) --> save relaxation time (LBM)
#                 flags(35) --> save sound velocity (LBM)
#                 flags(36) --> save particle equilibrium populations (LBM)
#                 flags(37) --> save particle populations (LBM)
#                 flags(38) --> save deformation gradient (LSM)
#                 flags(39) --> save right Cauchy-Green tensor (LSM)
#                 flags(40) --> save Euler-Lagrange strain tensor (LSM)
#                 flags(41) --> save Cauchy stress tensor (LSM)
    
    ##
    
    if i != 0:
        idigits=fix(abs(log10(abs(i)))) + 1
    else:
        idigits=1
    
    if itmax != 0:
        itmaxdigits=fix(abs(log10(abs(itmax)))) + 1
    else:
        itmaxdigits=1
    
    if idigits < itmaxdigits:
        itstring=num2str(i)
        diffdigits=itmaxdigits - idigits
        for i in arange(1,diffdigits).reshape(-1):
            itstring=strcat('0',itstring)
    
    filename=strcat(folder,'/',baseoutfilename,'_N',itstring,'.csv')
    dataindex=matlabarray([])
    data=matlabarray([])
    C1=- 1
    C2=- 1
    for i in arange(1,length(flags)).reshape(-1):
        if flags[i]:
            R1=6
            R2=N + 5
            C1=C2 + 1
            if 1 == i:
                C2=C2 + 3
                data=matlabarray(cat(data,lattice[:,1:3]))
            else:
                if 2 == i:
                    C2=C2 + 3
                    data=matlabarray(cat(data,lattice[:,7:9]))
                else:
                    if 3 == i:
                        C2=C2 + 3
                        data=matlabarray(cat(data,vel))
                    else:
                        if 4 == i:
                            C2=C2 + 1
                            data=matlabarray(cat(data,m))
                        else:
                            if 5 == i:
                                C2=C2 + 3
                                data=matlabarray(cat(data,Fel))
                            else:
                                if 6 == i:
                                    C2=C2 + 3
                                    data=matlabarray(cat(data,Fdamp))
                                else:
                                    if 7 == i:
                                        C2=C2 + 3
                                        data=matlabarray(cat(data,Fext))
                                    else:
                                        if 8 == i:
                                            C2=C2 + 3
                                            data=matlabarray(cat(data,Fel + Fdamp + Fext))
                                        else:
                                            if 9 == i:
                                                C2=C2 + 3
                                                data=matlabarray(cat(data,Ekinpdof))
                                            else:
                                                if 10 == i:
                                                    C2=C2 + 1
                                                    data=matlabarray(cat(data,Ekinp))
                                                else:
                                                    if 11 == i:
                                                        C2=C2 + 1
                                                        data=matlabarray(cat(data,dot(Ekin,ones(N,1))))
                                                    else:
                                                        if 12 == i:
                                                            C2=C2 + 1
                                                            data=matlabarray(cat(data,Epotp))
                                                        else:
                                                            if 13 == i:
                                                                C2=C2 + 1
                                                                data=matlabarray(cat(data,dot(Epot,ones(N,1))))
                                                            else:
                                                                if 14 == i:
                                                                    C2=C2 + 1
                                                                    data=matlabarray(cat(data,Dfuncp))
                                                                else:
                                                                    if 15 == i:
                                                                        C2=C2 + 1
                                                                        data=matlabarray(cat(data,dot(Dfunc,ones(N,1))))
                                                                    else:
                                                                        if 16 == i:
                                                                            C2=C2 + 3
                                                                            data=matlabarray(cat(data,covariantbase))
                                                                        else:
                                                                            if 17 == i:
                                                                                C2=C2 + 3
                                                                                data=matlabarray(cat(data,contravariantbase))
                                                                            else:
                                                                                if 18 == i:
                                                                                    C2=C2 + 6
                                                                                    data=matlabarray(cat(data,metriccoefficients))
                                                                                else:
                                                                                    if 19 == i:
                                                                                        C2=C2 + 1
                                                                                        data=matlabarray(cat(data,g))
                                                                                    else:
                                                                                        if 20 == i:
                                                                                            C2=C2 + 1
                                                                                            data=matlabarray(cat(data,sqrtg))
                                                                                        else:
                                                                                            if 21 == i:
                                                                                                C2=C2 + 6
                                                                                                data=matlabarray(cat(data,reciprocalmetriccoefficients))
                                                                                            else:
                                                                                                if 22 == i:
                                                                                                    C2=C2 + 27
                                                                                                    data=matlabarray(cat(data,firstChristoffelsymbol))
                                                                                                else:
                                                                                                    if 23 == i:
                                                                                                        C2=C2 + 27
                                                                                                        data=matlabarray(cat(data,secondChristoffelsymbol))
                                                                                                    else:
                                                                                                        if 24 == i:
                                                                                                            C2=C2 + 81
                                                                                                            data=matlabarray(cat(data,Riemanntensor))
                                                                                                        else:
                                                                                                            if 25 == i:
                                                                                                                C2=C2 + 6
                                                                                                                data=matlabarray(cat(data,Riccitensor))
                                                                                                            else:
                                                                                                                if 26 == i:
                                                                                                                    C2=C2 + 1
                                                                                                                    data=matlabarray(cat(data,R))
                                                                                                                else:
                                                                                                                    if 27 == i:
                                                                                                                        C2=C2 + 1
                                                                                                                        data=matlabarray(cat(data,rho))
                                                                                                                    else:
                                                                                                                        if 28 == i:
                                                                                                                            C2=C2 + 3
                                                                                                                            data=matlabarray(cat(data,u))
                                                                                                                        else:
                                                                                                                            if 29 == i:
                                                                                                                                C2=C2 + 1
                                                                                                                                data=matlabarray(cat(data,p))
                                                                                                                            else:
                                                                                                                                if 30 == i:
                                                                                                                                    C2=C2 + 6
                                                                                                                                    data=matlabarray(cat(data,S))
                                                                                                                                else:
                                                                                                                                    if 31 == i:
                                                                                                                                        C2=C2 + 1
                                                                                                                                        data=matlabarray(cat(data,gammadot))
                                                                                                                                    else:
                                                                                                                                        if 32 == i:
                                                                                                                                            C2=C2 + 6
                                                                                                                                            data=matlabarray(cat(data,sigma))
                                                                                                                                        else:
                                                                                                                                            if 33 == i:
                                                                                                                                                C2=C2 + 1
                                                                                                                                                data=matlabarray(cat(data,mu))
                                                                                                                                            else:
                                                                                                                                                if 34 == i:
                                                                                                                                                    C2=C2 + 1
                                                                                                                                                    data=matlabarray(cat(data,tau))
                                                                                                                                                else:
                                                                                                                                                    if 35 == i:
                                                                                                                                                        C2=C2 + 1
                                                                                                                                                        data=matlabarray(cat(data,cs))
                                                                                                                                                    else:
                                                                                                                                                        if 36 == i:
                                                                                                                                                            C2=C2 + Q
                                                                                                                                                            data=matlabarray(cat(data,feq))
                                                                                                                                                        else:
                                                                                                                                                            if 37 == i:
                                                                                                                                                                C2=C2 + Q
                                                                                                                                                                data=matlabarray(cat(data,f))
                                                                                                                                                            else:
                                                                                                                                                                if 38 == i:
                                                                                                                                                                    C2=C2 + 9
                                                                                                                                                                    data=matlabarray(cat(data,defgrad))
                                                                                                                                                                else:
                                                                                                                                                                    if 39 == i:
                                                                                                                                                                        C2=C2 + 9
                                                                                                                                                                        data=matlabarray(cat(data,rightCauGretens))
                                                                                                                                                                    else:
                                                                                                                                                                        if 40 == i:
                                                                                                                                                                            C2=C2 + 9
                                                                                                                                                                            data=matlabarray(cat(data,EulLagstrain))
                                                                                                                                                                        else:
                                                                                                                                                                            if 41 == i:
                                                                                                                                                                                C2=C2 + 9
                                                                                                                                                                                data=matlabarray(cat(data,Cauchystress))
            dataindex=matlabarray(cat(dataindex,cat([i],[R1],[C1],[R2],[C2])))
    
    nvars=size(dataindex,2)
    basicdata=matlabarray(cat(N,Nx,Ny,Nz,dt,tmax,t,i,nvars))
    fid=fopen(filename,'w')
    dlmwrite(filename,basicdata,'-append')
    dlmwrite(filename,dataindex,'-append')
    dlmwrite(filename,data,'-append')
    fclose(fid)
    return