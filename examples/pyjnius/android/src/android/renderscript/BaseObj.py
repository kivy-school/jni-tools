from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseObj"]

class BaseObj(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/BaseObj"
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    setName = JavaMethod("(Ljava/lang/String;)V")
    destroy = JavaMethod("()V")