from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Advanceable"]

class Advanceable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Advanceable"
    advance = JavaMethod("()V")
    fyiWillBeAdvancedByHostKThx = JavaMethod("()V")