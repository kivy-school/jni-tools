from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjIntConsumer"]

class ObjIntConsumer(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ObjIntConsumer"
    accept = JavaMethod("(Ljava/lang/Object;I)V")