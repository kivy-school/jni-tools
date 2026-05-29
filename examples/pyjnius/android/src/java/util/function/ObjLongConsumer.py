from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjLongConsumer"]

class ObjLongConsumer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ObjLongConsumer"
    accept = JavaMethod("(Ljava/lang/Object;J)V")