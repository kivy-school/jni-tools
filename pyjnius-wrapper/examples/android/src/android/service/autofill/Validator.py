from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Validator"]

class Validator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/Validator"