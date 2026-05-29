from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Consumer"]

class Consumer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/Consumer"
    accept = JavaMethod("(Ljava/lang/Object;)V")
    andThen = JavaMethod("(Ljava/util/function/Consumer;)Ljava/util/function/Consumer;")