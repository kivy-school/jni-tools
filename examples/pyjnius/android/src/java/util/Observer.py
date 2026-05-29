from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Observer"]

class Observer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Observer"
    update = JavaMethod("(Ljava/util/Observable;Ljava/lang/Object;)V")