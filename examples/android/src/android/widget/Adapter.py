from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Adapter"]

class Adapter(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Adapter"
    IGNORE_ITEM_VIEW_TYPE = JavaStaticField("I")
    NO_SELECTION = JavaStaticField("I")
    registerDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    unregisterDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    getCount = JavaMethod("()I")
    getItem = JavaMethod("(I)Ljava/lang/Object;")
    getItemId = JavaMethod("(I)J")
    hasStableIds = JavaMethod("()Z")
    getView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    getItemViewType = JavaMethod("(I)I")
    getViewTypeCount = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    getAutofillOptions = JavaMethod("()[Ljava/lang/CharSequence;")