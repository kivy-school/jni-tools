from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SparseArray"]

class SparseArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/SparseArray"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    clone = JavaMethod("()Landroid/util/SparseArray;")
    contains = JavaMethod("(I)Z")
    get = JavaMultipleMethod([("(I)Ljava/lang/Object;", False, False), ("(ILjava/lang/Object;)Ljava/lang/Object;", False, False)])
    delete = JavaMethod("(I)V")
    remove = JavaMethod("(I)V")
    removeAt = JavaMethod("(I)V")
    removeAtRange = JavaMethod("(II)V")
    set = JavaMethod("(ILjava/lang/Object;)V")
    put = JavaMethod("(ILjava/lang/Object;)V")
    size = JavaMethod("()I")
    keyAt = JavaMethod("(I)I")
    valueAt = JavaMethod("(I)Ljava/lang/Object;")
    setValueAt = JavaMethod("(ILjava/lang/Object;)V")
    indexOfKey = JavaMethod("(I)I")
    indexOfValue = JavaMethod("(Ljava/lang/Object;)I")
    clear = JavaMethod("()V")
    append = JavaMethod("(ILjava/lang/Object;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    contentEquals = JavaMethod("(Landroid/util/SparseArray;)Z")
    contentHashCode = JavaMethod("()I")