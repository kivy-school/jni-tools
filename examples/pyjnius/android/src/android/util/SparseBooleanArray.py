from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SparseBooleanArray"]

class SparseBooleanArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/SparseBooleanArray"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    clone = JavaMethod("()Landroid/util/SparseBooleanArray;")
    get = JavaMultipleMethod([("(I)Z", False, False), ("(IZ)Z", False, False)])
    delete = JavaMethod("(I)V")
    removeAt = JavaMethod("(I)V")
    put = JavaMethod("(IZ)V")
    size = JavaMethod("()I")
    keyAt = JavaMethod("(I)I")
    valueAt = JavaMethod("(I)Z")
    setValueAt = JavaMethod("(IZ)V")
    indexOfKey = JavaMethod("(I)I")
    indexOfValue = JavaMethod("(Z)I")
    clear = JavaMethod("()V")
    append = JavaMethod("(IZ)V")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")