"""Faça um programa que leia um ângulo qualquer e mostre
o valor do seno, cosseno e tangente"""
import math
#seno a = cateto_oposto/hipotenusa
#cosseno a = cateto_adjacente/hipotenusa
#tangente a = cateto_oposto/cateto_adjacente
ang=float(input('Digite o ângulo:'))
seno=math.sin(math.radians(ang))#é usado math.radians para converter de degrees pra radians
coss=math.cos(math.radians(ang))
tang=math.tan(math.radians(ang))
print('O ângulo de {} tem o seno de {:.2f}'.format(ang,seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ang,coss))
print('O ãngulo de {} tem a tangente de {:.2f}'.format(ang,tang))
