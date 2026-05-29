from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebViewRenderProcessClient"]

class WebViewRenderProcessClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebViewRenderProcessClient"
    __javaconstructor__ = [("()V", False)]
    onRenderProcessResponsive = JavaMethod("(Landroid/webkit/WebView;Landroid/webkit/WebViewRenderProcess;)V")
    onRenderProcessUnresponsive = JavaMethod("(Landroid/webkit/WebView;Landroid/webkit/WebViewRenderProcess;)V")