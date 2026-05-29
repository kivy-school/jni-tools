from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectStreamClass"]

class ObjectStreamClass(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ObjectStreamClass"
    NO_FIELDS = JavaStaticField("[Ljava/io/ObjectStreamField;")
    getName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    lookup = JavaStaticMethod("(Ljava/lang/Class;)Ljava/io/ObjectStreamClass;")
    getFields = JavaMethod("()[Ljava/io/ObjectStreamField;")
    getField = JavaMethod("(Ljava/lang/String;)Ljava/io/ObjectStreamField;")
    getSerialVersionUID = JavaMethod("()J")
    lookupAny = JavaStaticMethod("(Ljava/lang/Class;)Ljava/io/ObjectStreamClass;")
    forClass = JavaMethod("()Ljava/lang/Class;")