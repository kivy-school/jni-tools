from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Guard"]

class Guard(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Guard"
    checkGuard = JavaMethod("(Ljava/lang/Object;)V")