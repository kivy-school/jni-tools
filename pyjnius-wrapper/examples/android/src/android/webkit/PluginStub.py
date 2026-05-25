from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PluginStub"]

class PluginStub(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/PluginStub"
    getEmbeddedView = JavaMethod("(ILandroid/content/Context;)Landroid/view/View;")
    getFullScreenView = JavaMethod("(ILandroid/content/Context;)Landroid/view/View;")