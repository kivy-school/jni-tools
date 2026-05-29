from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SingleLineTransformationMethod"]

class SingleLineTransformationMethod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/SingleLineTransformationMethod"
    __javaconstructor__ = [("()V", False)]
    getInstance = JavaStaticMethod("()Landroid/text/method/SingleLineTransformationMethod;")