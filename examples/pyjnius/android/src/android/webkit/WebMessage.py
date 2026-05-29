from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebMessage"]

class WebMessage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebMessage"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;[Landroid/webkit/WebMessagePort;)V", False)]
    getPorts = JavaMethod("()[Landroid/webkit/WebMessagePort;")
    getData = JavaMethod("()Ljava/lang/String;")