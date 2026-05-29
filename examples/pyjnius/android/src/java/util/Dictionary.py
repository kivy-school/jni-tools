from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Dictionary"]

class Dictionary(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Dictionary"
    __javaconstructor__ = [("()V", False)]
    remove = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    size = JavaMethod("()I")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    isEmpty = JavaMethod("()Z")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    elements = JavaMethod("()Ljava/util/Enumeration;")
    keys = JavaMethod("()Ljava/util/Enumeration;")