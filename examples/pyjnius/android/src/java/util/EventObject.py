from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EventObject"]

class EventObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/EventObject"
    __javaconstructor__ = [("(Ljava/lang/Object;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    getSource = JavaMethod("()Ljava/lang/Object;")