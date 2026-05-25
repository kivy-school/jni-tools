from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EventListenerProxy"]

class EventListenerProxy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/EventListenerProxy"
    __javaconstructor__ = [("(Ljava/util/EventListener;)V", False)]
    getListener = JavaMethod("()Ljava/util/EventListener;")