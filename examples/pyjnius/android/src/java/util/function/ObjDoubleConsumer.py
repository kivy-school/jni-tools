from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjDoubleConsumer"]

class ObjDoubleConsumer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ObjDoubleConsumer"
    accept = JavaMethod("(Ljava/lang/Object;D)V")