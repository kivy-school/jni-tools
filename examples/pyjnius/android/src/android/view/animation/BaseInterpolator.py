from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseInterpolator"]

class BaseInterpolator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/BaseInterpolator"
    __javaconstructor__ = [("()V", False)]