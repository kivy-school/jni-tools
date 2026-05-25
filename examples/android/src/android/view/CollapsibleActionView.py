from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CollapsibleActionView"]

class CollapsibleActionView(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/CollapsibleActionView"
    onActionViewExpanded = JavaMethod("()V")
    onActionViewCollapsed = JavaMethod("()V")