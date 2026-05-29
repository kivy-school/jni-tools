from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ComponentCallbacks"]

class ComponentCallbacks(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ComponentCallbacks"
    onLowMemory = JavaMethod("()V")
    onConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")