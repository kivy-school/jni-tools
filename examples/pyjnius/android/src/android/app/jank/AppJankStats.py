from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppJankStats"]

class AppJankStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/jank/AppJankStats"
    __javaconstructor__ = [("(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;JJLandroid/app/jank/RelativeFrameTimeHistogram;)V", False)]
    WIDGET_CATEGORY_ANIMATION = JavaStaticField("Ljava/lang/String;")
    WIDGET_CATEGORY_KEYBOARD = JavaStaticField("Ljava/lang/String;")
    WIDGET_CATEGORY_MEDIA = JavaStaticField("Ljava/lang/String;")
    WIDGET_CATEGORY_NAVIGATION = JavaStaticField("Ljava/lang/String;")
    WIDGET_CATEGORY_OTHER = JavaStaticField("Ljava/lang/String;")
    WIDGET_CATEGORY_SCROLL = JavaStaticField("Ljava/lang/String;")
    WIDGET_CATEGORY_UNSPECIFIED = JavaStaticField("Ljava/lang/String;")
    WIDGET_STATE_ANIMATING = JavaStaticField("Ljava/lang/String;")
    WIDGET_STATE_DRAGGING = JavaStaticField("Ljava/lang/String;")
    WIDGET_STATE_FLINGING = JavaStaticField("Ljava/lang/String;")
    WIDGET_STATE_NONE = JavaStaticField("Ljava/lang/String;")
    WIDGET_STATE_PLAYBACK = JavaStaticField("Ljava/lang/String;")
    WIDGET_STATE_PREDICTIVE_BACK = JavaStaticField("Ljava/lang/String;")
    WIDGET_STATE_SCROLLING = JavaStaticField("Ljava/lang/String;")
    WIDGET_STATE_SWIPING = JavaStaticField("Ljava/lang/String;")
    WIDGET_STATE_TAPPING = JavaStaticField("Ljava/lang/String;")
    WIDGET_STATE_UNSPECIFIED = JavaStaticField("Ljava/lang/String;")
    WIDGET_STATE_ZOOMING = JavaStaticField("Ljava/lang/String;")
    getWidgetState = JavaMethod("()Ljava/lang/String;")
    getWidgetCategory = JavaMethod("()Ljava/lang/String;")
    getTotalFrameCount = JavaMethod("()J")
    getWidgetId = JavaMethod("()Ljava/lang/String;")
    getRelativeFrameTimeHistogram = JavaMethod("()Landroid/app/jank/RelativeFrameTimeHistogram;")
    getJankyFrameCount = JavaMethod("()J")
    getNavigationComponent = JavaMethod("()Ljava/lang/String;")
    getUid = JavaMethod("()I")