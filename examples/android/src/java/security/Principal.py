from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Principal"]

class Principal(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Principal"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getName = JavaMethod("()Ljava/lang/String;")
    implies = JavaMethod("(Ljavax/security/auth/Subject;)Z")