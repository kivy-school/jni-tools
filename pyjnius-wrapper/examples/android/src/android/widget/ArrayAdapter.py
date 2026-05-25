from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArrayAdapter"]

class ArrayAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ArrayAdapter"
    __javaconstructor__ = [("(Landroid/content/Context;I)V", False), ("(Landroid/content/Context;II)V", False), ("(Landroid/content/Context;I[Ljava/lang/Object;)V", False), ("(Landroid/content/Context;II[Ljava/lang/Object;)V", False), ("(Landroid/content/Context;ILjava/util/List;)V", False), ("(Landroid/content/Context;IILjava/util/List;)V", False)]
    add = JavaMethod("(Ljava/lang/Object;)V")
    addAll = JavaMultipleMethod([("(Ljava/util/Collection;)V", False, False), ("([Ljava/lang/Object;)V", False, True)])
    insert = JavaMethod("(Ljava/lang/Object;I)V")
    remove = JavaMethod("(Ljava/lang/Object;)V")
    clear = JavaMethod("()V")
    sort = JavaMethod("(Ljava/util/Comparator;)V")
    notifyDataSetChanged = JavaMethod("()V")
    setNotifyOnChange = JavaMethod("(Z)V")
    getContext = JavaMethod("()Landroid/content/Context;")
    getCount = JavaMethod("()I")
    getItem = JavaMethod("(I)Ljava/lang/Object;")
    getPosition = JavaMethod("(Ljava/lang/Object;)I")
    getItemId = JavaMethod("(I)J")
    getView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    setDropDownViewResource = JavaMethod("(I)V")
    setDropDownViewTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    getDropDownViewTheme = JavaMethod("()Landroid/content/res/Resources$Theme;")
    getDropDownView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    createFromResource = JavaStaticMethod("(Landroid/content/Context;II)Landroid/widget/ArrayAdapter;")
    getFilter = JavaMethod("()Landroid/widget/Filter;")
    getAutofillOptions = JavaMethod("()[Ljava/lang/CharSequence;")