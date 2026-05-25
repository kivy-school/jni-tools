from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SearchEvent"]

class SearchEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/SearchEvent"
    __javaconstructor__ = [("(Landroid/view/InputDevice;)V", False)]
    getInputDevice = JavaMethod("()Landroid/view/InputDevice;")