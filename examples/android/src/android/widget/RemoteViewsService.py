from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoteViewsService"]

class RemoteViewsService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/RemoteViewsService"
    __javaconstructor__ = [("()V", False)]
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onGetViewFactory = JavaMethod("(Landroid/content/Intent;)Landroid/widget/RemoteViewsService$RemoteViewsFactory;")

    class RemoteViewsFactory(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/RemoteViewsService/RemoteViewsFactory"
        onCreate = JavaMethod("()V")
        onDataSetChanged = JavaMethod("()V")
        onDestroy = JavaMethod("()V")
        getCount = JavaMethod("()I")
        getViewAt = JavaMethod("(I)Landroid/widget/RemoteViews;")
        getLoadingView = JavaMethod("()Landroid/widget/RemoteViews;")
        getViewTypeCount = JavaMethod("()I")
        getItemId = JavaMethod("(I)J")
        hasStableIds = JavaMethod("()Z")