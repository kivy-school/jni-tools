from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LoadParams"]

class LoadParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/LoadParams"
    getPassword = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/LoadParams/Builder"
        __javaconstructor__ = [("()V", False)]
        setPassword = JavaMethod("(Ljava/lang/String;)Landroid/graphics/pdf/LoadParams$Builder;")
        build = JavaMethod("()Landroid/graphics/pdf/LoadParams;")