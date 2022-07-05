INITIAL_CAPACITY = 1000000

# Classe nó
class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
	def __str__(self):
		return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next != None)
	def __repr__(self):
		return str(self)


# Classe HashTable
class HashTable:
	# Inicializa a HashTable
	def __init__(self):
		self.capacity = INITIAL_CAPACITY
		self.size = 0
		self.buckets = [None]*self.capacity
	# Dado uma Key (String), gera um índice.
	def hash(self, key):
		hashsum = 0
		# Para cada caracter na Key
		for idx, c in enumerate(key):
			hashsum += (idx + len(key)) ** ord(c)
			hashsum = hashsum % self.capacity
		return hashsum

	# Insere um conjunto (Key, Value)
	def insert(self, key, value):
		# Incrementa o tamanho da HashTable
		self.size += 1
		#Calcula o índice
		index = self.hash(key)
		# Vai para o nó correspondente ao índice
		node = self.buckets[index]
		# 3. Se o Bucket for None
		if node is None:
			# Cria um nó e adiciona
			self.buckets[index] = Node(key, value)
			return
		# 4. Itera até o fim da linked list do índice
		prev = node
		while node is not None:
			prev = node
			node = node.next
		# Adiciona o novo nó no final da linked list
		prev.next = Node(key, value)

	# Encontra o valor com base na Chave
	def find(self, key):
		# Calcula o Hash
		index = self.hash(key)
		# Vai para o primeiro nó do Índice
		node = self.buckets[index]
		# 3. Percorre a Linked List
		while node is not None and node.key != key:
			node = node.next
		if node is None:
			# Não encountrou (Retorna None)
			return None
		else:
			# Encontrou (Retorna o valor)
			return node.value

	# Remove um nó dado o valor
	def remove(self, key):
		# Calcula o Hash
		index = self.hash(key)
		node = self.buckets[index]
		prev = None
		# Percorre a linked list
		while node is not None and node.key != key:
			prev = node
			node = node.next

		if node is None:
			# Não encontrou
			return None
		else:
			# Encontrou 
			self.size -= 1
			result = node.value
			# Deleta o nó da linked list
			if prev is None:
				self.buckets[index] = node.next
			else:
				prev.next = prev.next.next
			# Retorna o valor removido
			return result