from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectInputValidation"]

class ObjectInputValidation(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ObjectInputValidation"
    validateObject = JavaMethod("()V")