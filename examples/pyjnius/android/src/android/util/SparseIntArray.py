from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SparseIntArray"]

class SparseIntArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/SparseIntArray"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    size = JavaMethod("()I")
    put = JavaMethod("(II)V")
    toString = JavaMethod("()Ljava/lang/String;")
    append = JavaMethod("(II)V")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/util/SparseIntArray;", False, False)])
    clear = JavaMethod("()V")
    get = JavaMultipleMethod([("(II)I", False, False), ("(I)I", False, False)])
    delete = JavaMethod("(I)V")
    setValueAt = JavaMethod("(II)V")
    keyAt = JavaMethod("(I)I")
    valueAt = JavaMethod("(I)I")
    indexOfKey = JavaMethod("(I)I")
    removeAt = JavaMethod("(I)V")
    indexOfValue = JavaMethod("(I)I")