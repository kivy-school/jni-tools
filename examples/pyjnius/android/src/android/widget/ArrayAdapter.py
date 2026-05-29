from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArrayAdapter"]

class ArrayAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ArrayAdapter"
    __javaconstructor__ = [("(Landroid/content/Context;I[Ljava/lang/Object;)V", False), ("(Landroid/content/Context;ILjava/util/List;)V", False), ("(Landroid/content/Context;II[Ljava/lang/Object;)V", False), ("(Landroid/content/Context;I)V", False), ("(Landroid/content/Context;II)V", False), ("(Landroid/content/Context;IILjava/util/List;)V", False)]
    IGNORE_ITEM_VIEW_TYPE = JavaStaticField("I")
    NO_SELECTION = JavaStaticField("I")
    remove = JavaMethod("(Ljava/lang/Object;)V")
    sort = JavaMethod("(Ljava/util/Comparator;)V")
    insert = JavaMethod("(Ljava/lang/Object;I)V")
    clear = JavaMethod("()V")
    add = JavaMethod("(Ljava/lang/Object;)V")
    addAll = JavaMultipleMethod([("(Ljava/util/Collection;)V", False, False), ("([Ljava/lang/Object;)V", False, True)])
    getCount = JavaMethod("()I")
    getContext = JavaMethod("()Landroid/content/Context;")
    getPosition = JavaMethod("(Ljava/lang/Object;)I")
    notifyDataSetChanged = JavaMethod("()V")
    getDropDownView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    createFromResource = JavaStaticMethod("(Landroid/content/Context;II)Landroid/widget/ArrayAdapter;")
    setNotifyOnChange = JavaMethod("(Z)V")
    getAutofillOptions = JavaMethod("()[Ljava/lang/CharSequence;")
    getItem = JavaMethod("(I)Ljava/lang/Object;")
    getItemId = JavaMethod("(I)J")
    getView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    getDropDownViewTheme = JavaMethod("()Landroid/content/res/Resources$Theme;")
    getFilter = JavaMethod("()Landroid/widget/Filter;")
    setDropDownViewResource = JavaMethod("(I)V")
    setDropDownViewTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")