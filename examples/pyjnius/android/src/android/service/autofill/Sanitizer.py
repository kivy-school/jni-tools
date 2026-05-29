from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Sanitizer"]

class Sanitizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/Sanitizer"