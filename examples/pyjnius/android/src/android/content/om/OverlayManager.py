from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OverlayManager"]

class OverlayManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/om/OverlayManager"
    commit = JavaMethod("(Landroid/content/om/OverlayManagerTransaction;)V")
    getOverlayInfosForTarget = JavaMethod("(Ljava/lang/String;)Ljava/util/List;")