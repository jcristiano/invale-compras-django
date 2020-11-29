from django.contrib import admin
from treenode.admin import TreeNodeModelAdmin
from treenode.forms import TreeNodeForm
from controle.models import Categoria, Compra, Local, ItemCompra


class CategoryAdmin(TreeNodeModelAdmin):
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION
    form = TreeNodeForm

admin.site.register(Categoria, CategoryAdmin)
admin.site.register(Compra)
admin.site.register(Local)
admin.site.register(ItemCompra)