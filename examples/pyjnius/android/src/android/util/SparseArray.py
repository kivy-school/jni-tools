from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SparseArray"]

class SparseArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/SparseArray"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    remove = JavaMethod("(I)V")
    size = JavaMethod("()I")
    put = JavaMethod("(ILjava/lang/Object;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    append = JavaMethod("(ILjava/lang/Object;)V")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/util/SparseArray;", False, False)])
    clear = JavaMethod("()V")
    contentEquals = JavaMethod("(Landroid/util/SparseArray;)Z")
    get = JavaMultipleMethod([("(I)Ljava/lang/Object;", False, False), ("(ILjava/lang/Object;)Ljava/lang/Object;", False, False)])
    contains = JavaMethod("(I)Z")
    set = JavaMethod("(ILjava/lang/Object;)V")
    delete = JavaMethod("(I)V")
    removeAtRange = JavaMethod("(II)V")
    setValueAt = JavaMethod("(ILjava/lang/Object;)V")
    keyAt = JavaMethod("(I)I")
    valueAt = JavaMethod("(I)Ljava/lang/Object;")
    indexOfKey = JavaMethod("(I)I")
    removeAt = JavaMethod("(I)V")
    indexOfValue = JavaMethod("(Ljava/lang/Object;)I")
    contentHashCode = JavaMethod("()I")