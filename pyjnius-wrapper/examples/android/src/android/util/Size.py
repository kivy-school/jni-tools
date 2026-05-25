from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Size"]

class Size(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Size"
    __javaconstructor__ = [("(II)V", False)]
    getWidth = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    parseSize = JavaStaticMethod("(Ljava/lang/String;)Landroid/util/Size;")
    hashCode = JavaMethod("()I")