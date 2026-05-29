from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FabricatedOverlay"]

class FabricatedOverlay(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/om/FabricatedOverlay"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    setNinePatchResourceValue = JavaMethod("(Ljava/lang/String;Landroid/os/ParcelFileDescriptor;Ljava/lang/String;)V")
    setResourceValue = JavaMultipleMethod([("(Ljava/lang/String;IILjava/lang/String;)V", False, False), ("(Ljava/lang/String;Landroid/content/res/AssetFileDescriptor;Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;Landroid/os/ParcelFileDescriptor;Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;ILjava/lang/String;Ljava/lang/String;)V", False, False)])
    setTargetOverlayable = JavaMethod("(Ljava/lang/String;)V")
    getIdentifier = JavaMethod("()Landroid/content/om/OverlayIdentifier;")