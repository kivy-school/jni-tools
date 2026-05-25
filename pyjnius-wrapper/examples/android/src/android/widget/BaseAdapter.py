from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseAdapter"]

class BaseAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/BaseAdapter"
    __javaconstructor__ = [("()V", False)]
    hasStableIds = JavaMethod("()Z")
    registerDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    unregisterDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    notifyDataSetChanged = JavaMethod("()V")
    notifyDataSetInvalidated = JavaMethod("()V")
    areAllItemsEnabled = JavaMethod("()Z")
    isEnabled = JavaMethod("(I)Z")
    getDropDownView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    getItemViewType = JavaMethod("(I)I")
    getViewTypeCount = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    getAutofillOptions = JavaMethod("()[Ljava/lang/CharSequence;")
    setAutofillOptions = JavaMethod("([Ljava/lang/CharSequence;)V", varargs=True)