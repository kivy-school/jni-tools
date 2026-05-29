from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GuardedObject"]

class GuardedObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/GuardedObject"
    __javaconstructor__ = [("(Ljava/lang/Object;Ljava/security/Guard;)V", False)]
    getObject = JavaMethod("()Ljava/lang/Object;")