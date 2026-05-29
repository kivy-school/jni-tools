from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyRep"]

class KeyRep(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyRep"
    __javaconstructor__ = [("(Ljava/security/KeyRep$Type;Ljava/lang/String;Ljava/lang/String;[B)V", False)]

    class Type(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyRep$Type"
        SECRET = JavaStaticField("Ljava/security/KeyRep$Type;")
        PUBLIC = JavaStaticField("Ljava/security/KeyRep$Type;")
        PRIVATE = JavaStaticField("Ljava/security/KeyRep$Type;")
        values = JavaStaticMethod("()[Ljava/security/KeyRep$Type;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/KeyRep$Type;")
        SECRET = JavaStaticField("Ljava/security/KeyRep$Type;")
        PUBLIC = JavaStaticField("Ljava/security/KeyRep$Type;")
        PRIVATE = JavaStaticField("Ljava/security/KeyRep$Type;")