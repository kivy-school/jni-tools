from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Observer"]

class Observer(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Observer"
    update = JavaMethod("(Ljava/util/Observable;Ljava/lang/Object;)V")