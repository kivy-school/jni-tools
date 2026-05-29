from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongSparseArray"]

class LongSparseArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/LongSparseArray"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    remove = JavaMethod("(J)V")
    size = JavaMethod("()I")
    put = JavaMethod("(JLjava/lang/Object;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    append = JavaMethod("(JLjava/lang/Object;)V")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/util/LongSparseArray;", False, False)])
    clear = JavaMethod("()V")
    get = JavaMultipleMethod([("(JLjava/lang/Object;)Ljava/lang/Object;", False, False), ("(J)Ljava/lang/Object;", False, False)])
    delete = JavaMethod("(J)V")
    setValueAt = JavaMethod("(ILjava/lang/Object;)V")
    keyAt = JavaMethod("(I)J")
    valueAt = JavaMethod("(I)Ljava/lang/Object;")
    indexOfKey = JavaMethod("(J)I")
    removeAt = JavaMethod("(I)V")
    indexOfValue = JavaMethod("(Ljava/lang/Object;)I")