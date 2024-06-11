from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao
    
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self, desconto):
        desconto_item = float(desconto) / 100
        valor_com_desconto = self._preco - (self._preco * desconto_item)
        self._preco = round(valor_com_desconto,3)