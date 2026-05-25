from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GestureLibraries"]

class GestureLibraries(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/gesture/GestureLibraries"
    fromFile = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/gesture/GestureLibrary;", True, False), ("(Ljava/io/File;)Landroid/gesture/GestureLibrary;", True, False)])
    fromFileDescriptor = JavaStaticMethod("(Landroid/os/ParcelFileDescriptor;)Landroid/gesture/GestureLibrary;")
    fromPrivateFile = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)Landroid/gesture/GestureLibrary;")
    fromRawResource = JavaStaticMethod("(Landroid/content/Context;I)Landroid/gesture/GestureLibrary;")