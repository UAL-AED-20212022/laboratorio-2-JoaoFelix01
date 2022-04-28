from models.LinkedList import LinkedList

lista = LinkedList()

def rpi(scan, lista):
    lista.insert_at_start(scan[1])
    lista.traverse_list()
    return lista

def rpf(scan):
    lista.insert_at_end(scan[1])
    lista.traverse_list()
    return lista

def rpde(scan):
    lista.insert_after_item(scan[2], scan[1])
    lista.traverse_list()
    return lista

def rpae(scan):
    lista.insert_before_item(scan[2], scan[1])
    lista.traverse_list()
    return lista

def rpii(scan):
    lista.insert_at_index(int(scan[2]), scan[1])
    lista.traverse_list()
    return lista

def vne():
    return lista.get_count()

def vp(scan):
    return lista.search_item(scan[1])

def epe():
    x = lista.start_node
    lista.delete_at_start()
    return x

def eue():
    x = lista.get_last_node()
    lista.delete_at_end()
    return x

def ep(scan):
    lista.delete_element_by_value(scan[1])
    return lista