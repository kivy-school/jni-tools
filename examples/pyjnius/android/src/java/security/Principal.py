from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Principal"]

class Principal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Principal"
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    implies = JavaMethod("(Ljavax/security/auth/Subject;)Z")