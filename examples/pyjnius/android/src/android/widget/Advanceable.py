from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Advanceable"]

class Advanceable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Advanceable"
    advance = JavaMethod("()V")
    fyiWillBeAdvancedByHostKThx = JavaMethod("()V")