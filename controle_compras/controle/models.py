from django.db import models
from treenode.models import TreeNodeModel


class Category(TreeNodeModel):
    treenode_display_field = 'name'
    name = models.CharField(db_column='STR_NAME', null=False, blank=False, max_length=50)

    class Meta(TreeNodeModel.Meta):
        db_table = 'TBL_CATEGORIES'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
