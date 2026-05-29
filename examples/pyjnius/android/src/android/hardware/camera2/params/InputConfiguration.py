from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputConfiguration"]

class InputConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/InputConfiguration"
    __javaconstructor__ = [("(III)V", False), ("(Ljava/util/Collection;I)V", False)]
    getWidth = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    getFormat = JavaMethod("()I")
    isMultiResolution = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")