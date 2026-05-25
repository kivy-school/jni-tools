from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Filter"]

class Filter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Filter"
    __javaconstructor__ = [("()V", False)]
    filter = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(Ljava/lang/CharSequence;Landroid/widget/Filter$FilterListener;)V", False, False)])
    performFiltering = JavaMethod("(Ljava/lang/CharSequence;)Landroid/widget/Filter$FilterResults;")
    publishResults = JavaMethod("(Ljava/lang/CharSequence;Landroid/widget/Filter$FilterResults;)V")
    convertResultToString = JavaMethod("(Ljava/lang/Object;)Ljava/lang/CharSequence;")

    class FilterListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/Filter/FilterListener"
        onFilterComplete = JavaMethod("(I)V")

    class FilterResults(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/Filter/FilterResults"
        __javaconstructor__ = [("()V", False)]
        count = JavaField("I")
        values = JavaField("Ljava/lang/Object;")