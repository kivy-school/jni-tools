from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SystemOnBackInvokedCallbacks"]

class SystemOnBackInvokedCallbacks(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/window/SystemOnBackInvokedCallbacks"
    finishAndRemoveTaskCallback = JavaStaticMethod("(Landroid/app/Activity;)Landroid/window/OnBackInvokedCallback;")
    moveTaskToBackCallback = JavaStaticMethod("(Landroid/app/Activity;)Landroid/window/OnBackInvokedCallback;")