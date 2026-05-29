from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Filter"]

class Filter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Filter"
    __javaconstructor__ = [("()V", False)]
    filter = JavaMultipleMethod([("(Ljava/lang/CharSequence;Landroid/widget/Filter$FilterListener;)V", False, False), ("(Ljava/lang/CharSequence;)V", False, False)])
    convertResultToString = JavaMethod("(Ljava/lang/Object;)Ljava/lang/CharSequence;")

    class FilterListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/Filter$FilterListener"
        onFilterComplete = JavaMethod("(I)V")