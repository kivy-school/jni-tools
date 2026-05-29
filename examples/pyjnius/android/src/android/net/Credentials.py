from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Credentials"]

class Credentials(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/Credentials"
    __javaconstructor__ = [("(III)V", False)]
    getGid = JavaMethod("()I")
    getPid = JavaMethod("()I")
    getUid = JavaMethod("()I")