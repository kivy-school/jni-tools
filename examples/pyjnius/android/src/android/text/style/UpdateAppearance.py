from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UpdateAppearance"]

class UpdateAppearance(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/UpdateAppearance"