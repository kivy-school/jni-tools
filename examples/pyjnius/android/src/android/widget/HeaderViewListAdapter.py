from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HeaderViewListAdapter"]

class HeaderViewListAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/HeaderViewListAdapter"
    __javaconstructor__ = [("(Ljava/util/ArrayList;Ljava/util/ArrayList;Landroid/widget/ListAdapter;)V", False)]
    IGNORE_ITEM_VIEW_TYPE = JavaStaticField("I")
    NO_SELECTION = JavaStaticField("I")
    isEmpty = JavaMethod("()Z")
    isEnabled = JavaMethod("(I)Z")
    getCount = JavaMethod("()I")
    getFootersCount = JavaMethod("()I")
    getHeadersCount = JavaMethod("()I")
    removeFooter = JavaMethod("(Landroid/view/View;)Z")
    removeHeader = JavaMethod("(Landroid/view/View;)Z")
    getWrappedAdapter = JavaMethod("()Landroid/widget/ListAdapter;")
    areAllItemsEnabled = JavaMethod("()Z")
    getItem = JavaMethod("(I)Ljava/lang/Object;")
    getItemId = JavaMethod("(I)J")
    getItemViewType = JavaMethod("(I)I")
    getView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    getViewTypeCount = JavaMethod("()I")
    hasStableIds = JavaMethod("()Z")
    registerDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    unregisterDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    getFilter = JavaMethod("()Landroid/widget/Filter;")