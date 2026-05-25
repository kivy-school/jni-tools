from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseObj"]

class BaseObj(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/BaseObj"
    setName = JavaMethod("(Ljava/lang/String;)V")
    getName = JavaMethod("()Ljava/lang/String;")
    finalize = JavaMethod("()V")
    destroy = JavaMethod("()V")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")