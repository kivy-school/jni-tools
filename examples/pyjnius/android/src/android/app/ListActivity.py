from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ListActivity"]

class ListActivity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/ListActivity"
    __javaconstructor__ = [("()V", False)]
    onListItemClick = JavaMethod("(Landroid/widget/ListView;Landroid/view/View;IJ)V")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Bundle;)V")
    onDestroy = JavaMethod("()V")
    onContentChanged = JavaMethod("()V")
    setListAdapter = JavaMethod("(Landroid/widget/ListAdapter;)V")
    setSelection = JavaMethod("(I)V")
    getSelectedItemPosition = JavaMethod("()I")
    getSelectedItemId = JavaMethod("()J")
    getListView = JavaMethod("()Landroid/widget/ListView;")
    getListAdapter = JavaMethod("()Landroid/widget/ListAdapter;")