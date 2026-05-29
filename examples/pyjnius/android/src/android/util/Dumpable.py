from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Dumpable"]

class Dumpable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Dumpable"
    getDumpableName = JavaMethod("()Ljava/lang/String;")
    dump = JavaMethod("(Ljava/io/PrintWriter;[Ljava/lang/String;)V")