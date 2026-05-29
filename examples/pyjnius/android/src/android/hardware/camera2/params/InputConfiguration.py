from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputConfiguration"]

class InputConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/InputConfiguration"
    __javaconstructor__ = [("(Ljava/util/Collection;I)V", False), ("(III)V", False)]
    isMultiResolution = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    getWidth = JavaMethod("()I")
    getFormat = JavaMethod("()I")