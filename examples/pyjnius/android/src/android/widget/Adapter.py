from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Adapter"]

class Adapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Adapter"
    IGNORE_ITEM_VIEW_TYPE = JavaStaticField("I")
    NO_SELECTION = JavaStaticField("I")
    isEmpty = JavaMethod("()Z")
    getCount = JavaMethod("()I")
    getAutofillOptions = JavaMethod("()[Ljava/lang/CharSequence;")
    getItem = JavaMethod("(I)Ljava/lang/Object;")
    getItemId = JavaMethod("(I)J")
    getItemViewType = JavaMethod("(I)I")
    getView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    getViewTypeCount = JavaMethod("()I")
    hasStableIds = JavaMethod("()Z")
    registerDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    unregisterDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")