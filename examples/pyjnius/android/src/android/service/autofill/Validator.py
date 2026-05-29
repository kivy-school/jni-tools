from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Validator"]

class Validator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/Validator"