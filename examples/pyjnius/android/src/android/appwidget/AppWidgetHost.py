from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppWidgetHost"]

class AppWidgetHost(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/appwidget/AppWidgetHost"
    __javaconstructor__ = [("(Landroid/content/Context;I)V", False)]
    deleteAppWidgetId = JavaMethod("(I)V")
    onAppWidgetRemoved = JavaMethod("(I)V")
    getAppWidgetIds = JavaMethod("()[I")
    deleteHost = JavaMethod("()V")
    deleteAllHosts = JavaStaticMethod("()V")
    allocateAppWidgetId = JavaMethod("()I")
    startAppWidgetConfigureActivityForResult = JavaMethod("(Landroid/app/Activity;IIILandroid/os/Bundle;)V")
    startListening = JavaMethod("()V")
    stopListening = JavaMethod("()V")
    createView = JavaMethod("(Landroid/content/Context;ILandroid/appwidget/AppWidgetProviderInfo;)Landroid/appwidget/AppWidgetHostView;")