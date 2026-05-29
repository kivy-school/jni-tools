from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ListFragment"]

class ListFragment(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/ListFragment"
    __javaconstructor__ = [("()V", False)]
    TRIM_MEMORY_BACKGROUND = JavaStaticField("I")
    TRIM_MEMORY_COMPLETE = JavaStaticField("I")
    TRIM_MEMORY_MODERATE = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_CRITICAL = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_LOW = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_MODERATE = JavaStaticField("I")
    TRIM_MEMORY_UI_HIDDEN = JavaStaticField("I")
    onViewCreated = JavaMethod("(Landroid/view/View;Landroid/os/Bundle;)V")
    onDestroyView = JavaMethod("()V")
    onListItemClick = JavaMethod("(Landroid/widget/ListView;Landroid/view/View;IJ)V")
    getListAdapter = JavaMethod("()Landroid/widget/ListAdapter;")
    setListAdapter = JavaMethod("(Landroid/widget/ListAdapter;)V")
    setListShown = JavaMethod("(Z)V")
    setEmptyText = JavaMethod("(Ljava/lang/CharSequence;)V")
    setListShownNoAnimation = JavaMethod("(Z)V")
    getListView = JavaMethod("()Landroid/widget/ListView;")
    getSelectedItemId = JavaMethod("()J")
    getSelectedItemPosition = JavaMethod("()I")
    setSelection = JavaMethod("(I)V")
    onCreateView = JavaMethod("(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Landroid/os/Bundle;)Landroid/view/View;")