from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebViewFragment"]

class WebViewFragment(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebViewFragment"
    __javaconstructor__ = [("()V", False)]
    TRIM_MEMORY_BACKGROUND = JavaStaticField("I")
    TRIM_MEMORY_COMPLETE = JavaStaticField("I")
    TRIM_MEMORY_MODERATE = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_CRITICAL = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_LOW = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_MODERATE = JavaStaticField("I")
    TRIM_MEMORY_UI_HIDDEN = JavaStaticField("I")
    getWebView = JavaMethod("()Landroid/webkit/WebView;")
    onDestroyView = JavaMethod("()V")
    onCreateView = JavaMethod("(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Landroid/os/Bundle;)Landroid/view/View;")
    onPause = JavaMethod("()V")
    onResume = JavaMethod("()V")
    onDestroy = JavaMethod("()V")