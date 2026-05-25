from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SparseIntArray"]

class SparseIntArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/SparseIntArray"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    clone = JavaMethod("()Landroid/util/SparseIntArray;")
    get = JavaMultipleMethod([("(I)I", False, False), ("(II)I", False, False)])
    delete = JavaMethod("(I)V")
    removeAt = JavaMethod("(I)V")
    put = JavaMethod("(II)V")
    size = JavaMethod("()I")
    keyAt = JavaMethod("(I)I")
    valueAt = JavaMethod("(I)I")
    setValueAt = JavaMethod("(II)V")
    indexOfKey = JavaMethod("(I)I")
    indexOfValue = JavaMethod("(I)I")
    clear = JavaMethod("()V")
    append = JavaMethod("(II)V")
    toString = JavaMethod("()Ljava/lang/String;")