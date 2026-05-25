from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppWidgetHost"]

class AppWidgetHost(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/appwidget/AppWidgetHost"
    __javaconstructor__ = [("(Landroid/content/Context;I)V", False)]
    startListening = JavaMethod("()V")
    stopListening = JavaMethod("()V")
    allocateAppWidgetId = JavaMethod("()I")
    startAppWidgetConfigureActivityForResult = JavaMethod("(Landroid/app/Activity;IIILandroid/os/Bundle;)V")
    getAppWidgetIds = JavaMethod("()[I")
    deleteAppWidgetId = JavaMethod("(I)V")
    deleteHost = JavaMethod("()V")
    deleteAllHosts = JavaStaticMethod("()V")
    createView = JavaMethod("(Landroid/content/Context;ILandroid/appwidget/AppWidgetProviderInfo;)Landroid/appwidget/AppWidgetHostView;")
    onCreateView = JavaMethod("(Landroid/content/Context;ILandroid/appwidget/AppWidgetProviderInfo;)Landroid/appwidget/AppWidgetHostView;")
    onProviderChanged = JavaMethod("(ILandroid/appwidget/AppWidgetProviderInfo;)V")
    onAppWidgetRemoved = JavaMethod("(I)V")
    onProvidersChanged = JavaMethod("()V")
    clearViews = JavaMethod("()V")