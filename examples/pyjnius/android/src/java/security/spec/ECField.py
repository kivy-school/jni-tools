from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ECField"]

class ECField(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECField"
    getFieldSize = JavaMethod("()I")