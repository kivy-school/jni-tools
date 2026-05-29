from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlphabetIndexer"]

class AlphabetIndexer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/AlphabetIndexer"
    __javaconstructor__ = [("(Landroid/database/Cursor;ILjava/lang/CharSequence;)V", False)]
    getPositionForSection = JavaMethod("(I)I")
    getSectionForPosition = JavaMethod("(I)I")
    getSections = JavaMethod("()[Ljava/lang/Object;")
    setCursor = JavaMethod("(Landroid/database/Cursor;)V")
    onChanged = JavaMethod("()V")
    onInvalidated = JavaMethod("()V")