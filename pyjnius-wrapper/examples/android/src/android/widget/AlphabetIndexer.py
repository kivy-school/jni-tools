from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlphabetIndexer"]

class AlphabetIndexer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/AlphabetIndexer"
    __javaconstructor__ = [("(Landroid/database/Cursor;ILjava/lang/CharSequence;)V", False)]
    mAlphabet = JavaField("Ljava/lang/CharSequence;")
    mColumnIndex = JavaField("I")
    mDataCursor = JavaField("Landroid/database/Cursor;")
    getSections = JavaMethod("()[Ljava/lang/Object;")
    setCursor = JavaMethod("(Landroid/database/Cursor;)V")
    compare = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)I")
    getPositionForSection = JavaMethod("(I)I")
    getSectionForPosition = JavaMethod("(I)I")
    onChanged = JavaMethod("()V")
    onInvalidated = JavaMethod("()V")