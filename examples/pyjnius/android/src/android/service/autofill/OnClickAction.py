from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnClickAction"]

class OnClickAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/OnClickAction"