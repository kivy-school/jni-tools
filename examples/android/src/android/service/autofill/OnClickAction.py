from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnClickAction"]

class OnClickAction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/OnClickAction"