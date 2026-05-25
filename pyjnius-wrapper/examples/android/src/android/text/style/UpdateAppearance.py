from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UpdateAppearance"]

class UpdateAppearance(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/UpdateAppearance"