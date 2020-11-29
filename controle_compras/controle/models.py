from django.db import models
from treenode.models import TreeNodeModel
from django.utils import timezone


class Conta(models.Model):
    nome = models.CharField(db_column='STR_NOME', null=False, blank=False, unique=True, max_length=200)

    class Meta:
        db_table = 'TBL_CONTA'
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'


class Categoria(TreeNodeModel):
    treenode_display_field = 'name'
    nome = models.CharField(db_column='STR_NOME', null=False, blank=False, max_length=50)

    class Meta(TreeNodeModel.Meta):
        db_table = 'TBL_CATEGORIAS'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Local(models.Model):
    nome = models.CharField(db_column='STR_NOME', null=False, blank=False, max_length=100)
    detalhe = models.TextField(db_column='STR_DETALHES')

    class Meta:
        db_table = 'TBL_LOCAL'
        verbose_name = 'Local'
        verbose_name_plural = 'Locais'

    def __str__(self):
        return self.nome


class Compra(models.Model):
    resumo = models.CharField(db_column='STR_RESUMO', null=False, blank=False, max_length=500)
    conta = models.ForeignKey(Conta, null=False, blank=False, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, null=False, blank=False, on_delete=models.CASCADE)
    data = models.DateField(db_column='DT_DATA_COMPRA', null=False, blank=False, default=timezone.now)

    class Meta:
        db_table = 'TBL_COMPRA'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def __str__(self):
        return self.resumo


class ItemCompra(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, null=True)
    item = models.CharField(db_column='STR_ITEM_COMPRA', max_length=500, null=False, blank=False)
    quantidade = models.IntegerField(db_column='N_QTDE', default=1)
    desconto = models.FloatField(db_column='D_DESCONTO', default=0.0)
    valor = models.FloatField(db_column='D_VALOR', default=0.0)
    observacao = models.TextField(db_column='STR_OBSERVACAO')

    class Meta:
        db_table = 'TBL_ITEM_COMPRA'
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return self.item

    @property
    def valor_pago(self):
        return self.quantidade * (self.valor - self.desconto)
