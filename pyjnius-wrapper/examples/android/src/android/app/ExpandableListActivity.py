from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExpandableListActivity"]

class ExpandableListActivity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/ExpandableListActivity"
    __javaconstructor__ = [("()V", False)]
    onCreateContextMenu = JavaMethod("(Landroid/view/ContextMenu;Landroid/view/View;Landroid/view/ContextMenu$ContextMenuInfo;)V")
    onChildClick = JavaMethod("(Landroid/widget/ExpandableListView;Landroid/view/View;IIJ)Z")
    onGroupCollapse = JavaMethod("(I)V")
    onGroupExpand = JavaMethod("(I)V")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Bundle;)V")
    onContentChanged = JavaMethod("()V")
    setListAdapter = JavaMethod("(Landroid/widget/ExpandableListAdapter;)V")
    getExpandableListView = JavaMethod("()Landroid/widget/ExpandableListView;")
    getExpandableListAdapter = JavaMethod("()Landroid/widget/ExpandableListAdapter;")
    getSelectedId = JavaMethod("()J")
    getSelectedPosition = JavaMethod("()J")
    setSelectedChild = JavaMethod("(IIZ)Z")
    setSelectedGroup = JavaMethod("(I)V")