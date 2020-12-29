from django import forms
from treenode.forms import TreeNodeForm
from controle.models import Categoria


class CategoriaForm(TreeNodeForm):
    class Meta:
        model = Categoria
        fields = ['nome']
