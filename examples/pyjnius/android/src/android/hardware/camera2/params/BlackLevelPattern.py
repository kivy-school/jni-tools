from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BlackLevelPattern"]

class BlackLevelPattern(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/BlackLevelPattern"
    __javaconstructor__ = [("([I)V", False)]
    COUNT = JavaStaticField("I")
    getOffsetForIndex = JavaMethod("(II)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    copyTo = JavaMethod("([II)V")