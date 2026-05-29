from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Schema"]

class Schema(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/validation/Schema"
    newValidator = JavaMethod("()Ljavax/xml/validation/Validator;")
    newValidatorHandler = JavaMethod("()Ljavax/xml/validation/ValidatorHandler;")