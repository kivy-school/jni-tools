from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SigningInfoException"]

class SigningInfoException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/SigningInfoException"
    getCode = JavaMethod("()I")