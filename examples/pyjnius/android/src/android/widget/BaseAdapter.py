from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseAdapter"]

class BaseAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/BaseAdapter"
    __javaconstructor__ = [("()V", False)]
    IGNORE_ITEM_VIEW_TYPE = JavaStaticField("I")
    NO_SELECTION = JavaStaticField("I")
    isEmpty = JavaMethod("()Z")
    isEnabled = JavaMethod("(I)Z")
    setAutofillOptions = JavaMethod("([Ljava/lang/CharSequence;)V", varargs=True)
    notifyDataSetChanged = JavaMethod("()V")
    notifyDataSetInvalidated = JavaMethod("()V")
    getDropDownView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    areAllItemsEnabled = JavaMethod("()Z")
    getAutofillOptions = JavaMethod("()[Ljava/lang/CharSequence;")
    getItemViewType = JavaMethod("(I)I")
    getViewTypeCount = JavaMethod("()I")
    hasStableIds = JavaMethod("()Z")
    registerDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    unregisterDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")