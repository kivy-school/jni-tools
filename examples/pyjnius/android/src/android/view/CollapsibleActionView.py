from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CollapsibleActionView"]

class CollapsibleActionView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/CollapsibleActionView"
    onActionViewCollapsed = JavaMethod("()V")
    onActionViewExpanded = JavaMethod("()V")