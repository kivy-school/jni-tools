from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HideReturnsTransformationMethod"]

class HideReturnsTransformationMethod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/HideReturnsTransformationMethod"
    __javaconstructor__ = [("()V", False)]
    getOriginal = JavaMethod("()[C")
    getReplacement = JavaMethod("()[C")
    getInstance = JavaStaticMethod("()Landroid/text/method/HideReturnsTransformationMethod;")