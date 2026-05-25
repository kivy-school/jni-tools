from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaDrmResetException"]

class MediaDrmResetException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaDrmResetException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]