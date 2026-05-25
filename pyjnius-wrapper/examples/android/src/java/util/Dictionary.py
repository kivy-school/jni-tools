from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Dictionary"]

class Dictionary(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Dictionary"
    __javaconstructor__ = [("()V", False)]
    size = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    keys = JavaMethod("()Ljava/util/Enumeration;")
    elements = JavaMethod("()Ljava/util/Enumeration;")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    remove = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")