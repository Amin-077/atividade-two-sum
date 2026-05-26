def two_sum(nums, target):
    """
    Encontra os índices de dois números no array que somam o valor alvo (target).
    
    Lógica:
    Iteramos pela lista apenas uma vez. Em cada passo, calculamos o "complemento"
    (que é o target menos o número atual). Se o complemento já estiver no nosso
    dicionário (hash map), significa que encontramos o par correto.
    Se não estiver, adicionamos o número atual e seu índice no dicionário para 
    verificações futuras.
    
    :param nums: List[int] - Lista de números inteiros.
    :param target: int - O valor soma desejado.
    :return: List[int] - Lista com os dois índices encontrados.
    """
    
    # Dicionário para armazenar os números já visitados e seus respectivos índices.
    # A estrutura será: {valor_do_numero: indice_na_lista}
    num_map = {}
    
    for i, num in enumerate(nums):
        complemento = target - num
        
        # Verifica se o complemento já foi visto antes na lista
        if complemento in num_map:
            # Retorna o índice do complemento (visto no passado) e o índice atual (i)
            return [num_map[complemento], i]
        
        # Caso não tenha encontrado, salva o número atual e seu índice no dicionário
        num_map[num] = i
        
    # Retorna uma lista vazia caso não encontre nenhuma solução
    # (A descrição do problema garante que sempre haverá uma solução, 
    # mas é uma boa prática ter um retorno padrão).
    return []

# ==========================================
# Testes Realizados (Conforme a descrição)
# ==========================================
if __name__ == "__main__":
    print("--- Testes do Problema Two Sum ---")
    
    # Exemplo 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Exemplo 1: nums = {nums1}, target = {target1}")
    print(f"Saída: {two_sum(nums1, target1)}")  # Esperado: [0, 1]
    print("-" * 30)
    
    # Exemplo 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Exemplo 2: nums = {nums2}, target = {target2}")
    print(f"Saída: {two_sum(nums2, target2)}")  # Esperado: [1, 2]
    print("-" * 30)
    
    # Exemplo 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Exemplo 3: nums = {nums3}, target = {target3}")
    print(f"Saída: {two_sum(nums3, target3)}")  # Esperado: [0, 1]
    print("-" * 30)