from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ComponentCallbacks"]

class ComponentCallbacks(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ComponentCallbacks"
    onConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")
    onLowMemory = JavaMethod("()V")