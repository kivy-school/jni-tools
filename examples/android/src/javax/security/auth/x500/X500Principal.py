from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X500Principal"]

class X500Principal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/x500/X500Principal"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/util/Map;)V", False), ("([B)V", False), ("(Ljava/io/InputStream;)V", False)]
    CANONICAL = JavaStaticField("Ljava/lang/String;")
    RFC1779 = JavaStaticField("Ljava/lang/String;")
    RFC2253 = JavaStaticField("Ljava/lang/String;")
    getName = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/util/Map;)Ljava/lang/String;", False, False)])
    getEncoded = JavaMethod("()[B")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")