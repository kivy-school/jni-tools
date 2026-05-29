from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Conferenceable"]

class Conferenceable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/Conferenceable"