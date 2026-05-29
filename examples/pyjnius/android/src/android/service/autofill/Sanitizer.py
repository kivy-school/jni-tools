from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Sanitizer"]

class Sanitizer(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/Sanitizer"