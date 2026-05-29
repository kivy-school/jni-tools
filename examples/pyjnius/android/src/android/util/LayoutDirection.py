from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LayoutDirection"]

class LayoutDirection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/LayoutDirection"
    INHERIT = JavaStaticField("I")
    LOCALE = JavaStaticField("I")
    LTR = JavaStaticField("I")
    RTL = JavaStaticField("I")