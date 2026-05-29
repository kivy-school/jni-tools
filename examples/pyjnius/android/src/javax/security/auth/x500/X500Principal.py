from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X500Principal"]

class X500Principal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/x500/X500Principal"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/util/Map;)V", False), ("([B)V", False)]
    RFC1779 = JavaStaticField("Ljava/lang/String;")
    RFC2253 = JavaStaticField("Ljava/lang/String;")
    CANONICAL = JavaStaticField("Ljava/lang/String;")
    getName = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/util/Map;)Ljava/lang/String;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getEncoded = JavaMethod("()[B")