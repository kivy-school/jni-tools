from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjLongConsumer"]

class ObjLongConsumer(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ObjLongConsumer"
    accept = JavaMethod("(Ljava/lang/Object;J)V")