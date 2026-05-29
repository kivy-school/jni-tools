from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppWidgetProvider"]

class AppWidgetProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/appwidget/AppWidgetProvider"
    __javaconstructor__ = [("()V", False)]
    onReceive = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")
    onRestored = JavaMethod("(Landroid/content/Context;[I[I)V")
    onDeleted = JavaMethod("(Landroid/content/Context;[I)V")
    onAppWidgetOptionsChanged = JavaMethod("(Landroid/content/Context;Landroid/appwidget/AppWidgetManager;ILandroid/os/Bundle;)V")
    onUpdate = JavaMethod("(Landroid/content/Context;Landroid/appwidget/AppWidgetManager;[I)V")
    onDisabled = JavaMethod("(Landroid/content/Context;)V")
    onEnabled = JavaMethod("(Landroid/content/Context;)V")