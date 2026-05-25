from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ECField"]

class ECField(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECField"
    getFieldSize = JavaMethod("()I")