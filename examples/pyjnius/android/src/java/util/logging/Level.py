from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Level"]

class Level(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/Level"
    OFF = JavaStaticField("Ljava/util/logging/Level;")
    SEVERE = JavaStaticField("Ljava/util/logging/Level;")
    WARNING = JavaStaticField("Ljava/util/logging/Level;")
    INFO = JavaStaticField("Ljava/util/logging/Level;")
    CONFIG = JavaStaticField("Ljava/util/logging/Level;")
    FINE = JavaStaticField("Ljava/util/logging/Level;")
    FINER = JavaStaticField("Ljava/util/logging/Level;")
    FINEST = JavaStaticField("Ljava/util/logging/Level;")
    ALL = JavaStaticField("Ljava/util/logging/Level;")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    intValue = JavaMethod("()I")
    parse = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/logging/Level;")
    getLocalizedName = JavaMethod("()Ljava/lang/String;")
    getResourceBundleName = JavaMethod("()Ljava/lang/String;")