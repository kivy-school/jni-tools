from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ListFragment"]

class ListFragment(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/ListFragment"
    __javaconstructor__ = [("()V", False)]
    onCreateView = JavaMethod("(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Landroid/os/Bundle;)Landroid/view/View;")
    onViewCreated = JavaMethod("(Landroid/view/View;Landroid/os/Bundle;)V")
    onDestroyView = JavaMethod("()V")
    onListItemClick = JavaMethod("(Landroid/widget/ListView;Landroid/view/View;IJ)V")
    setListAdapter = JavaMethod("(Landroid/widget/ListAdapter;)V")
    setSelection = JavaMethod("(I)V")
    getSelectedItemPosition = JavaMethod("()I")
    getSelectedItemId = JavaMethod("()J")
    getListView = JavaMethod("()Landroid/widget/ListView;")
    setEmptyText = JavaMethod("(Ljava/lang/CharSequence;)V")
    setListShown = JavaMethod("(Z)V")
    setListShownNoAnimation = JavaMethod("(Z)V")
    getListAdapter = JavaMethod("()Landroid/widget/ListAdapter;")