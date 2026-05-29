from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebViewFragment"]

class WebViewFragment(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebViewFragment"
    __javaconstructor__ = [("()V", False)]
    onCreateView = JavaMethod("(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Landroid/os/Bundle;)Landroid/view/View;")
    onPause = JavaMethod("()V")
    onResume = JavaMethod("()V")
    onDestroyView = JavaMethod("()V")
    onDestroy = JavaMethod("()V")
    getWebView = JavaMethod("()Landroid/webkit/WebView;")