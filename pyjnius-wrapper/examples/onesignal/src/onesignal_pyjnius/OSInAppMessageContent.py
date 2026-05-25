from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSInAppMessageContent"]

class OSInAppMessageContent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSInAppMessageContent"
    __javaconstructor__ = [("(Lorg/json/JSONObject;)V", False)]
    getContentHtml = JavaMethod("()Ljava/lang/String;")
    setContentHtml = JavaMethod("(Ljava/lang/String;)V")
    getUseHeightMargin = JavaMethod("()Z")
    setUseHeightMargin = JavaMethod("(Z)V")
    getUseWidthMargin = JavaMethod("()Z")
    setUseWidthMargin = JavaMethod("(Z)V")
    isFullBleed = JavaMethod("()Z")
    setFullBleed = JavaMethod("(Z)V")
    getDisplayLocation = JavaMethod("()Lcom/onesignal/WebViewManager$Position;")
    setDisplayLocation = JavaMethod("(Lcom/onesignal/WebViewManager$Position;)V")
    getDisplayDuration = JavaMethod("()Ljava/lang/Double;")
    setDisplayDuration = JavaMethod("(Ljava/lang/Double;)V")
    getPageHeight = JavaMethod("()I")
    setPageHeight = JavaMethod("(I)V")