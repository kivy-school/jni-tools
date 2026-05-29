from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SparseBooleanArray"]

class SparseBooleanArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/SparseBooleanArray"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    size = JavaMethod("()I")
    put = JavaMethod("(IZ)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    append = JavaMethod("(IZ)V")
    hashCode = JavaMethod("()I")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/util/SparseBooleanArray;", False, False)])
    clear = JavaMethod("()V")
    get = JavaMultipleMethod([("(IZ)Z", False, False), ("(I)Z", False, False)])
    delete = JavaMethod("(I)V")
    setValueAt = JavaMethod("(IZ)V")
    keyAt = JavaMethod("(I)I")
    valueAt = JavaMethod("(I)Z")
    indexOfKey = JavaMethod("(I)I")
    removeAt = JavaMethod("(I)V")
    indexOfValue = JavaMethod("(Z)I")