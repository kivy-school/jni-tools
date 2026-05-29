from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectInputValidation"]

class ObjectInputValidation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ObjectInputValidation"
    validateObject = JavaMethod("()V")