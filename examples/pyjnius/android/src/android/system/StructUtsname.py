from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StructUtsname"]

class StructUtsname(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/system/StructUtsname"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    machine = JavaField("Ljava/lang/String;")
    nodename = JavaField("Ljava/lang/String;")
    release = JavaField("Ljava/lang/String;")
    sysname = JavaField("Ljava/lang/String;")
    version = JavaField("Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")