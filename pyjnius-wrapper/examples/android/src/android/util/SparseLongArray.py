from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SparseLongArray"]

class SparseLongArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/SparseLongArray"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    clone = JavaMethod("()Landroid/util/SparseLongArray;")
    get = JavaMultipleMethod([("(I)J", False, False), ("(IJ)J", False, False)])
    delete = JavaMethod("(I)V")
    removeAt = JavaMethod("(I)V")
    put = JavaMethod("(IJ)V")
    size = JavaMethod("()I")
    keyAt = JavaMethod("(I)I")
    valueAt = JavaMethod("(I)J")
    indexOfKey = JavaMethod("(I)I")
    indexOfValue = JavaMethod("(J)I")
    clear = JavaMethod("()V")
    append = JavaMethod("(IJ)V")
    toString = JavaMethod("()Ljava/lang/String;")