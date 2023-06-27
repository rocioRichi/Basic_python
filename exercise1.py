def media(datos):  # podríamos añadirle los nan o cualquier otra cosa
    """ función que calcula la media de una lista
    """
    if not isinstance(datos,list):
        print('input parameter must be a list')
        return 
    suma = 0
    num_nans = datos.count('nan')  # uso función count de las listas
    num_datos = len(datos) - num_nans
    for d in datos:
        suma += d 
    return suma/num_datos
 
def compute_max(datos):
    
    if 'nan' not in datos:
        return max(datos)
    else:
        print('Hay un nan')

def compute_min(datos):
    
     if 'nan' not in datos:
         return min(datos)
     else:
        print('Hay un nan')

def variance(datos):
    """function that returns variance of list"""
    if not isinstance(datos,list):
        print('input parameter must be a list')
        return 
    suma = 0
    num_nans = datos.count('nan')  # uso función count de las listas
    num_datos = len(datos) - num_nans
    for d in datos:
        suma += d**2
    return suma/num_datos