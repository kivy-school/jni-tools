from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VirtualViewFillInfo"]

class VirtualViewFillInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/autofill/VirtualViewFillInfo"
    getAutofillHints = JavaMethod("()[Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/autofill/VirtualViewFillInfo/Builder"
        __javaconstructor__ = [("()V", False)]
        setAutofillHints = JavaMethod("([Ljava/lang/String;)Landroid/view/autofill/VirtualViewFillInfo$Builder;", varargs=True)
        build = JavaMethod("()Landroid/view/autofill/VirtualViewFillInfo;")