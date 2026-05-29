from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Compiler"]

class Compiler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Compiler"
    compileClass = JavaStaticMethod("(Ljava/lang/Class;)Z")
    compileClasses = JavaStaticMethod("(Ljava/lang/String;)Z")
    command = JavaStaticMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    enable = JavaStaticMethod("()V")
    disable = JavaStaticMethod("()V")