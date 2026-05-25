from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HeaderViewListAdapter"]

class HeaderViewListAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/HeaderViewListAdapter"
    __javaconstructor__ = [("(Ljava/util/ArrayList;Ljava/util/ArrayList;Landroid/widget/ListAdapter;)V", False)]
    getHeadersCount = JavaMethod("()I")
    getFootersCount = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    removeHeader = JavaMethod("(Landroid/view/View;)Z")
    removeFooter = JavaMethod("(Landroid/view/View;)Z")
    getCount = JavaMethod("()I")
    areAllItemsEnabled = JavaMethod("()Z")
    isEnabled = JavaMethod("(I)Z")
    getItem = JavaMethod("(I)Ljava/lang/Object;")
    getItemId = JavaMethod("(I)J")
    hasStableIds = JavaMethod("()Z")
    getView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    getItemViewType = JavaMethod("(I)I")
    getViewTypeCount = JavaMethod("()I")
    registerDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    unregisterDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    getFilter = JavaMethod("()Landroid/widget/Filter;")
    getWrappedAdapter = JavaMethod("()Landroid/widget/ListAdapter;")