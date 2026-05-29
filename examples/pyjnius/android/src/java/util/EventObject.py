from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EventObject"]

class EventObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/EventObject"
    __javaconstructor__ = [("(Ljava/lang/Object;)V", False)]
    source = JavaField("Ljava/lang/Object;")
    getSource = JavaMethod("()Ljava/lang/Object;")
    toString = JavaMethod("()Ljava/lang/String;")