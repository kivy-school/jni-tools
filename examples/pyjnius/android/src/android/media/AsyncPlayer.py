from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsyncPlayer"]

class AsyncPlayer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AsyncPlayer"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    stop = JavaMethod("()V")
    play = JavaMultipleMethod([("(Landroid/content/Context;Landroid/net/Uri;ZLandroid/media/AudioAttributes;)V", False, False), ("(Landroid/content/Context;Landroid/net/Uri;ZI)V", False, False)])