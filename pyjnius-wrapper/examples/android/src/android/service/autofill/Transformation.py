from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Transformation"]

class Transformation(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/Transformation"