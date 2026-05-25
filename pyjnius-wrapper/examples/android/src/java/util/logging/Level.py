from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Level"]

class Level(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/Level"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False), ("(Ljava/lang/String;ILjava/lang/String;)V", False)]
    ALL = JavaStaticField("Ljava/util/logging/Level;")
    CONFIG = JavaStaticField("Ljava/util/logging/Level;")
    FINE = JavaStaticField("Ljava/util/logging/Level;")
    FINER = JavaStaticField("Ljava/util/logging/Level;")
    FINEST = JavaStaticField("Ljava/util/logging/Level;")
    INFO = JavaStaticField("Ljava/util/logging/Level;")
    OFF = JavaStaticField("Ljava/util/logging/Level;")
    SEVERE = JavaStaticField("Ljava/util/logging/Level;")
    WARNING = JavaStaticField("Ljava/util/logging/Level;")
    getResourceBundleName = JavaMethod("()Ljava/lang/String;")
    getName = JavaMethod("()Ljava/lang/String;")
    getLocalizedName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    intValue = JavaMethod("()I")
    parse = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/logging/Level;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")