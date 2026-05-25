from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Guard"]

class Guard(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Guard"
    checkGuard = JavaMethod("(Ljava/lang/Object;)V")