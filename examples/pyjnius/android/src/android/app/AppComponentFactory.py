from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppComponentFactory"]

class AppComponentFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/AppComponentFactory"
    __javaconstructor__ = [("()V", False)]
    instantiateActivity = JavaMethod("(Ljava/lang/ClassLoader;Ljava/lang/String;Landroid/content/Intent;)Landroid/app/Activity;")
    instantiateApplication = JavaMethod("(Ljava/lang/ClassLoader;Ljava/lang/String;)Landroid/app/Application;")
    instantiateClassLoader = JavaMethod("(Ljava/lang/ClassLoader;Landroid/content/pm/ApplicationInfo;)Ljava/lang/ClassLoader;")
    instantiateProvider = JavaMethod("(Ljava/lang/ClassLoader;Ljava/lang/String;)Landroid/content/ContentProvider;")
    instantiateService = JavaMethod("(Ljava/lang/ClassLoader;Ljava/lang/String;Landroid/content/Intent;)Landroid/app/Service;")
    instantiateReceiver = JavaMethod("(Ljava/lang/ClassLoader;Ljava/lang/String;Landroid/content/Intent;)Landroid/content/BroadcastReceiver;")