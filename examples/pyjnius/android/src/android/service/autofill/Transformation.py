from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Transformation"]

class Transformation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/Transformation"