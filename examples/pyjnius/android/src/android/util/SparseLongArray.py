from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SparseLongArray"]

class SparseLongArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/SparseLongArray"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    size = JavaMethod("()I")
    put = JavaMethod("(IJ)V")
    toString = JavaMethod("()Ljava/lang/String;")
    append = JavaMethod("(IJ)V")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/util/SparseLongArray;", False, False)])
    clear = JavaMethod("()V")
    get = JavaMultipleMethod([("(IJ)J", False, False), ("(I)J", False, False)])
    delete = JavaMethod("(I)V")
    keyAt = JavaMethod("(I)I")
    valueAt = JavaMethod("(I)J")
    indexOfKey = JavaMethod("(I)I")
    removeAt = JavaMethod("(I)V")
    indexOfValue = JavaMethod("(J)I")