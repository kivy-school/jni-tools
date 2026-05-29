from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongSparseArray"]

class LongSparseArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/LongSparseArray"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    clone = JavaMethod("()Landroid/util/LongSparseArray;")
    get = JavaMultipleMethod([("(J)Ljava/lang/Object;", False, False), ("(JLjava/lang/Object;)Ljava/lang/Object;", False, False)])
    delete = JavaMethod("(J)V")
    remove = JavaMethod("(J)V")
    removeAt = JavaMethod("(I)V")
    put = JavaMethod("(JLjava/lang/Object;)V")
    size = JavaMethod("()I")
    keyAt = JavaMethod("(I)J")
    valueAt = JavaMethod("(I)Ljava/lang/Object;")
    setValueAt = JavaMethod("(ILjava/lang/Object;)V")
    indexOfKey = JavaMethod("(J)I")
    indexOfValue = JavaMethod("(Ljava/lang/Object;)I")
    clear = JavaMethod("()V")
    append = JavaMethod("(JLjava/lang/Object;)V")
    toString = JavaMethod("()Ljava/lang/String;")