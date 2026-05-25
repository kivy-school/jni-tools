from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BlackLevelPattern"]

class BlackLevelPattern(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/BlackLevelPattern"
    __javaconstructor__ = [("([I)V", False)]
    COUNT = JavaStaticField("I")
    getOffsetForIndex = JavaMethod("(II)I")
    copyTo = JavaMethod("([II)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")