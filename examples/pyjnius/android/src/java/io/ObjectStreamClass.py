from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectStreamClass"]

class ObjectStreamClass(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ObjectStreamClass"
    NO_FIELDS = JavaStaticField("[Ljava/io/ObjectStreamField;")
    lookup = JavaStaticMethod("(Ljava/lang/Class;)Ljava/io/ObjectStreamClass;")
    lookupAny = JavaStaticMethod("(Ljava/lang/Class;)Ljava/io/ObjectStreamClass;")
    getName = JavaMethod("()Ljava/lang/String;")
    getSerialVersionUID = JavaMethod("()J")
    forClass = JavaMethod("()Ljava/lang/Class;")
    getFields = JavaMethod("()[Ljava/io/ObjectStreamField;")
    getField = JavaMethod("(Ljava/lang/String;)Ljava/io/ObjectStreamField;")
    toString = JavaMethod("()Ljava/lang/String;")