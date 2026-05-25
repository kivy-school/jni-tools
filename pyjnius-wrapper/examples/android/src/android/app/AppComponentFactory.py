from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppComponentFactory"]

class AppComponentFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/AppComponentFactory"
    __javaconstructor__ = [("()V", False)]
    instantiateClassLoader = JavaMethod("(Ljava/lang/ClassLoader;Landroid/content/pm/ApplicationInfo;)Ljava/lang/ClassLoader;")
    instantiateApplication = JavaMethod("(Ljava/lang/ClassLoader;Ljava/lang/String;)Landroid/app/Application;")
    instantiateActivity = JavaMethod("(Ljava/lang/ClassLoader;Ljava/lang/String;Landroid/content/Intent;)Landroid/app/Activity;")
    instantiateReceiver = JavaMethod("(Ljava/lang/ClassLoader;Ljava/lang/String;Landroid/content/Intent;)Landroid/content/BroadcastReceiver;")
    instantiateService = JavaMethod("(Ljava/lang/ClassLoader;Ljava/lang/String;Landroid/content/Intent;)Landroid/app/Service;")
    instantiateProvider = JavaMethod("(Ljava/lang/ClassLoader;Ljava/lang/String;)Landroid/content/ContentProvider;")