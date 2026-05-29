from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceStartNotAllowedException"]

class ServiceStartNotAllowedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/ServiceStartNotAllowedException"
    getCause = JavaMethod("()Ljava/lang/Throwable;")