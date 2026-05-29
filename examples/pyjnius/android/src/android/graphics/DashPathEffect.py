from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DashPathEffect"]

class DashPathEffect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/DashPathEffect"
    __javaconstructor__ = [("([FF)V", False)]