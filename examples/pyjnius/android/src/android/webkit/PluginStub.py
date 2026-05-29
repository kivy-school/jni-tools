from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PluginStub"]

class PluginStub(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/PluginStub"
    getFullScreenView = JavaMethod("(ILandroid/content/Context;)Landroid/view/View;")
    getEmbeddedView = JavaMethod("(ILandroid/content/Context;)Landroid/view/View;")