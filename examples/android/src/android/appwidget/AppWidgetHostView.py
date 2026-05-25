from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppWidgetHostView"]

class AppWidgetHostView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/appwidget/AppWidgetHostView"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;II)V", False)]
    setAppWidget = JavaMethod("(ILandroid/appwidget/AppWidgetProviderInfo;)V")
    getDefaultPaddingForWidget = JavaStaticMethod("(Landroid/content/Context;Landroid/content/ComponentName;Landroid/graphics/Rect;)Landroid/graphics/Rect;")
    getAppWidgetId = JavaMethod("()I")
    getAppWidgetInfo = JavaMethod("()Landroid/appwidget/AppWidgetProviderInfo;")
    dispatchSaveInstanceState = JavaMethod("(Landroid/util/SparseArray;)V")
    dispatchRestoreInstanceState = JavaMethod("(Landroid/util/SparseArray;)V")
    onLayout = JavaMethod("(ZIIII)V")
    updateAppWidgetSize = JavaMultipleMethod([("(Landroid/os/Bundle;IIII)V", False, False), ("(Landroid/os/Bundle;Ljava/util/List;)V", False, False)])
    updateAppWidgetOptions = JavaMethod("(Landroid/os/Bundle;)V")
    generateLayoutParams = JavaMethod("(Landroid/util/AttributeSet;)Landroid/widget/FrameLayout$LayoutParams;")
    setExecutor = JavaMethod("(Ljava/util/concurrent/Executor;)V")
    setOnLightBackground = JavaMethod("(Z)V")
    updateAppWidget = JavaMethod("(Landroid/widget/RemoteViews;)V")
    prepareView = JavaMethod("(Landroid/view/View;)V")
    getDefaultView = JavaMethod("()Landroid/view/View;")
    getErrorView = JavaMethod("()Landroid/view/View;")
    setColorResources = JavaMethod("(Landroid/util/SparseIntArray;)V")
    resetColorResources = JavaMethod("()V")
    dispatchDraw = JavaMethod("(Landroid/graphics/Canvas;)V")