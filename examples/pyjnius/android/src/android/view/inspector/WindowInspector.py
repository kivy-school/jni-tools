from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WindowInspector"]

class WindowInspector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/WindowInspector"
    getGlobalWindowViews = JavaStaticMethod("()Ljava/util/List;")