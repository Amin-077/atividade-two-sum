class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    dummy = ListNode()
    atual = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            atual.next = list1
            list1 = list1.next
        else:
            atual.next = list2
            list2 = list2.next

        atual = atual.next

    if list1:
        atual.next = list1
    else:
        atual.next = list2

    return dummy.next


# Funções auxiliares para testar
def criar_lista(valores):
    dummy = ListNode()
    atual = dummy

    for valor in valores:
        atual.next = ListNode(valor)
        atual = atual.next

    return dummy.next


def imprimir_lista(head):
    resultado = []

    while head:
        resultado.append(head.val)
        head = head.next

    print(resultado)


# Teste
list1 = criar_lista([1, 2, 4])
list2 = criar_lista([1, 3, 4])

resultado = merge_two_lists(list1, list2)

imprimir_lista(resultado)