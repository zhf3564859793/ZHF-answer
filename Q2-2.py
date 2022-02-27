import numpy as np
import math as m
from sympy import *
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False

Earray=[]
Sarray=[]
ESarray=[]
Parray=[]
array=[]

def fE(E,S,ES):
    a=-100*E*S+750*ES
    return a

def fS(E,S,ES):
    a=-100*E*S+600*ES
    return a

def fES(E,S,ES):
    a=100*E*S-750*ES
    return a

def fP(ES):
    a=150*ES
    return a

def RK4():
    h=0.00002
    a=0
    E=1
    S=10
    ES=0
    P=0

    while a<=0.25:
        array.append(a)
        Earray.append(E)
        Sarray.append(S)
        ESarray.append(ES)
        Parray.append(P)
        a+=h

        fE1=fE(E,S,ES) #第一步
        e1=E+fE1*h/2
        fS1=fS(E,S,ES)
        s1=S+fS1*h/2
        fES1=fES(E,S,ES)
        es1=ES+fES1*h/2
        fP1=fP(ES)
        p1=P+fP1*h/2

        fE2=fE(e1,s1,es1)#第二步
        e2=E+fE2*h/2
        fS2=fS(e1,s1,es1)
        s2=S+fS2*h/2
        fES2=fES(e1,s1,es1)
        es2=ES+fE2*h/2
        fP2=fP(es1)
        p2=P+fE2*h/2


        fE3=fE(e2,s2,es2) #第三步
        e3=E+fE3*h
        fS3=fS(e2,s2,es2) 
        s3=S+fS3*h
        fES3=fES(e2,s2,es2) 
        es3=ES+fES3*h
        fP3=fP(es2)
        p3=P+fP3*h

        fE4=fE(e3,s3,es3) #第四步
        fS4=fS(e3,s3,es3)
        fES4=fES(e3,s3,es3)
        fP4=fP(es3)
        
        E=E+(fE1+2*fE2+2*fE3+fE4)*h/6
        S=S+(fS1+2*fS2+2*fS3+fS4)*h/6
        ES=ES+(fES1+2*fES2+2*fES3+fES4)*h/6
        P=P+(fP1+2*fP2+2*fP3+fP4)*h/6

def main():
    RK4()
    #for i in Earray:
       #print(i)
    print("-------------")
    #for i in Sarray:
        #print(i)
    fig1=plt.figure()
    E_t=fig1.add_subplot(1,1,1)
    E_t.plot(array, Earray, alpha=0.2)
    E_t.set_title("[E]-T")
    E_t.set_xlabel("Time/min")
    E_t.set_ylabel("[E]/uM")

    fig2=plt.figure()
    S_t=fig2.add_subplot(1,1,1)
    S_t.plot(array, Sarray, alpha=0.2)
    S_t.set_title("[S]-T")
    S_t.set_xlabel("Time/min")
    S_t.set_ylabel("[S]/uM")

    fig3=plt.figure()
    ES_t=fig3.add_subplot(1,1,1)
    ES_t.plot(array, ESarray, alpha=0.2)
    ES_t.set_title("[ES]-T")
    ES_t.set_xlabel("Time/min")
    ES_t.set_ylabel("[ES]/uM")

    fig4=plt.figure()
    P_t=fig4.add_subplot(1,1,1)
    P_t.plot(array, Parray, alpha=0.2)
    P_t.set_title("[P]-T")
    P_t.set_xlabel("Time/min")
    P_t.set_ylabel("[P]/uM")
    plt.show()
main()