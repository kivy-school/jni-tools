from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GestureLibraries"]

class GestureLibraries(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/gesture/GestureLibraries"
    fromRawResource = JavaStaticMethod("(Landroid/content/Context;I)Landroid/gesture/GestureLibrary;")
    fromFileDescriptor = JavaStaticMethod("(Landroid/os/ParcelFileDescriptor;)Landroid/gesture/GestureLibrary;")
    fromPrivateFile = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)Landroid/gesture/GestureLibrary;")
    fromFile = JavaMultipleMethod([("(Ljava/io/File;)Landroid/gesture/GestureLibrary;", True, False), ("(Ljava/lang/String;)Landroid/gesture/GestureLibrary;", True, False)])