from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EventListener"]

class EventListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/EventListener"