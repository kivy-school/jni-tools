from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EventListener"]

class EventListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/EventListener"