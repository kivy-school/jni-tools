from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Size"]

class Size(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Size"
    __javaconstructor__ = [("(II)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    getWidth = JavaMethod("()I")
    parseSize = JavaStaticMethod("(Ljava/lang/String;)Landroid/util/Size;")