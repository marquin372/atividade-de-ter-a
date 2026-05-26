import copy
lista=[[1,2],[3,4]]
rasa=copy.copy(lista)
profunda=copy.deepcopy(lista)
rasa[0][0]=999
print(lista)
print(rasa)
print(profunda)